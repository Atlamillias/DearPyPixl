// Contains rust equivelents of performance-critical Python
// functions for dearpypixl.
// TODO: cross-platform, build script

use pyo3::prelude::*;


#[pymodule]
fn _dearpypixl(py: Python<'_>, module: &PyModule) -> PyResult<()>
{
    // _dearpypixl.grid
    let px_grid = PyModule::new(py, "grid")?;
    grid::init_mod(module)?;
    module.add_submodule(px_grid)?;

    Ok(())
}



// Python submodules

pub mod grid {
    use pyo3::prelude::*;
    use pyo3::types::{
        PyList, PyAny, PyModule
    };
    use std::collections::{
        HashMap,
    };

    #[pyfunction]
    pub fn draw_cells(
        rect_size : (f64, f64),
        rect_pad  : (f64, f64, f64, f64),
        cell_pad  : (f64, f64, f64, f64),
        x_axis    : &PyAny,  // rows (height)
        y_axis    : &PyAny,  // cols (width)
    ) -> PyResult<HashMap<(usize, usize), (f64, f64, f64, f64)>>
    {
        // x1_pad = left, x2_pad = right, y1_pad = top, y2_pad = bottom
        let bbox_x1_pad = rect_pad.0;
        let bbox_y1_pad = rect_pad.2;
        let bbox_ht = rect_size.1 - bbox_y1_pad - rect_pad.3;
        let bbox_wt = rect_size.0 - bbox_x1_pad - rect_pad.1;

        let _x_min_size: f64 = x_axis.getattr("min_size")?.extract()?;
        let _x_weight  : f64 = x_axis.getattr("weight")?.extract()?;
        let weighted_ht: f64 = (bbox_ht - _x_min_size).max(0.0) / _x_weight.max(1.0);

        let _y_min_size: f64 = y_axis.getattr("min_size")?.extract()?;
        let _y_weight  : f64 = y_axis.getattr("weight")?.extract()?;
        let weighted_wt: f64 = (bbox_wt - _y_min_size).max(0.0) / _y_weight.max(1.0);

        let cell_x1_pad: f64 = (cell_pad.0 / 2.0) as f64;
        let cell_y1_pad: f64 = (cell_pad.2 / 2.0) as f64;
        let cell_x_pad : f64 = cell_x1_pad + (cell_pad.1 / 2.0);
        let cell_y_pad : f64 = cell_y1_pad + (cell_pad.3 / 2.0);

        let py_rows: &PyList = x_axis.getattr("_members")?.extract()?;
        let py_cols: &PyList = y_axis.getattr("_members")?.extract()?;
        let mut py_cell_map = HashMap::new();

        let mut alloc_ht: f64 = 0.0;
        for (r_idx, py_row) in py_rows.iter().enumerate() {
            let _r_size: i64 = py_row.getattr("_size")?.extract()?;
            let row_ht : f64;
            if _r_size.max(0) > 0 {
                row_ht = _r_size as f64;
            }
            else {
                let _r_weight: f64 = py_row.getattr("_weight")?.extract()?;
                row_ht = weighted_ht * _r_weight;
            }
            let cell_y_pos : f64 = bbox_y1_pad + cell_y1_pad + alloc_ht;
            let cell_height: f64 = row_ht - cell_y_pad;

            let mut alloc_wt: f64 = 0.0;
            for (c_idx, py_col) in py_cols.iter().enumerate() {
                let _c_size: i64 = py_col.getattr("_size")?.extract()?;
                let col_wt : f64;
                if _c_size.max(0) > 0 {
                    col_wt = _c_size as f64
                }
                else {
                    let _c_weight: f64 = py_col.getattr("_weight")?.extract()?;
                    col_wt = weighted_wt * _c_weight
                }
                let cell_x_pos: f64 = bbox_x1_pad + cell_x1_pad + alloc_wt;
                let cell_width: f64 = col_wt - cell_x_pad;
                alloc_wt += col_wt;
                py_cell_map.insert((r_idx, c_idx), (cell_x_pos, cell_y_pos, cell_width, cell_height));
            }
            alloc_ht += row_ht;
        }
        Ok(py_cell_map.into())
    }


    pub fn init_mod(module: &PyModule) -> PyResult<()>
    {
        module.add_function(wrap_pyfunction!(draw_cells, module)?)?;
        Ok(())
    }

}



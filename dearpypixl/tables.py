from typing import Any, Callable, Union
from functools import singledispatchmethod
from dearpygui import dearpygui
from dearpygui._dearpygui import (
    get_item_info,  # used A LOT
    get_value
)
import dearpypixl.appitems.tables
from dearpypixl.appitems.tables import *
from dearpypixl.components import Item



__all__ = [
    *dearpypixl.appitems.tables.__all__,
    "Table",
    "TableCell",
    "TableColumn",
    "TableRow"
]



# NOTE: Many methods use the raw DPG API because there are very few
# pieces of info needed from several things and the code itself would be
# about as long when using the DearPyPixl API. There's no point in adding
# in its overhead -- gotta go fast.

# TODO: Find use of unset_table_row_color`. 



class Table(Table):
    ##########################
    #### List-ish methods ####
    ##########################
    def index(self, row_col_cell_item: Union[TableRow, TableColumn, TableCell]) -> Union[list[int], int]:
        """Return the position of a row, column, or cell item in this table. An `int`
        is returned for `TableRow` and `TableColumn` items. If the item is a `TableCell`,
        a list is returned instead containing row and column indices as [row, column]. 

        Args:
            * row_col_cell_item (Union[TableRow, TableColumn, TableCell]): The item
            to retrieve the position of in the table.
        """
        return row_col_cell_item.position

    def reverse_columns(self) -> None:
        """Invert the order of the columns in this table.
        """
        # avoiding loop lookups
        reorder_items = dearpygui.reorder_items

        child_slots = get_item_info(self._tag)["children"]
        col_uuids = child_slots[0][::-1]
        reorder_items(self._tag, 0, col_uuids)
        # Reordering columns only adjusts headers. Also need to reorder row children.
        row_uuids = child_slots[1]
        for row_uuid in row_uuids:
            row_values = get_item_info(row_uuid)["children"][1]
            reorder_items(row_uuid, 1, row_values[::-1])

    def reverse_rows(self) -> None:
        """Invert the order of the rows in this table.
        """
        row_uuids = get_item_info(self._tag)["children"][1][::-1]
        dearpygui.reorder_items(self._tag, 1, row_uuids)

    def remove_row(self, row_idx: int) -> None:
        """Deletes the row at the specified index.
        """
        row_uuid = get_item_info(self._tag)["children"][1][row_idx]
        row_item = self.__registry__[0][row_uuid]
        row_item.delete()

    def remove_column(self, column_idx: int) -> None:
        """Deletes the column at the specified index.
        """
        col_uuid = get_item_info(self._tag)["children"][0][column_idx]
        col_item = self.__registry__[0][col_uuid]
        col_item.delete()

    #########################
    #### DPG cmd methods ####
    #########################
    def is_row_highlighted(self, row_idx: int) -> bool:
        return dearpygui.is_table_row_highlighted(self._tag, row_idx)

    def is_column_highlighted(self, column_idx: int) -> bool:
        return dearpygui.is_table_column_highlighted(self._tag, column_idx)

    def is_cell_highlighted(self, row_idx: int, column_idx: int) -> bool:
        return dearpygui.is_table_cell_highlighted(self._tag, row_idx, column_idx)

    def highlight_cell(self, row_idx: int, column_idx: int, color: Union[tuple[int], list[int]]) -> None:
        dearpygui.highlight_table_cell(self._tag, row_idx, column_idx, color)

    def highlight_column(self, column_idx: int, color: Union[tuple[int], list[int]]) -> None:
        dearpygui.highlight_table_column(self._tag, column_idx, color)

    def highlight_row(self, row_idx: int, color: Union[tuple[int], list[int]]) -> None:
        dearpygui.highlight_table_row(self._tag, row_idx, color)

    def unhighlight_cell(self, row_idx: int, column: int) -> None:
        dearpygui.unhighlight_table_cell(self._tag, row_idx, column)

    def unhighlight_column(self, column_idx: int) -> None:
        dearpygui.unhighlight_table_column(self._tag, column_idx)

    def unhighlight_row(self, row_idx: int) -> None:
        dearpygui.unhighlight_table_row(self._tag, row_idx)

    def reorder(self, slot: int, new_order: list):
        dearpygui.reorder_items(self._tag, slot, new_order)


    #########################
    ######### Misc. #########
    #########################
    @property
    def rows(self) -> list[TableRow]:
        """Return a list of all `TableRow` children in this table in
        the order of their current positions.
        """
        row_uuids = get_item_info(self._tag)["children"][1]
        appitems = self.__registry__[0]
        return [appitems[row_uuid] for row_uuid in row_uuids]

    @property
    def columns(self) -> list[TableColumn]:
        """Return a list of all `TableColumn` children in this table in
        the order of their current positions.
        """
        col_uuids = get_item_info(self._tag)["children"][0]
        appitems = self.__registry__[0]
        return [appitems[col_uuid] for col_uuid in col_uuids]



class TableRow(TableRow):
    @property
    def position(self) -> int:
        """Return the specific index for this row.
        """
        table_uuid = self.parent._tag
        table_rows = get_item_info(table_uuid)["children"][1]
        return table_rows.index(self._tag)

    @property
    def value(self) -> list[Any]:
        """Return a list of values of all items in this row.
        """
        children = self.children(slot=1)
        return [child.value for child in children]

    @property
    def is_highlighted(self) -> bool:
        """Check if this row is highlighted.
        """
        return dearpygui.is_table_row_highlighted(self.parent._tag, self.position)

    def _get_index_params(method):
        def wrapper(self, color: Union[tuple[int], list[int]] = None, **kwargs) -> None:
            parent_uuid = self.parent._tag
            parent_rows = get_item_info(parent_uuid)["children"][1]
            row_position = parent_rows.index(self._tag)
            if color:
                kwargs["color"] = color
            return method(self, color=color, table=parent_uuid, row=row_position)
        return wrapper

    @_get_index_params
    def highlight(self, color: Union[tuple[int], list[int]], **kwargs) -> None:
        """Highlight this specific table row.

        Args:
            * color (Union[tuple[int], list[int]]): color of the highlight as
            [red, blue, green, alpha].
        """
        dearpygui.highlight_table_row(color=color, **kwargs)

    @_get_index_params
    def unhighlight(self, **kwargs) -> None:
        """Remove the highlight from this specific table row.
        """
        dearpygui.highlight_table_row(**kwargs)


class TableColumn(TableColumn):
    color = (0, 0, 0, 255)

    @property
    def position(self) -> int:
        """Return the specific index for this column.
        """
        table_uuid = self.parent._tag
        table_cols = get_item_info(table_uuid)["children"][0]
        return table_cols.index(self._tag)

    @property
    def value(self) -> list[Any]:
        """Return a list of values of all items in this cell.
        """
        # NOTE: This operation can potentially be VERY expensive.
        # It varies on the size of the table. Just thought i'd mention...

        # Need to pull info from ALL of the rows...
        appitems = self.__registry__[0]
        position = self.position  # index for the row child
        values = []
        # Using the DPP API pre-loop. In the loop though we're using the DPG API as
        # it avoids lookup overhead (through possibly hundreds/thousands of items).
        for row in self.parent.children(slot=1):
            row_child_value = get_item_info(row._tag)["children"][1][position]
            values.append(appitems[row_child_value])
        return values

    @property
    def is_highlighted(self) -> bool:
        """Check if this row is highlighted.
        """
        return dearpygui.is_table_column_highlighted(self.parent._tag, self.position)

    def _get_index_params(method):
        def wrapper(self, color: Union[tuple[int], list[int]] = None, **kwargs) -> None:
            parent_uuid = self.parent._tag
            parent_cols = get_item_info(parent_uuid)["children"][0]
            col_position = parent_cols.index(self._tag) 
            if color:
                kwargs["color"] = color
            return method(self, table=parent_uuid, column=col_position, **kwargs)
        return wrapper

    @_get_index_params
    def highlight(self, color: Union[tuple[int], list[int]] = None, **kwargs) -> None:
        """Highlight this specific table column.

        Args:
            * color (Union[tuple[int], list[int]]): color of the highlight as
            [red, blue, green, alpha].
        """
        dearpygui.highlight_table_column(color=color or self.color, **kwargs)

    @_get_index_params
    def unhighlight(self, **kwargs) -> None:
        """Remove the highlight from this specific table column.
        """
        dearpygui.unhighlight_table_column(**kwargs)


class TableCell(TableCell):
    color = (0, 0, 0, 255)

    @property
    def row(self) -> int:
        """Return the specific row item for this cell.
        """
        # This is literally just this cell's parent, but the API feels
        # incomplete without it.
        return self.parent

    @property
    def column(self) -> int:
        """Return the specific column item for this cell.
        """
        # Goal here is to get the tag of the column that this cell is in.
        # Since table columns are parented by the tables, we need to go
        # through this cell's parent (row) as it is parented by the table.
        row_uuid = self.parent._tag
        row_info = get_item_info(row_uuid)
        row_childs = row_info["children"][1]
        col_position = row_childs.index(self._tag)
        table_uuid = get_item_info(row_uuid)["parent"]
        table_columns = get_item_info(table_uuid)["children"][0]
        return self.__registry__[0][table_columns[col_position]]

    @property
    def position(self) -> tuple[int, int]:
        """Return the specific row and column indices for this cell.
        """
        row_uuid = self.parent._tag
        row_info = get_item_info(row_uuid)
        row_childs = row_info["children"][1]
        table_uuid = row_info["parent"]
        row_position = get_item_info(table_uuid)["children"][1].index(row_uuid)
        col_position = row_childs.index(self._tag)
        return [row_position, col_position]

    @property
    def is_highlighted(self) -> bool:
        """Check if this row is highlighted.
        """
        return dearpygui.is_table_cell_highlighted(self.parent.parent._tag, *self.position)

    @property
    def value(self) -> list[Any]:
        """Return a list of values of all items in this cell.
        """
        children = self.children(slot=1)
        return [child.value for child in children]

    def _get_index_params(method):
        def wrapper(self, color: Union[tuple[int], list[int]] = None, **kwargs) -> None:
            row_uuid = self.parent._tag  # row
            row_info = get_item_info(row_uuid)
            row_childs = row_info["children"][1]
            col_position = row_childs.index(self._tag)  # column
            table_uuid = row_info["parent"]  # row parent
            table_rows = get_item_info(table_uuid)["children"][1]
            row_position = table_rows.index(row_uuid)
            if color:
                kwargs["color"] = color
            return method(self, table=table_uuid, row=row_position, column=col_position, **kwargs)
        return wrapper

    @_get_index_params
    def highlight(self, color: Union[tuple[int], list[int]] = None, **kwargs) -> None:
        """Highlight this specific table cell.

        Args:
            * color (Union[tuple[int], list[int]]): color of the highlight as
            [red, blue, green, alpha].
        """
        dearpygui.highlight_table_cell(color=color or self.color, **kwargs)

    @_get_index_params
    def unhighlight(self, **kwargs) -> None:
        """Remove the highlight from this specific table cell.
        """
        dearpygui.unhighlight_table_cell(**kwargs)



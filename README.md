**DPGWidgets** is an object-oriented wrap around the [DearPyGui](https://github.com/hoffstadt/DearPyGui) graphical interface framework.

It ships in two parts - **dpgwrap** and **dpgwidgets**. **dpgwrap** is mostly auto-generated from a script that parses the locally installed DearPyGui API, identifies objects, and sorts them - wrapping most item-producing objects in **class**-objects and dumping them to Python files. This is different from many libraries that are built at runtime where IDE intellisense and language servers can't help you. **dpgwidgets** is loosely built on top of **dpgwrap** and *not* auto-generated. It uses a few objects from **dpgwrap** but it mostly calls from the DearPyGui API directly. Things such as managing the application, adding event handlers, and theming is streamlined and made more "pythonic".

Documentation, examples, etc will be added periodically. The source code has many comments and docstrings, and it is encouraged to read through them. MOST of the [DearPyGui documentation](https://github.com/hoffstadt/DearPyGui/wiki) will also apply here.


## Example
```python
import dpgwidgets as dpgw
from dpgwidgets import containers
from dpgwidgets import widgets

app = dpgw.Viewport()
app.title = "ExampleApp"

with containers.Window("Window1") as window1:
    ...

@app.on_resize
def on_app_resize():
    widgets.Text(f"{app.title} resized!", parent=window1)

@window1.on_resize
def on_window1_resize():
    widgets.Text(f"{window1.label} resized!", parent=window1)

app.start()
```
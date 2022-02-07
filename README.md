DearPyPixl is a graphical user interface library offering object-oriented bindings and extensions of [DearPyGui](https://github.com/hoffstadt/DearPyGui).

Documentation is always a work-in-progress, however most of the documentation for DearPyGui will also apply to DearPyPixl. It can be found [here](https://dearpygui.readthedocs.io/en/latest/index.html). DearPyPixl also has its own channel in the official [DearPyGui Discord server](https://discord.gg/tyE7Gu4) where you can ask me questions.


## Installation
The newest version of this library is currently not available on PyPi. To install:
* Clone the repo.
* Build the wheel. On Windows, you can run `built.bat` in `./scripts`, or `python setup.py process` from a command terminal (MacOS/Linux closly mirror this process).
* Use **pip** to install using the wheel (i.e. `python -m pip install <dearpypixl_wheel>`).


# Usage (WIP)
## Basic Example
DearPyPixl maintains the same flow and structure of DearPyGui. Below is an example of how to create an application viewport, a window item, and a text item in DearPyGui:

```python
from dearpygui import dearpygui as dpg
dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


with dpg.window() as main_window:
    txt = dpg.add_text("Hello!")


dpg.show_viewport()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()
```

And below is the equivelent of the above using DearPyPixl:

```python
from dearpypixl import Application
from dearpypixl.containers import Window
from dearpypixl.basic import Text

with Window() as main_window:
    txt = Text("Hello!")

Application.start()
```

The largest difference between these is that it is not necessary for the user to set up the library, application, or viewport as it is done automatically. However, DearPyPixl does not obsufucate the important bits from the user -- for example, the main render loop can still be created manually instead of calling `Application.start`.

## License
DearPyPixl is licensed under [MIT License](https://github.com/Atlamillias/DPG-Widgets/blob/main/LICENSE).

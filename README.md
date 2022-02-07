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


# NOTE: In DearPyGui, `main_window` is bound to the `tag` of the window. When using DearPyPixl,
# it is bound to the newly created instance of `Window`.
with Window() as main_window:
    txt = Text("Hello!")  # `txt` is bound to the created instance of `Text`


Application.start()
```

The largest difference between these is that it is not necessary for the user to set up the library, application, or viewport as it is done automatically. However, DearPyPixl does not obfuscate the important bits from the user -- for example, the main render loop can still be created manually instead of calling `Application.start`.

## The `Item` Object
All objects representing an item(s) in DearPyGui are descendants of the [`Item`](https://github.com/Atlamillias/dearpypixl/blob/384f064e1ce328e860717db85c2984325718d76d/dearpypixl/components/item.py#L175) abstract class. It has several methods for setting and fetching various data regarding the object's state, configuration, specific parents, etc. An item's configuration are also bound as attributes, and can be fetched and set with ease.


```python
from dearpypixl import Application
from dearpypixl.containers import Window
from dearpypixl.basic import Text
from dearpypixl.misc import Seperator


with Window(height=750, width=400) as main_window:
    # The configuration of `main_window` can be fetched using dotted attribute access.
    main_window.height  # 500
    main_window.width   # 800

    # Configuration can also be changed just like you'd expect.
    main_window.label = "main_window"

    # The `configure` method allows for several options to be changed.
    main_window.configure(no_close=True, no_collapse=True)

    # Similarly, calling the `configuration` method will return a dict of the item's
    # current and editable configuration.
    config_title_txt = Text("MY CONFIGURATION")
    title_txt_sep    = Separator()
    for option, value in main_window.configuration().items():
        # Creating a `Text` item for every configuration pair.
        Text(f"{option}: {value}")

# Just like when using DearPyGui, you can specify the item's parent at creation.
# NOTE: When a reference to another item is required (for `parent`, `before`, etc) you can pass
# the `tag` of the item, or the item itself.
Separator(parent=main_window    , before=title_txt_sep)
Separator(parent=main_window.tag, before=config_title_txt)


Application.start()
```


[](https://github.com/Atlamillias/dearpypixl/blob/main/examples/images/config_ex1.png)


Something to keep in mind is that all descendants of the `Item` object can accept the `tag` parameter in its constructor, much like every item in DearPyGui can. One of the key differences between DearPyPixl and DearPyGui is that the use of **aliases is not supported** -- the value of `tag` is always expected to be `int`. It is suggested that you do not pass your own tags as it is done automatically, and can be accessed after creation using via the `tag` attribute.

## Application and Viewport
The `Application` and `Viewport` objects are  

## License
DearPyPixl is licensed under [MIT License](https://github.com/Atlamillias/DPG-Widgets/blob/main/LICENSE).

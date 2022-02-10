DearPyPixl is a graphical user interface library offering object-oriented bindings and extensions of [DearPyGui](https://github.com/hoffstadt/DearPyGui).

## Installation
The newest version of this library is currently not available on PyPi. To install:
* Clone the repo.
* Build the wheel. On Windows, you can run `built.bat` in `./scripts`, or `python setup.py process` from a command terminal (MacOS/Linux closly mirror this process).
* Use **pip** to install using the wheel (i.e. `python -m pip install <dearpypixl_wheel>`).


# Usage (WIP)
Documentation is a work-in-progress. DearPyPixl maintains the same flow and structure of DearPyGui, and almost all of the documentation for DearPyGui will also apply to DearPyPixl (found [here](https://dearpygui.readthedocs.io/en/latest/index.html)). As such, documentation in the short-term will focus primarily on things that DearPyGui's documentation does *not* cover. Docstrings of wrapped items are taken directly from DearPyGui, while more custom objects unique to DearPyPixl have more detailed information.

DearPyPixl also has its own channel in the official [DearPyGui Discord server](https://discord.gg/tyE7Gu4) where you can ask me questions.


## Basic Example
Below is an example of how to create an application viewport, a window item, and a text item in DearPyGui:

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


with Window() as main_window:  # `main_window` == `Window` instance
    txt = Text("Hello!")


Application.start()
```

The most notable difference between these is that it is not necessary for the user to set up the library, application, or viewport as it is done automatically. However, DearPyPixl does not obfuscate the important bits from the user -- for example, the main render loop can still be created manually instead of calling `Application.start`.


## The `Item` Object
All objects representing an item(s) in DearPyGui are descendants of the [`Item`](https://github.com/Atlamillias/dearpypixl/blob/384f064e1ce328e860717db85c2984325718d76d/dearpypixl/components/item.py#L175) abstract class. It has several methods for setting and fetching various data regarding `Item` instances or the item type. Most item data is sorted into three categories:

* **configuration**: Editable attributes that are used internally to manage the item. 
* **information**: Data that is unique to the item and is either read-only (like the `tag` attribute), or not as freely editable as "configuration" (such as `parent`). This data rarely changes.
* **state**: Read-only data regarding an item's condition. Can update frequently.

The data sorted into these categories can vary per item type, and do not always contain the same data of DearPyGui's `get_item_configuration/info/state` getter functions. For example, the return of `get_item_configuration` may contain a key-value pair that cannot be passed to `configure_item` without raising an error. In DearPyPixl, data such as this would be categorized as "information" instead. Another example is that the return of `get_item_state` includes `pos` (if applicable for the item, like a button) despite being an accepted parameter for `configure_item`. DearPyPixl categorizes `pos` as "configuration" and is included in the return of an item's `configuration` method, not the `state` method.

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

    # The `configure` method allows for several options to be changed, similar to the
    # `configure_item` function in DearPyGui.
    main_window.configure(no_close=True, no_collapse=True)

    # Similarly, calling the `configuration` method will return a dict of the item's
    # current and editable configuration. Calling this method is similar to calling
    # DearPyGui's `get_item_configuration` on an item.
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

<img src="https://github.com/Atlamillias/dearpypixl/blob/main/examples/images/config_ex1.png">


Some methods such as `unique_parents` and `unique_children` offer information that is not directly accessable using DearPyGui -- many of which are classmethods. Others are instance methods that simply replace common functions called on items in DearPyGui like `move_up` (`move_item_up`) and `delete` (`delete_item`) methods. More information regarding each of these can be found within each method's docstring.


Something to keep in mind is that all descendants of the `Item` object can accept the `tag` parameter in its constructor, much like every item in DearPyGui can. One of the key differences between DearPyPixl and DearPyGui is that the use of **aliases is not supported** -- the value of `tag` is always expected to be `int`. It is suggested that you do not commonly pass your own tags as they are generated automatically, and can be accessed after creation using via the `tag` property.


## Application and Viewport
`Application` and `Viewport` are among the more unique objects in DearPyPixl. They aren't derived from the `Item` object, but *its* parent class. As such, they have limited functionality in comparison to other `Item` subclasses. Like all `Item` derivatives, they have access to the `configure`, `configuration`, `information`, and `state` methods, as well as the `tag` attribute. Other methods are unique to each object.


```python
from dearpypixl import Application, Viewport
from dearpypixl.containers import Window, TreeNode, CollapsingHeader


Viewport.height         = 800
Viewport.width          = 1000
Viewport.configure(title="Clever Viewport Title", resizable=False)

with Window() as main_window:
    with Group(horizontal=True):
        TreeNodeTemplate = TreeNode.as_template(bullet=True, selectable=False)

        with ChildWindow(width=490):
            with CollapsingHeader("Application Config", default_open=True):
                for option, value in Application.configuration().items():
                    TreeNodeTemplate(label=f"{option}: {value}")
            with CollapsingHeader("Application Info", default_open=True):
                for option, value in Application.information().items():
                    TreeNodeTemplate(label=f"{option}: {value}")
            with CollapsingHeader("Application State", default_open=True):
                for option, value in Application.state().items():
                    TreeNodeTemplate(label=f"{option}: {value}")

        with ChildWindow():
            with CollapsingHeader("Viewport Config", default_open=True):
                for option, value in Viewport.configuration().items():
                    TreeNodeTemplate(label=f"{option}: {value}")
            with CollapsingHeader("Viewport Info", default_open=True):
                for option, value in Viewport.information().items():
                    TreeNodeTemplate(label=f"{option}: {value}")
            with CollapsingHeader("Viewport State", default_open=True):
                for option, value in Viewport.state().items():
                    TreeNodeTemplate(label=f"{option}: {value}")

Viewport.primary_window = main_window

Application.start()
```

<img src="https://github.com/Atlamillias/dearpypixl/blob/main/examples/images/app_vp_ex1.png">


The thing to note here is that *all* functionality is class-bound, not instance-bound. This is important because:
* you do not need to create instances of each to access and change their settings
* you are not limited to stuffing all of your UI code within a single module (each module can simply import `Application`/`Viewport`)
* unlike modules, supports inheritance
With that said, creating `Application`/`Viewport` instances will not in any way create additional application windows -- only 1 "application" and 1 "viewport" can exist, and is set up upon importing DearPyPixl. This will change once DearPyGui offers multi-viewport support.


## Events and Callbacks
Coming soon...


## Theming
Coming soon...


## License
DearPyPixl is licensed under [MIT License](https://github.com/Atlamillias/DPG-Widgets/blob/main/LICENSE).

# Dear PyPixl
Dear PyPixl is an object-oriented, lightweight, modular framework and toolkit for [Dear PyGui](https://github.com/hoffstadt/DearPyGui) with minimal dependencies and zero use restrictions (MIT license). It is very "use what you want/need", allowing you to use both Dear PyPixl and Dear PyGui API's in the same project without conflict.

I highly suggest visiting Dear PyGui's [documentation](https://dearpygui.readthedocs.io/en/latest/index.html) if you are unfamiliar with the project. Basic usage of Dear PyPixl is very similar (identical) to that of Dear PyGui.

___
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Dear PyPixl](#dear-pypixl)
      - [Features](#features)
      - [Requirements](#requirements)
      - [Installation](#installation)
- [Overview](#overview)
  - [Item Interfaces](#item-interfaces)
      - [Creating Interfaces](#creating-interfaces)
      - [Methods & Properties](#methods--properties)
      - [Behaviors](#behaviors)
  - [Item Types](#item-types)
  - [Global State & Setup](#global-state--setup)
  - [Modules](#modules)
  - [Limitations, Bugs, & Gachas](#limitations-bugs--gachas)
      - [Interfaces are Integers, For Better or Worse](#interfaces-are-integers-for-better-or-worse)
      - [Passing Explicit UUID's and Aliases](#passing-explicit-uuids-and-aliases)
- [FAQ](#faq)

<!-- /code_chunk_output -->
___

#### Features
 - extensible high-level object-oriented API for creating and/or interfacing with Dear PyGui items, including theme elements
 - low-level API that fills various gaps in Dear PyGui's API
 - strongly typed
 - allows the use of both `dearpypixl` and `dearpygui` code together with minimal conflicts
 - typing for `mvBuffer`, `mvVec4`, and `mvMat4`
 - improved docstrings, errors, and type signatures
 - contains numerous extensions and other helpful tools
<br>

#### Requirements
 - Operating System; Windows 8.1+, MacOS, Linux*
 - Python: 3.10 x64* (or newer)
 - `pip` dependencies:
    * `dearpygui` 1.9 (or newer)
    * `typing-extensions` (Python < 3.12 only)

*Dear PyPixl is available on all platforms already supported by Dear PyGui. Availability for 32-bit systems and Raspberry Pi OS is *loosely* supported, but requires building Dear PyGui from the source. Please visit their [wiki](https://github.com/hoffstadt/DearPyGui/wiki) for more information.
<br>

#### Installation

Using `pip`;
```python
python3 -m pip install dearpypixl
```
<br>
Alternatively, build the wheel and install locally. Download/clone the source;
```
git clone https://github.com/Atlamillias/DearPyPixl
```
Then, from the project directory;
```
python3 -m pip install build
```
```
python3 -m build <path_to_dearpypixl_dir>
```
```
python3 -m pip install <path_to_generated_whl>
```

# Overview
Dear PyPixl is not undocumented. The information below supplements the detailed information available via docstrings. However, I highly suggest visiting Dear PyGui's [documentation](https://dearpygui.readthedocs.io/en/latest/index.html) if you are unfamiliar with the project. Basic usage of Dear PyPixl is very similar (identical) to that of Dear PyGui, and you may feel lost without some background.

## Item Interfaces
#### Creating Interfaces
An item type is, functionally, a drop-in replacement for any Dear PyGui function that would create item an item;
```python
from dearpypixl import *


window = Window(label="A window")
button = Button(
    label="A button",
    callback=lambda: print("stuff is happening...!",
    parent=window
)
```

For container items, Dear PyGui offers two functions; a "normal" one, and a context manager. The class replaces *both*;
```python
from dearpypixl import *


with Window(label="A window") as window:
    button = Button(label="A button", callback=lambda: print("stuff is happening...!"))
```


While calling `dearpygui.add_window` or `dearpygui.window` returns a **tag**, or a unique integer or string identifier, for the created window, the above results in an **item interface** object. Interfaces *are* item identifiers - integers specifically - and can be used wherever an item tag is appropriate. For the lifetime of the interface, instance-bound methods will operate exclusively on the interfaced item. In the case above, the "interfaced item" was created along with the interface. However, there are ways to create interfaces for existing items, too;
```python
from dearpypixl import *
import dearpygui.dearpygui as dpg


with Window() as window:
    button_id = dpg.add_button(tag="a button")

# Method 1A: Call the interface class and include an existing `tag`
button_if1 = Button(tag=button_id)   # -> `mvButton(tag=..., alias='a button', ...)`
# Method 1B: Call the `.new` classmethod
button_if2 = Button.new(button_id)   # -> `mvButton(tag=..., alias='a button', ...)`

# Method 2: Use the `interface` function
button_if = interface(button_id)     # -> `mvButton(tag=..., alias='a button', ...)`

# Method 3: Use the `mvAll` interface class
generic_if = mvAll(button_id)        # -> `mvAll(tag=..., alias='a button', ...)`
```

The first is pretty intuitive; include the `tag` keyword argument when creating an interface. If the `tag` value is an existing item identifier, a new interface object will be created but won't (rather, *can't*) create a new item. This is useful when using primitive interfaces and when you are aware of the type of item you're interfacing with. However, this isn't without caveats. User-defined interfaces often implement a custom `__init__` method -- you likely won't appreciate another initialization. Additionally, an exception is raised (and suppressed) when the interface fails to create a new item with the in-use `tag`, so this approach isn't recommended if you're doing it *thousands* of times within a short window. In either case, all interface types have a class-bound `.new` method. Accepting a sole positional `tag` argument, the `.new` method creates and returns an interface of that type while skipping instance initialization.

There may be times when you'll feel the need to query an item's type to find the correct interface. The `interface` function accepts a sole positional `tag` argument and a few other optional keywords. Its' default behavior is to query Dear PyGui for the item's type, find the appropriate class for that type, and return the result of calling the class' `.new` method. This procedure is faster than calling the class directly when the "item already exists" exception would be caught and discarded, even when you know the correct class beforehand.

Lastly, when just want an interface and you don't know and/or don't care to know the item and interface type, or the interface is just a "stepping stone" to another one (like a parent or child), consider creating a generic item interface with `mvAll`. These interfaces have a *very* broad API, supporting items of any type to some degree. Their creation process is greatly simplified from that of other interfaces, so they're fast to make. The downside is their benefits -- they're *generic*. Some methods only work when interfacing with items of specific types. Additionally, their lack of type identity and simplified creation procedure means that they do not create items or generate identifiers. They also lack behaviors unique to more "narrow" interface types; as a convenience, however, they can be used as context managers when interfacing with container items.


> **Note:** *No attempts are made to stop you from trying to bind an interface to an existing item of a different or unsupported type. Don't expect things to go well.*

<br>

#### Methods & Properties
The members available to an inteface can vary based on the type of item it supports. This means that some interfaces can have a fairly large API. However, all of them do share a collection of core methods and properties. While member names are not 1-to-1, they are named similarly to that of the used Dear PyGui hook. While not exhaustive, the table below outlines many of them;

| Bound Interface Method   | Dear PyGui Function                     |
| :----------------------: | :-------------------------------------: |
| `item.configure(...)`    | `configure_item(item, ...)`             |
| `item.configuration()`   | `get_item_configuration(item)`          |
| `item.information()`     | `get_item_info(item)`                   |
| `item.state()`           | `get_item_state(item)`                  |
| `item.delete(...)`       | `delete_item(item, ...)`                |
| `item.set_font(...)`     | `bind_item_font(item, ...)`             |
| `item.set_theme(...)`    | `bind_item_theme(item, ...)`            |
| `item.set_handlers(...)` | `bind_item_handler_registry(item, ...)` |

In addition, a few other information-related hooks are also available;
| Bound Interface Method   | Dear PyGui Function                                                |
| :----------------------: | :----------------------------------------------------------------: |
| `item.children(...)`     | `get_item_info(item)['children']`<br>`get_item_children(item, ...)`|
| `item.get_font()`        | `get_item_info(item)['font']`<br>`get_item_font(item)`             |
| `item.get_theme()`       | `get_item_info(item)['theme']`<br>`get_item_theme(item)`           |
| `item.get_handlers()`    | `get_item_info(item)['handlers']`<br>`get_item_handlers(item)`     |

Note that the `.configuration` and `.state` methods are not functionally equivelent to Dear PyGui's `get_item_configuration` and `get_item_state` functions respectively. The `.configuration` method is unique to each dedicated interface type, and filters out useless item configuration options. This allows for the usage of the `type(item)(**item.configuration())` idiom -- in most cases, this creates a "reproduction" or proto-copy of an item. The behavior of the `.state` isn't as glamorous; unlike `get_item_state`, the dictionary returned by the `.state` method includes keys for every state an item could possibly have. When an item does not support a Dear PyGui state, the value of that state in the returned dictionary will be `None`. By default, the mapping returned by the `.information` method is unchanged from that returned by Dear PyGui's `get_item_info` function.

<br>
<br>

Usage of the `configuration`, `information`, and `.state` methods is common. As a convenience, interfaces also expose various configuration, information, and state options as properties. Availible configuration properties vary between interface types; expect one for each key in the dictionary returned from the `.configuration` method. In contrast, available information-related properties are consistent between all item interface types. However, only the most useful/common-use are exposed;

| Interface Property | Interface Method Hook                             |
| :----------------: | :-----------------------------------------------: |
| `item.parent`      | `item.information()['parent']`                    |
| `item.theme`       | `item.get_theme()`<br>`item.set_theme(...)`       |
| `item.font`        | `item.get_font()`<br>`item.set_font(...)`         |
| `item.handlers`    | `item.get_handlers()`<br>`item.set_handlers(...)` |

The *get* behavior of these properties are not equivelent to their related *get* hook. Calling the method returns an item identifier (or None) as returned by Dear PyGui, where the property returns an item interface when applicable. This means that `.theme`, `.font`, `.handlers` can return `None`, or an instance of `mvTheme`, `mvFont`, or `mvItemHandlerRegistry` respectively.

<br>

State-related properties don't do anything fancy. They return the value of the related state as returned by the `.state` method, unchanged;

| Interface Property               | Interface Method Hook                    |
| :------------------------------: | :--------------------------------------: |
| `item.is_ok`                     | `item.state()["ok"]`                     |
| `item.is_hovered`                | `item.state()["hovered"]`                |
| `item.is_active`                 | `item.state()["active"]`                 |
| `item.is_focused`                | `item.state()["focused"]`                |
| `item.is_clicked`                | `item.state()["clicked"]`                |
| `item.is_left_clicked`           | `item.state()["left_clicked"]`           |
| `item.is_right_clicked`          | `item.state()["right_clicked"]`          |
| `item.is_middle_clicked`         | `item.state()["middle_clicked"]`         |
| `item.is_visible`                | `item.state()["visible"]`                |
| `item.is_edited`                 | `item.state()["edited"]`                 |
| `item.is_activated`              | `item.state()["activated"]`              |
| `item.is_deactivated`            | `item.state()["deactivated"]`            |
| `item.is_deactivated_after_edit` | `item.state()["deactivated_after_edit"]` |
| `item.is_resized`                | `item.state()["resized"]`                |
| `item.rect_min`                  | `item.state()["rect_min"]`               |
| `item.rect_max`                  | `item.state()["rect_max"]`               |
| `item.rect_size`                 | `item.state()["rect_size"]`              |
| `item.content_region_avail`      | `item.state()["content_region_avail"]`   |

The above properties are consistent across all interface types; one for every possible item state...*almost*. Many items support explicit positioning via the `pos` configuration option. However, queries regarding an item's position are made by checking it's state, making `pos` a bit of an odd-ball. As previously mentioned, the mapping returned by the `.state` method includes keys for *all possible* states, which includes `pos`. Because of this behavior, interfaces only have a `pos` property (read-write) when the supported item type support explicit positioning (`item.state()['pos'] != None`).

<br>

#### Behaviors
Some interface types implement unique behavors or inherit them from a parenting proto-type(s). Previous examples demonstrate using **interfaces as context managers** -- a behavior unique to **container-type** and `mvAll` interfaces;

```python
with Window() as window:
    button = Button(tag=40000)

with window:
    text = Text("Some text", tag=50000)
```
You'll get yelled at when trying that kind of thing with a primitive button interface;
```python
with button:  # -> `TypeError: 'mvButton' object does not support the context manager protocol`
    ...
```

<br>
<br>

**All interfaces** support some kind of **indexing and slicing** behavior. By default, this operates on the item's child slots; specifically the result of `.information()["children"]` (not the `.children` method). Although only useful for containers, even basic items like buttons have child slots;
```python
# This is equivelent to `window.children(1)`, returning the
# contents of child slot 1.
window[1]   # -> [40000, 50000]
# We can do this  with non-containers, too. Every slot will
# be empty, though.
button[1]   # -> []

# Slice to include several slots;
window[0:]  # -> [[], [40000, 50000], [], []]
```
Meanwhile, theme element and "series"-type interfaces override the above behavior. Indexing, slicing, and rich comparisons operate on the item's value. In particular, they behave like lists of a fixed size;
```python
from dearpypixl import *
from dearpypixl import color, style

with Theme() as theme:
    with ThemeComponent():
        # `dearpygui.add_theme_color(
        #     dearpygui.mvThemeCol_WindowBg,
        #     (200, 50, 50, 250),
        #     category=dearpygui.mvThemeCat_Core,
        # )`
        window_bg = color.WindowBg(200, 50, 50, 250)

# theme elements are semi-mutable lists (values can change, but not shape)
window_bg == window_bg.get_value() == list(window_bg) == [*window_bg] == [200, 50, 50, 250]  # -> `True`

# update the alpha channel
window_bg[-1] = 200
window_bg.get_value()  # -> `[200.0, 50.0, 50.0, 200.0]`

# update color channels
window_bg[:-1] = [50, 200, 50]
window_bg.get_value()  # -> `[50.0, 200.0, 50.0, 200.0]`
```

<br>
<br>

Additionally, primitive interfaces can be **pickled**;
```python
import pickle
from dearpypixl import *


with Window(label="a window") as window:
    Text("some text")
    with ChildWindow(label="a child window"):
        InputText(default_value="more text")

pickled = pickle.dumps(window)

# If we were to load the pickled tree now, it would
# only copy the interface state. The tree would not
# be reproduced.
window.delete()

# Reload the pickled hierarchy. Since the item tree
# no longer exists, this will recreate the interface
# state and the item tree.
window = pickled.loads(pickled)
```

The pickling process is fairly comprehensive. It creates a save state of the target's alias, configuration (including `pos` and `source`), bindings (theme, etc), children, and value. This procedure is repeated on the target's children recursively, ensuring that the *entire* item tree from the target is included. Item `source`s are uniquely handled so that they can be properly set even if the actual source item is created further down the hierarchy. The process also pickles interfaces found on user-defined interfaces (again, recursively). When an item hierarchy is about to be pickled, all items/interfaces found are ensured to have assigned **aliases** at the time of serialization. If an item does not have an alias, one is generated automatically using its' current integer id and a universally-unique id created using the `uuid` module's `uuid4` function<b>*</b>.

Below is a more complex, working example. Note that both `window` and `theme` are destroyed before reloading the pickled hierarchy. The `mvHandlerRegistry` interface object on `window.events`, however, is not. The loading process still creates a `mvHandlerRegistry` interface and sets it on the reconstructed `window.events` interface, but the handler registry itself is not recreated since it exists already.

```python
import pickle
from dearpypixl import *


class UserWindow(Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # covered through interface association
        self.events = HandlerRegistry()


with Theme() as theme:
    with ThemeComponent() as tc:
        window_bg = color.WindowBg(200, 50, 50, 250)

with UserWindow(label="a window") as window:
    # covered through item association (binding)
    window.theme = theme

    # covered through item association (children)
    text = Text("some text")
    with ChildWindow(label="a child window") as child_window:
        input_text = InputText(default_value="more text")
        with Plot(label="and an empty plot"):
            ...
    text.source = input_text  # `source` will be properly reflected


window_pkl = pickle.dumps(window)

window.delete()
theme.delete()

window = pickle.loads(window_pkl)
```

Items/interfaces are pickled from the top-down and does not traverse upward. This is important because parent references of serialized items are *not* tracked. Instead, a loaded "parent" explicitly passes itself down to its' children during the loading process. This is a non-issue when pickling an entire item tree since root items don't require parents. Things are different when pickling item *branches*; the top-level pickled item/interface needs a parent! Simply load the branch while a suitable parent is atop the container stack;
```python
with Window(label="a window") as window:
    Text("some text")
    with ChildWindow(label="a child window") as child_window:
        InputText(default_value="more text")

child_wndw_pkl = pickle.dumps(child_window)
child_window.delete()

# load the saved branch within a completely different parent
with Window():
    with Table():
        TableColumn()
        with TableRow():
            child_window = pickle.loads(child_wndw_pkl)


```
Avoid "reference tangles" when making pickle-able trees. An interface of a user-defined type should not keep a reference of a non-root item of a completely different branch. Similarly, don't set item `source`s to items in other branches. The pickling procedure will assign aliases to such items, but will not attempt to pickle the item or reference. The below example results in a `RuntimeError` while trying to load reload `window2`;
```python
with Window() as window1:
    w1_text1 = Text()
    w1_text2 = Text(source=w_text1)


with Window() as window2:
    w2_text = Text(source=w1_text1)  # "reference tangle"


# create a snapshot while `w2_text` is still "outsourcing"
window2_pkl = pickle.dumps(window1)
window1.delete()
window2.delete()

pickle.loads(window2_pkl)  # -> `RuntimeError()`
```
A good solution for the above is using value registries, ensuring they are loaded first before anything else. Interfaces of user-defined types have an advantage here, as different interfaces can hold different (or same, doesn't matter) interfaces that operate on the same item (like a value registry). In that case, the value registry would always be loaded regardless of the load order of those that reference it.



> ***Pickling** is an **experimental feature**. Please submit a bug report if a primitive interface fails to serialize.*

<br>

## Item Types

In Dear PyPixl, each of Dear PyGui's item types are represented by a subclass of `AppItemType`. Easily identifiable by their "mv" prefixes, class names mirror the name of the internal type it represents and *not* necessarily the name of the Dear PyGui function used to create items of that type (although, they usually go hand-in-hand). The adherence to a specific naming nomenclature means that some names can be a bit...verbose. As a convenience, classes are aliased (some more than once) to be less-so, or to make them easier to identify from other types;
```python

# most are straight-forward;
ChildWindow == mvChildWindow
DrawNode == mvDrawNode
# some are obvious...
Window == mvWindowAppItem
# some aren't...
HistogramSeries2D == mv2dHistogramSeries
PlotAnnotation == mvAnnotation
```
<br>

The classes themselves would be poor representations if you couldn't gleam some useful information from them. Casting an item class as an `int` or `str` yields a bit of information regarding the represented type; `str(mvWindowAppItem)` will always compare equal to `dearpygui.get_item_type(item)` when `item` is a window item identifier, wheras casting to an integer returns the enumeration value of the internal type -- the latter compares equal to a similarly-named constant found in the `dearpygui` namespace. Classes also have a `.command` attribute; the (non-context manager) function that is typically called to create items of that type. In addition, several class-level properties regarding the item type's "category" and/or identity are exposed;

```python
import dearpypixl as *


# ItemType       | String Repr                      | Int Repr       | Function
# ------------------------------------------------------------------------------------
mvButton         # "mvAppItemType::mvButton"        | 2              | `add_button`
mvText           # "mvAppItemType::mvText"          | 28             | `add_text`
mvInputText      # "mvAppItemType::mvInputText"     | 1              | `add_input_text`
mvWindowAppItem  # "mvAppItemType::mvWindowAppItem" | 33             | `window`, `add_window`
mvLabelSeries    # "mvAppItemType::mvLabelSeries    |                | `add_text_point`


...


str(mvWindowAppItem) == dpg.get_item_type(dpg.add_window())  # True
int(mvWindowAppItem) == dpg.mvWindowAppItem                  # True
mvWindowAppItem.command == dpg.add_window                    # True

# some class-level properties
mvWindowAppItem.is_root_item  # True
mvWindowAppItem.is_container  # True
mvWindowAppItem.is_node_item  # False
```

<br>

## Global State & Setup
The examples in the previous section omitted any of Dear PyGui's usual setup. Below is one of the first few examples used in a previous section with the added required setup. I'm sure it's a lot to take in;

```python
from dearpypixl import *


with Window(label="A window") as window:
    button = Button(label="A button", callback=lambda: print("stuff is happening...!"))

Runtime.start()
```


The framework does the bulk of the setup automatically with a 2-step procedure. The first step, the initial application setup (`create_context()`, `setup_dearpgui()`, etc), is done when a user creates the very first item interface, while the second step is done within `Runtime.start()`. The latter will perform the initial setup if necessary (in the event that no interfaces are made) in addition to verifying the state of the viewport (creating and showing it as needed) before starting the runtime loop. Dear PyPixl may also run the initial application setup when using a part of the API that requires initializing Dear PyGui.

Just because setup is done automatically doesn't mean the framework obfuscates the process from users. Any and/or all setup can be performed manually using Dear PyGui's API or through Dear PyPixl. Regardless, the framework will always be aware of what needs done, and what doesn't. In Dear PyPixl, users can run setup procedures and manage global-level settings using the `Application`, `Viewport`, `Runtime` classes. They, like modules, have very "functional" API. Like classes (and unlike modules), they support overrides and extending through subclassing, while not interfering with anything relying on the original implementations. They are not, however, fundamentally different from item interfaces;


```python
from dearpypixl import *
import dearpygui.dearpygui as dpg



# manually perform app setup (optional)
Application.create_context()  # `dearpygui.create_context()`
Application.prepare()         # `dearpygui.setup_dearpygui()`

Application.state()['ok']     # | -> True (False if the above is not done yet)
Application.is_ok             # |

# update application settings, just like item interfaces
# NOTE: If we did not manually run setup, DPX would do it
# at `Application.docking = True` below, since it requires
# DPG initialization.
Application.docking = True
Application.docking           # -> True
Application.configure(docking=False)
Application.docking           # -> False

app_theme = Theme(label="Application Theme")
# set the application theme
Application.theme = app_theme
# unlike Dear PyGui's API, you can always fetch it later...
Application.theme.label      # -> "Application Theme"
# REGARDLESS of how you set it...
dpg.bind_theme(None)
Application.theme            # -> None
Application().theme = app_theme
Application.theme.label      # -> "Application Theme"

# the returned mapping mirrors `Item.information(...)`, so
# it includes `font` and `theme`
Application.information()    # -> {'type': 'Application', ..., 'font': None, ...}

# Even though the class and instances operate on the
# same state(s), they are NOT the same object
Application is Application()    # -> False
Application == Application()    # -> False
# again, different objects
Application() is Application()  # -> False



# manually setup the viewport (again, optional)
Viewport.state()['ok']          # | -> False (True once created)
Viewport.is_ok                  # |
Viewport.create()
Viewport.is_ok                  # -> True

Viewport.state()['visible']     # | -> False (not shown yet)
Viewport.is_visible             # |
# `Viewport.show()`, but using DPG's API because, again, DPX
# knows. It knows, and it will always know.
dpg.show_viewport()
Viewport.is_visible             # -> True

# NOTE: If application setup has not been done up until now,
# DPX will do so before creating the `window` interface/item.
with Window(label="A window", tag=50000) as window:
    button = Button(label="A button", callback=lambda: print("stuff is happening...!"))

# second verse, same as the first
Viewport.width = 700
dpg.configure_viewport(
    "DPG NOT USED YET",  # `Viewport.tag`
    label="IT ALWAYS KNOWS",
)
# Unique to DPX, 'primary_window', 'callback', and 'user_data'
# are "configuration". All three of these cannot be fetched
# using DPG's API, while 'callback', and 'user_data' cannot be
# set separately. DPX sets things right.
Viewport.configure(
    height=550,
    primary_window=window,
    callback=lambda sender, app_data, user_data: print(user_data),
    user_data="the cake is delicious",
)
Viewport.user_data = "the cake is a lie"
Viewport.configuration() # -> {
#    'label'         : 'IT ALWAYS KNOWS',
#    'width'         : 700,
#    'height'        : 550,
#    ...,
#    'primary_window': 50000,
#    'callback'      : <function <lambda> at ...>,
#    'user_data      : 'the cake is a lie',
# }


# NOTE: DPX will run any app or viewport setup we
# missed (we didn't miss any) before starting the
# runtime.
Runtime.start()
```
 <br>
 <br>

`Application` and `Viewport` interface with already existing global states. `Runtime` is a bit different because the "runtime" state is unique to Dear PyPixl -- manufactured through patching Dear PyGui's API holes and other various things, so it's API is less obvious. The runtime state is the state of the main event loop. This encompasses things like starting and stopping the runtime, target frame rate, and events that occur within the loop such as those scheduled to run on specific frames. It's the closest thing Dear PyPixl has to a `tkinter.Tk`, `kivy.app.App`, etc.

The `Runtime` class' `.start` method implements a general-purpose event loop. Although kept relatively simple, it is more complex than most user implementations. It uses a synchronized fixed time step to decouple task execution from rendering. Tasks can be pushed to the event loop using the `queue.Queue` object found on `Runtime.queue`, but users replace it with another object implementing `queue.Queue`s protocol before starting the event loop. Tasks are de-queued upon prior to their execution. However, tasks can re-queue themselves, making them reoccuring tasks.
```python
from dearpypixl import *


def printer():
    print('the cake is a lie')

# this is ran once
Runtime.queue.put(printer)


with Window() as window:
    ...

def print_window_state():
    print(window.state())
    Runtime.queue.put(print_window_state)

# this is re-occuring
Runtime.queue.put(print_window_state)

# Since task execution is fairly isolated, the
# re-occuring task will not block rendering frames.
# A LONG running task may result in dropped frames,
# though.
Runtime.start()
```
The number of tasks executed is limited to a number of real-time milliseconds, set on `Runtime.update_interval`.

<br>

Frame rate can be managed by updating the `target_frame_rate` and `clamp_frame_rate` attributes. When `clamp_frame_rate` is True, the number of frames rendered per second is limited to the value of `target_frame_rate`, as long as it isn't zero or `None`. These values can be updated at any time, even after the event loop has started.
```python
from dearpypixl import *


def print_frame_rate():
    print(Runtime.frame_rate())
    Runtime.queue.put(print_frame_rate)

Runtime.queue.put(print_frame_rate)


# limit to 30 fps
Runtime.target_frame_rate = 30
Runtime.clamp_frame_rate  = True

Runtime.start()
```

<br>

## Modules

Only interface types are exposed directly within the `dearpypixl` namespace. Other useful tools and extensions are housed within their respective modules;
* `api`: Contains the lower-level API used by the framework.
* `typing`: Exposes type aliases and protocols used by the library. In addition to the `AppItemType` base class, primitive interface bases, abstract bases, and protocols for Dear PyGui's `mvBuffer`, `mvVec4`, and `mvMat4` objects.
* `constants`: Stores static Dear PyGui and Dear PyPixl values/variables as enumerations.
* `events`: Extensions of callback-related interface types and related utilities.
* `theming`: Extensions of theme and font-related interface types.
* `color`, `style`: Contains helper functions for creating specific theme color and style elements.
* `console`: Homebrew stream and console-related item interfaces.
* `grid`: Contains the `Grid` item layout manager, which leverages the ability to explicitly position items to emulate a table-like layout without creating any items.
<br>

## Limitations, Bugs, & Gachas

Dear PyPixl tries to maintain the same semantics and feel that Dear PyGui has so that it's intuitive coming from Dear PyGui, while being different in ways that only benefit the user. However, there are some situations and use-cases where Dear PyGui and Dear PyPixl and aren't exactly 1-to-1 due to implementation details of the framework, bugs within Dear PyGui, etc. Below explains some of Dear PyPixl's behavior and some consequences that stem as a result.
<br>


#### Interfaces are Integers, For Better or Worse

Interface types are derived from Python's built-in `int` type. This allows interfaces to be used as arguments where item identifiers are expected. In addition, it simplifies the public and internal API's alike in regards to interface and item creation. This unfortunately has a few side effects;
* interface subclasses **cannot declare non-empty `__slots__`**
* interfaces cannot include a `__weakref__` attribute, meaning they **cannot have proxies**
* **`__bool__` cannot be implemented**

The last limitation has less to do with `int` and more to do with how Dear PyGui is inspecting identifier values. `__bool__` must operate on the integer value of the interface; hard-to-diagnose bugs *will* occur otherwise. For this reason, Dear PyPixl will throw a `TypeError` when defining an interface class that does not point to `int.__bool__`.

<br>

#### Passing Explicit UUID's and Aliases

Item-creating functions in Dear PyGui all accept a `tag` keyword argument in the form of an item's integer identifier (*uuid*) or string *alias*. While Dear PyPixl does its' best to accomodate, **the basic interface constructor cannot properly manage aliases when the alias is new**. This is in part due to Dear PyPixl's internal design, along with the fact that Dear PyGui's item registry API was never finished. Since the interface's creation logic (`.__new__`) is isolated from the item creation logic (`.__init__`), Dear PyPixl would need to register the new alias to a new uuid in advance. This can be done, however, Dear PyGui does not behave as expected in any scenario.

As a workaround, interfaces have the `.aliased` class method, an alternative constructor, which will set the alias onto the item once it is created. Note that this is only necessary when creating the interface would also cause the interfaced item to be created, while aliases of existing items can be passed as normal.

As is recommended when using Dear PyGui, users should *not* generate their own integer identifiers for Dear PyPixl interfaces.

<br>

# FAQ

---

**Q**: **Performance?**

**A**: The framework tries to keep a very low profile. When profiling on a pretty low-performance machine, creating one million window items with `mvWindowAppItem` took 15.72 seconds (worst-case); only ~1.2 seconds of that was spent executing Dear PyPixl code. Marginal overhead is to be expected for methods, properties, etc. as there are simply more function calls. In high-traffic areas like the main runtime loop, consider using the `.configuration`, `.information`, and `.state` methods over interface properties.


---

**Q**: **Can I use both Dear PyPixl and Dear PyGui code in my project?**

**A**: **Yes**, and you are **encouraged to do so**.

---

**Q**: **I need to conform to an older version of Dear PyGui. Can I still use this?**

**A**: On paper? **No**. Dear PyPixl will absolutely *not* work with Dear PyGui beta versions (pre-1.0).

However, key areas in the framework were developed using Dear PyGui v1.8.0. A lot may work, some stuff won't. You are welcome to try.

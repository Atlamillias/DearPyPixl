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

## Features
 - extensible high-level object-oriented API for creating and/or interfacing with Dear PyGui items, including theme elements
 - low-level API that fills various gaps in Dear PyGui's API
 - strongly typed
 - allows the use of both `dearpypixl` and `dearpygui` code together with minimal conflicts
 - typing for `mvBuffer`, `mvVec4`, and `mvMat4`
 - improved docstrings, errors, and type signatures
 - contains numerous extensions and other helpful tools
<br>

## Requirements
 - Operating System; Windows 8.1+, MacOS, Linux*
 - Python: 3.10 x64* (or newer)
 - `pip` dependencies:
    * `dearpygui` 1.9 (or newer)
    * `typing-extensions` (Python < 3.12 only)

*Dear PyPixl is available on all platforms already supported by Dear PyGui. Availability for 32-bit systems and Raspberry Pi OS is *loosely* supported, but requires building Dear PyGui from the source. Please visit their [wiki](https://github.com/hoffstadt/DearPyGui/wiki) for more information.
<br>

## Installation

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
Dear PyPixl is not undocumented -- the information below supplements the detailed information is available via docstrings. However, I highly suggest visiting Dear PyGui's [documentation](https://dearpygui.readthedocs.io/en/latest/index.html) if you are unfamiliar with the project. Basic usage of Dear PyPixl is very similar (identical) to that of Dear PyGui, and you may feel lost without some background.

## Item Interfaces
##### Creating Interfaces
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


The only difference between creating items using an item type class and using a Dear PyGui function is the return value. Where the latter returns a **tag**, or a unique integer or string identifier for the item, the former results in an **item interface** object. Interfaces *are* item identifiers - integers specifically - and can be used wherever an item tag is appropriate. For the lifetime of the interface, instance-bound methods will operate exclusively on the interfaced item. In the case above, the "interfaced item" was created along with the interface. However, interfaces can be made for existing items as well by passing its' identifier to the `mvAll` type, the `interface` function, or as the `tag` keyword argument to the appropriate item type for the item you're interfacing with.

`mvAll` is the generic interface type. Its' API supports every kind of item to some degree, but lacks type identity. As such, it does not implement custom behavior that a more *narrow* interface may have. However, creating them is extremely fast. In addition, the lack of custom behaviors makes their API more performant. This is a good option when you don't care to work with an interface for very long, you don't know the item's type and/or don't care to know, or the item is just a stepping stone to get to another item. Note that `int(mvAll)` will always return `0`.

If you know the type of the item you're trying to interface with, you can simply call the appropriate class and include the item identifier as the value for the `tag` keyword. After the interface is created, it will try to create a new item using its' bound identifier. It can't, however, as an item with the bound identifier already exists. The error is silenced and life continues as normal. Consider this option when you care about the specific item you're working with, or you are intending to work with it for a little bit. This option does have an overhead penalty since the process causes an exception, which may be noticable when it happens a lot. This process also involves creating a new instance, invoking the `__new__` and `__init__` constructor methods. This is a non-issue for "built-in" item types, but user subclasses often implement a custom `__init__`, and likely won't appreciate another initialization. As an alternative, item types have a class-bound `.new` method. Accepting a sole positional `tag` argument, the `.new` method creates and returns an interface of that type while skipping instance initialization.

Lastly, when you want a proper interface for an item and would need to query Dear PyGui for its' type, consider using the `interface` function found in the `dearpypixl` root namespace. The `interface` function accepts a sole positional `tag` argument and a few other optional keywords. Its' default behavior is to query Dear PyGui for the item's type, find the appropriate class for that type, and return the result of calling the class' `.new` method. This procedure is faster than calling the class directly when the "item already exists" exception would be caught and discarded, even if you know the class beforehand.

Here's an example using each of the methods above to create an interface for an existing button item (the *same* button item);
```python
from dearpypixl import *
import dearpygui.dearpygui as dpg


with Window() as window:
    button_id = dpg.add_button(tag=40000)


# Method 1: `mvAll`
generic_if = mvAll(button_id)        # -> `mvAll(tag=40000, ...)`

# Method 2A: `Button`
button_if1 = Button(tag=button_id)   # -> `mvButton(tag=40000, ...)`
# Method 2B: `Button.new`
button_if2 = Button.new(button_id)   # -> `mvButton(tag=40000, ...)`

# Method 3: `interface`
button_if = interface(button_id)     # -> `mvButton(tag=40000, ...)`
```


> **Note**: Dear PyPixl makes no attempt to not stop you from using the wrong interface type for an item.

<br>
##### Methods & Properties

With a half-dozen ways to make interfaces, some methods would be nice. Interfaces can have a fairly large API. While member names are not 1-to-1, Dear PyGui users should easily be able to make the connection between the two APIs. The table below outlines the core interface API and the equivelent Dear PyGui function;

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

Unlike `get_item_configuration`, the dictionary returned from the `.configuration` method of type-specific interfaces does not include "useless" configuration options. The opposite is true for the `.state` method, which includes keys for every available state an item can have. The value for the state key will be `None` if the state is unsupported for the item. With the exception those two methods, all other members in the above tables that return a value do so as returned from Dear PyGui and are not mutated by Dear PyPixl.

Interfaces also expose several configuration, information, and state options as properties. The configuration properties availible vary depending on the type of item interface; expect one for each key in the dictionary returned from the `.configuration` method. In contrast, available information-related properties are consistent between all item interface types;

| Interface Property | Interface Method Hook                             |
| :----------------: | :-----------------------------------------------: |
| `item.parent`      | `item.information()['parent']`                    |
| `item.theme`       | `item.get_theme()`<br>`item.set_theme(...)`       |
| `item.font`        | `item.get_font()`<br>`item.set_font(...)`         |
| `item.handlers`    | `item.get_handlers()`<br>`item.set_handlers(...)` |

Where the related method hook can return an item identifier, the property will return an interface for the item instead. This means that `.theme`, `.font`, `.handlers` will return an instance of `mvTheme`, `mvFont`, or `mvItemHandlerRegistry` respectively, or `None`.


> **Note**: As a reminder, both Dear PyGui and Dear PyPixl do not distinguish item identifiers and item interfaces differently when used as item-related arguments.

<br>
<br>

Like the above, state-related properties are consistent across all interfaces. And, like configuration properties, one exists for each item state. They are all read-only, and return the value as returned from the `.state` method;

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

Unfortunately, there is a sole exception. While `pos` is always included in the return of calling the `.state()` method (as a 2-item list, or `None` if unsupported), not all interface types implement the `.pos` property. This is because it can be updated as a configuration option via `configure_item` function or the `.configuration` method for items that do support explicit positioning. If an interface type implements the `.pos` property, it is writable. If it doesn't, then `.state()["pos"]` will always return `None`.


<br>
##### Behaviors
An interface type may implement or inherit behavior from a parenting proto-type. A previous example was given where an interface was used as a context manager;

```python
with Window() as window:
    button = Button(tag=40000)

with window:
    text = Text("Some text", tag=50000)
```
This behavior is unique to container-type interfaces, in addition to instances of `mvAll`. An exception will be thrown trying to do the same for the button;
```python
with button:  # this doesn't work
    ...
```

<br>
By default, all interfaces support indexing and slicing. This operates on the result of calling the `.children` method. Although it is only useful for container-types, even basic items have child slots;

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

Meanwhile, theme color/style and "series"-type interfaces override the above behavior. Indexing, slicing, and rich comparisons operate on the item's value;
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

Primitive interfaces can be pickled. This works by ensuring the items have assigned **aliases** at the time of serialization.
```python
import pickle
from dearpypixl import *


with Window(label="a window") as window:
    Text("some text")
    with ChildWindow(label="a child window"):
        InputText(default_value="more text")
        with Plot(label="and an empty plot")


```

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

`Application` and `Viewport` interface with already existing global states. `Runtime` is a bit different because the "runtime" state is unique to Dear PyPixl -- manufactured through patching Dear PyGui's API holes and other various things, so it's API is less obvious. The runtime state is the state of the main event loop. This encompasses things like starting and stopping the runtime, target frame rate, and events that occur within the loop such as those scheduled to run on specific frames. It's the closest thing Dear PyPixl has to a `tkinter.Tk`, `kivy.app.App`, etc.
<br>

## Modules

Only interface types are exposed directly within the `dearpypixl` namespace. Other useful tools and extensions are housed within their respective modules;
* `api`: Contains the lower-level API used by the framework.
* `typing`: Defines common type variables, aliases, and protocols used throughout the library, including `mvBuffer`, `mvVec4`, and `mvMat4`.
* `constants`: Stores static Dear PyGui and Dear PyPixl values/variables as enumerations.
* `interface`: Home to the `AppItemType` base class and other primitive interface types, in addition to the `ABCAppItemType` class and `ABCAppItemTypeMeta` metaclass for creating abstract interface types.
* `events`: Extensions of callback-related interface types.
* `theming`: Extensions of theme and font-related interface types.
* `color`, `style`: Exposes theme color and style elements as individual interface types.
* `console`: Homebrew stream and console-related item interfaces.
* `grid`: Contains the `Grid` item layout manager, which leverages the ability to explicitly position items to emulate a table-like layout without creating any items.
<br>

## Limitations, Bugs, & Gachas

Dear PyPixl tries to maintain the same semantics and feel that Dear PyGui has so that it's intuitive coming from Dear PyGui, while being different in ways that only benefit the user. However, there are some situations and use-cases where Dear PyGui and Dear PyPixl and aren't exactly 1-to-1 due to implementation details of the framework, bugs within Dear PyGui, etc. Below explains some of Dear PyPixl's behavior and some consequences that stem as a result.
<br>


##### Interfaces are Integers, For Better or Worse

Interface types are derived from Python's built-in `int` type. This allows interfaces to be used as arguments where item identifiers are expected. In addition, it simplifies the public and internal API's alike in regards to interface and item creation. This unfortunately has a few side effects;
* interface subclasses **cannot declare non-empty `__slots__`**
* interfaces cannot include a `__weakref__` attribute, meaning they **cannot have proxies**
* **`__bool__` cannot be implemented**

The last point has less to do with `int` and more to do with how Dear PyGui is inspecting identifier values. `__bool__` must operate on the integer value of the interface; hard-to-diagnose bugs *will* occur otherwise. For this reason, Dear PyPixl will throw a `TypeError` when defining an interface class that does not point to `int.__bool__`.
<br>

##### Passing Explicit UUID's and Aliases

Item-creating functions in Dear PyGui all accept a `tag` keyword argument in the form of an item's integer identifier (*uuid*) or string *alias*. While Dear PyPixl does its' best to accomodate, **the basic interface constructor cannot properly manage aliases when the alias is new**. This is in part due to Dear PyPixl's internal design, along with the fact that Dear PyGui's item registry API was never finished. Since the interface's creation logic (`.__new__`) is isolated from the item creation logic (`.__init__`), Dear PyPixl would need to register the new alias to a new uuid in advance. This can be done, however, Dear PyGui does not behave as expected in any scenario.

As a workaround, interfaces have the `.aliased` class method, an alternative constructor, which will set the alias onto the item once it is created. Note that this is only necessary when creating the interface would also cause the interfaced item to be created, while aliases of existing items can be passed as normal.

<br>

# FAQ

**Q**: **Performance?**

**A**: The framework tries to keep a very low profile. When profiling on a pretty low-performance machine, creating one million window items with `mvWindowAppItem` took 15.72 seconds (worst-case); only ~1.2 seconds of that was spent executing Dear PyPixl code. Marginal overhead is to be expected for methods, properties, etc. as there are simply more function calls. In high-traffic areas like the main runtime loop, consider using the `.configuration`, `.information`, and `.state` methods over interface properties.


---

**Q**: **Can I use both Dear PyPixl and Dear PyGui code in my project?**

**A**: **Yes**, and you are **encouraged to do so**.

---

**Q**: **I need to conform to an older version of Dear PyGui. Can I still use this?**

**A**: On paper? **No**. Dear PyPixl will absolutely *not* work with Dear PyGui beta versions (pre-1.0). Not a chance. However, key areas in the framework were developed using Dear PyGui v1.8.0. A lot may work, even when using slightly older versions -- you are welcome to try.

With using older versions of Dear PyGui, you may want to update the type stubs. At the time of writing, this can be done via `python3 -m dearpypixl` shell command (this requires that the parent process has write-access to Dear PyPixl's install directory). Note that this feature may be removed from Dear PyPixl without warning.


# Dear PyPixl
Dear PyPixl is a light-weight, object-oriented framework and toolkit for [Dear PyGui](https://github.com/hoffstadt/DearPyGui) with minimal dependencies and zero use restrictions (MIT license).

## Features

 - extensible object-oriented API for creating and/or interfacing with Dear PyGui items
 - allows users to use both `dearpypixl` and`dearpygui` code together with little to no conflicts between packages
 - contains *completely optional* tools to help solve common problems, such as;
      - **Grid** item layout manager
      - **Application** and **Viewport** classes that help manage their respective global states
      - **Runtime** main-loop manager for scheduling tasks, clamping frame rate, etc.

## Requirements

 - Operating System; Windows 8.1+, MacOS, Linux*
 - Python 3.11 x64 (or newer)
 - Dear PyGui 1.9 (installed automatically)

*Dear PyPixl is available on all platforms already supported by Dear PyGui. Support for 32-bit systems and Raspberry Pi OS is *loosely* supported, but requires building Dear PyGui from the source. Please visit their [wiki](https://github.com/hoffstadt/DearPyGui/wiki) for more information.

## Installation

Using pip;
```python
python3 -m pip install dearpypixl
```

Alternatively, build the wheel and install locally;
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
Before reading further, I suggest visiting Dear PyGui's [documentation](https://dearpygui.readthedocs.io/en/latest/index.html) if you are unfamiliar with the project. Basic usage of Dear PyPixl is very similar to that of Dear PyGui. As such, writing "dedicated" documentation is not currently on the to-do list. However, Dear PyPixl is *not* undocumented -- The core API, in addition to several modules and other caveats, includes fairly detailed information via their docstrings.

Dear PyPixl is part "framework", part "toolkit". Objects directly available in the `dearpypixl` namespace represent the "framework" part of the package, while other modules represent the "toolkit" part. The framework half is blissfully unaware of the toolkit half, but parts of the toolkit *may* depend on the framework. Dear PyPixl tries to be as "use only what you want" as possible, so tools are often isolated from each other.

## Item Type Classes

The bulk of the framework consists of classes derived from `AppItemType`, which are available in the `dearpypixl` namespace. Each class represents an internal Dear PyGui item type (derived from the framework's own `mvAppItem` base class). The name of each class mirrors the name of the internal type it represents, and *not* necessarily the name of the Dear PyGui function used to create items of that type (although they usually go hand-in-hand);
```python
import dearpypixl as dpx


# ItemType           | String Repr                      | Int Repr       | Function
# ------------------------------------------------------------------------------------
dpx.mvButton         # "mvAppItemType::mvButton"        | 2              | `add_button`
dpx.mvText           # "mvAppItemType::mvText"          | 28             | `add_text`
dpx.mvInputText      # "mvAppItemType::mvInputText"     | 1              | `add_input_text`
dpx.mvWindowAppItem  # "mvAppItemType::mvWindowAppItem" | 33             | `window`, `add_window`

```
Item type classes, when cast, compare equal to certain things. For example, `str(mvWindowAppItem)` will always compare equal to `dearpygui.get_item_type(item)` when `item` is a reference to a window item. Additionally, the class compares equal to a similarly-named constant in `dearpygui` when cast as an `int`;
```python
from dearpypixl import *
import dearpygui.dearpygui as dpg


# Because window items are commonly used, I got very annoyed of how friggin'
# lengthy `mvWindowAppItem` is. Only two item types are assigned aliases --
# it's one of them, as `mvWindow`.
wndw_id = dpg.add_window()
str(mvWindow) == dpg.get_item_type(wndw_id)  # True
int(mvWindow) == dpg.mvWindow                # True
mvWindow.command == dpg.add_window           # True

# As an `int`, `mvWindowAppItem` compares equal to the `dpg.mvWindow` const
# and internal type's enum value, so it can be used for stuff like this;
theme_component_id = dpg.add_theme_component(int(mvWindow), parent=dpg.add_theme())

```
Item types also have access to properties that return `True` if the item type falls under certain item "categories". For example, `mvWindow.is_root_item` will return `True`, while `mvWindow.is_node_item` will return `False`. These are class-bound, so they can be used on the class and its instances.

## Item Interfaces
By default, calling an item type class will also create an item in Dear PyGui of the same type. It's no different from calling the related Dear PyGui function; the rules, arguments, syntax, etc. is identical. If your setup uses a Python language server, it should provide the correct argument signature (which will mirror the related function's argument signature);
```python
from dearpypixl import *


with mvWindow(label="An Ordinary Window") as wndw:
    btn = mvButton(label="An Ordinary Button", callback=lambda: print("stuff happened...!"))

# DPG usually has two different functions for creating container items --
# one for "normal" usage, and one for context-manager usage. The same
# DPX class can be used both ways;
wndw2 = mvWindow("Another ordinary window")
btn2 = mvButton(parent=wndw2)  # gotta include the parent here

```
The only real difference when using either API to create items is what we are left with afterwards. The `add_window` function would return the **tag** -- the unique item identifier -- of the created window so we can mess with it later, where calling `mvWindow` returned an instance of `mvWindowAppItem`. As an **interface**, instance-bound methods will now operate exclusively on that item. They also have a *lot* of properties and methods, and many forward their calls to a Dear PyGui function of similar name. Below showcases a few of them, in addition to some behaviors added via dunder methods;
```python
# NOTE: Only a small handful of behaviors, methods, etc. are shown.
# There's more. A lot more.

# instances have useful string representations
str(wndw)                  # mvWindowAppItem(tag=1000, label='', parent=None)
# casting to type `int` yields the interfaced item's integer id
int(wndw)                  # 1000

# freely use existing container interfaces in a `with` statement
# for "runtime parenting"
with wndw:
    mvText("another child")

try:
    with btn:  # not a container...
        ...
except TypeError:
    pass

# configuration/settings hooks
wndw.configure(width=400)  # -> `configure_item(wndw, width=400)`
wndw.configuration()       # -> `get_item_configuration(wndw)`      -> dict[str, ...]
# several configuration settings are also exposed as properties
wndw.width = 600           # -> `wndw.configure(width=600)`
wndw.width                 # -> `wndw.configuration()["width"]`     -> 600

# same thing here, but for item info
wndw.information()         # -> `get_item_info(wndw)`               -> dict[str, ...]
wndw.theme                 # -> `self.information()["theme"]`       -> None
wndw.children()            # -> `self.information()["children"]`    -> dict[int, list[int | str]]
wndw.children(1)           # -> `self.information()["children"][1]` -> list[int | str]
# Containers like windows can be indexed. This;
wndw[0]
# is equivelent to this;
wndw.children(1)[0]

# States are exposed similarly, except that *most* items have *most*
# states exposed, regardless if they're actually supported. Unsupported
# states return NoneType.
wndw.state()               # -> `get_item_state(wndw)`              -> dict[str, ...]
wndw.is_visible            # -> `wndw.state()["visible"]`           -> True/False
wndw.is_focused            # -> `wndw.state()["focused"]`           -> True/False
wndw.is_clicked            # -> `wndw.state()["clicked"]`           -> None (unsupported)

```
It's important to understand that **any method that can contain item references in their return value(s) are included as they were when returned from Dear PyGui**. That means `wndw.children(1)[0]` from the above example returned the integer identifier of the item interfaced via `btn`, and *not* the actual instance that is `btn`. This might seem problematic -- That doesn't matter much in this case since we have access to `btn` (the interface). What if there was no interface? Consider a more realistic scenario where we want a button to add another button to its parent when clicked. Gonna need a callback for that.
```python
from typing import Any
from dearpypixl import *


def make_initial_items():
    with mvWindow():
        btn1 = mvButton(callback=cb_button)


def cb_button(sender: int | str, app_data: Any, user_data: Any):
    """Creates a new button and adds it to the parent of *sender*."""
    ... # no peeking...


make_initial_items()

```
Dear PyPixl does not interfere with how callbacks are registered or how Dear PyGui runs them, so `cb_button` will recieve the button item reference (`sender`) as type `int` regardless of the fact that the button was originally created using `mvButton`. Since `cb_button` cannot access `btn1` (the interface) created in `make_initial_items`, you would need to either use Dear PyGui's API to manage the process (pretty much invalidating any reason to use this package), or pass the instance itself via `user_data`. Fortunately, interfaces are not unique. We can make more (and without creating additional items) by calling the item type again and passing an existing item reference via the `tag` keyword argument (shown below in our callback);
```python
def cb_button(sender: int | str, app_data: Any, user_data: Any):
    """Creates a new button and adds it to the parent of *sender*."""
    # a new button to `sender`s parent
    sender = mvButton(tag=sender)
    parent = mvWindow(tag=sender.parent)
    with parent:
        mvButton()
```
The above lets us use interfaces to get the behavior we want. Let's consider another possibility where we don't know what `sender` will be. Now, the framework won't try and stop you from making bad decisions such as calling `mvWindow(tag=button_id)`, but there are many reasons why you *shouldn't* do that. Instead, there are two appropriate ways of wrapping an item of an unknown type. The first is calling the item type base class `AppItemType` in the same manor as above. This will provide you with a generic (and basic) item interface. For convenience, `AppItemType` is aliased as `mvAll`.
```python
def cb_button(sender: int | str, app_data: Any, user_data: Any):
    """Creates a new button and adds it to the parent of *sender*.
    """
    # NOTE: Instantiating `AppItemType` without `tag` does not
    # create any items and will not throw an error (although
    # trying to call its methods likely will).
    #`AppItemType` has a numeric representation value of zero.
    sender = mvAll(tag=sender)
    parent = mvWindow(tag=sender.parent)
    with parent:
        mvButton()
```
This likely works well enough for most cases. However, you can get the *correct* interface for an item using the `.wrap_item` class method. The result is independant of the class or instance it is called on.
```python
def cb_button(sender: int | str, app_data: Any, user_data: Any):
    """Creates a new button and adds it to the parent of *sender*.
    """
    # a new button to `sender`s parent
    sender = mvAll.wrap_item(sender)           # `type(sender) == mvButton`
    parent = sender.wrap_item(sender.parent)   # `type(parent) == mvWindow`
    with parent:
        mvButton()
```
As a closing note, keep in mind that **the relationship between an interface and its target item is one-sided**; the interface *thinks* it's an item, compares equal to its target item's id, and **is even accepted by Dear PyGui as an item reference**. The reality is that **it's just a proxy** -- and *not* an actual Python `proxy` object (unfortunately). Items have no way of informing their handlers of their status, and **when the interface's target item is destroyed, the interface itself is not -- breaking future calls to most instance-bound methods and properties**.


## TODO
 - non-`AppItemType`s to use `AppItemLike`
 - add API reference
 - "documentation"

## FAQ

**Q**: **What overhead can I expect using Dear PyPixl's item type classes over Dear PyPixl's functions?**
**A**: **Less than 8%** when creating both items and instances. On my machine, creating one million `mvWindowAppItem` instances took 15.72 seconds (worst-case), while ~1.2 seconds was spent executing Dear PyPixl code (profiled using the `cProfile` module).

---

**Q**: **Can I use both Dear PyPixl and Dear PyGui code in my project?**
**A**: **Yes**, and you are **encouraged to do so**. Dear PyPixl does not aim to be a stand-alone framework, but exists to make using Dear PyGui more familiar to those not used to its functional API, in addition to other conveniences (hopefully). **Some hooks have yet to be implemented**, such as the **supporting functions for tables, plots, etc, as methods**, so there may be times when you *need* to access Dear PyGui.

---

**Q**: **What is the `px_patcher` module and what is it doing?**
**A**: The `px_patcher` module **contains "functional equivalents" of functions found in Dear PyGui**'s `dearpygui` and/or `_dearpygui` modules. When Dear PyPixl is imported, **these functions replace the originals in those modules**. If using both Dear PyPixl and Dear PyGui, it is highly **recommended to import Dear PyPixl *before* importing and/or using Dear PyGui.**

There are several reasons for a function to have been *patched*;
 - to throw proper exceptions in the event that calling the function could result in an irregular or misleading result (subsequent calls to `setup_dearpygui`, `create_viewport`, etc.)
 - the original implementation has a bug with a simple workaround
 - the original implementation is error-prone and/or does not play nice with Dear PyPixl (`run_callbacks`)
 - help Dear PyPixl expose critical features that are missing in Dear PyGui (application-level theme & font access, viewport screen state, etc.)

The replacement function's `__signature__` should be identical to the signature of the original. The original function can be accessed on the replacement function's `__wrapped__` attribute, although there is often little reason to do so.

---

**Q**: **Why do items created using Dear PyPixl classes have large integer ids?**
**A**:  This is to **mitigate item id collisions between Dear PyGui-generated and Dear PyPixl-generated identifiers**. Due to a performance-related [issue](https://github.com/hoffstadt/DearPyGui/issues/2028), Dear PyPixl does not use Dear PyGui's `generate_uuid` function. Instead, it uses a `itertools.count` object with a high starting value, hence the large id values.

Note that to further mitigate the risk of collisions, Dear PyPixl patches the `generate_uuid` functions in both the `dearpygui.dearpygui` and `dearpygui._dearpygui` modules *on import* so that they also use the aforementioned workaround .

---

**Q**: **I need to conform to an older version of Dear PyGui. Can I still use this?
**A**: **On paper? No**. The honest answer? ***Maybe***. Dear PyPixl will absolutely *not* work with Dear PyGui beta versions (pre-1.0). Not a chance. However, key areas in the framework were developed using Dear PyGui v1.8.0. A lot may work, even when using slightly older versions -- you are welcome to try.

With using older versions of Dear PyGui, you may get a warning when trying to import Dear PyPixl indicating that various file definitions do not match the installed Dear PyGui version. You may be able to update them to match your installed version via `python3 -m dearpypixl` (this requires that the parent process has write-access to Dear PyPixl's install directory). Note that this feature may be removed from Dear PyPixl without warning.

---

**Q**: **Why do I get errors/weird behavior when using aliases (string IDs)?**
**A**:  The short version; **Dear PyPixl cannot guarantee the support of aliases when interfacing with items via instances**. This is due to an implementation detail of Dear PyPixl's `AppItemType` class, from which all core framework objects are derived.

The core framework was designed not to be not stand-alone and/or proprietary, but to allow users to pick-and-choose what they want to use from both Dear PyPixl and Dear PyGui without conflicts. To accomplish this, `AppItemType` inherits from the built-in `int` type -- the default item identifier type returned when creating items in Dear PyGui -- to allow it's instances to be used as direct item references when using Dear PyGui's API. As a consequence, this means that all of it's instances *must* be created using an integral value. When the `tag` keyword argument is passed to an item type's constructor (`__new__` in this case), that value is used as the "integral value" to create the instance.

When creating item type instances, one of two things can happen; both the instance/interface and item are created, or
just the instance (interfacing with an already existing item). When a user passes along a tag of type `str`, the constructor tries to work with it as best as it can. It first tries to fetch the numeric identifier associated with the alias using Dear PyGui's `get_alias_id` function. If successful (meaning that the alias is tied to both a numeric identifier AND an existing item), that value is used to create the instance. Otherwise, the instance is created using a newly-generated numeric identifier. The original `tag` value is then associated with the original `tag` value using the the `set_item_alias` function.

That "weird behavior"? Previous experiments show that **Dear PyGui may choose to accept only one of the two identifiers as an item reference**. If the instance creates a new item, users may only be able to use that instance or an `int` of equal value to reference the item using Dear PyGui's API. The opposite may happen when the instance was made to interface with an already existing item. It's expected that Dear PyGui accepts integer identifiers as item references, so the latter has the added consequence of **borking almost every method available to the object**.

---

**Q**: **Why does my program crash/error when creating creating [*i*] items?**
**A**:  There is a known Dear PyPixl-related [issue]() where **it is possible to produce item id collisions under specific circumstances**. Other than that, the issue is **likely related to Dear PyGui when your program crashes without error** and *not* Dear PyPixl.


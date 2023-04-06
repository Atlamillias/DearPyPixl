"""This module exposes "built-in" DearPyGui item types as class objects.
Instances of item type classes act as interfaces to a specific item
throughout their lifetime. Users do not need to import this module --
All objects are added to the `dearpypixl` namespace automatically.

    >>> import time
    >>> from dearpypixl import (
    ...     runtime,
    ...     mvWindow,
    ...     mvText,
    ...     mvButton,
    ...     mvItemHandlerRegistry,
    ...     mvHoverHandler,
    ... )
    >>>
    >>>
    >>> with mvWindow(label="A window", width=400, height=300) as wndw:
    >>>     button = mvButton(label="A button")
    >>>
    >>> # Update item settings using the `.configure` method or various properties.
    >>> wndw.label = "I'm actually a squirrel"
    >>> wndw.label += ", a window-y squirrel."
    >>> button.label = "*call 'window' a liar*"
    >>>
    >>>
    >>> def reveal_plot_twist():  # `time.sleep` for dramatic effect
    ...     wndw.label = "OK fine, maybe I AM a window."
    ...     time.sleep(2.0)
    ...     button.configure(label="My work here is done.", callback=None)
    ...
    ...     # Add items to existing containers (i.e. the "squirrel") at runtime,
    ...     # in one of two ways;
    ...     with wndw:
    ...         time.sleep(2.0)
    ...         mvText("But you didn't do anything...")
    ...     time.sleep(1.8)
    ...     mvText("*surprised_pikachu_face.jpg*", parent=wndw)
    ...
    ...     time.sleep(2.0)
    ...     button.label = "..."
    >>>
    >>>
    >>> button.callback = reveal_plot_twist
    >>>
    >>> runtime.Runtime().start()  # `start_dearpygui()`


Notes:
    * code examples found here are also testcases used for `doctest`
    * the terms "instance" and "interface" are thrown around a lot and are
    the same thing within the context of `dearpypixl`
    * the information below is not comprehensive documentation, and only covers
    key points regarding major differences between the DearPyPixl and DearPyGui API
    regarding items and basic item management
    * if you are unfamiliar with DearPyGui, I highly recommend checking out
    its [documentation](https://dearpygui.readthedocs.io/en/latest/)




Basic usage of item type classes is identical to that of related DearPyGui
functions. The two examples below are functionally equivelent;
    >>> # using DearPyGui
    >>> from dearpygui.dearpygui import *
    >>>
    >>> with window(label="I never lie about anything!") as wndw:
    ...     button = add_button(label="*doubt*")
    >>>
    >>>
    >>> # using DearPyPixl
    >>> from dearpypixl import *
    >>>
    >>> with mvWindow(label="I never lie about anything!") as wndw:
    ...     button = mvButton(label="*doubt*")


DearPyGui often has two different functions for creating container items; one for
usage as a context manager (i.e. `window()`), and one for "normal" usage
(`add_window()`). A user may expect that using the `window` function as a *normal*
function to be functionally the same as using the `add_window` function;

    >>> # Python 3.11
    >>> wndw1 = add_window()
    >>> wndw2 = window()
    >>> type(wndw1) == type(wndw2)
    False
    >>> type(wndw1)
    <class 'int'>
    >>> type(wndw2)
    <class 'contextlib._GeneratorContextManager'>

...which isn't the case. The call was only half-baked, leaving the user without a
window. This is the nature of functions decorated with `contextlib.contextmanager`.
Meanwhile, the same object in DearPyPixl can cover both use-cases;
    >>> wndw1 = mvWindow()
    >>> type(wndw1)
    'mvAppItemType::mvWindowAppItem'
    >>> with mvWindow() as wndw2: ...
    >>> type(wndw1) == type(wndw2)
    True

Either use-case has the same result; a newly created window item and a reference to
that window in the form of an *interface*.


NOTE: In the example above, it may be surprising to see the result of `type(wndw1)`
as `'mvAppItemType::mvWindowAppItem'` instead of something like `<class 'mvWindow'>`.
Item type classes in DearPyPixl try to identify as close to the actual internal
DearPyGui item type as possible. The string representation of `mvWindow` type will
compare equal to `get_item_type(add_window())`, and will also compare equal to the
internal type's enumeration value (i.e. `dearpygui.mvWindowAppItem`) as an integer.
Item type class names also mirror the names of the internal types and *not* the names
of the DearPyGui functions used to create items*.

*`mvWindow` is actually an alias of the `mvWindowAppItem` class.




Item interfaces are just that; interfaces. DearPyPixl does not write any data onto
interfaces. They serve as a pass-through, sending data to and from DearPyGui.
Several interfaces can exist for an item, but an item interface cannot (rather,
*should not*) exist without an existing and identifiable item. In the examples so
far, creating an item type instance also tells DearPyGui to create an item of the
type it represents. However, interfaces can be made for existing items as well by
including the `tag` keyword argument when creating the interface. The value of the
`tag` argument should be a reference (uuid, tag, etc.) to an existing item.
    >>> import dearpypixl as dpx
    >>> import dearpygui.dearpygui as dpg
    >>>
    >>>
    >>> wndw_id = dpg.add_window()
    >>> wndw = mvWindow(tag=wndw_id)
    >>> wndw == wndw_id
    True

Regardless if the item existed prior to the interface's creation or if the item
was created to validate the interface's own existence, **an interface's binding to
its target item cannot and will not change** throughout its lifetime. The above
comparison reveals why, but it's easy to miss. A detail of sizable importance --
their type.

    >>> isinstance(wndw, mvWindow)
    True
    >>> isinstance(wndw, int)
    True

All item type classes in DearPyPixl inherit from the `AppItemType` base class,
which is a direct subclass of the built-in `int` type. Instances of these classes
-- the interfaces -- *are* references of their respective target items, and more
importantly, are proof of their own existances. To summarize, interfaces;

    * are compact, hashable, and immutable

    * compare equal to their target item's *numeric* identifier (i.e. `tag`)

    * are fully compatible with all DearPyGui functions that require an item
    reference or identifier

    * hook onto a single target item

    * are dead weight once their target item is destroyed


NOTE: DearPyGui supports both string and integer item identifiers. The sole caveat
of DearPyPixl's compatibility with DearPyGui is that it *requires* every "target
item" to have a numeric identifier. One of two things happen when creating an
instance and including an alias (string identifier) via the `tag` keyword;

    * When an item would be created: A numeric identifier is created and used
    to create both the item and interface, while the alias is assigned as such
    to the generated numeric identifier via `set_item_alias`.

    * When creating an interface for an existing item: The numeric identifier
    for the item is fetched via `get_alias_id` and is used it to create the
    instance. If `get_alias_id` fails or is 0 or `None`, a numeric identifier
    is generated and used to create the instance instead, while the alias is
    assigned as such to the generated numeric identifier via `set_item_alias`.
"""
# Workarounds for DearPyGui/Imgui bugs/lack of fundamental
# features, additional DearPyGui hooks, and *small* API
# extensions are added here.

from .px_items import AppItemType
from ._appitems import *
from . import _appitems


__all__ = [
    "AppItemType",
    "mvAll",
    "mvWindow",
    *_appitems.__all__,
]


mvAll    = AppItemType
mvWindow = mvWindowAppItem

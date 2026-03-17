# Dear PyPixl
Dear PyPixl is an object-oriented, lightweight, modular framework and toolkit for [Dear PyGui](https://github.com/hoffstadt/DearPyGui) with minimal dependencies and zero use restrictions (MIT license).




#### Features

Dear PyPixl provides object-oriented interfaces for Dear PyGui items and systems. In addition, it ships with an arrangement of optional extensions and tools to help tackle common hurdles.
- Extensible object-oriented API for creating and/or interfacing with Dear PyGui items
- A strongly-typed core library to help get the most out of your development tools
- A functional API for theme color and styles
- Patches a few holes in within Dear PyGui's API, such as allowing users to access the application-level font and theme and manage "on-frame" callbacks
- Organizes DearPyGui's global constants into individual `enum.IntEnum` classes and exposes more of ImGUI's key code constants
- Exposes various item type information, such as parent-child relationships between item types
- An optional layout system and a widget emulating an embedded Python console
- Provides a near drop-in substitute for Dear PyGui's API

<br>


#### Requirements

- Operating System; Windows 8.1+, MacOS, Linux*
- Python: 3.14 x64 (or newer)
- `dearpygui` 2.2 (or newer)

[!NOTE]
**Dear PyPixl is available on all platforms already supported by Dear PyGui. Availability for 32-bit systems and Raspberry Pi OS is *loosely* supported (at the time of writing), but requires building Dear PyGui from the source. Please visit their [wiki](https://github.com/hoffstadt/DearPyGui/wiki) for more information.*

[!IMPORTANT]
This project prioritizes supporting the most recent version of Dear PyGui available, but tries to allow for some backwards compatability when possible.

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
Dear PyPixl's core library is very similar to Dear PyGui, so a lot of existing code will work with a simple change of imports:
```python
import dearpypixl as dpg

dpg.create_context()
dpg.setup_dearpygui()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
```
<p style="text-align:center;font-size:14px;"><i>Example: "First Run" example code from <a href="https://dearpygui.readthedocs.io/en/latest/tutorials/first-steps.html#first-run">Dear PyGui's documentation </a> that imports <b>dearpypixl</b> instead of <b>dearpygui.dearpygui</b></i>.</p>

```python
import dearpypixl as dpx
from dearpygui import demo

dpx.create_context()
dpx.setup_dearpygui()
dpx.create_viewport()
dpx.show_viewport()

with open(demo.__file__, "r") as file:
    # replace the import
    source = file.read().replace(f"import dearpygui.dearpygui as dpg", "import dearpypixl as dpg", 1)

# rebuild the module
demo = type(demo)(demo.__name__)
exec(source, demo.__dict__)

demo.show_demo()
dpx.start_dearpygui()
```
<p style="text-align:center;font-size:14px;"><i>Example: Running Dear PyGui's demo that has been patched to import <b>dearpypixl</b>.</i></p>


As such, most of Dear PyGui's [documentation](https://dearpygui.readthedocs.io/en/latest/index.html) applies to Dear PyPixl as well. APIs unique to Dear PyPixl are typed and documented — your type-checker, language server, and other development tools will typically display this information for you.

### Item Interfaces
In Dear PyGui, functions such as `window()` and `add_button()` return the **tag** of the item they create. A **tag** is a unique identifier representing that item in Dear PyGui's registry. Similar functions exist in Dear PyPixl as well, but return item **interface** objects in place of normal integer or string identifiers. Item interfaces can be used anywhere expecting that item's *tag*. In addition, interfaces expose various methods and properties that operate on that item:
```python
import dearpypixl as dpx

# DPG setup code
...

with dpx.window(autosize=True) as window:
    text = dpx.add_text("The next test is impossible.")

    def update_text(button_id: int | str, value: bool, text: dpx.mvText) -> None:
        button = dpx.mvButton(button_id)
        text.value = button.label

    labels = (
        "Cake and grief counseling will be available at the conclusion of the test.",
        "The Enrichment Center is required to remind you that you will be baked, and then there will be cake.",
        "Uh oh. Somebody cut the cake.",
    )
    for label in labels:
        dpx.add_button(label=label, user_data=text, callback=update_text)

dpx.start_dearpygui()
```
[!NOTE]
*Further code examples may omit the typical Dear PyGui boilerplate code e.g. `create_context()`, `setup_dearpygui()`, etc. However, they probably won't run without it.*

The above code shouldn't be too unfamiliar for those familiar with Dear PyGui. The snippet creates a window item, a text item, and three button items. When a button is clicked, the text item's value is updated to mirror the button's `label`. The part to unpack is the `update_text()` callback function:
```python
    def update_text(sender: int | str, app_data: bool, user_data: dpx.mvText) -> None:
        button = dpx.mvButton(sender)
        user_data.value = button.label
```
While creating each button, its `user_data` was assigned to the item whose value they'll update (`text` in this case). Since functions like `add_text()` in Dear PyPixl return interfaces, `text` is not a typical integer but an instance of the `mvText` class. Dear PyGui will send this along with the [usual suite of other arguments](https://dearpygui.readthedocs.io/en/latest/documentation/item-callbacks.html) to `update_text()` when our buttons are clicked.

However, *sender* is still an item tag. You can use the functional API to operate on it as you typically would via Dear PyGui e.g. [`set_value()`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=set_value#dearpygui.dearpygui.set_value), or you can wrap it in an interface and use Dear PyPixl's object-oriented API. Interface objects of built-in interface types are stateless and do not have instance dictionaries. Properties and methods operate on their associated items using Dear PyGui's functions. This means that as long as we have access to an existing item's tag, we can get an interface for it simply by calling the appropriate class' constructor:
```python
        button = dpx.mvButton(sender)
```
Once we have our button interface, we update the target text item's value to match the `label` of our button. This line:
```python
        user_data.value = button.label
```
... is functionally equivelent to `set_value(user_data, get_item_configuration(sender)["label"])`, which would work even though `user_data` is an interface object.

[!NOTE]
*When creating interfaces by calling the class directly, the **tag** argument optional. If omitted, the constructor will make one using `dearpygui.generate_uuid()`. However, keep in mind that most instance members will raise `SystemError` while an item does not exist with that tag. If you create an item with this tag later, the interface will work properly.*

[!NOTE]
*At runtime, the most appropriate concrete interface type for an existing item can be obtained using `getattr(dearpypixl, get_item_info(item)["type"].removeprefix("mvAppItemType::"))`, or the Dear PyPixl function `dearpypixl.get_interface_type()`. Alternatively, the `dearpygui.AppItem` class can be used to create basic interfaces for any item.*

<br>


### Interface Members
Properties like `label`, `use_internal_label`, and `user_data` are available on any interface regardless of its type. However, the most appropriate interface for an item will expose others that may be unique to items of that type. These properties typically fall into one of three categories based on the system or function(s) used to manage the item setting of the same name: **configuration**, **information**, or **state**. For example, users of Dear PyGui will likely recognize `label`, `use_internal_label`, and `user_data` as common item settings that are managed using the [`get_item_configuration()`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=get_item_configuration#dearpygui.dearpygui.get_item_configuration) and [`configure_item()`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=configure_it#dearpygui.dearpygui.configure_item) functions. If an item's setting could be initially set when the item was created *and* that setting is included in the dictionary returned by [`get_item_configuration(item)`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=get_item_configuration#dearpygui.dearpygui.get_item_configuration), a **configuration** property for that setting is available on the interface. If that setting can later be updated using [`configure_item()`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=configure_it#dearpygui.dearpygui.configure_item), that property will also be writable. A similar relationship exists for settings returned via [`get_item_info()`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=get_item_info#dearpygui.dearpygui.get_item_info) and [`get_item_state()`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=get_item_state#dearpygui.dearpygui.get_item_state) as well, but most are read-only unlike configuration-related settings.

In addition to properties, all interfaces have a method named after each system/function:

| System            | Dear PyPyxl Interface Method | Dear PyGui Function                     |
| :---------------: | :--------------------------: | :-------------------------------------: |
| **configuration** | `item.configure(**kwargs)`   | `configure_item(item, **kwargs)`        |
| **configuration** | `item.configuration()`       | `get_item_configuration(item)`          |
| **information**   | `item.information()`         | `get_item_info(item)`                   |
| **state**         | `item.state()`               | `get_item_state(item)`                  |

There are a few exceptions:
- **configuration**: We glossed over this one — properties for configuration-related item settings are only available if that setting could be set when creating the item and later obtained via `get_item_configuration()`. This is because `get_item_configuration()` packs a few "common default" settings for every item, even if the item doesn't support them. An interface type won't implement a property for a setting that is redundant or useless e.g. `mvButton` does not implement a `source` property even though `get_item_configuration(button)` includes a `"source"` key. These settings will still be included via `item.configuration()` though, since that method simply returns the result of `get_item_configuration(item)`.
- **information**:
  * Interface types do not implement `*_handler_applicable` properties even though they're included in the dictionary returned by `get_item_info()`. The rationale for not doing so is opinionated — I don't believe they are useful enough at runtime to warrant the API bloat (it's an opinion that can easily change). However, those settings are still returned via the `information()` method.
  * All items have writable `theme`, `font`, and `handlers` properties. Accessing these settings via named property returns all non-null values (ones that typically would be item tags) as `mvTheme`, `mvFont`, and `mvItemHandlerRegistry` objects, respectively. On set, the appropriate `bind_item_*()` Dear PyGui function is used to update the item with the new setting. Additionally, deleting the value e.g. `del item.theme` is equivelent to setting it to `0` or `None`.
- **state**:
  * Interfaces do not implement the `ok` property. The the `exists()` method, which calls [`does_item_exist()`](https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html?highlight=does_item_exist#dearpygui.dearpygui.does_item_exist), roughly serves the same purpose and is more performant as Dear PyGui does not need to pack a new Python dictionary.
  * `pos` is a very special case. All interfaces have a readable `pos` property as `get_item_state(item)["pos"]` is valid for all items, even for those without geometry. If `configure_item(item, pos=...)` is valid for that item, the appropriate interface will have a writable variant instead. Additionally, the writable implementation supports deletion which will restore the associated item to its default position (roughly equivelent to `configure_item(item, pos=())`).


[!NOTE]
*HTML-friendly docs and API reference coming soon! In the meantime, please refer to the source code definitions and/or type stub symbols for a complete view of available members for each interface class.*

<br>

### Interface Types
Dear PyGui exposes over 150 different types of items and widgets. In Dear PyPixl, every type of item is represented by an `AppItem` subclass available in the `dearpypixl` namespace. Concrete interface types are named after an item's internal Dear PyGui type name and always have the *mv* prefix (`mvButton`, `mvChildWindow`, etc). They have a fairly simple structure and can be subclassed with a couple considerations in mind. Just like any other Python class, calling an interface class creates an interface object. The associated Dear PyGui item is *not* coupled to the interface's creation. Typically, you would create the Dear PyGui item first, then create an interface for it by providing the constructor that item's tag. This is what the `create()` class method does — by calling a function like `dearpypixl.add_button()`, you are actually calling `mvButton.create()`. This is particularly important when extending or subclassing an existing interface class, as the constructor and destructor methods you implement or override may limit how and when those objects can be created and used.

The easiest way to extend an existing interface class in a way that keeps their behavior consistent with that of built-in types is by deriving from both the interface class of choice and the `CompositeItem` mixin class, in addition to overridding the `create()` class method:
```python
import typing
import dearpypixl as dpx


class LogWindow(dpx.CompositeItem, dpx.mvChildWindow):

    @classmethod
    def create(self, /, maxsize: int = 0, *, auto_scroll: bool = False, **kwargs) -> typing.Self:  # override
        self = super().create(**kwargs)

        # initialize the object like you would in `__init__` or `__new__`
        self.maxsize = maxsize
        self.auto_scroll = auto_scroll
        self._overflow = dpx.add_stage()

        return self

    # other properties/methods

    def get_value(self, *, include_clipped: bool = False) -> str:
        if include_clipped:
            children = self._overflow.children(1)
            children.extend(self.children(1))
        else:
            children = self.children(1)

        value = '\n'.join(v for v in dpx.get_values(children) if v is not None)

        return value

    def move_overflow_text(self) -> None:
        children = self.children(1)

        item_count = len(children)
        while item_count > self.maxsize:
            item = children.pop(0)
            dpx.move_item(item, parent=self._overflow)

            item_count = len(children)

        if self.auto_scroll:
            self.y_scroll_pos = -1.0

    def add_text(self, value: str) -> dpx.mvText:
        item = dpx.add_text(value, parent=self)
        self.move_overflow_text()
        return item

    def write(self, value: str) -> None:
        self.add_text(value)

    @property
    def maxsize(self) -> int:
        return self._maxsize
    @maxitems.setter
    def maxsize(self, value: int) -> None:
        if value == self.maxsize:
            return

        if value < 0:
            value = 0

        self.maxitems = value
        self.move_overflow_text()

    def __exit__(self, *args) -> None:
        super().__enter__(*args)
        self.move_overflow_text()

# optional — alias the `create()` method
log_window = add_log_window = LogWindow.create

# typical DPG boilerplate
...

with dpx.window():
    with log_window(maxsize=3, auto_scroll=True, tag="log-window") as log:
        log.write("Cake and grief counseling will be available at the conclusion of the test.")
        log.write("The Enrichment Center is required to remind you that you will be baked, and then there will be cake.")
        log.write("Uh oh. Somebody cut the cake.")
        log.write("The cake is a lie!")

```
`LogWindow` objects manage a widget for displaying lines of text from a file or log. Calling `LogWindow.create()` creates the underlying Dear PyGui item and interface, initializes the interface, then returns it. So, what happens if we override `__new__()` instead?
```python
import typing
import dearpypixl as dpx
import dearpygui.dearpygui as dpg

class LogWindow(dpx.mvChildWindow):

    def __new__(cls, /, maxsize: int = 0, *, auto_scroll: bool = False, tag: int | str = 0, **kwargs) -> typing.Self:
        item = dpg.add_child_window(tag=tag, **kwargs)
        self = super().__new__(item)

        self.maxsize = maxsize
        self.auto_scroll = auto_scroll
        self._overflow = dpx.add_stage()

        return self

    ...

# optional — alias the constructor
log_window = add_log_window = LogWindow
```
Well, this code still works:
```python
with dpx.window():
    with log_window(maxsize=3, auto_scroll=True, tag="log-window") as log:
        log.write("Cake and grief counseling will be available at the conclusion of the test.")
        log.write("The Enrichment Center is required to remind you that you will be baked, and then there will be cake.")
        log.write("Uh oh. Somebody cut the cake.")
        log.write("The cake is a lie!")
```
Now you need to pass `log` around or pack it into its item's own `user_data` field to ensure they can access it. But then, why subclass `mvChildWindow`? By deriving from `CompositeItem` and using `create()` as the primary constructor, you effectively extend your additional state and API to the item itself — different interface objects created with the same tag become views of the original:

```python
with dpx.window():
    log = LogWindow.create(maxsize=3, auto_scroll=True, tag="log-window")

# different interface objects, same state
LogWindow("log-window").maxsize = 8
LogWindow("log-window").auto_scroll = False

log.maxsize == 8          # True
log.auto_scroll == False  # True
```

Another benefit of deriving from `CompositeItem` is item dependency management. Custom widgets usually involve creating several items. But, what happens to those other items when *your* item is deleted? This is a non-issue if they are its direct or indirect children as `dearpygui.delete_item()` will take care of it for you. That is not the case for items like themes and handler registries, which linger around in Dear PyGui's item registry until they are explicitly deleted:
```python
# this deletes the underlying `mvChildWindow` item, but not the `mvStage`
# assigned to `log._overflow`
log.destroy()
```

Just like how interfaces have a dedicated constructor method in the form of `create()`, the `destroy()` method acts as their destructor. We can override it, but that isn't necessary to fix our problem here — we just need to add a line of code to `create()`:
```python
class LogWindow(dpx.CompositeItem, dpx.mvChildWindow):

    @classmethod
    def create(self, /, maxsize: int = 0, *, auto_scroll: bool = False, **kwargs) -> typing.Self:
        self = super().create(**kwargs)

        self.maxsize = maxsize
        self.auto_scroll = auto_scroll
        self._overflow = dpx.add_stage()

        self.components = [self._overflow]

        return self
```
The `components` attribute is special-cased by `CompositeItem.destroy()`. When `destroy()` is called, it checks to see if `item.components` is a sequence of items (either item interfaces or normal item identifiers). Every item interface will have its `destroy()` method called while every other item is destroyed via `delete_item()`. Additionally, the procedure puts the interface object in a near-unusable state similar to calling a normal object's `__del__()` method.


[!NOTE]
*HTML-friendly docs and API reference coming soon! In the meantime, please refer to the source code definitions and/or type stub symbols for a complete view of available members for each interface class.*

<br>

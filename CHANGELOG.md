# CHANGELOG

This document lists changes as they are made between releases. It includes both high and low-level changes. This library aims to support the latest versions of DearPyGui -- Note that there is **no plans for a deprecation system**. Things may break between major releases as items are added and removed.

## v0.5.0 (DearPyGui v1.0.x)

### General
* `Item` class (affects all items):
    * removed methods: `handlers`
    * new methods: `duplicate`, `renew` (formerly a method of `Container`)
    * removed the `option` parameter from the `configuration` method
    * the `delete` method now removes child references from the appitem registry
    * instances can now be tested for equality based on their configurations (excluding `tag`,`label`, `parent`, `before`, and `pos` values)
    * `tag` is no longer included in the return value of the `configuration` method
    * fixed an issue where the value of `tag` was displayed as `None` when used as a parameter for `repr`
    * performance optimizations for configuration attribute access
* `containers` module:
    * new classes: `ItemSet`, `ItemPool`
    * renamed classes: `Child` -> `ChildWindow`, `StagingContainer` -> `Stage`
* Others:
    * `table` module (new): added `TableCell`, `TableRow`, `TableColumn`
    * `tools` module: added `find_reference`
    * renamed modules: `keycode` -> `constants`
    * renamed Container item properties: `is_top_level` -> `is_root_item`
    * new constants/enums in `constants`
    * the `id` keyword/property has been replaced with `tag` for all items
    * redundant parameters `payload_type`, `drag_callback` and `drop_callback` have been removed from several constructors
    * all `table`-related items have been moved to the `table` module
    * some positional arguments for constructors/items may have changed positions w/DearPyGui's 1.0.0 update
    * eliminated several strong references to other item objects, significantly reducing memory usage (ex. the `theme` property of `Container`/`Widget` no longer binds the `Theme` reference directly to the item)
    * updated several docstrings throughout the library


### `application` module
Large portions of this module were re-written to better support the recent (and future) DearPyGui updates. The `Application` class has lost many of its properties and methods (which now belong to the new `Viewport` class). However, several new methods and properties have been added.

* `Application` class:
    * removed methods: `cleanup`, `show`, `maximize`, `minimize`, `on_resize`, `enable/disable_virtual_scaling` (Windows-only)
    * removed properties: `staging_mode`, `mouse_drag_delta`, `local/global/drawing/plot_mouse_pos`, `primary_window`, `is_running`, `use_primary_window`
    * new methods: `split_frame`, `on_frame`, `is_running`, `is_key_pressed`, `is_key_down`, `is_key_released`,
    * new properties: `version`, `platform`, `device_name`, `process_id`, `virtual_scaling` (Windows-only), `events`, `calls_on_startup`, `calls_on_render`, `calls_on_exit`
    * renamed: `font_scaling` -> `font_scale`
    * updated to support configuration for `auto_device`, `docking`, `docking_space` and `device`
    * the `theme` property now correctly return whichever `Theme` instance is set as default as it is no longer directly set as an instance attribute
    **NOTE: `Theme` items can still be set on the `theme` property, and doing so will bind it as the default theme**
    * constructor no longer accepts parameters
    * removed the need for instantiation (now done automatically)
    * simplified the steps needed to manually create the render loop (now identical to DearPyGui)
* `Viewport` class (new):
    * new properties: `mouse_drag_delta`, `local/global/drawing/plot_mouse_pos`, `primary_window`, `active_window`, `use_primary_window`
    * new methods: `show`, `maximize`, `minimize`, `on_resize`
    * does not need to be instantiated, and the constructor does not accept parameters


### `theming` module
Like the `application` module, large sections needed to be re-written. Changes to the `Theme` API where made to similarly reflect the DearPyGui API. The system was made to be much more flexible than the previous iteration. On the surface it feels very similar to the previous version -- `Theme` can still have the `color` and `style` attributes, and WILL still have `font`-related attributes. `color` and `style` still have easy dotted attribute-access to theming elements if they exist (see below). However, there is no longer a significant trade-off when it is desired to use the theme-aspected objects of this library similarly to the way themes are built in DearPyGui.

* `Theme` class:
    * new constructor parameter `include_presets`: If `True` (default is `True`), `color` and `style` attributes will be bound to `ColorComponent` and `StyleComponent` instances respectively (see below). Otherwise, these attributes will not be created.
    * removed methods: `apply`, `apply_as_disabled`, `unapply`, `unapply_as_disabled`
    * removed properties: `color`, `style`
    * new methods: `bind`, `unbind`
    * new properties:
* `ThemeComponent` class (new):
    * new methods:
    * new properties:
* `Font` class:
    * removed methods: `get_range_hints`



    


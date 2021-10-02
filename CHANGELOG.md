# CHANGELOG

This document lists changes as they are made between releases. This library aims to support the latest versions of DearPyGui -- Note that there is **no plans for a deprecation system**. Things will break between major releases as items are added and removed.

## v0.5.0 (DearPyGui v1.0.x)

### New
* added `table` module
* `table` module: added `TableCell`, `TableRow`, `TableColumn`
* `containers` module: added `ItemSet`, `ItemPool`

### Changes
* all `table`-related items have been moved to the `table` module
* the `id` keyword/property has been replaced with `tag`
* `payload_type`, `drag_callback` and `drop_callback` parameters (all redundant) have been removed from several constructors/items
* `Child` is now `ChildWindow`
* `StagingContainer` is now `Stage`

### Removed

### Bugfixes


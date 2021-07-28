**DPGWidgets** is an object-oriented wrap around the [DearPyGui](https://github.com/hoffstadt/DearPyGui) graphical interface framework.

It ships in two parts - **dpgwrap** and **dpgwidgets**. **dpgwrap** is mostly auto-generated from a script that parses the locally installed DearPyGui API, identifies objects, and sorts them - wrapping most item-producing objects in **class**-objects and dumping them to files. **dpgwidgets** is built on top of **dpgwrap**, focusing on unifying, streamlining (and sometimes and extending) the end-user API.

Documentation, examples, etc will be added periodically. The source code has many comments and docstrings, and it is encouraged to read through them. MOST of the [DearPyGui documentation](https://github.com/hoffstadt/DearPyGui/wiki) will also apply here.
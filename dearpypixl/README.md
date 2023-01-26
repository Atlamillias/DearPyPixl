**Naming Conventions**
* Modules (.py) prefixed with a single underscore "_" are automatically
generated via script and should not be directly edited.
* Modules prefixed with "px_" do not and should not import other
submodules, except other "px_" submodules.
* Classes prefixed with "mv" represent a DearPyGui item type with
minimal additions, except functionality added via dunder methods
and convience properties. Constructor arguments mirror a function
in DearPyGui that is called to create the item. Most instance
methods just call the similarly-named DearPyGui function. Instances
are fully supported by DearPyGui's functional API and can be used
arguments for any function expecting an item identifier, such as
`tag`. They should be exposed in the `dearpypixl` namespace.
* Classes prefixed with "px" represent a DearPyGui item type and
expose an extended API. The constructor may require more or less
arguments, and instance methods may slightly differ in functionality
from the "mv" implementation. They are similar to something a user
might create. If the class is public, it should exposed in the
`dearpypixl` namespace indirectly via a seperate module or
subpackage.
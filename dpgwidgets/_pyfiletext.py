from __future__ import annotations
from pathlib import Path
from io import StringIO
from inspect import Parameter, formatannotation


class _PyTextList(list):
    def append(self, value):
        if not isinstance(value, _PyTextObject):
            value = PyTextObject(value)
        super().append(value)

class _PyTextObject:
    obj = None

    @property
    def name(self):
        if isinstance(self.obj, str):
            return self.obj
        try:
            return self.obj.__name__
        except AttributeError:
            return formatannotation(self.obj)


class PyTextObject(_PyTextObject):
    """Creates an instance representing any Python object. It can be
    represented in a file-friendly text format.
    
    """
    def __init__(self, obj: object, namespace: PyTextNamespace = None):
        self.obj = obj
        self.namespace = namespace

    @property
    def name(self):
        if isinstance(self.obj, str):
            return self.obj
        try:
            return self.obj.__name__
        except AttributeError:
            return formatannotation(self.obj)

    def __str__(self):
        if self.namespace and self.namespace.alias:
            return f"{self.namespace.alias}.{self.name}"
        elif self.namespace:
            return f"{self.namespace.name}.{self.name}"

        return self.name

class PyTextNamespace(_PyTextObject):
    """Creates an instance representing a Python namespace (import, etc). It
    can be represented in a file-friendly text format.
    
    """

    def __init__(self, namespace: object, alias: str = None, imports: list = None):
        self.obj = namespace
        self.alias = alias
        self.imports: _PyTextList[PyTextObject] = _PyTextList()

        if imports:
            [self.imports.append(obj) for obj in imports]

    def __str__(self) -> str:
        if not self.imports:
            return f"import {self.name}\n"
        else:
            length = len(self.imports)
            text = f"from {self.name} import "
            if length == 1:
                text += f"{self.imports[0].name}"
            elif length < 4:
                text += ", ".join([i.name for i in self.imports]).rstrip(",")
            else:
                text += "("
                text += f"".join((f'\n    {i.name},' for i in self.imports))
                text += "\n)"
            text += "\n"
            return text


class PyTextClass(_PyTextObject):
    """Creates an instance representing a (simple) Python class. It can be
    represented in a file-friendly text format.
    
    Only supports name, baseclasses, a metaclass, class
    attributes, simplified __init__, and instance attributes. If the 
    class is a subclass, super().__init__() will be the first line 
    written under the __init__ definition, and any __init__ parameters
    will be passed to it. 
    
    The namespace for the class is expected to be module-level, not
    nested within other objects (i.e. one level of indentation).

    NOTE: Has very limited use, and is made somewhat generalized despite
    its sole existance being to wrap one library - Purposely so in case
    I choose to revisit this concept.

    """

    def __init__(
        self, 
        cls_name: str,
        baseclass: list[object] = None, 
        metaclass: object = None,
        class_attribs: list[tuple[str, PyTextObject]] = None,
        instance_parameters: list[Parameter] = None,
        docstring: str = None
    ):
        self._name = cls_name
        self.baseclass = _PyTextList()
        self._metaclass = None

        if isinstance(baseclass, list):
            [self.baseclass.append(obj) for obj in baseclass]
        if metaclass is not None:
            self._metaclass = PyTextObject(metaclass)

        # class_attribs = [(var_name, value), ...]
        self.class_attribs = class_attribs or []
        self.instance_parameters = [param for param in instance_parameters]
        self.doc = docstring


    def _fix_name(self, string):  # if name starts with any number
        if string[0].isdigit():
            return string[2:]
        return string

    @property
    def name(self):
        return self._fix_name(self._name.title().replace("_", ""))
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def metaclass(self):
        return self._metaclass
    @metaclass.setter
    def metaclass(self, value: object):
        self._metaclass = PyTextObject(value)

    def __str__(self):
        c_text = StringIO()

        ## class definition ##
        text = f"class {self.name}"
        if not self.baseclass or self.metaclass:
            text += ":"
        else:
            text += f"(" + f", ".join((bcls.name for bcls in self.baseclass))
            if self.metaclass:
                text += f"metaclass={self.metaclass}):"
            else:
                text = f"{text.rstrip(', ')}):"
        c_text.write(text)

        ## docstring  ##
        doc = f'\n"""{self.doc}\n\n"""'
        doc = doc.replace("\n", "\n    ")
        c_text.write(doc)

        ## class attributes ##
        for var, value in self.class_attribs:
            c_text.write(f"\n    {var} = {value.__str__()}")
        c_text.write("\n")

        ## __init__ definition ##
        text = f"\n    def __init__("
        # Inserting "self"
        self.instance_parameters.insert(0, Parameter("self", Parameter.POSITIONAL_ONLY))
        if len(self.instance_parameters) < 4:
            for parameter in self.instance_parameters:
                p = str(parameter)
                text += p
            text = f'{text.rstrip(", ")}):'
            c_text.write(text)
        else:
            c_text.write(text)
            for parameter in self.instance_parameters:
                p = str(parameter)
                text = f"\n        {p}"
                text += ", "
                c_text.write(text)
            c_text.write("\n    ):")
        # __init__ body, call to super
        kwargs = None
        args = None
        for idx, p in enumerate(self.instance_parameters):
            if p.kind == Parameter.VAR_KEYWORD:
                kwargs = self.instance_parameters.pop(idx)
            elif p.kind == Parameter.VAR_POSITIONAL:
                args = self.instance_parameters.pop(idx)
        if self.baseclass:
            c_text.write(f"\n        super().__init__(")
            [c_text.write(f"\n            {p.name}={p.name},")
             for p in self.instance_parameters if p.name != "self"]
            if kwargs:
                c_text.write(f"\n            **{kwargs.name},")
            if args:
                c_text.write(f"\n            **{args.name},")
            c_text.write("\n        )")
        # __init__ body, instance parameters
        [c_text.write(f"\n        self.{p.name} = {p.name}") for p in
         self.instance_parameters if p.name != "self" and p.kind !=
         Parameter.VAR_KEYWORD and p.kind != Parameter.VAR_POSITIONAL]  # exclude self, args, kwargs

        filetext = c_text.getvalue()
        c_text.close()

        return filetext

class PyFile:
    banner = [
        "##################################################\n"
        "####### NOTE: This file is auto-generated. #######\n"
        "##################################################\n"
    ]

    def __init__(
        self, 
        filename: str, 
        dirpath: str, 
        banner: list[str] = None, 
        imports: list[PyTextNamespace] = None
    ):
        self.filename = filename
        self.dirpath = dirpath
        self.banner = banner or self.__class__.banner

        self.imports = imports or []
        self.objects: list[PyTextClass] = []

    def all_objects(self) -> list[_PyTextObject]:
        return [obj for obj in self.objects]

    def write(self):
        dirpath = Path(self.dirpath)
        if not dirpath.exists():
            dirpath.mkdir()

        filename = dirpath / f"{self.filename}.py"
        buffer = StringIO()
        def newlines(): return buffer.write("\n\n\n")

        # imports
        for _import in self.imports:
            buffer.write(_import.__str__())
        buffer.write("\n")

        # banner
        buffer.writelines(self.banner)
        buffer.write("\n")

        # __all__
        buffer.write("__all__ = [")
        for cls in self.objects:
            buffer.write(f'\n    "{cls.name}",')
        buffer.write("\n]")

        # objects
        for obj in self.objects:
            newlines()
            buffer.write(str(obj))

        buffer.write("\n")

        # dumping to filename.py
        with open(str(filename), "w") as file:
            file.write(buffer.getvalue())

        buffer.close()

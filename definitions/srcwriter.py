from __future__ import annotations
from inspect import Parameter, formatannotation, _empty
from typing import Union
from io import StringIO
from pathlib import Path
import functools


class _PyTextList(list):
    def append(self, value):
        if not isinstance(value, PyTextObject):
            value = PyTextObject(value)
        super().append(value)


class PyTextObject:
    """An object representing any Python object. It can be
    represented in a file-friendly text format.
    
    Args:
        * obj (object): The object or object reference. Can also be a string.
        * namespace (PyNamespace): The namespace for <obj>.
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

    def __repr__(self):
        return str(self)


class PyTextNamespace(PyTextObject):
    """An object representing a Python namespace (import, etc). It
    can be represented in a file-friendly text format.
    """

    def __init__(self, namespace: object, alias: str = None, imports: list = None):
        self.obj = namespace
        self.alias = alias
        self._imports: list[PyTextObject] = []

        if imports:
            self.imports = imports

    def __str__(self) -> str:
        if not self.imports:
            return f"import {self.name}\n"
        else:
            length = len(self._imports)
            text = f"from {self.name} import "
            if length == 1:
                text += f"{self._imports[0].name}"
            elif length < 4:
                text += ", ".join([i.name for i in self._imports]).rstrip(",")
            else:
                text += "("
                text += f"".join((f'\n    {i.name},' for i in self._imports))
                text += "\n)"
            text += "\n"
            return text

    @property
    def name(self):
        if isinstance(self.obj, str):
            return self.obj
        try:
            return self.obj.__name__
        except AttributeError:
            return formatannotation(self.obj)

    @property
    def imports(self):
        return self._imports
    @imports.setter
    def imports(self, value):
        if isinstance(value, list):
            value = _PyTextList([PyTextObject(nspace) for nspace in value])
            self._imports = value
        else:
            raise ValueError("Must be a list of `PyTextObject`'s.")


class PyTextClass(PyTextObject):
    init_max_oneline_params     = 4
    init_params_incl_args_var   = False
    init_params_incl_kwargs_var = False
    init_params_as_self_attrs   = False

    def __init__(
        self,
        name           : str,
        baseclasses    : list[Union[str, PyTextObject]] = None,
        metaclass      : Union[str, PyTextObject]       = None,
        cls_attributes : list[Parameter]                = None,
        self_attributes: list[Parameter]                = None,
        init_parameters: list[Parameter]                = None,
        docstring      : str                            = None,
    ) -> None:
        self._name           = None
        self._baseclasses    = self._PyTextList()
        self._metaclass      = None
        self._buffer         = None

        self.name            = name
        self.baseclasses     = baseclasses
        self.metaclass       = metaclass
        self.cls_attributes  = cls_attributes or []
        self.self_attributes = self_attributes or []
        self.init_parameters = init_parameters or []
        self.docstring       = docstring

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value: str):
        if value is None:
            raise ValueError("`name` property cannot be set to None.")
        name = value.replace("_","")
        if name[0].isdigit():
            number, letter = name[:2]
            suffix = f"{number}{letter.upper()}"
            name = f"{name[2:]}{suffix}"
        self._name = name

    @property
    def baseclasses(self) -> list[PyTextObject]:
        return self._baseclasses
    @baseclasses.setter
    def baseclasses(self, value):
        if value is None:
            value = _PyTextList()
        elif not isinstance(value, PyTextObject):
            value = _PyTextList(value)
        self._baseclasses = value
    
    @property
    def metaclass(self):
        return self._metaclass
    @metaclass.setter
    def metaclass(self, value: object):
        if value is None:
            self._metaclass = None
        elif not isinstance(value, PyTextObject):
            self._metaclass = PyTextObject(value)
        else:
            raise ValueError(f"`metaclass` property cannot be set to {type(value)!r}")

    def _apply_buffer(method):
        @functools.wraps(method)
        def wrapper(self):
            if not self._buffer:
                self._buffer = StringIO()
                method(self)
                string = self._buffer.getvalue()
                self._buffer.close()
                self._buffer = None
                return string
            return method(self)
        return wrapper

    @_apply_buffer
    def __str__(self):
        self._write_cls_def()
        self._write_docstring()
        self._write_cls_attrs()
        self._write_init()


    @_apply_buffer
    def _write_cls_def(self):
        text: str = f"class {self.name}:"
        if self.baseclasses or self.metaclass:
            bases_text = ", ".join(base for base in self.baseclasses)
            text = text.replace(":", f"({bases_text}):").replace(",)", ")")

        if self.metaclass and self.baseclasses:
            text = text.replace("):", f", metaclass={self.metaclass}):")
        elif self.metaclass:
            text = text.replace(":", f"(metaclass={self.metaclass}):")
        self._buffer.write(f"{text}\n")

    @_apply_buffer
    def _write_docstring(self):
        if not self.docstring:
            return None
        text = self.docstring.replace('\n', '\n    ')
        self._buffer.write(f'    """{text.strip()}\n    """\n')

    @_apply_buffer
    def _write_cls_attrs(self):
        if not self.cls_attributes:
            return None

        attr_strings = self._format_parameters_as_strings(self.cls_attributes, 4)
        # Sorting
        public_attrs = []
        private_attrs = []
        for attr_str in attr_strings:           
            if attr_str.lstrip().startswith("_"):
                private_attrs.append(attr_str)
                continue
            public_attrs.append(attr_str)

        text = ""
        if public_attrs:
            linebreak = False
            for line in public_attrs:
                # Messy formatting fix to add a newline between config and states.
                if not linebreak and 'ItemAttribute("state"' in line:
                    linebreak = True
                    text += "\n"
                text += f"\n{line}"
            text += "\n"
        if private_attrs:
            for line in private_attrs:
                text += f"\n{line}"
            text += "\n"

        self._buffer.write(f"{text}")
        
    @_apply_buffer
    def _write_init(self):
        text = "\n    def __init__("
        # __init__ definition
        init_parameters = [Parameter("self", Parameter.POSITIONAL_ONLY), *self.init_parameters]
        # Formatting depends on the number of parameters.
        if len(init_parameters) < self.init_max_oneline_params:
            text += ", ".join([str(param) for param in init_parameters]) + ") -> None:"
        else:
            formatted = self._format_parameters_as_strings(init_parameters, 8)
            text += "".join((f"\n{line}," for line in formatted))
            text += "\n    ) -> None:"

        # __init__ body
        if not self.baseclasses and not self.self_attributes and not self.init_max_oneline_params:
            text += "\n        ..."
            self._buffer.write(f"{text}\n")
            return None

        self_attributes = []
        var_keyword     = None
        var_positional  = None
        if self.baseclasses or self.init_params_as_self_attrs:
            for idx, param in enumerate(self.init_parameters):
                if param._name == "self":
                    continue
                elif param.kind == Parameter.VAR_KEYWORD:
                    var_keyword = self.init_parameters[idx]
                elif param.kind == Parameter.VAR_POSITIONAL:
                    var_positional = self.init_parameters[idx]
                else:
                    self_attributes.append(param)

        # super().__init__
        if self.baseclasses:  
            text += "\n        super().__init__("
            for param in self_attributes:
                text += f"\n            {param.name}={param.name},"
            if var_positional:
                text += f"\n            *{var_positional.name}"
            if var_keyword:
                text += f"\n            **{var_keyword.name},"
            text += "\n        )"
        self._buffer.write(f"{text}")

    def _format_parameters_as_strings(self, parameters: list[Parameter], indent: int = 0) -> list[str]:
        len_ceil_name = 0
        len_ceil_anno = 0
        len_ceil_defv = 0

        param_lines = []
        for param in parameters:
            spaces = " " * indent
            param_string = f"{spaces}{str(param)}"
            if param._annotation is not _empty and param._default is not _empty:
                name, param_string = param_string.split(":", maxsplit=1)
                anno, defv = param_string.split("=", maxsplit=1)
                if (length := len(name)) > len_ceil_name:
                    len_ceil_name = length
                if (length := len(anno)) > len_ceil_anno:
                    len_ceil_anno = length
                if (length := len(defv)) > len_ceil_defv:
                    len_ceil_defv = length
                param_lines.append((name, anno, defv))

            elif param._annotation is not _empty:
                name, anno = param_string.split(":", maxsplit=1)
                if (length := len(name)) > len_ceil_name:
                    len_ceil_name = length
                if (length := len(anno)) > len_ceil_anno:
                    len_ceil_anno = length
                param_lines.append((name, anno, None))
                    
            elif param._default is not _empty:
                name, defv = param_string.split(":", maxsplit=1)
                if (length := len(name)) > len_ceil_name:
                    len_ceil_name = length
                if (length := len(defv)) > len_ceil_defv:
                    len_ceil_defv = length
                param_lines.append((name, None, anno))

            else:
                name = param_string
                if (length := len(name)) > len_ceil_name:
                    len_ceil_name = length
                param_lines.append((name, None, None))
        
        name_temp = "{name:<{len_name}}"
        anno_temp = "{anno:<{len_anno}}"
        defv_temp = "{defv:<{len_defv}}"
        name_anno_defv_temp = name_temp + ":" + anno_temp + "=" + defv_temp
        name_anno_temp = name_temp + ":" + anno_temp
        name_defv_temp = name_temp + " = " + defv_temp

        formatted = []
        for param_parts in param_lines:
            name, anno, defv = param_parts
            if anno is not None and defv is not None:
                formatted_string = name_anno_defv_temp.format(
                    name=name,
                    len_name=len_ceil_name,
                    anno=anno,
                    len_anno=len_ceil_anno,
                    defv=defv,
                    len_defv=len_ceil_defv
                )
            elif anno is not None:
               formatted_string = name_anno_temp.format(
                    name=name,
                    len_name=len_ceil_name,
                    anno=anno,
                    # The "1" accounts for the padding that would be included
                    # with the default delimiter `=`.
                    len_anno=len_ceil_anno + len_ceil_defv + 1
                )
            elif defv is not None:
               formatted_string = name_defv_temp.format(
                    name=name,
                    len_name=len_ceil_name + len_ceil_anno,
                    defv=defv,
                    len_defv=len_ceil_defv
                )
            else:
               formatted_string = name_temp.format(
                    name=name,
                    # The "2" accounts for the padding that would be included
                    # with the annotation/default delimiters (= or :).
                    len_name=len_ceil_name + len_ceil_anno + len_ceil_defv + 2,
                )
            formatted.append(formatted_string)
        return formatted

    class _PyTextList(list):
        def append(self, value):
            if not isinstance(value, PyTextObject):
                value = PyTextObject(value)
            super().append(value)


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
        self._buffer = None

        self.filename = filename
        self.dirpath = dirpath
        self.banner = banner or self.banner

        self.imports = imports or []
        self.objects: list[PyTextClass] = []

    @property
    def path(self) -> Path:
        return Path(self.dirpath, f"{self.filename}.py")

    _apply_buffer = PyTextClass._apply_buffer

    @_apply_buffer
    def __str__(self):
        self._write_imports()
        self._write_banner()
        self._write_all_dunder()
        self._write_objects()

    @_apply_buffer
    def _write_imports(self):
        for module in self.imports:
            self._buffer.write(str(module))
        self._buffer.write("\n")

    @_apply_buffer
    def _write_banner(self):
        self._buffer.writelines(self.banner)
        self._buffer.write("\n")

    @_apply_buffer
    def _write_all_dunder(self):
        self._buffer.write("__all__ = [")
        for cls in self.objects:
            self._buffer.write(f'\n    "{cls.name}",')
        self._buffer.write("\n]")

    @_apply_buffer
    def _write_objects(self):
        for obj in self.objects:
            self._buffer.write("\n\n\n")
            self._buffer.write(str(obj))
        self._buffer.write("\n")

    def write(self):
        dirpath = Path(self.dirpath)
        if not dirpath.exists():
            dirpath.mkdir()

        filetext = str(self)
        with open(str(self.path), "w") as file:
            file.write(filetext)


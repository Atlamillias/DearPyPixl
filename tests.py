from dearpypixl.components import Item
from dearpypixl import basic
from dearpypixl import colors
from dearpypixl import containers
from dearpypixl import drawing
from dearpypixl import misc
from dearpypixl import nodes
from dearpypixl import plotting
from dearpypixl import tables
from dearpypixl import textures
from dearpypixl import values

from dearpygui import dearpygui as dpg
import inspect


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()

modules = (
    basic,
    colors,
    containers,
    drawing,
    misc,
    nodes,
    plotting,
    tables,
    textures,
    values,
)

appitems = {}
for module in modules:
    objs = [getattr(module, attr) for attr in dir(module) if not attr.startswith("_")]
    for obj in objs:
        try:
            Item in obj.mro()
        except:
            continue
        if ".appitems" in obj.__module__:
            appitems[obj.__qualname__] = obj

root_items = {}
non_root_containers = {}
other_items = {}
for item_name in [*appitems]:
    itemT = appitems[item_name]
    if itemT._is_root_item:
        root_items[item_name] = appitems.pop(item_name)
    elif itemT._is_container:
        non_root_containers[item_name] = appitems.pop(item_name)
    else:
        other_items[item_name] = appitems.pop(item_name)


type_map = {
    "int": 100,
    "float": 1.0,
    "list": [],
    "tuple": (),
    "str": "",
}

error_items = []


for itemT in root_items.values():
    parameters = inspect.signature(itemT).parameters.values()
    req_params = [p for p in parameters if 
                p.default == inspect.Parameter.empty and p.name != "kwargs"]
    kwargs = {}
    try:
        for p in req_params:
            anno = inspect.formatannotation(p.annotation)
            kwargs[p.name] = type_map[anno]
    except KeyError as e:
        error_items.append(itemT)
        break
    item = itemT(**kwargs)

    try:
        item.configuration()
    except Exception as e:
        print(itemT.__qualname__, "on 'configuration()':")
        raise e
    try:
        item.information()
    except Exception as e:
        print(itemT.__qualname__, "on 'information()':")
        raise e
    try:
        item.state()
    except Exception as e:
        print(itemT.__qualname__, "on 'state()':")
        raise e
    
with containers.Window() as win:
    for items in (non_root_containers, other_items):
        for itemT in items.values():
            if not itemT._unique_parents:
                parameters = inspect.signature(itemT).parameters.values()
                req_params = [p for p in parameters if 
                            p.default == inspect.Parameter.empty and p.name != "kwargs"]
                kwargs = {}
                try:
                    for p in req_params:
                        anno = inspect.formatannotation(p.annotation)
                        kwargs[p.name] = type_map[anno]
                except KeyError as e:
                    error_items.append(itemT)
                    break
                item = itemT(parent=win, **kwargs)

                try:
                    item.configuration()
                except Exception as e:
                    print(itemT.__qualname__, "on 'configuration()':")
                    raise e
                try:
                    item.information()
                except Exception as e:
                    print(itemT.__qualname__, "on 'information()':")
                    raise e
                try:
                    item.state()
                except Exception as e:
                    print(itemT.__qualname__, "on 'state()':")
                    raise e


while dpg.is_dearpygui_running():
     dpg.render_dearpygui_frame()
dpg.destroy_context()


for itemT in error_items:
    print(itemT.__qualname__)

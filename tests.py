from dearpypixl.components import Item
from dearpypixl import Application
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

from dearpypixl.components import registries

from dearpygui import dearpygui as dpg
from pathlib import Path
from dataclasses import dataclass
import inspect


@dataclass(slots=True)
class PixlItem:
    item: Item
    category: str = None

    AppItems = []

    def __post_init__(self):
        self.name = self.item.__qualname__
        self.parent_tree = []

    def build_parent_tree(self):
        parents = [parent for parent in self.item.unique_parents
                   if parent not in ("Stage", "TextureRegistry")
                   and not parent.endswith("Handler")]
        if not parents:
            self.parent_tree.append("Window")

exclude_items = (
    "ItemSet",
    "ItemPool"
)


def get_appitems():
    modules = (
        containers,                        
        registries,
        basic,
        colors,
        #drawing,
        misc,
        #nodes,
        #plotting,
        tables,
        #textures,
        values,
    )

    appitems = {}
    for module in modules:
        module_name = Path(module.__file__).stem
        objs = [getattr(module, attr) for attr in dir(module) if not 
                attr.startswith("_") and inspect.isclass(getattr(module, attr))]
        objs = tuple([obj for obj in objs if obj.__module__.split(".")[-1] == module_name])
        for obj in objs:
            try:
                Item in obj.mro()
            except:
                continue
            if obj.__qualname__ not in exclude_items:
                appitems[obj.__qualname__] = obj

    root_items: dict[str, object] = {}
    non_root_containers: dict[str, object] = {}
    other_items: dict[str, object] = {}
    for item_name in [*appitems]:
        itemT = appitems[item_name]
        if itemT.is_root_item:
            root_items[item_name] = appitems.pop(item_name)
        elif itemT.is_container:
            non_root_containers[item_name] = appitems.pop(item_name)
        else:
            other_items[item_name] = appitems.pop(item_name)

    return root_items, non_root_containers, other_items





ROOT_ITEMS, CONTAINERS, WIDGETS = get_appitems()
ALL_ITEMS = ROOT_ITEMS | CONTAINERS | WIDGETS
error_items = []

class DearPyPixlTestCase:
    type_defaults = {
        "int": 100,
        "float": 1.0,
        "list": [],
        "tuple": (),
        "str": "",
        "bool": True,
    }
    item_defaults = {
        "ColorMap": {"colors": [[0,0,0,255], [255,255,255,255]], "qualitative": False}
    }
    test_items = {"Window": containers.Window()}

    def __init__(self, item_type: object):
        self.item_name = item_type.__qualname__
        self.item_type = item_type
        self.item_params = inspect.signature(item_type).parameters.values()
        self.req_params = [p for p in self.item_params if 
                           p.default == inspect.Parameter.empty and p.name != "kwargs"]
        self.item_config = {}
        self.item_instance = None

        for p in self.req_params:
            anno = inspect.formatannotation(p.annotation)
        if self.item_name in self.item_defaults:
            self.item_config |= self.item_defaults[self.item_name]
        else:
            for p in self.req_params:
                anno = inspect.formatannotation(p.annotation).replace("L", "l").replace("T", "t")
                try:
                    self.item_config[p.name] = self.type_defaults[anno]
                except KeyError as e:
                    if "Union" not in anno:
                        raise e
                    elif "Tuple[" or "List[" in anno:
                        self.item_config[p.name] = self.type_defaults["float"]

        self.item_config["label"] = f"TEST_{self.item_type.__qualname__}"



    def ItemCreation_Test(self):
        if self.item_type.__qualname__ == "MenuBar":
            print
        if self.item_type.is_root_item:
            item = self.item_type(**self.item_config)
            self.item_instance = item
            if self.item_type.__qualname__ not in self.test_items:
                self.test_items[self.item_type.__qualname__] = item
            return None

        else:
            parents = [p for p in self.item_type.unique_parents if p
                    not in ("TemplateRegistry", "Stage") and not p.endswith("Handler")]
            if not parents:
                self.item_config["parent"] = self.test_items["Window"]
                self.item_instance = self.item_type(**self.item_config)
            else:
                for parent in parents:
                    if parent in self.test_items:
                        self.item_config["parent"] = self.test_items[parent]
                        self.item_instance = self.item_type(**self.item_config)
                        break
                else:
                    item_tree = [self.item_type]
                    while True:
                        item = item_tree[0]
                        parents = [p for p in item.unique_parents if p not in 
                                ("TemplateRegistry", "Stage") and not p.endswith("Handler")]
                        if not parents:
                            item_tree.insert(0, ALL_ITEMS["Window"])
                            break
                        parent = ALL_ITEMS[parents[0]]
                        item_tree.insert(0, parent)
                        if parent.is_root_item:
                            break
                    if item_tree[0].__qualname__ in self.test_items:
                        last_parent = self.test_items[item_tree[0].__qualname__]
                    else:
                        last_parent = item_tree[0]()
                        self.test_items[item.__qualname__] = last_parent
                    item_tree.pop(0)
                    for item in item_tree:
                        if item == self.item_type:
                            item_obj = item(parent=last_parent, **self.item_config)
                            self.item_instance = item_obj
                        else:
                            test_instance = type(self)(item)
                            item_obj = test_instance.item_type(parent=last_parent, **test_instance.item_config)
                        if item.__qualname__ not in self.test_items:
                            self.test_items[item.__qualname__] = item_obj
                        last_parent = item_obj
                

        assert self.item_instance             
  
            
        

    def GetItemConfig_Test(self):
        if not self.item_instance:
            self.ItemCreation_Test()
 
        try:
            self.item_instance.configuration()
        except Exception as e:
            print(self.item_type.__qualname__, "on 'configuration()':")
            raise e

    def GetItemInfo_Test(self):
        if not self.item_instance:
            self.ItemCreation_Test()
 
        try:
            self.item_instance.information()
        except Exception as e:
            print(self.item_type.__qualname__, "on 'information()':")
            raise e

    def GetItemStates_Test(self):
        if not self.item_instance:
            self.ItemCreation_Test()
 
        try:
            self.item_instance.state()
        except Exception as e:
            print(self.item_type.__qualname__, "on 'state()':")
            raise e


for item in ROOT_ITEMS.values():
    appitem = DearPyPixlTestCase(item)
    creation_result = appitem.ItemCreation_Test()
    appitem.GetItemConfig_Test()
    appitem.GetItemInfo_Test()
    appitem.GetItemStates_Test()

for item in CONTAINERS.values():
    appitem = DearPyPixlTestCase(item)
    creation_result = appitem.ItemCreation_Test()
    appitem.GetItemConfig_Test()
    appitem.GetItemInfo_Test()
    appitem.GetItemStates_Test()

for item in WIDGETS.values():
    print(item)
    if item.__qualname__ in ("Image"):
        continue
    appitem = DearPyPixlTestCase(item)
    creation_result = appitem.ItemCreation_Test()
    appitem.GetItemConfig_Test()
    appitem.GetItemInfo_Test()
    appitem.GetItemStates_Test()


Application.start()



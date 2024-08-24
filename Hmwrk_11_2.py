import inspect
from pprint import pprint

def introspection_info(obj):
    dict_info = {}
    dict_info["type"] = type(obj)

    dict_info["method"] = dir(obj)
    dict_info["module"] = inspect.getmodule(obj)
    attr_list = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        attr_list.append(attr)
        dict_info["attr"] = attr_list
    return dict_info
pprint(introspection_info(42))
pprint(introspection_info([34,25,"oops"]))
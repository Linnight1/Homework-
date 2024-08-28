import inspect
from pprint import pprint
class MyClass:
    attr = "Class"
    def __init__(self,obj):
        self.obj = obj
        self.instance_attr = "Instance"
obj = MyClass(42)
def introspection_info(obj):
    dict_info = {}
    dict_info["type"] = type(obj)

    dict_info["method"] = dir(obj)
    dict_info["module"] = inspect.getmodule(obj)
    try:
        dict_info["attr"] = obj.__dict__
    except AttributeError:
        dict_info["attr"] = None

    return dict_info

pprint(introspection_info(obj))
pprint(introspection_info(42))
pprint(introspection_info([34,25,"oops"]))
import inspect

def get_sets(_collection):
    from datatypes import Set_Item
    for name, cls in inspect.getmembers(_collection, lambda x: inspect.isclass(x)):
        if issubclass(cls, Set_Item):
            print(name, cls)



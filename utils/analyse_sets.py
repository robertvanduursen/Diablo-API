import items_cache, inspect

def get_sets():
    for name, cls in inspect.getmembers(items_cache, lambda x: inspect.isclass(x)):
        if issubclass(cls, items_cache.Set_Item):
            print(name, cls)



get_sets()

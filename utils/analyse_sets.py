import items_cache, inspect

def get_sets():
    for name, cls in inspect.getmembers(items_cache): # , lambda x: issubclass(x.__class__, items_cache.Set_Item)
        print(name, cls)


    # import collections
    # sets = collections.defaultdict(int)
    # for item in self.items:
    #     if 'Set_Item' in str(item.__class__.__mro__):
    #         if item.set:
    #             sets[item.set] += 1
    # for _set, equipped in sets.items():
    #     print(_set, equipped)
    #     for bonus in _set().yield_bonus(equipped):
    #         print('bonus: {}'.format(bonus))
    #             # print(item.type, item.__doc__)
    #         # print(item.text)
get_sets()

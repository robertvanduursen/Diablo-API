import inspect, sys
sys.path.append("..\..")
from d3api.datatypes import classes
from datatypes import Item

# import Diablo
# from .datatypes import classes

def get_class_eligible_items(_collection, class_name='barbarian'):
    # import Barbarian.items_cache as items_cache

    total = 0
    items = []
    remaining_classes = set(classes) - {class_name}
    for name, cls in inspect.getmembers(_collection, inspect.isclass):
        if issubclass(cls, Item):
            class_str = inspect.getsource(cls).lower()
            if not any([_cls in class_str for _cls in remaining_classes]) or class_name in class_str:
                # print(inspect.getsource(cls))
                total += 1
                items.append(cls)

    print(total)
    return items

def get_skill_items(items, class_name):

    if not items:
        from classes.Crusader import items_cache as items
    eligible_items = get_class_eligible_items(items, class_name.lower())

    import importlib
    _skills = importlib.import_module('classes.{}.skills'.format(class_name))

    from datatypes import Active
    skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(_skills, inspect.isclass) if
                   Active in cls.__bases__]

    def match_skills(item):
        """ filter items based on if they match a class skill """
        text = inspect.getsource(item)
        if any([skill in text for skill in skill_names]):
            return True
        return False

    filtered = list(filter(match_skills, eligible_items))

    # for nr, item in enumerate(filtered):
    #     print(nr)
    #     print(inspect.getsource(item))
    #
    # print(len(filtered))

    return filtered


def item_patterns():
    import data.items_cache
    import data.weapons_cache
    import re

    total = 0
    every_effect_rune = []
    for name, cls in inspect.getmembers(data.items_cache, inspect.isclass):
        class_str = inspect.getsource(cls)
        if 'gains the effect of every' in class_str.lower():
            print(total, name)
            print(class_str)
            test = re.search(r"Set:(.*)? gains the effect of every rune", class_str)
            if test:
                every_effect_rune.append(test.groups()[0].strip())
            print
            total += 1

    for rune in set(every_effect_rune):
        print(rune)

# item_patterns()

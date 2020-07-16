import inspect, sys

sys.path.append("..\..")
from datatypes import Item, Set_Item, Classes


def skill_dict_generator(items, skill_names):
    import collections
    skill_dict = collections.defaultdict(list)
    for item in items:
        for name in skill_names:
            if name in item.text:
                # if name in inspect.getsource(item):
                skill_dict[name].append(item)
    return skill_dict


def get_class_eligible_items(_collection, class_name='barbarian'):
    """ all items """
    # import Barbarian.items_cache as items_cache

    total = 0
    items = []
    remaining_classes = set(Classes.names()) - {class_name}
    for name, cls in inspect.getmembers(_collection, inspect.isclass):
        if issubclass(cls, Item) and cls is not Item and cls is not Set_Item:
            # class_str = inspect.getsource(cls).lower()
            class_str = cls.text.lower()
            if not any([_cls in class_str for _cls in remaining_classes]) or class_name in class_str:
                # print(inspect.getsource(cls))
                total += 1
                items.append(cls)

    # print(total)
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
        text = item.text
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

def class_attributes(class_name):
    import importlib
    _attrs = []
    try:
        _attrs = importlib.import_module('classes.{}.data'.format(class_name.os_name)).attributes
    except Exception as e:
        print('Trying to get class attributes for {}'.format(class_name))
        print(e)

    return _attrs

def class_skill_names(class_name):
    import importlib
    _skills = importlib.import_module('classes.{}.skills'.format(class_name))

    from datatypes import Active
    skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(_skills, inspect.isclass) if
                   Active in cls.__bases__]

    return skill_names


def all_class_skill_names():
    from datatypes import Classes

    import classes, os

    all_skill_names = []
    for cls in os.listdir(classes.__path__[0]):
        if cls in [obj.os_name for obj in Classes.items()]:
            # print('excluding {}'.format(cls))
            all_skill_names += class_skill_names(cls)
    return all_skill_names


for x in sorted(all_class_skill_names()):
    print(x)

def exclude_other_class_items(_items, class_name):
    """ filter based on the presence of skill names of other classes """

    class_skills = class_skill_names(class_name)
    other_skill_names = list(set(all_class_skill_names()) - set(class_skills)) + class_attributes(Classes.DEMON_HUNTER)

    def match_invert_skills(item):
        """ filter items based on if they match a class skill """
        text = item.text

        if any([skill in text for skill in other_skill_names]):
            if any([skill in text for skill in class_skills]): # double check
                print('found a wizard skill', [skill for skill in class_skills if skill in text])
                print(item)
                return True
            return False
        return True

    return list(filter(match_invert_skills, _items))

    # def match_invert_skills(_item):
    #     """ filter items based on if they match a class skill """
    #     text = _item.text
    #
    #     if any([skill in text for skill in other_skill_names]):
    #
    #         if any([skill in text for skill in class_skills]): # double check
    #             print('found aa wizard skill', [skill for skill in class_skills if skill in text])
    #             print(_item)
    #             return True
    #         return False
    #
    #     print('lolll')
    #     return True
    #
    # print(other_skill_names)
    # to_return = []
    # for item in _items:
    #     if match_invert_skills(item):
    #         to_return.append(item)
    #
    #
    # return to_return




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

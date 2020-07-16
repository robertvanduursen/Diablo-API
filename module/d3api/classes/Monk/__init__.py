import os, sys, inspect

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..\..')))
import classes

import classes.Monk.skills as Monk_skills

import data.items_cache
import data.weapons_cache
from datatypes import Active
import classes.Monk.skills
import classes.Monk.passives
from item_utils import skill_dict_generator
from datatypes import Skill, isGenerator

if __name__ != '__main__':
    skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(Monk_skills, inspect.isclass) if
                   Active in cls.__bases__]

    from utils import item_utils

    items = item_utils.get_skill_items(data.items_cache, 'Monk') + item_utils.get_skill_items(data.weapons_cache,
                                                                                                'Monk')
    skill_dict = skill_dict_generator(items, skill_names)


def get_generators():
    total = 0
    generators = []
    for cache in [classes.Monk.skills, classes.Monk.passives, data.items_cache, data.weapons_cache]:
        for x, cls in inspect.getmembers(cache, isGenerator):
            print(x, inspect.getsource(cls))
            print()
            generators.append(x)
            total += 1

    # print(total)
    return generators


def get_items_that_boost(skillName: str):
    if skillName not in skill_names:
        raise Exception('not a valid skill')

    return skill_dict[skillName]


# generators = get_generators()


def get_class_armour_sets(class_name):
    import data.armor_sets as armor_sets
    from datatypes import Set

    class_armor_sets = []
    for x, cls in inspect.getmembers(armor_sets, lambda x: inspect.isclass(x) and issubclass(x, Set)):
        if cls._class == class_name:
            # print(x, inspect.getsource(cls))
            # print()
            class_armor_sets.append(cls)

    return class_armor_sets


armor_sets = get_class_armour_sets('Monk')

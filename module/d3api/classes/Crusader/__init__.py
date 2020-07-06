import os, sys, inspect

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..\..')))
import classes
import classes.Crusader.skills as crusader_skills

import data.items_cache
import data.weapons_cache
from datatypes import Active
import classes.Crusader.skills
import classes.Crusader.passives
from item_utils import skill_dict_generator
from datatypes import Skill, isGenerator

if __name__ != '__main__':

    skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(crusader_skills, inspect.isclass) if
                   Active in cls.__bases__]

    from utils import item_utils

    items = item_utils.get_skill_items(data.items_cache) + item_utils.get_skill_items(data.weapons_cache)

    import collections

    skill_dict = skill_dict_generator(items, skill_names)


def get_generators():
    total = 0
    generators = []
    for cache in [classes.Crusader.skills, classes.Crusader.passives, data.items_cache, data.weapons_cache]:
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

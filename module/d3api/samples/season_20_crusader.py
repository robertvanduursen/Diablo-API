"""

Season 20 Crusader build

"""

# https://www.youtube.com/watch?v=7D46AlZSur0

# https://www.d3planner.com/335087708

#https://eu.diablo3.com/en/profile/Ralicx-2273/

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import classes.Crusader.skills
import classes.Crusader.passives
import data.items_cache
import data.weapons_cache


from datatypes import Skill, isGenerator
import inspect

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


get_generators()



if 1 == 1:
    import os, sys

    # sys.path.append("..\..")

    from Playstyle import Playstyle
    from utils import analyse_sets
    from utils import item_utils
    from classes.Crusader import skills as _skills

    _test = Playstyle(cls='Crusader')
    _test.discover.focus('close up')

    # analyse_sets.get_sets(items)

    #
    # for x in item_utils.get_class_eligible_items(weapons, 'crusader'):
    #     print(x)

    total = 0
    skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(classes.Crusader.skills, inspect.isclass) if
                   _skills.Skill in cls.__bases__]

    import collections
    score_dict = collections.defaultdict(int)



    for item in item_utils.debug_get_items(data.items_cache) + item_utils.debug_get_items(data.weapons_cache):
        for name in skill_names:
            if name in inspect.getsource(item):
                score_dict[name] += 1

    for name, freq in sorted(score_dict.items(), key=lambda x: -x[1]):
        print(name, freq)


    # from d3api.character import Character
    # build_1 = Character()
    #
    # # import items_cache as items
    # # import weapons_cache as weapons
    # build_1.equip(items.Rolands_Bearing)
    # build_1.equip(items.Rolands_Visage)
    # build_1.equip(items.Spaulders_of_Valor)
    # build_1.equip(items.Stone_Gauntlets)
    # build_1.equip(weapons.Nutcracker)





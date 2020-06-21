"""

Season 20 Crusader build

"""

# https://www.youtube.com/watch?v=7D46AlZSur0

# https://www.d3planner.com/335087708

#https://eu.diablo3.com/en/profile/Ralicx-2273/

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import classes.Crusader
import classes.Crusader.skills
import classes.Crusader.passives
import data.items_cache
import data.weapons_cache
import inspect


def rank_skill_support():
    """ examine how many items support a skill """
    import collections
    score_dict = collections.defaultdict(int)
    for item in classes.Crusader.items:
        for name in classes.Crusader.skill_names:
            if name in inspect.getsource(item):
                score_dict[name] += 1

    for name, freq in sorted(score_dict.items(), key=lambda x: -x[1]):
        print(name, freq)


if 1 == 1:
    import os, sys

    # sys.path.append("..\..")

    from Playstyle import Playstyle

    _test = Playstyle(cls='Crusader')
    _test.discover.focus('close up')

    # rank_skill_support()

    # print(classes.Crusader.get_items_that_boost('Blessed Hammer'))

    crusader_belts = [x for x in classes.Crusader.items if x.type == 'waist']
    print(len(crusader_belts))
    for x in crusader_belts:
        print(x.__doc__)
        print(x.text)

    from character import Character
    build_1 = Character()

    import data.items_cache as items
    import data.weapons_cache as weapons
    build_1.equip(items.Ring_of_Royal_Grandeur)

    build_1.equip(items.Rolands_Bearing)
    build_1.equip(items.Rolands_Visage)
    build_1.equip(items.Spaulders_of_Valor)
    build_1.equip(items.Gauntlets_of_Valor)
    build_1.equip(weapons.Nutcracker)

    build_1.equip(items.Blessed_of_Haull)

    build_1.show_bonus()




# todo: an exercise in excluding option ranges through knowing / 100% fact reasoning


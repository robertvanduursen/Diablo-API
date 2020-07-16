"""

Season 20 Wizard build

"""


# https://www.youtube.com/watch?v=7D46AlZSur0

# https://www.d3planner.com/335087708

#https://eu.diablo3.com/en/profile/Ralicx-2273/

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import classes.Monk
import classes.Monk.skills
import classes.Monk.passives
import data.items_cache
import data.weapons_cache
import inspect
from datatypes import Set_Item

def rank_skill_support():
    """ examine how many items support a skill """
    import collections
    score_dict = collections.defaultdict(int)
    for item in classes.Monk.items:
        for name in classes.Monk.skill_names:
            if name in inspect.getsource(item):
                score_dict[name] += 1

    for name, freq in sorted(score_dict.items(), key=lambda x: -x[1]):
        print(name, freq)


        # Wizard_belts = [x for x in classes.Monk.items if x.type == 'waist']
        # print(len(Wizard_belts))
        # for x in Wizard_belts:
        #     print(x.__doc__)
        #     print(x.text)


for _set in classes.Monk.armor_sets:
    print(_set)
    for x in _set.levels.items():
        print(x)
    print(_set.pieces)
    print()

def class_legendary_item_effects(cls='Wizard'):
    for nr, item in enumerate(filter(lambda x: not issubclass(x, Set_Item), classes.Monk.items)):
        print(nr, item.__doc__.strip())
        print(item.text.strip())
        print()
class_legendary_item_effects()

print()
print("rank_skill_support")
rank_skill_support()

if 0:
    import os, sys

    from Playstyle import Playstyle, Discovery
    # chosen_skills = Discovery()
    # chosen_skills.save_file = r'G:\projects\Diablo-API\module\d3api\samples\season_21_Monk_skills.json'
    # chosen_skills.pick()

    chosen_skills = Discovery('season_21_Monk_skills.json').chosen_skills

    _test = Playstyle(cls='Monk')
    _test.discover.focus('close up')
    _test.discover.focus('resource regen')



    print()
    print('items_that_boost_my_chosen_skills')
    import collections
    items_that_boost_my_chosen_skills = collections.defaultdict(list)
    for name in chosen_skills:
        items_that_boost_my_chosen_skills[name] = classes.Monk.get_items_that_boost(name)
        print(name, [y.__doc__.strip() for y in items_that_boost_my_chosen_skills[name]])

    print()
    print('overlap between items that support multiple skills')
    competition = collections.defaultdict(int)
    for idx,(name, items) in enumerate(items_that_boost_my_chosen_skills.items()):
        print(name)
        print([x.type for x in items])
        for x in items:
            competition[x.type] += 1

    # print()
    # print('what is this? ')
    # for part, freq in competition.items():
    #     print(part, freq)

    if 0:
        overlap = tuple(tuple(items_that_boost_my_chosen_skills.values())[0])
        for idx, x in enumerate(items_that_boost_my_chosen_skills.values()):
            print(idx, overlap)
            print(tuple(x))
            overlap = set(overlap) & set(tuple(x))
        print(len(overlap), overlap)
        # print(classes.Monk.get_items_that_boost('Blessed Hammer'))

if 0:
    # Wizard_belts = [x for x in classes.Monk.items if x.type == 'waist']
    # print(len(Wizard_belts))
    # for x in Wizard_belts:
    #     print(x.__doc__)
    #     print(x.text)

    from character import Character
    build_1 = Character()

    import data.items_cache as items
    import data.weapons_cache as weapons

    activ = classes.Monk.skills
    build_1.active_skills = [
        activ.Army_of_the_Dead,  # + activ.Unconventional_Warfare,
        activ.Bone_Spear,  # + activ.Blood_Spear,
        activ.Siphon_Blood,  # + activ.Blood_Sucker,
        activ.Blood_Rush,  # + activ.Metabolism,
        activ.Frailty,  # + activ.Aura_of_Frailty,
        activ.Devour,  # + activ.Devouring_Aura,
    ]
    passiv = classes.Monk.passives
    build_1.passive_skills = [
        passiv.Life_from_Death,
        passiv.Blood_for_Blood,
        passiv.Serration,
        passiv.Spreading_Malediction
    ]

    build_1.equip(items.Ring_of_Royal_Grandeur)
    build_1.equip(items.Funerary_Pick)

    build_1.equip(items.Pestilence_Battle_Boots)
    build_1.equip(items.Maltorius_Petrified_Spike)
    build_1.equip(items.Haunted_Visions)
    build_1.equip(items.TragOuls_Guise)
    build_1.equip(items.TragOuls_Claws)
    build_1.equip(items.TragOuls_Heart)
    build_1.equip(items.TragOuls_Stalwart_Greaves)
    build_1.equip(items.TragOuls_Corroded_Fang)

    items.Mantle_of_Channeling
    weapons.Deathwish

    build_1.show_bonus()





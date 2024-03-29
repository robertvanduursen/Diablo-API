"""

Season 20 Necromancer build

"""


# https://www.youtube.com/watch?v=7D46AlZSur0

# https://www.d3planner.com/335087708

#https://eu.diablo3.com/en/profile/Ralicx-2273/

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import classes.Necromancer
import classes.Necromancer.skills
import classes.Necromancer.passives
import data.items_cache
import data.weapons_cache
import inspect


def rank_skill_support():
    """ examine how many items support a skill """
    import collections
    score_dict = collections.defaultdict(int)
    for item in classes.Necromancer.items:
        for name in classes.Necromancer.skill_names:
            if name in inspect.getsource(item):
                score_dict[name] += 1

    for name, freq in sorted(score_dict.items(), key=lambda x: -x[1]):
        print(name, freq)


        # Necromancer_belts = [x for x in classes.Necromancer.items if x.type == 'waist']
        # print(len(Necromancer_belts))
        # for x in Necromancer_belts:
        #     print(x.__doc__)
        #     print(x.text)


# for _set in classes.Necromancer.armor_sets:
#     print(_set)
#     print(_set.pieces)

# for item in classes.Necromancer.items:
#     print(item.__doc__)
#     print(item.text)
#     print()
#
# print(len(classes.Necromancer.items))

if 1:
    import os, sys

    # sys.path.append("..\..")

    from Playstyle import Playstyle, Discovery

    # chosen_skills = Discovery()
    # chosen_skills.save_file = r'G:\projects\Diablo-API\module\d3api\samples\season_20_Necromancer_skills.json'
    # chosen_skills.pick()

    chosen_skills = Discovery('season_21_Necromancer_skills.json').chosen_skills

    _test = Playstyle(cls='Necromancer')
    _test.discover.focus('close up')
    _test.discover.focus('resource regen')

    print()
    print("rank_skill_support")
    rank_skill_support()

    print()
    print('items_that_boost_my_chosen_skills')
    import collections
    items_that_boost_my_chosen_skills = collections.defaultdict(list)
    for name in chosen_skills:
        items_that_boost_my_chosen_skills[name] = classes.Necromancer.get_items_that_boost(name)
        print(name, [y.__doc__.strip() for y in items_that_boost_my_chosen_skills[name]])

    print()
    print('overlap between items that support multiple skills')
    competition = collections.defaultdict(int)
    for idx,(name, items) in enumerate(items_that_boost_my_chosen_skills.items()):
        print(name)
        print([x.type for x in items])
        for x in items:
            competition[x.type] += 1

    print()
    print('what is this? ')
    for part, freq in competition.items():
        print(part, freq)


    overlap = tuple(tuple(items_that_boost_my_chosen_skills.values())[0])
    for idx, x in enumerate(items_that_boost_my_chosen_skills.values()):
        print(idx, overlap)
        print(tuple(x))
        overlap = set(overlap) & set(tuple(x))
    print(len(overlap), overlap)
        # print(classes.Necromancer.get_items_that_boost('Blessed Hammer'))

if 1:


    from character import Character
    build_1 = Character()

    import data.items_cache as items
    import data.weapons_cache as weapons

    activ = classes.Necromancer.skills
    build_1.active_skills = [
        activ.Simulacrum,  # + activ.Unconventional_Warfare,
        activ.Bone_Spear,  # + activ.Blood_Spear,

        activ.Siphon_Blood,  # + activ.Blood_Sucker,
        activ.Blood_Rush,  # + activ.Metabolism,
        activ.Frailty,  # + activ.Aura_of_Frailty,
        activ.Devour,  # + activ.Devouring_Aura,
    ]
    passiv = classes.Necromancer.passives
    build_1.passive_skills = [
        passiv.Life_from_Death,
        passiv.Blood_for_Blood,
        passiv.Serration,
        passiv.Spreading_Malediction
    ]

    build_1.equip(items.Ring_of_Royal_Grandeur)

    build_1.equip(items.Luxurious_Bauta)
    build_1.equip(items.Sophistocated_Vest)
    build_1.equip(items.Lavishing_Gloves)
    build_1.equip(items.Extravagant_Shoes)
    build_1.equip(items.Elegant_Pants)
    build_1.equip(items.Glamorous_Gigot)




    build_1.show_bonus()
    build_1.show_summary()



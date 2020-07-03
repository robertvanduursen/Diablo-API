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


if 1 == 1:
    import os, sys

    # sys.path.append("..\..")

    from Playstyle import Playstyle, Discovery

    # chosen_skills = Discovery()
    # chosen_skills.save_file = r'G:\projects\Diablo-API\module\d3api\samples\season_20_Necromancer_skills.json'
    # chosen_skills.pick()

    chosen_skills = Discovery('season_20_Necromancer_skills.json').chosen_skills

    _test = Playstyle(cls='Necromancer')
    _test.discover.focus('close up')
    print("rank_skill_support")
    rank_skill_support()

    print()
    import collections
    items_that_boost_my_chosen_skills = collections.defaultdict(list)
    for name in chosen_skills:
        items_that_boost_my_chosen_skills[name] = classes.Necromancer.get_items_that_boost(name)
        print(name, [y.__doc__.strip() for y in items_that_boost_my_chosen_skills[name]])

    print()
    competition = collections.defaultdict(int)
    for idx,(name, items) in enumerate(items_that_boost_my_chosen_skills.items()):
        print(name)
        print([x.type for x in items])
        for x in items:
            competition[x.type] += 1

    print()
    for part, freq in competition.items():
        print(part, freq)


    overlap = tuple(tuple(items_that_boost_my_chosen_skills.values())[0])
    for idx, x in enumerate(items_that_boost_my_chosen_skills.values()):
        print(idx, overlap)
        print(tuple(x))
        overlap = set(overlap) & set(tuple(x))
    print(len(overlap), overlap)
        # print(classes.Necromancer.get_items_that_boost('Blessed Hammer'))

    if 0:
        Necromancer_belts = [x for x in classes.Necromancer.items if x.type == 'waist']
        print(len(Necromancer_belts))
        for x in Necromancer_belts:
            print(x.__doc__)
            print(x.text)

        from character import Character
        build_1 = Character()

        import data.items_cache as items
        import data.weapons_cache as weapons

        build_1.equip(items.Ring_of_Royal_Grandeur)
        build_1.equip(items.Blessed_of_Haull)

        build_1.equip(items.Pestilence_Battle_Boots)
        build_1.equip(items.Maltorius_Petrified_Spike)
        build_1.equip(items.Haunted_Visions)
        build_1.equip(items.Gauntlets_of_Valor)
        build_1.equip(weapons.Nutcracker)


        build_1.show_bonus()




# todo: an exercise in excluding option ranges through knowing / 100% fact reasoning


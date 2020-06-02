"""

Season 20 Barbarian build

"""
import inspect
from items import Immortal_Kings_Call
import skills

# print(Immortal_Kings_Call().setbonus)




# skills.Call_of_the_Ancients().data

classes = [
    'barbarian',
    'wizard',
    'witch doctor',
    'demon hunter',
    'necromancer',
    'crusader',
    'monk',
]

def get_class_eligible_items(class_name = 'barbarian'):

    import items_cache

    total = 0
    items = []
    remaining_classes = set(classes) - {class_name}
    for name, cls in inspect.getmembers(items_cache, inspect.isclass):
        class_str = inspect.getsource(cls).lower()
        if not any([_cls in class_str for _cls in remaining_classes]) or class_name in class_str:
            # print(inspect.getsource(cls))
            total += 1
            items.append(cls)

    print(total)
    return items


eligible_items = get_class_eligible_items()

skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(skills, inspect.isclass) if skills.Skill in cls.__bases__]

def match_skills(item):
    """ filter items based on if they match a class skill """
    text = inspect.getsource(item)
    if any([skill in text for skill in skill_names]):
        return True
    return False

filtered = list(filter(match_skills, eligible_items))

# for nr, item in enumerate(filtered):
#     print(nr, inspect.getsource(item))

print(len(filtered))


from character import Character

build_1 = Character()

from items_cache import Raekors_Burden, Ring_of_Royal_Grandeur
from items_cache import Cuirass_of_the_Wastes, Tasset_of_the_Wastes, Gauntlet_of_the_Wastes, Sabaton_of_the_Wastes

build_1.equip(Raekors_Burden)
build_1.equip(Ring_of_Royal_Grandeur)
build_1.equip(Cuirass_of_the_Wastes)
build_1.equip(Tasset_of_the_Wastes)
build_1.equip(Gauntlet_of_the_Wastes)
build_1.equip(Sabaton_of_the_Wastes)

build_1.show_summary()



build_2 = Character()

from items_cache import Ring_of_Royal_Grandeur
from weapons_cache import Blade_of_the_Tribes
from items_cache import Raekors_Breeches, Raekors_Burden, Raekors_Striders, Raekors_Will


build_2.equip(Raekors_Burden)
build_2.equip(Ring_of_Royal_Grandeur)
build_2.equip(Raekors_Burden)
build_2.equip(Raekors_Breeches)
build_2.equip(Raekors_Striders)

build_2.equip(Raekors_Will)
build_2.equip(Blade_of_the_Tribes)

build_2.show_bonus()

print(build_2.recognize(build_2.two_handed))

build_2.two_handed.get_stat_potential()


'''
todo: how can you reason that:
you want X, Y and Z, but have these constraints
then you still need an Aim / maximizer / sorting mechanism

'''


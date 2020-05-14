"""

Season 20 Barbarian build

"""
import inspect
from items import Immortal_Kings_Call
import skills

# print(Immortal_Kings_Call().setbonus)




skills.Call_of_the_Ancients().data

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

for item in filtered:
    # print(item)
    print(inspect.getsource(item))

print(len(filtered))


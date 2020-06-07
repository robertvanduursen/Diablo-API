import inspect

from datatypes import classes


def get_class_eligible_items(class_name = 'barbarian'):

    import Barbarian.items_cache as items_cache

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

import Barbarian.skills as _skills
skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(_skills, inspect.isclass) if _skills.Skill in cls.__bases__]

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

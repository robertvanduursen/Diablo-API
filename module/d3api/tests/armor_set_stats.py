from datatypes import Classes
from item_utils import get_class_armour_sets, get_non_class_armour_sets

stats = {}
biggest_set = [0, 'none']
most_sets = [0, 'none']

for cls in Classes.items():
    armor_sets = get_class_armour_sets(cls.value)  # 'Necromancer'
    print('The {} has {} set armors'.format(cls.value, len(armor_sets)))

    if len(armor_sets) > most_sets[0]:
        most_sets = [len(armor_sets), cls]

    for x in armor_sets:
        print(x.__doc__)
        print("{} pieces".format(x.size))
        if x.size > biggest_set[0]:
            biggest_set = [x.size, cls]
        for level, effect in x.levels.items():
            print("@ {} -> {}".format(level, effect))
        print()
    print()


print()
print('----- NON-CLASS ARMOUR SETS -----')
non_class_armour_sets = get_non_class_armour_sets()
print('The remaining has {} armors'.format(len(non_class_armour_sets)))

for idx, armor in enumerate(non_class_armour_sets):
    print(idx, armor.__doc__)
    print("{} pieces".format(armor.size))
    for level, effect in armor.levels.items():
        print("@ {} -> {}".format(level, effect))
    print()
print()

print('biggest set =', biggest_set)
print('most sets =', most_sets)

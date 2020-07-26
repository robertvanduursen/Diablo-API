from item_utils import get_class_armour_sets
armor_sets = get_class_armour_sets('Necromancer')

for x in armor_sets:
    print(x)
    print(x.size)
    for level in x.levels.items():
        print(level)
    print()

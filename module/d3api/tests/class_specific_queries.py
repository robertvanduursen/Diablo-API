import os, sys, inspect

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..\..')))

import classes.Barbarian as myClass


print('belts')
class_belts = [x for x in myClass.items if x.type == 'waist']
print(len(class_belts))
for x in class_belts:
    print(x.__doc__)
    print(x.text)

print('rings')
class_belts = [x for x in myClass.items if x.type == 'ring']
print(len(class_belts))
for x in class_belts:
    print(x.__doc__)
    print(x.text)

print('amulets')
class_belts = [x for x in myClass.items if x.type == 'amulet']
print(len(class_belts))
for x in class_belts:
    print(x.__doc__)
    print(x.text)

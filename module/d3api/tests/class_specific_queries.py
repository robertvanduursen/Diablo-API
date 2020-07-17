import os, sys, inspect

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..\..')))

import classes.Monk as myClass


print('belts')
Monk_belts = [x for x in myClass.items if x.type == 'waist']
print(len(Monk_belts))
for x in Monk_belts:
    print(x.__doc__)
    print(x.text)

print('rings')
Monk_belts = [x for x in myClass.items if x.type == 'ring']
print(len(Monk_belts))
for x in Monk_belts:
    print(x.__doc__)
    print(x.text)

print('amulets')
Monk_belts = [x for x in myClass.items if x.type == 'neck']
print(len(Monk_belts))
for x in Monk_belts:
    print(x.__doc__)
    print(x.text)
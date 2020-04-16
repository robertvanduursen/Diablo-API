
from activeSkills import *
from passiveSkills import *

# print(globals().items())



levels = []
for k,v in list(globals().items()):

    if type(v) == type:
        if issubclass(v, Passive) and v != Passive:
            print(v.level, v)
            levels.append(v.level)

        if issubclass(v, Spell) and v != Spell:
            print(v.level, v)
            levels.append(v.level)

for x in range(70):
    if x not in levels:
        print('no new unlock @ level: %s' % x)


Goal = """

a way to visualize the sheer depth of all the possible Builds in all its glory
and learning to recognize shapes of preferred ones

"""

Build_desires = [
    max('damage per time'),
    max('best range'),
    max('not having to spec into defense'),
    max('pure offense'),
    max('best control'), # control CAN BE through sheer offensive power, if control == 'not dying'
]
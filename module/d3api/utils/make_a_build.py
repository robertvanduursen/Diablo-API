"""

10/07/2020 09:49
'make a build around this item'


"""

# item = 'Spear of Jairo'
from data.weapons_cache import Spear_of_Jairo

item = Spear_of_Jairo()
print(item.text)

tokens = item.interpret()
print(tokens)


import Interpeter

inter = Interpeter.Interpeter(tokens)
print(inter.process())
build_focus = []
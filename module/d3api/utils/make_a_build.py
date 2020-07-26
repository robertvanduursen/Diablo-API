"""

10/07/2020 09:49
'make a build around this item'


"""

# item = 'Spear of Jairo'
from data.weapons_cache import Spear_of_Jairo

from data.items_cache import Lavishing_Gloves

item = Lavishing_Gloves()
print(item.text)

tokens = item.interpret()
print('tokens =', tokens)


import Interpeter

inter = Interpeter.Interpeter(tokens)
inter.process()
build_focus = []

print(inter.result)
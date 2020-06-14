"""

Season 20 Crusader build

"""

# https://www.youtube.com/watch?v=7D46AlZSur0

# https://www.d3planner.com/335087708

#https://eu.diablo3.com/en/profile/Ralicx-2273/

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Crusader
import Crusader.skills as skills
print(skills)
print(Crusader)

import os, sys

sys.path.append("..\..")
from d3api.Crusader import items_cache as items
from d3api.Crusader import weapons_cache as weapons
from d3api.Playstyle import Playstyle
from d3api.utils import analyse_sets
from d3api.utils import item_utils
from d3api.Crusader import skills as _skills

_test = Playstyle(cls='Crusader')
_test.discover.focus('close up')

# analyse_sets.get_sets(items)


for x in item_utils.get_class_eligible_items(weapons, 'crusader'):
    print(x)




from d3api.character import Character
build_1 = Character()

# import items_cache as items
# import weapons_cache as weapons
build_1.equip(items.Rolands_Bearing)
build_1.equip(items.Rolands_Visage)
build_1.equip(items.Spaulders_of_Valor)
build_1.equip(items.Stone_Gauntlets)
build_1.equip(weapons.Nutcracker)





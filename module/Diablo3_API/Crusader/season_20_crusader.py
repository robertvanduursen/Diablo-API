"""

Season 20 Crusader build

"""

# https://www.youtube.com/watch?v=7D46AlZSur0

# https://www.d3planner.com/335087708

#https://eu.diablo3.com/en/profile/Ralicx-2273/

import Crusader.skills

from Playstyle import Playstyle

_test = Playstyle(cls='Crusader')

_test.discover.focus('close up')

from utils import analyse_sets
from utils import item_utils



import Crusader.items_cache as items
# analyse_sets.get_sets(items)


for x in item_utils.get_class_eligible_items(items, 'crusader'):
    print(x)
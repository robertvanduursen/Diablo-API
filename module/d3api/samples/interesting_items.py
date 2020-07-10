"""

Season 20 Wizard build

"""


# https://www.youtube.com/watch?v=7D46AlZSur0

# https://www.d3planner.com/335087708

#https://eu.diablo3.com/en/profile/Ralicx-2273/

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import data.items_cache
import data.weapons_cache
from datatypes import Item, Set_Item

from item_utils import get_class_eligible_items, exclude_other_class_items

import inspect


if __name__ == '__main__':

    items = []
    for name, cls in inspect.getmembers(data.items_cache, inspect.isclass):
        if issubclass(cls, Item) and cls is not Item and cls is not Set_Item:
            items.append(cls)

    weapons = []
    for name, cls in inspect.getmembers(data.weapons_cache, inspect.isclass):
        if issubclass(cls, Item) and cls is not Item and cls is not Set_Item:
            weapons.append(cls)

    eligible_items = exclude_other_class_items(items + weapons, 'Wizard')

    for nr, item in enumerate(eligible_items):
        print(nr, item.__doc__.strip())
        print(item.text.strip())
        print()


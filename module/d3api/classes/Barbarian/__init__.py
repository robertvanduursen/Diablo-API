import os, sys, inspect

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..\..')))

import classes.Barbarian.skills as Barbarian_skills

import data.items_cache
import data.weapons_cache
from datatypes import Active
import classes.Barbarian.skills
import classes.Barbarian.passives
from item_utils import skill_dict_generator

if __name__ != '__main__':
    skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(Barbarian_skills, inspect.isclass) if
                   Active in cls.__bases__]

    from utils import item_utils

    items = item_utils.get_skill_items(data.items_cache, 'Barbarian') + item_utils.get_skill_items(data.weapons_cache, 'Barbarian')

    skill_dict = skill_dict_generator(items, skill_names)


class ItemsManager:

    def __init__(self):
        pass

    def strip_lang_from_url(self, url):
        parts = url.split('/')
        # print(parts)
        return '/'.join(parts[2:])

    def load_by_url(self, url, part_hint: str = False):

        import data.items_cache

        import inspect

        url = self.strip_lang_from_url(url)

        for name, cls in inspect.getmembers(data.items_cache):
            if hasattr(cls, 'url'):
                item_url = self.strip_lang_from_url(cls.url)
                if url == item_url:
                    # print(name)
                    return cls

        if part_hint:
            if part_hint in ['slot-mainHand', 'slot-mainHand']:
                # then try the weapons cache
                import data.weapons_cache
                for name, cls in inspect.getmembers(data.weapons_cache):
                    if hasattr(cls, 'url'):
                        item_url = self.strip_lang_from_url(cls.url)
                        if url == item_url:
                            # print(name)
                            return cls

        return False


items_manager = ItemsManager()
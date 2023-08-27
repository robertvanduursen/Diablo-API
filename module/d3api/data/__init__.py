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
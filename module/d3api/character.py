import enum


class Weapon:
    damage = int


class Resource(enum.Enum):
    FURY = "Fury"
    ARCANA = "Arcana"

    regen = 'way of generating'  # update tick & trigger


class Character(object):
    """ a character template """

    name = str
    classType = None

    ring_left = False
    ring_right = False
    amulet = False
    helm = False
    shoulders = False
    torso = False
    wrists = False
    hands = False
    waist = False
    pants = False
    feet = False
    phylactery = False

    off_hand = False
    one_handed = False
    two_handed = False

    weapon = Weapon
    resource = Resource

    # def check(self):
    #     if weapon = 2 hander: then off hand has no item

    cube_power_1 = False
    cube_power_2 = False
    cube_power_3 = False

    paragon_points = 0

    Strength = 0
    Dexterity = 0
    Intelligence = 0
    Vitality = 0
    Damage = 0
    Toughness = 0
    Recovery = 0

    active_skills = list
    passive_skills = list

    def __init__(self):

        import inspect
        for name, cls in inspect.getmembers(self.__class__, lambda x: not inspect.isroutine(x)):
            if not name.startswith('__'):
                # print(name, cls)
                # todo: why the set-to-none again?
                self.__dict__[name] = None
                self.Damage = 0

        # for x in self.__dict__.items():
        #     print(x)

    def recognize(self, item):
        print('recognizing item')
        print(item.text)

        import skills, inspect
        skill_names = [cls.__doc__.strip() for name, cls in inspect.getmembers(skills, inspect.isclass) if
                       skills.Skill in cls.__bases__]

        def match_skills(item):
            """ filter items based on if they match a class skill """
            text = inspect.getsource(item)
            if any([skill in text for skill in skill_names]):
                return True
            return False

        def get_matching_skill(item):
            """ filter items based on if they match a class skill """
            text = inspect.getsource(item)
            for skill in skill_names:
                if skill in text:
                    print(skill)

        if match_skills(item.__class__):
            print(get_matching_skill(item.__class__))

    def load_from_save(self):
        pass
        saves_folder = r"G:\Diablo-API\module\d3api\saves\test.json"
        from data.items_cache import Raekors_Burden, Ring_of_Royal_Grandeur
        from data.items_cache import Cuirass_of_the_Wastes, Tasset_of_the_Wastes, Gauntlet_of_the_Wastes, \
            Sabaton_of_the_Wastes

        import json
        from data import items_manager

        with open(saves_folder, 'r') as save_file:
            data = json.load(save_file)
            self.name = data['name']
            self.classType = data['classType']

            # now fetch the actives and passives for the class
            import importlib
            myClassModule = importlib.import_module('classes.{}'.format(self.classType))

            self.active_skills = []
            for skill in data['active_skills']:
                name = skill['name']
                rune = skill['rune']

                skill = eval(f"myClassModule.skills.{name.replace(' ', '_')}()")
                print("skill.runes", skill.runes)
                for _rune in skill.runes:
                    if _rune.__name__ == rune.replace(' ', '_'):
                        skill.rune = _rune
                        break
                self.active_skills.append(skill)


            self.passive_skills = []
            import importlib
            passives = importlib.import_module('classes.{}.passives'.format(self.classType))
            from datatypes import Passive
            import inspect
            passives = {cls.__doc__.strip():cls for name, cls in inspect.getmembers(passives, inspect.isclass) if
                           Passive in cls.__bases__}
            for name in data['passive_skills']:
                self.passive_skills.append(passives[name]())



            for attr, val in data['core_attrs'].items():
                exec(f"self.{attr} = {int(val)}")

            for attr, val in data['sec_attrs'].items():
                exec(f"self.{attr} = {int(val)}")

            for part, url in data['gear_slots']:
                item = items_manager.load_by_url(url, part)
                # print(f"found item: {item} for url: {url}")
                self.equip(item)

        self.resource = Resource.FURY

    @property
    def items(self):
        # for item in self.__dict__.items():
        #     print(item)
        print('Summary =')
        from datatypes import Item
        return [item[1] for item in self.__dict__.items() if
                item[1] is not None and issubclass(item[1].__class__, Item)]

    def swap(self):
        print('which item do you want to swap?')
        equipped_items = {nr: item for nr, item in enumerate(self.items)}
        for nr, item in equipped_items.items():
            print('\t', nr, item)

        print('which nr?')
        choice = int(input())

        print('swapping {}'.format(equipped_items[choice]))
        print('options are:')

        import classes.Necromancer

        typed_items = {nr: item for nr, item in
                       enumerate(filter(lambda x: x.type == equipped_items[choice][0], classes.Necromancer.items))}
        for nr, item in typed_items.items():
            print('\t', nr, item.__doc__)
            print(item.text)
            print()

        print('which nr?')
        choice = int(input())

        print('looking to equip: {}'.format(typed_items[choice]))
        self.equip(typed_items[choice])

    def equip(self, item):
        # print('equipping {}'.format(item.__name__))

        if item.type == 'ring':
            # check for empty slot
            if not self.ring_left:
                self.__dict__['ring_left'] = item()
                print('equipped left ring:', self.__dict__['ring_left'])
            elif self.ring_left and not self.ring_right:
                self.__dict__['ring_right'] = item()
                print('equipped right ring:', self.__dict__['ring_right'])



        elif item.type == 'mighty-weapon-2h':
            # check for empty slot
            if not self.two_handed:
                self.__dict__['two_handed'] = item()
                print('equipped weapon:', self.__dict__['two_handed'])

        else:
            self.__dict__[item.type] = item()
            print('equipped', self.__dict__[item.type])

    def show_summary(self):
        for item in self.items:
            print(item.type, item.__doc__)
            print(item.text)

    def show_bonus(self):
        import collections
        sets = collections.defaultdict(int)
        for item in self.items:
            if 'Set_Item' in str(item.__class__.__mro__):
                if item.set:
                    sets[item.set] += 1

        # dirty edge case:
        from data.items_cache import Ring_of_Royal_Grandeur
        if isinstance(self.ring_left, Ring_of_Royal_Grandeur) or isinstance(self.ring_right, Ring_of_Royal_Grandeur):
            # print('Ring_of_Royal_Grandeur is equipped')
            for _set in sets.keys():
                sets[_set] += 1

        for _set, equipped in sets.items():
            print(_set, equipped)
            for bonus in _set().yield_bonus(equipped):
                print('bonus: {}'.format(bonus))
                # print(item.type, item.__doc__)
                # print(item.text)

    def max_me(self):
        """ """

    def calc_stats(self):
        """ signal calculates based off of Gear """

    def __sub__(self, other):
        self.Strength -= other.Strength
        # self.Dexterity -= other.Dexterity
        # self.Intelligence -= other.Intelligence

    def check_build_properties(self):
        pass

    def save(self):
        if self.save_file:
            import json
            with open(self.save_file, 'w') as save_off:
                json.dump(self.chosen_skills, save_off)

    def load(self):
        if self.save_file:
            import json
            with open(self.save_file) as load_in:
                self.chosen_skills = json.load(load_in)


'''
todo:
on Character obj -> a method or mechanism to compare 
i.e. distance to Goal or Criteria

a way to turn statements into effects
- 


'''

if __name__ == '__main__':
    t = Character()
    t.Strength = 100

    t.load_from_save()

    y = Character()
    y.Strength = 33

    t - y

    print(t.Strength)

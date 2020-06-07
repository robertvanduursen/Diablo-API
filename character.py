class Character(object):
    """ a character template """

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


    def __init__(self):

        import inspect
        for name, cls in inspect.getmembers(self.__class__, lambda x: not inspect.isroutine(x)):
            if not name.startswith('__'):
                # print(name, cls)
                self.__dict__[name] = None

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


    @property
    def items(self):
        for item in self.__dict__.items():
            print(item)
        return [item for item in self.__dict__.values() if item is not None]


    def equip(self, item):
        print('equipping {}'.format(item.__name__))

        if item.type == 'ring':
            # check for empty slot
            if not self.ring_left:
                self.__dict__['ring_left'] = item()
                print('equipped ring:', self.__dict__['ring_left'])
            elif self.ring_left and not self.ring_right:
                self.__dict__['ring_right'] = item()
                print('equipped ring:', self.__dict__['ring_right'])

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


'''
todo:
on Character obj -> a method or mechanism to compare 
i.e. distance to Goal or Criteria

a way to turn statements into effects
- 


'''


# todo: how does Gear / Character stat levels correspond to which Rift level is appropriate?


t = Character()
t.Strength = 100


y = Character()
y.Strength = 33

t - y

print(t.Strength)
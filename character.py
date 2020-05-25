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

    def __init__(self):

        import inspect
        for name, cls in inspect.getmembers(self.__class__, lambda x: not inspect.isroutine(x)):
            if not name.startswith('__'):
                # print(name, cls)
                self.__dict__[name] = None

        # for x in self.__dict__.items():
        #     print(x)



    def equip(self, item):
        print('equipping {}'.format(item.__name__))

        if item.type == 'ring':
            # check for empty slot
            slot = False

            if not self.ring_left:
                slot = self.__dict__['ring_left']

            slot = item()
            print('equipped', slot)
        else:
            self.__dict__[item.type] = item()
            print('equipped', self.__dict__[item.type])

'''
todo:
on Character obj -> a method or mechanism to compare 
i.e. distance to Goal or Criteria

a way to turn statements into effects
- 


'''


# todo: how does Gear / Character stat levels correspond to which Rift level is appropriate?

class Playstyle:
    """ the notion of a play-style """

    # emerges from items + skills + interface

    # yields: <the best build for X>

    cls = ''

    def __init__(self, cls=False):
        if cls:
            self._class = cls

    class Discover:

        def pick(self):
            return True

        def focus(self, on):
            """ what to focus on """

    def goals(self):
        return self.Goals()

    class Goals:

        def set(self):
            pass

    @property
    def discover(self):
        return self.Discover()

from d3api.datatypes import Classes, Gear


# helm = Gear(1)
# # shoulders = Gear(1)
# torso = Gear(3)
# # wrists = Gear(1)
# # hands = Gear(1)
# # waist = Gear(0)
# pants = Gear(2)
# # feet = Gear(1)
#
# amulet = Gear(1)
# ring_left_hand = Gear(1)
# ring_right_hand = Gear(1)
#
# main_hand = Gear(1)
# off_hand = Gear(1)
#
# import copy
#
# totalGems = 0
# # 15 * 280 = 4200

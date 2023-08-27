import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


class Discovery:

    def __init__(self, save_file=False):
        if save_file:
            self.save_file = save_file
            self.load(self.save_file)

    def pick(self):
        print('which class?')
        import classes
        import os
        print(classes)

        print(os.listdir(os.path.dirname(classes.__file__)))

        _class = input()
        print("picked {}".format(_class))

        print('classes.{}'.format(_class))
        import importlib
        myClassModule = importlib.import_module('classes.{}'.format(_class))
        print('myClassModule = {}'.format(myClassModule))
        # import classes.Crusader.skills

        chosen_skills = []
        for choice in range(6):
            for x in sorted(set(myClassModule.skill_names) - set(chosen_skills)):
                print(x)
            print('Pick a skill - {} choices left'.format(6 - choice))
            _skill_choice = input()
            print("you picked {}".format(_skill_choice))
            chosen_skills.append(_skill_choice)

        print('chosen_skills: {}'.format(chosen_skills))

        self.chosen_skills = chosen_skills
        self.save()

    def save(self):
        if self.save_file:
            import json
            with open(self.save_file, 'w') as save_off:
                json.dump(self.chosen_skills, save_off)

    def load(self, _file):
        if self.save_file:
            import json
            with open(_file) as load_in:
                self.chosen_skills = json.load(load_in)
                print("loaded saved skills: {}".format(self.chosen_skills))

    def focus(self, on):
        """ what to focus on """

    def swap_item(self):
        """ the notion of being able to pick from options """
        # todo: to be synergized with Character


# 'C:\Users\rober\Desktop\test\Diablo-API\module\d3api\samples'

class Maxxer:
    op = max

    def __init__(self):
        pass


class Playstyle:
    """ the notion of a play-style """

    # emerges from items + skills + interface

    # yields: <the best build for X>

    cls = ''

    def __init__(self, cls=False):
        from character import Character
        if isinstance(cls, Character):
            self._class = cls
        if cls:
            self._class = cls

        self.fixed_points = []

    def goals(self):
        return self.Goals()

    class Goals:

        def set(self):
            pass

    @property
    def discover(self):
        return Discovery()

    @property
    def fixed_points(self):
        return self.__fixed_pts

    @fixed_points.setter
    def fixed_points(self, val):
        self.__fixed_pts = val

    def shake(self):

        # measure dist of Char
        # dist = (char & fixed_points) - (char + Goals)
        # if dist < 0.0:
        #   then: room for improvement: start testing

        # todo: assemble a Char Min or Maxer
        #   ergo: if we cant't pre-configure a optimum char
        #   then play with things until you build the tool or toolset to do so

        from classes.Barbarian import items as class_items
        from classes.Barbarian import skill_dict

        for goal in self.Goals:
            # maxxing
            print(f"the goal is to max <{goal}>")
            options = []  # choose thing that are 'close' to the goals

            things_to_swap = self._class.active_skills
            things_to_swap += self._class.passive_skills
            things_to_swap += self._class.items

            for x in things_to_swap:
                if isinstance(x, self.fixed_points[0]):
                    things_to_swap.remove(x)
                    break

            import datatypes as dt
            for thing in things_to_swap:
                print(f"we got {thing}, lets see what the alternatives are:")
                cls = thing.__class__.__mro__[1]
                print(cls)

                if cls == dt.Active:
                    # fetch all
                    others = skill_dict
                elif cls == dt.Passive:
                    others = skill_dict
                elif cls == dt.Item:
                    print(thing.type)
                    others = [c for c in class_items if c.type == thing.type]
                    print(f"\t{len(others)} = {others}")

                    # swap the original for the other; in a *copy* of the build!
                    self._class.swap()

                    # then compare the copy to the original, with a metric

                else:
                    print('huh?')
                print()


# from d3api.datatypes import Classes, Gear


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

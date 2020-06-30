class Discovery:

    def __init__(self, save_file=False):
        if save_file:
            self.save_file = save_file
            self.load(self.save_file)


    def pick(self):
        print('which class?')
        import classes
        import os
        print(os.listdir(classes.__package__))

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

# 'C:\Users\rober\Desktop\test\Diablo-API\module\d3api\samples'

class Playstyle:
    """ the notion of a play-style """

    # emerges from items + skills + interface

    # yields: <the best build for X>

    cls = ''

    def __init__(self, cls=False):
        if cls:
            self._class = cls



    def goals(self):
        return self.Goals()

    class Goals:

        def set(self):
            pass

    @property
    def discover(self):
        return Discovery()

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

class TechTree:
    """ which chain yields the most insane damage """

    # which combinations work the best
    def __init__(self):
        pass



from classes.Barbarian import skills
from classes.Barbarian import passives
from datatypes import Active

for skill in dir(skills)[1:-8]:
    skill = eval(f'skills.{skill}')
    if issubclass(skill, Active):
        print(f"{skill} = {skill().description}")
        print(f"{skill} = {skill().tags}")
        print()


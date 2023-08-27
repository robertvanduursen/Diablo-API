from Playstyle import Playstyle
from classes.Barbarian.skills import Whirlwind
from character import Character

build_1 = Character()

# load Smitina
build_1.load_from_save()

print(build_1.active_skills)

ps = Playstyle(build_1)
ps.fixed_points = [Whirlwind]
print(ps.fixed_points)
ps.Goals = ['max effects on Whirlwind']

ps.shake()



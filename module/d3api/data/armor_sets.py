""" Items repository """

'''

ideally, I'd have this as as fully linked data network:
to facilitate exploring, contextual feedback &
python / pycharm automated type highlighting

'''

from datatypes import Item, Set, Set_Item



class Pestilence_Battle(Set):
    """ Pestilence Battle """
    items = list
    levels = {
    	2 : 'Each corpse you consume fires a Corpse Lance at a nearby enemy.',
    	4 : 'Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.',
    	6 : 'Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.'
    }

class Masquerade_of_the_Burning_Carnival(Set):
    """ Masquerade of the Burning Carnival """
    items = list
    levels = {
    	2 : 'Your Simulacrums no longer take damage, gains all runes, and its cooldown is refreshed when you die.',
    	4 : 'While you have a Simulacrum, damage is reduced by 50%. Damage you take is split with your Simulacrums as well.',
    	6 : 'Your Bone Spear deals 10,000% increased damage. Simulacrums gain triple this bonus.'
    }

class Rolands_Legacy(Set):
    """ Roland's Legacy """
    items = list
    levels = {
    	2 : 'Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.',
    	4 : 'Increase the damage of Shield Bash and Sweep Attack by 13,000%.',
    	6 : 'Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.'
    }

class The_Legacy_of_Raekor(Set):
    """ The Legacy of Raekor """
    items = []
    levels = {
        2: 'Increase the damage per second of Rend by 500% and its duration to 15 seconds.',
        4: 'During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.',
        6: 'Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.',
    }

class Aegis_of_Valor(Set):
    """ Aegis of Valor """
    items = list
    levels = {
	    2: "'Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.",
	    4: "Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.",
	    6: "Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%."
    }


class Immortal_Kings_Call(Set):
    """ Immortal King's Call armor set """
    set_size = 7

    @property
    def setbonus(self):
        return '''

        (2) Set:
             Call of the Ancients last until they die.
        (4) Set:
             Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
        (6) Set:
             While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.

        '''

    class Head:
        """ Helms """
        type = 'Helms'
        name = "Immortal King's Triumph"
        url = r'https://us.diablo3.com/en/item/immortal-kings-triumph-Unique_Helm_008_x1'

    class Hands:
        """ Gloves """
        type = 'Gloves'
        name = "Immortal King's Irons"
        url = r'https://us.diablo3.com/en/item/immortal-kings-irons-Unique_Gloves_008_x1'

    class Torso:
        """ Chest Armor """
        type = 'Chest Armor'
        name = "Immortal King's Eternal Reign"
        url = r'https://us.diablo3.com/en/item/immortal-kings-eternal-reign-Unique_Chest_013_x1'

    class Waist:
        """ Mighty Belts """
        type = 'Mighty Belts'
        name = "Immortal King's Tribal Binding"
        url = r'https://us.diablo3.com/en/item/immortal-kings-tribal-binding-Unique_BarbBelt_009_x1'

    class Legs:
        """ Pants """
        type = 'Pants'
        name = "Immortal King's Stature"
        url = r'https://us.diablo3.com/en/item/immortal-kings-stature-P2_Unique_Pants_02'

    class Feet:
        """ Boots """
        type = 'Boots'
        name = "Immortal King's Stride"
        url = r'https://us.diablo3.com/en/item/immortal-kings-stride-Unique_Boots_012_x1'

    class Two_Handed:
        """ Mighty Weapons """
        type = 'Mighty Weapons'
        name = "Immortal King's Boulder Breaker"
        url = r'https://us.diablo3.com/en/item/immortal-kings-boulder-breaker-Unique_Mighty_2H_010_x1'



'''
from Diablo.Diablo3_webScraper import get_part_from_url

for _url in [
    'https://us.diablo3.com/en/item/immortal-kings-triumph-Unique_Helm_008_x1',
    'https://us.diablo3.com/en/item/immortal-kings-irons-Unique_Gloves_008_x1',
    'https://us.diablo3.com/en/item/immortal-kings-eternal-reign-Unique_Chest_013_x1',
    'https://us.diablo3.com/en/item/immortal-kings-tribal-binding-Unique_BarbBelt_009_x1',
    'https://us.diablo3.com/en/item/immortal-kings-stature-P2_Unique_Pants_02',
    'https://us.diablo3.com/en/item/immortal-kings-stride-Unique_Boots_012_x1',
    'https://us.diablo3.com/en/item/immortal-kings-boulder-breaker-Unique_Mighty_2H_010_x1',
]:

    test = get_part_from_url(_url)
    if not test:
        assert False
    else:
        print(test)
'''

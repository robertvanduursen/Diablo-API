""" Items repository """

'''

ideally, I'd have this as as fully linked data network:
to facilitate exploring, contextual feedback &
python / pycharm automated type highlighting

'''

from datatypes import Item, Set, Set_Item
from datatypes import Head, Hands, Torso, Waist, Legs, Feet, Shoulders


class Pestilence_Masters_Shroud(Set):
    """ Pestilence Master's Shroud """
    _class = 'Necromancer'
    items = list
    levels = {
        2: 'Each corpse you consume fires a Corpse Lance at a nearby enemy.',
        4: 'Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.',
        6: 'Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.'
    }
    pieces = [Head, Hands, Torso, Legs, Feet, Shoulders]


class Masquerade_of_the_Burning_Carnival(Set):
    """ Masquerade of the Burning Carnival """
    _class = 'Necromancer'
    items = list
    levels = {
        2: 'Your Simulacrums no longer take damage, gains all runes, and its cooldown is refreshed when you die.',
        4: 'While you have a Simulacrum, damage is reduced by 50%. Damage you take is split with your Simulacrums as well.',
        6: 'Your Bone Spear deals 10,000% increased damage. Simulacrums gain triple this bonus.'
    }
    pieces = [Head, Hands, Torso, Legs, Feet, Shoulders]  # todo ?


class Rolands_Legacy(Set):
    """ Roland's Legacy """
    items = list
    levels = {
        2: 'Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.',
        4: 'Increase the damage of Shield Bash and Sweep Attack by 13,000%.',
        6: 'Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.'
    }


class The_Legacy_of_Raekor(Set):
    """ The Legacy of Raekor """
    items = []
    _class = 'Barbarian'
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


class Grace_of_Inarius(Set):
    """ Grace of Inarius """
    items = list
    _class = 'Necromancer'
    levels = {
        2: "'Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.",
        4: "Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.",
        6: "Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%."
    }
    pieces = []


class TragOuls_Avatar(Set):
    """ TragOul's Avatar """
    items = list
    _class = 'Necromancer'
    levels = {
        2: "Blood Rush gains the effect of every rune.",
        4: "While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.",
        6: "Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%."
    }
    pieces = [Hands, Legs, Head, Torso, Feet, Shoulders]


class Delseres_Magnum_Opus(Set):
    """ Delsere's Magnum Opus """
    items = list
    _class = "Wizard"
    levels = {
        2: "Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.",
        4: "You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.",
        6: "Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities."
    }
    pieces = [Hands, Legs, Head, Torso, Feet, Shoulders]


class Tal_Rashas_Elements(Set):
    """ Tal Rasha's Elements """
    items = list
    _class = "Wizard"
    levels = {
        2: "Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.",
        4: "Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.",
        6: "Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds."
    }
    pieces = [Hands, Legs, Head, Torso, Feet, Shoulders]


class The_Typhons_Veil(Set):
    """ 'The Typhon's Veil """
    items = list
    _class = "Wizard"
    levels = {
        2: "Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.",
        4: "Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.",
        6: "Hydras deal 1300% increased damage for each Hydra head alive."
    }
    pieces = [Hands, Legs, Head, Torso, Feet, Shoulders]


class Vyrs_Amazing_Arcana(Set):
    """ 'Vyr's Amazing Arcana' """
    items = list
    _class = "Wizard"
    levels = {
        2: "Archon gains the effect of every rune.",
        4: "Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.",
        6: "You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%."
    }
    pieces = [Hands, Legs, Head, Torso, Feet, Shoulders]


class Firebirds_Finery(Set):
    """ Firebird's Finery """
    items = list
    _class = "Wizard"
    levels = {
	    2: "When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.",
	    4: "Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.",
	    6: "Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited."
    }
    pieces = [Hands, Legs, Head, Torso, Feet, Shoulders]


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



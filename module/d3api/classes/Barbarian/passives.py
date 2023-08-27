from datatypes import Passive


class Pound_of_Flesh(Passive):
    """ Pound of Flesh """
    category = "passive"
    description = """When you are healed by a health globe, gain 2% Life regeneration per second and 4% increased movement speed for 15 seconds. This bonus stacks up to 5 times."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/pound-of-flesh'


class Ruthless(Passive):
    """ Ruthless """
    category = "passive"
    description = """You deal 40% additional damage to enemies below 30% health."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/ruthless'


class Nerves_of_Steel(Passive):
    """ Nerves of Steel """
    category = "passive"
    description = """Fatal damage instead reduces you to 15% Life. For 3 seconds afterward, you take 95% reduced damage and are immune to all control-impairing effects.

This effect may occur once every 60 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/nerves-of-steel'


class Weapons_Master(Passive):
    """ Weapons Master """
    category = "passive"
    description = """Gain a bonus based on the weapon type of your main hand weapon:
Swords/Daggers: 8% increased damage
Maces/Axes: 5% Critical Hit Chance
Polearms/Spears: 8% attack speed
Mighty Weapons: 2 Fury per hit"""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/weapons-master'


class Inspiring_Presence(Passive):
    """ Inspiring Presence """
    category = "passive"
    description = """The duration of your shouts is doubled. After using a shout you and all allies within 100 yards regenerate 3% of maximum Life per second for 120 seconds.

Your shouts are: Battle Rage Threatening Shout War Cry"""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/inspiring-presence'


class Berserker_Rage(Passive):
    """ Berserker Rage """
    category = "passive"
    description = """You deal 25% additional damage while near maximum Fury."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/berserker-rage'


class Bloodthirst(Passive):
    """ Bloodthirst """
    category = "passive"
    description = """Each point of Fury spent heals you for 966 Life.

Heal amount is increased by 1% of your Health Globe Healing Bonus."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/bloodthirst'


class Animosity(Passive):
    """ Animosity """
    category = "passive"
    description = """Increase all Fury generation by 10%.
Increase maximum Fury by 20.

Fury is used to fuel your most powerful attacks."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/animosity'


class Superstition(Passive):
    """ Superstition """
    category = "passive"
    description = """Reduce all non-Physical damage by 20%. When you take damage from a ranged or elemental attack, you have a chance to gain 2 Fury."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/superstition'


class Tough_as_Nails(Passive):
    """ Tough as Nails """
    category = "passive"
    description = """Increase Armor by 25%.
Increase Thorns by 100%."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/tough-as-nails'


class No_Escape(Passive):
    """ No Escape """
    category = "passive"
    description = """Increase the damage of Weapon Throw, Seismic Slam, Ancient Spear, and Avalanche by 30% against enemies more than 15 yards away from you."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/no-escape'


class Relentless(Passive):
    """ Relentless """
    category = "passive"
    description = """While below 35% Life, all skills cost 50% less Fury, Life per Fury Spent is doubled, and all damage taken is reduced by 50%."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/relentless'


class Brawler(Passive):
    """ Brawler """
    category = "passive"
    description = """As long as there are 3 enemies within 12 yards, all of your damage is increased by 20%."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/brawler'


class Juggernaut(Passive):
    """ Juggernaut """
    category = "passive"
    description = """The duration of control-impairing effects on you are reduced by 50%. In addition, whenever a Stun, Freeze, Fear, or Immobilize is cast on you, you have a chance to recover 20% of your maximum Life."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/juggernaut'


class Unforgiving(Passive):
    """ Unforgiving """
    category = "passive"
    description = """You no longer degenerate Fury. Instead, you generate 2 Fury every 1 second."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/unforgiving'


class Boon_of_Bul_Kathos(Passive):
    """ Boon of Bul-Kathos """
    category = "passive"
    description = """Reduce the cooldowns of your: Earthquake by 15 seconds. Call of the Ancients by 30 seconds. Wrath of the Berserker by 30 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/boon-of-bulkathos'


class Earthen_Might(Passive):
    """ Earthen Might """
    category = "passive"
    description = """Gain 30 Fury when Avalanche or Earthquake is triggered."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/earthen-might'


class Sword_and_Board(Passive):
    """ Sword and Board """
    category = "passive"
    description = """While wielding a shield, reduce all damage taken by 30% and reduce Fury costs by 20%."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/sword-and-board'


class Rampage(Passive):
    """ Rampage """
    category = "passive"
    description = """Increase Strength by 1% for 8 seconds after killing or assisting in killing an enemy. This effect stacks up to 25 times."""
    url = r'https://us.diablo3.com//en/class/barbarian/passive/rampage'


# all_passives = [y for x, y in locals().items() if isinstance(y, type) and Passive in y.__mro__][1:]

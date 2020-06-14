
class Passive: pass

class Power_Hungry(Passive):
    """Power Hungry"""
    level = 10
    rules = '''You deal 30% additional damage to enemies farther than 30 yards.'''

class Blur(Passive):
    """Blur"""
    level = 10
    rules = '''Decrease damage taken by 17%.'''

class Evocation(Passive):
    """Evocation"""
    level = 13
    rules = '''Reduce all cooldowns by 20%.'''

class Glass_Cannon(Passive):
    """Glass Cannon"""
    level = 16
    rules = '''Increase all damage done by 15%, but decrease Armor and resistances by 10%.'''

class Prodigy(Passive):
    """Prodigy"""
    level = 20
    rules = '''When you cast a Signature spell, you gain 5 Arcane Power.'''

class Astral_Presence(Passive):
    """Astral Presence"""
    level = 24
    rules = '''Increase your maximum Arcane Power by 20 and Arcane Power regeneration by 2.5 per second.'''

class Illusionist(Passive):
    """Illusionist"""
    level = 27
    rules = \
        ['''When you take more than 15% of your maximum Life in damage within 1 second, the cooldowns on Mirror Image, Slow Time, and Teleport are reset.''',
        '''When you use Mirror Image, Slow Time, or Teleport, your movement speed is increased by 30% for 3 seconds.''']


class Cold_Blooded(Passive):
    """Cold Blooded"""
    level = 30
    rules = '''Enemies chilled or frozen by you take 10% more damage from all sources for the duration of the chill or Freeze.'''


class Conflagration(Passive):
    """Conflagration"""
    level = 34
    rules = '''Fire damage dealt to enemies applies a burning effect, increasing their chance to be critically hit by 6% for 3 seconds.'''


class Paralysis(Passive):
    """Paralysis"""
    level = 37
    rules = '''Lightning spells have a 15% chance to Stun all targets hit for 1.5 seconds.'''


class Galvanizing_Ward(Passive):
    """Galvanizing Ward"""
    level = 40
    rules = '''As long as you have not taken damage in the last 5 seconds you gain a protective shield that absorbs the next 60% of your Life in damage.'''


class Temporal_Flux(Passive):
    """Temporal Flux"""
    level = 45
    rules = '''Enemies that take Arcane damage are slowed by 80% for 2 seconds.'''


class Dominance(Passive):
    """Dominance"""
    level = 50
    rules = '''Killing an enemy grants a shield that absorbs 2% of your Life in damage for 3 seconds. This effect can stack up to 10 times.'''
    rules = '''Refreshing Dominance will set the shield to its maximum possible potency and each stack will increase its total duration by 0.5 seconds.'''


class Arcane_Dynamo(Passive):
    """Arcane Dynamo"""
    level = 55
    rules = '''When you cast a Signature spell, you gain a Flash of Insight. After 5 Flashes of Insight, your next non-Signature spell deals 60% additional damage.'''


class Unstable_Anomaly(Passive):
    """Unstable Anomaly"""
    level = 60
    rules = '''When you receive fatal damage, you instead gain a shield equal to 400% of your maximum Life for 5 seconds and release a shockwave that knocks enemies back and Stuns them for 3 seconds.
   This effect may occur once every 60 seconds.'''


class Unwavering_Will(Passive):
    """Unwavering Will"""
    level = 64
    rules = '''Standing still for 1.5 seconds increases the following attributes:
   Armor: 20%
   All Resistances: 20%
   Damage: 10%
   '''


class Audacity(Passive):
    """Audacity"""
    level = 66
    rules = '''You deal 30% additional damage to enemies within 15 yards.'''


class Elemental_Exposure(Passive):
    """Elemental Exposure"""
    level = 68
    rules = '''Damaging enemies with Arcane, Cold, Fire or Lightning will cause them to take 5% more damage from your attacks for 5 seconds. Each different damage type applies a stack, stacking up to 4 times.
   Elemental damage from your weapon contributes to Elemental Exposure.'''

from activeSkills import Magic_Missile,Shock_Pulse,Spectral_Blade,Electrocute

Signature_spells = [
    Magic_Missile,
    Shock_Pulse,
    Spectral_Blade,
    Electrocute
    ]

if 0:
    with open(__file__) as thisFile:
        lines = thisFile.readlines()
        for idx,line in enumerate(lines):
            line = line[:-1].strip()
            if line:
                if all([char.isdigit() for char in line]):

                    print("\nclass %s:" % lines[idx+1][:-1].strip())
                    print('\t"""%s"""' % lines[idx+1][:-1].strip())
                    print("\tlevel = %s" % line)
                else:
                    print(line)

if 0:
    with open(__file__) as thisFile:
        lines = thisFile.readlines()
        for idx,line in enumerate(lines):
            line = line[:-1]
            if line:
                if 'class' in line:
                    print('\n',line.replace(':','(Passive):'))
                else:
                    print(line)
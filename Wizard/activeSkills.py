from Meta import Style

class Spell:

    """
    Wizards still care about this, as many spells casting time is linked to the weapon speed.
    If you have a faster weapon you can cast more spells per second.
    This is really good if you rely on signature (free) spells, or have abilities that you want to trigger.

    """
    # https://us.battle.net/forums/en/d3/topic/5150757589

    def usage(self):
        return Style

class Signature_spell:
    # Signature spells are free to cast.
    cast_cost = 0

class Magic_Missile(Spell):
    """Magic Missile"""
    level = 1
    Primary = True
    Signature_spell = True
    rules = r'''
    Launch a missile of magic energy, dealing 230% weapon damage as Arcane.
    '''
    damage = 230
    type = 'Arcane'

    class runes:
        activeRune = False

        class Charged_Blast:
            """Charged Blast"""
            level = 6
            rules = '''
            Increase the damage of Magic Missile to 325% weapon damage as Arcane.
            '''

        class Glacial_Spike:
            """Glacial Spike"""
            level = 13
            rules = '''
            Cast out a shard of ice that explodes on impact, causing enemies within 4.5 yards to take 175% weapon damage as Cold and be Frozen for 1 second.
            Enemies cannot be Frozen by Glacial Spike more than once every 5 seconds.
            '''

        class Split:
            """Split"""
            level = 31
            rules = '''
            Fire 3 missiles that each deal 80% weapon damage as Arcane.
            '''
        class Seeker:
            """Seeker"""
            level = 42
            rules = '''
            Missiles track the nearest enemy. Missile damage is increased to 285% weapon damage as Arcane.
            '''
        
        class Conflagrate:
            """Conflagrate"""
            level = 52
            rules = '''
            The missile pierces through enemies and causes them to burn for 130% weapon damage as Fire over 3 seconds.
            Burn damage stacks up to 3 times and any Fire damage taken from your other spells refresh all stacks to their maximum duration.
                '''

class Ray_of_Frost(Spell):
    """Ray of Frost"""
    level = 2
    Secondary = True
    rules = r'''
    Project a beam of frozen ice that blasts enemies within 5 yards of the first enemy hit for 430% weapon damage as Cold and Slows their movement by 60% for 3 seconds.
    Ray of Frost damage is increased by 405% weapon damage every second, up to a maximum total of 1240% weapon damage as Cold.
    '''
    cost = 16 # Arcane Power
    damage = 405 # %
    type = 'Frost'

    def DPS(self):
        currMana = 109
        spellCost = 16
        shouldveLasted = 6.8125 # sec, but Mana reg = also Active
        timeTillDepleted = 8.28 # sec

        damageTick = 'based on weapon speed'



    class runes:
        activeRune = False

        class Cold_Blood:
            """Cold Blood"""
            level = 7
            rules = '''
            Cold Blood
            Reduce channeling cost to 11 Arcane Power.
                '''

        class Numb:
            """Numb"""
            level = 15
            rules = '''
        Numb
        Ray of Frost has a 10% chance to Freeze enemies for 1 second and increases the Slow amount to 80% for 3 seconds.
            '''

        class Black_Ice:
            """Black Ice"""
            level = 28
            rules = '''
        Black Ice
        Enemies killed by Ray of Frost leave behind a patch of ice that deals 1625% weapon damage as Cold to enemies moving through it over 3 seconds.
            '''

        class Sleet_Storm:
            """Sleet Storm"""
            level = 38
            rules = '''
        Sleet Storm
        Create a swirling storm around you that grows up to a 22 yard radius, dealing 300% weapon damage as Cold to all enemies caught within it.
        Ray of Frost damage is increased by 220% weapon damage every second, up to a maximum total of 740% weapon damage as Cold.
            '''

        class Snow_Blast:
            """Snow Blast"""
            level = 53
            rules = '''
        Snow Blast
        Enemies hit by Ray of Frost take 15% increased damage from Cold for 4 seconds.
        '''

class Shock_Pulse(Spell):
    """Shock Pulse"""
    level = 3
    Primary = True
    rules = r'''
    This is a Signature spell. Signature spells are free to cast.
    Release a medium range pulse of 3 unpredictable charges of electricity that deal 194% weapon damage as Lightning.
    '''
    class runes:
        activeRune = False

        class Explosive_Bolts:
            """Explosive Bolts"""
            level = 9
            rules = '''
        Explosive Bolts
        Slain enemies explode, dealing 184% weapon damage as Cold to every enemy within 10 yards.
        Shock Pulse's damage turns into Cold.
            '''

        class Fire_Bolts:
            """Fire Bolts"""
            level = 18
            rules = '''
        Fire Bolts
        Cast 3 bolts of fire that each deal 274% weapon damage as Fire.
            '''

        class Piercing_Orb:
            """Piercing Orb"""
            level = 33
            rules = '''
        Piercing Orb
        Merge the bolts in a single giant orb that oscillates forward dealing 214% weapon damage as Lightning to everything it hits.
            '''

        class Power_Affinity:
            """Power Affinity"""
            level = 47
            rules = '''
        Power Affinity
        Gain 2 Arcane Power for each enemy hit.
        Shock Pulse's damage turns into Arcane.
            '''

        class Living_Lightning:
            """Living Lightning"""
            level = 54
            rules = '''
        Living Lightning
        Conjure a being of lightning that drifts forward, electrocuting nearby enemies for 165% weapon damage as Lightning.
        '''

class Frost_Nova(Spell):
    """Frost Nova"""
    level = 4
    rules = r'''
    Defensive
    Cooldown: 11 seconds
    Blast nearby enemies with an explosion of ice and freeze them for 2 seconds.

12
Shatter
A frozen enemy that is killed has a 100% chance of releasing another Frost Nova.

18
Cold Snap
Reduce the cooldown to 7.5 seconds and increase the Freeze duration to 3 seconds.

28
Frozen Mist
Frost Nova no longer freezes enemies, but instead leaves behind a mist of frost that deals 915% weapon damage as Cold over 8 seconds.

41
Deep Freeze
Gain a 10% bonus to Critical Hit Chance for 11 seconds if Frost Nova hits 5 or more enemies.

51
Bone Chill
Enemies take 33% more damage while frozen or chilled by Frost Nova.
    '''

class Arcane_Orb(Spell):
    """Arcane Orb"""
    level = 5
    rules = r'''
    Secondary
    Cost: 30 Arcane Power
    Hurl an orb of pure energy that explodes on contact, dealing 435% weapon damage as Arcane to all enemies within 15 yards.

11
Obliteration
Increase the speed of the orb and its damage to 700% weapon damage as Arcane, but reduce the area of effect to 8 yards.

20
Arcane Orbit
Create 4 Arcane Orbs that orbit you, exploding for 265% weapon damage as Arcane when enemies get close.

32
Spark
Lob an electrified orb over enemies that zaps them for 349% weapon damage as Lightning and increases the damage of the next Lightning spell you cast by 2% for every enemy hit up to a maximum of 15.

45
Scorch
Launch a burning orb that deals 221% weapon damage as Fire. The orb leaves behind a wall of Fire that deals 734% weapon damage as Fire over 5 seconds.

55
Frozen Orb
Create an orb of frozen death that shreds an area with ice bolts, dealing 950% weapon damage as Cold.

    '''

class Diamond_Skin(Spell):
    """Diamond Skin"""
    level = 8
    rules = r'''
    Defensive
    Cooldown: 15 seconds
    Transform your skin to diamond for 3 seconds, absorbing up to 40% of your Life in damage from incoming attacks.
14
Crystal Shell
Increase the maximum amount of damage absorbed to 80% of your Life.

20
Prism
Reduce the Arcane Power cost of all skills by 9 while Diamond Skin is active.

32
Sleek Shell
Increases your movement speed by 30% while Diamond Skin is active.

44
Enduring Skin
Increase the duration of Diamond Skin to 6 seconds.

56
Diamond Shards
When Diamond Skin fades, diamond shards explode in all directions dealing 863% weapon damage as Arcane to nearby enemies.
    '''

class Wave_of_Force(Spell):
    """Wave of Force"""
    level = 9
    rules = r'''
    Force
    Cost: 25 Arcane Power
    Discharge a wave of pure energy that deals 390% weapon damage as Arcane to nearby enemies.
15
Impactful Wave
Wave of Force repels projectiles back toward their shooter, knocks back nearby enemies and Slows them by 60% for 3 seconds.

Wave of Force gains a 5 second cooldown.

22
Debilitating Force
Enemies hit deal 20% reduced damage for 4 seconds.

32
Arcane Attunement
Each enemy hit increases the damage of your next Arcane spell by 4%.

39
Static Pulse
Each enemy hit restores 1 Arcane Power.

Wave of Force's damage turns into Lightning.

49
Heat Wave
Increase the damage to 475% weapon damage as Fire.
    '''

class Spectral_Blade(Spell):
    """Spectral Blade"""
    level = 11
    rules = r'''
    Primary
    This is a Signature spell. Signature spells are free to cast.
    Summon a spectral blade that strikes all enemies up to 15 yards in front of you for 168% weapon damage as Arcane.
19
Flame Blades
Each enemy hit increases the damage of your Fire spells by 1%, up to a maximum of 30%, for 5 seconds.

24
Siphoning Blade
Gain 2 Arcane Power for each enemy hit.

35
Thrown Blade
Extend the reach of Spectral Blade to 20 yards and increase its damage to 231% weapon damage as Lightning.

51
Barrier Blades
With each cast, gain a protective shield for 3 seconds that absorbs 4% of your Life in damage.

57
Ice Blades
Chilled enemies have a 5% chance to be Frozen and Frozen enemies have a 5% increased chance to be critically hit by Spectral Blade.
    '''

class Arcane_Torrent(Spell):
    """Arcane Torrent"""
    level = 12
    rules = r'''
    Secondary
    Cost: 16 Arcane Power
    Hurl a barrage of arcane projectiles that deal 400% weapon damage as Arcane to all enemies near the impact location.
    Arcane Torrent damage is increased by 305% weapon damage every second, up to a maximum total of 1010% weapon damage as Arcane.
18
Flame Ward
You take 15% less damage from attacks while channeling. Every second you channel increases this amount by 5%, up to a maximum total of 25% damage reduction.

Arcane Torrent's damage turns into Fire.

25
Death Blossom
Unleash a torrent of power beyond your control. You no longer direct where the projectiles go, but their damage is greatly increased to 1215% weapon damage as Arcane.

Arcane Torrent damage is increased by 640% weapon damage every second, up to a maximum total of 2495% weapon damage as Arcane.

34
Arcane Mines
Lay Arcane mines that arm after 2 seconds. These mines explode when an enemy approaches, dealing 825% weapon damage as Arcane. Enemies caught in the explosion have their movement and attack speeds reduced by 60% for 3 seconds.

49
Static Discharge
Each missile explodes into 2 piercing bolts of electricity that each deal 150% weapon damage as Lightning.

57
Cascade
Enemies hit by Arcane Torrent have a 12.5% chance to fire a new missile at a nearby enemy dealing 582% weapon damage as Arcane.
    '''

class Energy_Twister(Spell):
    """Energy Twister"""
    level = 13
    rules = r'''
    Force
    Cost: 35 Arcane Power
    Unleash a twister of pure energy that deals 1525% weapon damage as Arcane over 6 seconds to everything in its path.
19
Mistral Breeze
Reduce the casting cost of Energy Twister to 25 Arcane Power.

Energy Twister's damage turns into Cold.

24
Gale Force
Enemies hit by Energy Twister take 15% increased damage from Fire for 4 seconds.

36
Raging Storm
When two Energy Twisters collide, they merge into a tornado with increased area of effect that causes 3200% weapon damage as Arcane over 6 seconds.

41
Wicked Wind
Energy Twister no longer travels but spins in place, dealing 835% weapon damage as Arcane over 6 seconds to everything caught in it.

52
Storm Chaser
Each cast of Energy Twister grants you a Lightning Charge. You can store up to 3 Lightning Charges at a time. Casting a Signature spell releases all Lightning Charges as a bolt of Lightning that deals 196% weapon damage as Lightning per Lightning Charge.

Energy Twister's damage turns into Lightning.

The following skills are Signature spells:

 Magic Missile

 Shock Pulse

 Spectral Blade

 Electrocute
    '''

class Ice_Armor(Spell):
    """Ice Armor"""
    level = 14
    rules = r'''
    Conjuration
    Cost: 25 Arcane Power
    Surround yourself in a barrier of ice that reduces damage from melee attacks by 12%. Melee attackers are either Chilled or Frozen for 3 seconds. Lasts 10 minutes.
    Only one Armor may be active at a time.
21
Chilling Aura
Lower the temperature of the air around you. Nearby enemies are chilled, slowing their movement speed by 80%.

31
Crystallize
When you are struck by a melee attack, your Armor is increased by 20% for 30 seconds. This effect stacks up to 3 times.

42
Jagged Ice
Melee attackers also take 189% weapon damage as Cold.

49
Ice Reflect
Melee attacks have a 40% chance to create a Frost Nova centered on the attacker, dealing 75% weapon damage as Cold.

53
Frozen Storm
A whirling storm of ice builds around you, dealing 80% weapon damage as Cold every second.
    '''

class Electrocute(Spell):
    """Electrocute"""
    level = 15
    rules = r'''
    Primary
    This is a Signature spell. Signature spells are free to cast.
    Lightning arcs from your fingertips, dealing 138% weapon damage as Lightning. The lightning can jump, hitting up to 2 additional enemies.
22
Chain Lightning
Increase the maximum number of enemies that can be electrocuted to 10.

29
Forked Lightning
Critical Hits release 4 charged bolts in random directions, dealing 44% weapon damage as Fire to any enemies hit.

36
Lightning Blast
Create streaks of lightning that pierce through enemies for 140% weapon damage as Lightning.

44
Surge of Power
Gain 1 Arcane Power for each enemy hit.

59
Arc Lightning
Blast a cone of lightning that deals 310% weapon damage as Lightning to all affected enemies.
    '''

class Slow_Time(Spell):
    """Slow Time"""
    level = 16
    rules = r'''
    Defensive
    Cooldown: 15 seconds
    Invoke a bubble of warped time and space at your target location up to 60 yards away for 15 seconds, reducing enemy attack speed by 20% and movement speed by 60%. This bubble also slows the speed of enemy projectiles by 90%.
23
Time Shell
Increase the potency of the movement speed reduction to 80% and reduces the cooldown to 12 seconds.

29
Exhaustion
Enemies caught by Slow Time deal 25% less damage.

39
Time Warp
Enemies caught in the bubble of warped time take 15% more damage.

47
Point of No Return
Enemies that enter or leave the Slow Time area are stunned for 5 seconds.

53
Stretch Time
Time is sped up for any allies standing in the area, increasing their attack speed by 10%.
    '''

class Storm_Armor(Spell):
    """Storm Armor"""
    level = 17
    rules = r'''
    Conjuration
    Cost: 25 Arcane Power
    Bathe yourself in electrical energy, periodically shocking a nearby enemy for 175% weapon damage as Lightning. Lasts 10 minutes.
    Only one Armor may be active at a time.
23
Reactive Armor
Ranged and melee attackers are shocked for 189% weapon damage as Lightning.

33
Power of the Storm
Reduce the Arcane Power cost of all skills by 3 while Storm Armor is active.

37
Thunder Storm
Increase the damage of the shock to 315% weapon damage as Lightning.

43
Scramble
Increase your movement speed by 25% for 3 seconds when you are hit by melee or ranged attacks.

58
Shocking Aspect
Critical Hits have a chance to electrocute a nearby enemy for 425% weapon damage as Lightning.
    '''

class Explosive_Blast(Spell):
    """Explosive Blast"""
    level = 19
    rules = r'''
    Mastery
    Cost: 20 Arcane Power
    Cooldown: 6 seconds
    Gather an infusion of energy around you that explodes after 1.5 seconds for 945% weapon damage as Arcane to all enemies within 12 yards.
24
Unleashed
Increases the damage of Explosive Blast to 1485%.

29
Flash
Reduce the cooldown of Explosive Blast to 3 seconds.

Explosive Blast's damage turns into Lightning.

39
Short Fuse
Immediately release the energy of Explosive Blast for 909% weapon damage as Fire.

50
Obliterate
Release an enormous Explosive Blast that deals 990% weapon damage as Cold to all enemies within 18 yards.

56
Chain Reaction
Instead of a single explosion, release a chain of 3 consecutive explosions, each dealing 520% weapon damage as Fire.
    '''

class Magic_Weapon(Spell):
    """Magic Weapon"""
    level = 20
    rules = r'''
    Conjuration
    Cost: 25 Arcane Power
    Imbue your weapon with magical energy, granting it 10% increased damage. Lasts 10 minutes.
    Requires Weapon
27
Electrify
Attacks have a chance to cause lightning to arc to 3 nearby enemies, dealing 61% weapon damage as Lightning.

35
Force Weapon
Increase the damage bonus of Magic Weapon to 20% damage.

38
Conduit
Enemies hit by your attacks restore up to 3 Arcane Power.

46
Ignite
Attacks have a chance to burn enemies, dealing 300% weapon damage as Fire over 3 seconds.

55
Deflection
When you perform an attack, gain a protective shield for 3 seconds that absorbs 4% of your Life in damage.
    '''

class Hydra(Spell):
    """Hydra"""
    level = 21
    rules = r'''
    Force
    Cost: 15 Arcane Power
    Summon a multi-headed Hydra for 15 seconds that attacks enemies with bolts of fire dealing 165% weapon damage as Fire.
    Only one Hydra may be active at a time.
26
Arcane Hydra
Summon an Arcane Hydra that spits Arcane Orbs that explode on impact, dealing 205% weapon damage as Arcane to enemies near the explosion.

33
Lightning Hydra
Summon a Lightning Hydra that electrocutes enemies for 255% weapon damage as Lightning.

38
Blazing Hydra
Summon a Blazing Hydra that spits bolts of Fire that burn enemies near the point of impact, dealing 155% weapon damage as Fire over 3 seconds. Burn damage can stack multiple times on the same enemy.

46
Frost Hydra
Summon a Frost Hydra that breathes a short range cone of frost, causing 255% weapon damage as Cold to all enemies in the cone.

56
Mammoth Hydra
Summon a Mammoth Hydra that breathes a river of flame at nearby enemies, dealing 330% weapon damage per second as Fire to enemies caught on the burning ground.
    '''

class Disintegrate(Spell):
    """Disintegrate"""
    level = 21
    rules = r'''
    Secondary
    Cost: 18 Arcane Power
    Channel a beam of pure energy, dealing 390% weapon damage as Arcane.
    Disintegrate damage is increased by 250% weapon damage every second, up to a maximum total of 890% weapon damage as Arcane.
26
Convergence
Increase the width of the beam allowing it to hit more enemies.

Disintegrate's damage turns into Fire.

30
Volatility
Enemies killed by the beam have a 35% chance to explode causing 750% weapon damage as Arcane to all enemies within 8 yards.

39
Entropy
The beam fractures into a short-ranged cone that deals 435% weapon damage as Arcane.

Disintegrate damage is increased by 340% weapon damage every second, up to a maximum total of 1115% weapon damage as Arcane.

48
Chaos Nexus
While channeling the beam you become charged with energy and discharge at nearby enemies dealing 115% weapon damage as Arcane.

59
Intensify
Enemies hit by Disintegrate take 15% increased damage from Arcane for 4 seconds.
    '''

class Familiar(Spell):
    """Familiar"""
    level = 22
    rules = r'''
    Conjuration
    Cost: 20 Arcane Power
    Summon a Familiar that attacks your enemies for 240% weapon damage as Arcane. This companion cannot be targeted or damaged by enemies. Lasts 10 minutes.
30
Sparkflint
Summon a fiery Familiar that grants you 10% increased damage.

40
Icicle
The Familiar's projectiles have a 35% chance to Freeze the enemy for 1 second.

44
Ancient Guardian
Summon a protective Familiar. When you are below 50% Life the Familiar will absorb damage from 1 attack every 6 seconds.

50
Arcanot
While the Familiar is active, you regenerate 4.5 Arcane Power every second.

57
Cannoneer
The Familiar's projectiles explode on impact, dealing 240% weapon damage as Arcane to all enemies within 6 yards.
    '''

class Teleport(Spell):
    """Teleport"""
    level = 22
    rules = r'''
    Defensive
    Cooldown: 11 seconds
    Teleport through the ether to the selected location up to 50 yards away.
26
Safe Passage
For 5 seconds after you Teleport, you will take 25% less damage.

31
Wormhole
After casting Teleport, you have 3 seconds to Teleport 1 additional time.

37
Reversal
Casting Teleport again within 5 seconds will instantly return you to your original location and set the remaining cooldown to 1 second.

43
Fracture
Summon 2 decoys for 6 seconds after teleporting.

59
Calamity
Cast a short range Wave of Force upon arrival, dealing 175% weapon damage as Arcane to all nearby enemies and stunning them for 1 second.
    '''

class Mirror_Image(Spell):
    """Mirror Image"""
    level = 25
    rules = r'''
    Mastery
    Cooldown: 15 seconds
    Summon 2 illusionary duplicates of yourself that taunt nearby enemies for 1 second, last for 7 seconds and have 50% of your Life.
    Spells cast by your Mirror Images will deal 10% of the damage of your own spells.
31
Hard Light
Increase the Life of your Mirror Images to 200% of your own.

37
Duplicates
Summon 4 Mirror Images that taunt nearby enemies for 1 second and each have 50% of your Life.

45
Mocking Demise
When a Mirror Image is destroyed, it explodes, dealing 309% weapon damage as Arcane with a 50% chance to Stun for 2 seconds.

51
Extension of Will
Increase the duration of your Mirror Images to 10 seconds and their Life to 100% of your Life.

58
Mirror Mimics
Spells cast by your Mirror Images will deal 20% of the damage of your own spells.
    '''

class Meteor(Spell):
    """Meteor"""
    level = 25
    rules = r'''
    Force
    Cost: 40 Arcane Power
    Summon an immense Meteor that plummets from the sky, crashing into enemies for 740% weapon damage as Fire. The ground it hits is scorched with molten fire that deals 235% weapon damage as Fire over 3 seconds.
29
Thunder Crash
Removes the delay before Meteor comes crashing down.

Meteor's damage turns into Lightning.

34
Star Pact
Expend all remaining Arcane Power. Each point of extra Arcane Power spent increases the impact damage of Meteor by 20% weapon damage as Arcane.

43
Comet
Summon a Comet that deals 740% weapon damage as Cold and freezes chilled enemies for 1 second upon impact.

The impact site is covered in an icy mist that deals 235% weapon damage as Cold over 3 seconds.

48
Meteor Shower
Unleash a volley of 7 small Meteors that each strike for 277% weapon damage as Fire.

58
Molten Impact
Greatly increases the size and increases the damage of the Meteor impact to 1648% weapon damage as Fire and the molten fire to 625% weapon damage as Fire over 3 seconds.

Adds a 15 second cooldown.
    '''

class Blizzard(Spell):
    """Blizzard"""
    level = 27
    rules = r'''
    Force
    Cost: 40 Arcane Power
    Call down shards of ice that deal 1075% weapon damage as Cold over 6 seconds to enemies in a 12 yard radius. Multiple casts in the same area from the same caster do not stack.
35
Lightning Storm
Enemies affected by Blizzard take 15% increased damage from Lightning.

42
Frozen Solid
Enemies caught in the Blizzard have a 100% chance to be Frozen for 2.5 seconds.

47
Snowbound
Reduce the casting cost of Blizzard to 10 Arcane Power.

54
Apocalypse
Increase the area of effect of Blizzard to a 30 yard radius.

Blizzard's damage turns into Fire.

60
Unrelenting Storm
Increase the duration and damage of Blizzard to deal 1810% weapon damage as Cold over 8 seconds.
    '''

class Energy_Armor(Spell):
    """Energy Armor"""
    level = 28
    rules = r'''
    Conjuration
    Cost: 25 Arcane Power
    Focus your energies, increasing your Armor by 35% but decreasing your maximum Arcane Power by 20. Lasts 10 minutes.
    Only one Armor may be active at a time.
32
Absorption
You have a chance to gain 4 Arcane Power when you are hit by a ranged or melee attack.

41
Pinpoint Barrier
Energy Armor also increases your Critical Hit Chance by 5%.

48
Energy Tap
Rather than decreasing your maximum Arcane Power, Energy Armor increases it by 20.

54
Force Armor
Incoming attacks that would deal more than 35% of your maximum Life are reduced to deal 35% of your maximum Life instead.

The amount absorbed cannot exceed 100% of your maximum Life.

60
Prismatic Armor
Energy Armor also increases your resistance to all damage types 25%.
    '''

class Archon(Spell):
    """Archon"""
    level = 30
    rules = r'''
    Mastery
    Cooldown: 120 seconds
    Transform into a being of pure arcane energy for 20 seconds. While in Archon form, your normal abilities are replaced by powerful Archon abilities, your damage is increased by 30%, and your Armor and resistances are increased by 150%.
    Each enemy killed while in Archon form increases your damage by 6% for the remaining duration of Archon.
36
Combustion
An explosion erupts around you when you transform, dealing 3680% weapon damage as Fire to all enemies within 15 yards.

Archon abilities deal Fire damage instead of Arcane.

40
Teleport
Archon form can cast Teleport with a 2 second cooldown.

46
Pure Power
Decrease the cooldown of Archon to 100 seconds.

Archon abilities deal Lightning damage instead of Arcane.

52
Slow Time
Archon form can cast a Slow Time that follows you and your Arcane Blast and Arcane Strike abilities Freeze enemies for 1 second.

Archon abilities deal Cold damage instead of Arcane.

60
Improved Archon
Increase the damage of all Archon abilities by 50%.
    '''

class Black_Hole(Spell):
    """Black Hole"""
    level = 61
    rules = r'''
    Mastery
    Cost: 20 Arcane Power
    Cooldown: 12 seconds
    Conjure a Black Hole at the target location that draws enemies to it and deals 700% weapon damage as Arcane over 2 seconds to all enemies within 15 yards.
62
Supermassive
Increases the Black Hole radius to 20 yards and damage to 1290% weapon damage as Lightning over 2 seconds.

63
Absolute Zero
Each enemy hit increases the damage of your Cold spells by 3% for 10 seconds.

Black Hole's damage turns into Cold.

65
Event Horizon
The Black Hole also absorbs enemy projectiles and objects from Elite monster affixes within 15 yards.

67
Blazar
Conjure a Black Hole at the target location that draws enemies to it and deals 700% weapon damage as Fire over 2 seconds to all enemies within 15 yards.

After the Black Hole disappears, an explosion occurs that deals 725% weapon damage as Fire to enemies within 15 yards.

69
Spellsteal
Enemies hit by Black Hole deal 10% reduced damage for 5 seconds. Each enemy hit by Black Hole grants you 3% increased damage for 5 seconds.
    '''




if 0:
    with open(__file__) as thisFile:
        lines = thisFile.readlines()
        for idx,line in enumerate(lines):
            line = line[:-1]
            if line:
                if 'class' in line:
                    print(line.replace(':','(Skill):'))
                else:
                    print(line)

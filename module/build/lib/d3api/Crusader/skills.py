import sys
sys.path.append("..\..")
from d3api.datatypes import Skill as _skill


class Punish(_skill):
    """ Punish """
    category = "active"
    description = """Generate: 5 Wrath per attack

Strike your enemy for 335% weapon damage and gain Hardened Senses, increasing your Block Chance by 15% for 5 seconds.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/punish'


"""
	 Roar
		 When you block with Hardened Senses active, you explode with fury dealing 75% weapon damage as Fire to enemies within 15 yards.

	 Celerity
		 When you block with Hardened Senses active, you gain 15% increased Attack Speed for 3 seconds.

	 Rebirth
		 When you block with Hardened Senses active, you gain 12,874 increased Life regeneration for 2 seconds.

	 Retaliate
		 When you block with Hardened Senses active, you deal 140% weapon damage as Holy to the attacker.

	 Fury
		 When you block with Hardened Senses active, you gain 15% increased Critical Hit Chance for your next attack.

"""


class Shield_Bash(_skill):
    """ Shield Bash """
    category = "active"
    description = """Cost: 30 Wrath

Charge at your enemy, bashing him and all nearby foes. Deals 700% weapon damage plus 300% of your shield Block Chance as Holy damage.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/shield-bash'


"""
	 Shattered Shield
		 The shield shatters into other smaller fragments, hitting more enemies for 740% weapon damage plus 335% of your shield Block Chance as damage.

	 One on One
		 The targeted monster is stunned for 1.5 seconds. All other monsters hit are knocked back.

	 Shield Cross
		 Additional shields erupt from you in a cross formation. Enemies hit by any of the additional shields take 155% weapon damage plus 100% of your shield Block Chance as damage.

	 Crumble
		 Increases the weapon damage of Shield bash to 875%.

	 Pound
		 Shield Bash will now deal 1320% weapon damage plus 500% shield Block Chance as damage. The range is reduced to 8 yards.

"""


class Slash(_skill):
    """ Slash """
    category = "active"
    description = """Generate: 5 Wrath per attack

Ignite the air in front of you, dealing 230% weapon damage as Fire."""
    url = r'https://us.diablo3.com//en/class/crusader/active/slash'


"""
	 Electrify
		 The slash becomes pure lightning and has a 25% chance to stun enemies for 2 seconds.

	 Carve
		 Carve a larger area in front of you, increasing the number of enemies hit.

	 Crush
		 Slash gains 20% increased Critical Hit Chance.

	 Zeal
		 Gain 1% increased Attack Speed for every enemy hit for 3 seconds. This effect stacks up to 10 times.

	 Guard
		 Gain 5% increased armor for each enemy hit. This effect stacks up to 5 times.

"""


class Shield_Glare(_skill):
    """ Shield Glare """
    category = "active"
    description = """Cooldown: 12 seconds

Light erupts from your shield, Blinding all enemies up to 30 yards in front of you for 4 seconds.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/shield-glare'


"""
	 Divine Verdict
		 Blinded enemies take 20% more damage for 4 seconds.

	 Uncertainty
		 Enemies caught in the glare have a 50% chance to be charmed and fight for you for 8 seconds.

	 Zealous Glare
		 Gain 9 Wrath for each enemy Blinded.

	 Emblazoned Shield
		 Enemies with health lower than 25% have a 50% chance to explode when Blinded, dealing 60% weapon damage to enemies within 8 yards.

	 Subdue
		 Enemies hit by the glare are Slowed by 80% for 6 seconds.

"""


class Sweep_Attack(_skill):
    """ Sweep Attack """
    category = "active"
    description = """Cost: 20 Wrath

Sweep a mystical flail through enemies up to 18 yards before you, dealing 480% weapon damage.

Requires Weapon"""
    url = r'https://us.diablo3.com//en/class/crusader/active/sweep-attack'


"""
	 Blazing Sweep
		 Enemies hit by the attack will catch on fire for 120% weapon damage over 2 seconds.

	 Trip Attack
		 Enemies hit by the sweep attack have a 50% chance to be tripped and Stunned for 2 seconds.

	 Holy Shock
		 Heal for 5364 Life for each enemy hit.

	 Gathering Sweep
		 Enemies caught in the sweep are pulled toward you.

Sweep Attack's damage turns into Holy.

	 Inspiring Sweep
		 Sweep Attack increases your Armor by 20% for 3 seconds.

"""


class Iron_Skin(_skill):
    """ Iron Skin """
    category = "active"
    description = """Cooldown: 30 seconds

Your skin turns to iron, absorbing 50% of all incoming damage for 4 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/iron-skin'


"""
	 Reflective Skin
		 While active, your Thorns is increased by 300%.

	 Steel Skin
		 Increase the duration to 7 seconds.

	 Explosive Skin
		 When Iron Skin expires the metal explodes off, dealing 1400% weapon damage to enemies within 12 yards.

	 Charged Up
		 Your metal skin is electrified, giving you a 20% chance to Stun enemies within 10 yards for 2 seconds.

	 Flash
		 If you take damage while Iron Skin is active, your movement speed is increased by 60% for 5 seconds and you can move through enemies unhindered.

"""


class Provoke(_skill):
    """ Provoke """
    category = "active"
    description = """Cooldown: 20 seconds
Generate: 30 Wrath

Taunt all nearby enemies and instantly generate an additional 5 Wrath for every enemy taunted. Taunted enemies will focus their attention on you for 4 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/provoke'


"""
	 Cleanse
		 For each enemy successfully taunted, you gain 1073 additional Life on Hit for 5 seconds.  

	 Flee Fool
		 Provoke no longer taunts, but instead causes enemies to flee in Fear for 8 seconds.

	 Too Scared to Run
		 Taunted enemies have their attack speed reduced by 50% and movement speed Slowed by 80% for 4 seconds.

	 Charged Up
		 For 4 seconds after casting Provoke, any damage you deal will also deal 50% weapon damage as Lightning.

	 Hit Me
		 Gain 50% increased Block Chance for 4 seconds after casting Provoke.

"""


class Smite(_skill):
    """ Smite """
    category = "active"
    description = """Generate: 5 Wrath per attack

Smite enemies up to 30 yards away with holy chains that deal 175% weapon damage as Holy. The chains break off and strike up to 3 additional enemies within 20 yards for 150% weapon damage as Holy."""
    url = r'https://us.diablo3.com//en/class/crusader/active/smite'


"""
	 Shatter
		 The holy chains explode dealing 60% weapon damage as Holy to enemies within 3 yards.

	 Shackle
		 Enemies hit by the chains have a 20% chance to be Immobilized in place for 1 second.

	 Surge
		 Increase the number of additional enemies hit to 5.

	 Reaping
		 Gain 6437 increased Life regeneration for 2 seconds for every enemy hit by the chains. This effect stacks up to 4 times.

	 Shared Fate
		 The chains bind those they hit, causing them to share one another's fate. Enemies who share fate will be stunned for 2 seconds if they move 15 yards away from each other.

"""


class Blessed_Hammer(_skill):
    """ Blessed Hammer """
    category = "active"
    description = """Cost: 10 Wrath

Summon a blessed hammer that spins around you, dealing 320% weapon damage as Holy to all enemies hit."""
    url = r'https://us.diablo3.com//en/class/crusader/active/blessed-hammer'


"""
	 Burning Wrath
		 The hammer is engulfed in fire and has a 25% chance to scorch the ground over which it passes. Enemies who pass through the scorched ground take 330% weapon damage as Fire per second.

	 Thunderstruck
		 The hammer is charged with lightning that occasionally arcs between you and the hammer as it spirals through the air, dealing 60% weapon damage as Lightning to enemies caught in the arcs. 

	 Limitless
		 Increase the damage of Blessed Hammer to 640% weapon damage as Holy and increase its area of effect by 20 yards.

	 Brute Force
		 The hammer Slows enemies it passes through and has a 35% chance to explode on impact, dealing 460% weapon damage as Physical and Stunning enemies within 6 yards for 1 second.

	 Dominion
		 The Hammer now orbits you as you move.

"""


class Steed_Charge(_skill):
    """ Steed Charge """
    category = "active"
    description = """Cooldown: 16 seconds

Mount a celestial war horse that allows you to ride through enemies unhindered for 2 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/steed-charge'


"""
	 Spiked Barding
		 The war horse deals 500% of your Thorns every second to enemies through which you ride.

	 Nightmare
		 The war horse is engulfed in righteous fire, scorching all who cross its path for 550% weapon damage per second as Fire.

	 Rejuvenation
		 While riding the war horse, you recover 15% of your maximum Life.

	 Endurance
		 Increase the duration to 3 seconds.

	 Draw and Quarter
		 Bind 5 monsters near you with chains and drag them as you ride, dealing 185% weapon damage as Holy every second.

"""


class Laws_of_Valor(_skill):
    """ Laws of Valor """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Empower the Law, granting you and your allies 15% increased Attack Speed for 5 seconds.

Passive: Recite the Law, granting you and your allies 8% increased Attack Speed.

Only one Law may be active at a time."""
    url = r'https://us.diablo3.com//en/class/crusader/active/laws-of-valor'


"""
	 Invincible
		 Active: Empowering the Law also increases your Life on Hit by 21,457.

	 Frozen in Terror
		 Active: Empowering the Law also grants you a 100% chance to Stun all enemies within 10 yards for 5 seconds.

	 Critical
		 Active: Empowering the Law also increases your Critical Hit Damage by 50%.

	 Unstoppable Force
		 Active: Empowering the law also reduces the Wrath cost of all _skills by 50% for 5 seconds.

	 Answered Prayer
		 Active: While the Law is empowered, each enemy killed increases the duration by 1 second, up to a maximum of 10 seconds of increased time.

"""


class Justice(_skill):
    """ Justice """
    category = "active"
    description = """Generate: 5 Wrath per attack

Hurl a hammer of justice at your enemies, dealing 245% weapon damage."""
    url = r'https://us.diablo3.com//en/class/crusader/active/justice'


"""
	 Burst
		 The hammer is charged with lightning and explodes on impact, dealing 60% weapon damage as Lightning to all enemies within 10 yards. Enemies caught in the explosion have a 20% chance to be stunned for 1 second.

	 Crack
		 When the hammer hits an enemy, there is an 100% chance it will crack into 2 smaller hammers that fly out and deal 245% weapon damage as Holy.

	 Hammer of Pursuit
		 The hammer seeks out nearby targets and deal 335% weapon damage.

	 Sword of Justice
		 Hurl a sword of justice at your enemies. When the sword hits an enemy, gain 5% increased movement speed for 3 seconds. This effect stacks up to 3 times.

	 Holy Bolt
		 Throw a bolt of holy power that heals you and your allies for 2146 - 3219 Life when it hits an enemy.

"""


class Consecration(_skill):
    """ Consecration """
    category = "active"
    description = """Cooldown: 30 seconds

Consecrate the ground 20 yards around you for 10 seconds. You and your allies heal for 32,185 Life per second while standing on the consecrated ground."""
    url = r'https://us.diablo3.com//en/class/crusader/active/consecration'


"""
	 Bathed in Light
		 Increase the radius of the consecrated ground to 24 yards and increase the amount you and your allies heal for to 48,278 Life per second.

	 Bed of Nails
		 The consecrated ground becomes covered in nails. Enemies that walk into the area take 100% of your Thorns damage every second.

	 Aegis Purgatory
		 The edge of the consecrated ground is surrounded by a sacred shield, preventing enemies from moving through it.

The duration of the consecration is reduced to 5 seconds.

	 Shattered Ground
		 Enemies standing on consecrated ground take 155% weapon damage as Fire per second.

	 Fearful
		 Enemies standing on consecrated ground have a 100% chance to be Feared for 3 seconds.

"""


class Laws_of_Justice(_skill):
    """ Laws of Justice """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Empower the Law, granting you and your allies 490 increased resistance to all elements for 5 seconds.

Passive: Recite the Law, granting you and your allies 140 increased resistance to all elements.

Only one Law may be active at a time."""
    url = r'https://us.diablo3.com//en/class/crusader/active/laws-of-justice'


"""
	 Protect the Innocent
		 Active: Empowering the Law also redirects 20% of the damage taken by your allies to you for the next 5 seconds.

	 Immovable Object
		 Active: Empowering the Law also increases Armor for you and your allies by 7000 for 5 seconds.

	 Faith's Armor
		 Active: Empowering the Law also surrounds you and your allies with shields of faith for 5 seconds. The shields absorb up to 26,821 damage.

	 Decaying Strength
		 Active: While the Law is empowered, any enemy who attacks you or your allies will have their damage reduced by 15% for 5 seconds, stacking up to a maximum of 60%.

	 Bravery
		 Active: Empowering the Law also grants immunity to control impairing effects to you and your allies for 5 seconds.

"""


class Falling_Sword(_skill):
    """ Falling Sword """
    category = "active"
    description = """Cost: 25 Wrath
Cooldown: 30 seconds

Launch yourself into the heavens and come crashing down on your enemies, dealing 1700% weapon damage to everything within 14 yards of where you land.

This ability does not start its cooldown until after its effects expire."""
    url = r'https://us.diablo3.com//en/class/crusader/active/falling-sword'


"""
	 Superheated
		 The ground you fall on becomes superheated for 6 seconds, dealing 310% weapon damage as Fire per second to all enemies who pass over it.

	 Part the Clouds
		 You build a storm of lightning as you fall which covers the area you land on for 5 seconds. Lightning strikes random enemies under the cloud, dealing 605% weapon damage as Lightning and Stunning them for 2 seconds.

	 Rise Brothers
		 You land with such force that 3 Avatars of the Order are summoned forth to fight by your side for 5 seconds. Each Avatar attacks for 280% of your weapon damage as Physical.

	 Rapid Descent
		 Reduce the cooldown by 1 second for each enemy hit by Falling Sword.  The cooldown cannot be reduced below 10 seconds.

	 Flurry
		 A flurry of swords is summoned at the impact location, dealing 230% weapon damage as Holy, hurling enemies around and incapacitating them for 5 seconds.

"""


class Blessed_Shield(_skill):
    """ Blessed Shield """
    category = "active"
    description = """Cost: 20 Wrath

Hurl your shield, dealing 430% weapon damage as Holy plus 250% of shield Block Chance as Holy damage. The shield will ricochet to 3 nearby enemies.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/blessed-shield'


"""
	 Staggering Shield
		 The shield becomes charged with lightning and has a 25% chance to Stun the first enemy hit for 2 seconds. Each enemy hit after the first has a 5% reduced chance to be Stunned.

	 Combust
		 The shield erupts in flames and has a 33% chance to explode on impact, dealing 310% weapon damage as Fire to all enemies within 10 yards.

	 Divine Aegis
		 When the shield hits an enemy, your Armor is increased by 5% and Life regeneration is increased by 5% for 4 seconds.

	 Shattering Throw
		 When the shield hits an enemy, it splits into 3 small fragments that bounce between nearby enemies, dealing 170% weapon damage as Holy to all enemies hit.

	 Piercing Shield
		 The shield no longer bounces, but pierces through all enemies with a 50% chance to knock them aside.

"""


class Condemn(_skill):
    """ Condemn """
    category = "active"
    description = """Cooldown: 15 seconds

Build up a massive explosion, unleashing it after 3 seconds, dealing 1160% weapon damage as Holy to all enemies within 15 yards."""
    url = r'https://us.diablo3.com//en/class/crusader/active/condemn'


"""
	 Vacuum
		 As the explosion charges up, it sucks in enemies. The closer it is to exploding, the more enemies it sucks in.

	 Unleashed
		 The explosion now unleashes instantly.

	 Eternal Retaliation
		 Reduce the cooldown by 1 second for each enemy hit by the explosion.

	 Shattering Explosion
		 Increase the damage radius to 20 yards.

	 Reciprocate
		 50% of all damage taken while the explosion is building is added to the damage of the explosion.

"""


class Judgment(_skill):
    """ Judgment """
    category = "active"
    description = """Cooldown: 20 seconds

Pass judgment on all enemies within 20 yards of the targeted location, Immobilizing them in place for 6 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/judgment'


"""
	 Penitence
		 For every enemy upon whom you pass judgment, you heal for 2682 Life per second for 3 seconds.

	 Mass Verdict
		 All enemies are drawn toward the center of the judged area.

	 Deliberation
		 Increase the duration of the Immobilize to 10 seconds.

	 Resolved
		 Damage dealt to judged enemies has an 8% increased chance to be a Critical Hit.

	 Debilitate
		 Enemies in the judged area deal 40% reduced damage for 6 seconds.

"""


class Laws_of_Hope(_skill):
    """ Laws of Hope """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Empower the Law, surrounding you and your allies in a shield for 5 seconds that absorbs up to 124,128 damage.

Passive: Recite the Law, healing you and your allies for 10,728 Life per second.

Only one Law may be active at a time."""
    url = r'https://us.diablo3.com//en/class/crusader/active/laws-of-hope'


"""
	 Wings of Angels
		 Active: Empowering the Law also increases movement speed for you and your allies by 50%, and allows everyone affected to run through enemies unimpeded.

	 Eternal Hope
		 Active: Empowering the Law also increases the maximum Life of you and your allies by 10%.

	 Hopeful Cry
		 Active: Empowering the Law also reduces all Physical damage taken by 25%.

	 Faith's Reward
		 Active: Empowering the Law also heals you and your allies for 1073 Life for every point of Wrath that you spend. 

	 Promise of Faith
		 Active: Empowering the Law also reduces all non-Physical damage taken by 25%.

"""


class Akarats_Champion(_skill):
    """ Akarat's Champion """
    category = "active"
    description = """Cooldown: 90 seconds
    
    Explode with the power of your order, increasing your damage by 35% and increasing your Wrath regeneration by 5 for 20 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/akarats-champion'

    """
         Fire Starter
             Dealing damage burns enemies with the power of Akarat, dealing 460% weapon damage as Fire over 3 seconds.
    
         Embodiment of Power
             Increases the bonus Wrath regeneration from Akarat's Champion to 10.
    
         Rally
             Using Akarat's Champion reduces the remaining cooldown of your other abilities by 12 seconds.
    
         Prophet
             Gain 150% additional Armor while Akarat's Champion is active.
    
    The first time you take fatal damage while Akarat's Champion is active, you will be returned to full health.
    
         Hasteful
             Gain 15% increased attack speed while Akarat's Champion is active.
    
    """


class Fist_of_the_Heavens(_skill):
    """ Fist of the Heavens """
    category = "active"
    description = """Cost: 30 Wrath

Call forth a pillar of lightning from the heavens that explodes, dealing 545% weapon damage as Lightning to any enemy within 8 yards. The explosion creates 6 piercing charged bolts that arc outward and deal 255% weapon damage as Lightning."""
    url = r'https://us.diablo3.com//en/class/crusader/active/fist-of-the-heavens'


"""
	 Divine Well
		 The holy bolts crackle with holy lightning and zap enemies within 18 yards as they travel, dealing 40% weapon damage as Holy.

	 Heaven's Tempest
		 Summon a fiery storm that covers a 8 yard radius for 5 seconds, dealing 100% weapon damage as Fire every second to enemies who pass underneath it.

	 Fissure
		 Creates a fissure of lightning energy that deals 410% weapon damage as Lightning over 5 seconds to nearby enemies. If there is another fissure nearby, lightning will arc between them dealing an additional 135% weapon damage as Lightning with each arc.

	 Reverberation
		 The bolt detonates with a shockwave on impact, causing all enemies hit to be knocked away from the blast and Slowed by 80% for 4 seconds.

	 Retribution
		 Hurl a fist of Holy power that pierces through your enemies, dealing 270% weapon damage as Holy, and exploding at your target, dealing 435% weapon damage as Holy to enemies within 8 yards.

The explosion creates 6 piercing charged bolts that crawl outward, dealing 185% weapon damage as Holy to enemies through whom they pass.

"""


class Phalanx(_skill):
    """ Phalanx """
    category = "active"
    description = """Cost: 30 Wrath

Summon powerful avatars who charge forward to the targeted destination. Enemies caught in the charge path take 490% weapon damage."""
    url = r'https://us.diablo3.com//en/class/crusader/active/phalanx'


"""
	 Bowmen
		 The summoned avatars no longer march forward, but will wield bows and attack enemies, dealing 185% weapon damage. These bowmen follow you as you move for 5 seconds.

The Bowmen can only be summoned once every 15 seconds.

	 Shield Charge
		 The summoned avatars charge the target and perform a shield bash, dealing an additional 180% weapon damage to enemies at that location.

	 Stampede
		 Summon warhorses that deal 490% weapon damage and have a 30% chance to Stun enemies for 2 seconds.

	 Shield Bearers
		 The avatars no longer walk forward, but stand at the summoned location, blocking all enemies from moving through.

The Avatars can only be summoned once every 15 seconds.

	 Bodyguard
		 Instead of sending the avatars out away from you, you summon 2 Avatars of the Order to protect you and fight by your side for 10 seconds. Each Avatar will attack for 560% of your weapon damage as Physical.

The Avatars can only be summoned once every 30 seconds.

"""


class Heavens_Fury(_skill):


    """ Heaven's Fury """
    category = "active"
    description = """Cooldown: 20 seconds
    
    Call down a furious ray of Holy power that deals 1710% weapon damage as Holy over 6 seconds to all enemies caught within it."""
    url = r'https://us.diablo3.com//en/class/crusader/active/heavens-fury'

    """
         Blessed Ground
             The ground touched by the ray becomes blessed, scorching it and dealing 1550% weapon damage over 5 seconds to enemies who walks through.
    
         Ascendancy
             The ray of Holy power grows to encompass 12 yards, dealing 2766% weapon damage as Holy over 6 seconds to enemies caught within it.
    
         Split Fury
             The ray splits into 3 smaller beams, each dealing 1980% weapon damage as Holy over 6 seconds.
    
         Thou Shalt Not Pass
             Ground touched by the ray pulses with power for 6 seconds, stopping enemies who try to pass over it.
    
         Fires of Heaven
             Call down a furious ray of Holy power that is focused through you in a beam across the battlefield, dealing 960% weapon damage as Holy to all enemies it hits.
    
    The cooldown is removed. Now costs 40 Wrath.
    
    """


class Bombardment(_skill):
    """ Bombardment """
    category = "active"
    description = """Cooldown: 60 seconds

Call in an assault from afar, raining 5 spheres of burning pitch and stone onto enemies around you, dealing 2850% total weapon damage to enemies within 12 yards of the impact zone."""
    url = r'https://us.diablo3.com//en/class/crusader/active/bombardment'


"""
	 Barrels of Spikes
		 In place of the burning spheres, barrels of spikes are hurled. Damage of each barrel is increased by 200% of your Thorns.

	 Annihilate
		 Each impact has a 100% Critical Hit Chance.

	 Mine Field
		 Each impact scatters 2 mines onto the battlefield that explode when enemies walk near them, dealing 160% weapon damage as Fire to all enemies within 10 yards.

	 Impactful Bombardment
		 A single, much larger ball of explosive pitch is hurled at the targeted location dealing 3320% weapon damage to all enemies within 18 yards.

	 Targeted
		 Instead of randomly finding targets nearby, the bombardment will continue to fall on your initial target.

"""

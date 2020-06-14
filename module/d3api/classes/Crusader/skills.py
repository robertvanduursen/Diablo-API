""" crusader active skills """

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datatypes import Active
from datatypes import Rune


class Roar(Rune):
    """ Roar """
    description = """When you block with Hardened Senses active, you explode with fury dealing 75% weapon damage as Fire to enemies within 15 yards."""


class Celerity(Rune):
    """ Celerity """
    description = """When you block with Hardened Senses active, you gain 15% increased Attack Speed for 3 seconds."""


class Rebirth(Rune):
    """ Rebirth """
    description = """When you block with Hardened Senses active, you gain 12,874 increased Life regeneration for 2 seconds."""


class Retaliate(Rune):
    """ Retaliate """
    description = """When you block with Hardened Senses active, you deal 140% weapon damage as Holy to the attacker."""


class Fury(Rune):
    """ Fury """
    description = """When you block with Hardened Senses active, you gain 15% increased Critical Hit Chance for your next attack."""


class Punish(Active):
    """ Punish """
    category = "active"
    description = """Generate: 5 Wrath per attack

Strike your enemy for 335% weapon damage and gain Hardened Senses, increasing your Block Chance by 15% for 5 seconds.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/punish'
    runes = [Roar, Celerity, Rebirth, Retaliate, Fury]


class Shattered_Shield(Rune):
    """ Shattered Shield """
    description = """The shield shatters into other smaller fragments, hitting more enemies for 740% weapon damage plus 335% of your shield Block Chance as damage."""


class One_on_One(Rune):
    """ One on One """
    description = """The targeted monster is stunned for 1.5 seconds. All other monsters hit are knocked back."""


class Shield_Cross(Rune):
    """ Shield Cross """
    description = """Additional shields erupt from you in a cross formation. Enemies hit by any of the additional shields take 155% weapon damage plus 100% of your shield Block Chance as damage."""


class Crumble(Rune):
    """ Crumble """
    description = """Increases the weapon damage of Shield bash to 875%."""


class Pound(Rune):
    """ Pound """
    description = """Shield Bash will now deal 1320% weapon damage plus 500% shield Block Chance as damage. The range is reduced to 8 yards."""


class Shield_Bash(Active):
    """ Shield Bash """
    category = "active"
    description = """Cost: 30 Wrath

Charge at your enemy, bashing him and all nearby foes. Deals 700% weapon damage plus 300% of your shield Block Chance as Holy damage.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/shield-bash'
    runes = [Shattered_Shield, One_on_One, Shield_Cross, Crumble, Pound]


class Electrify(Rune):
    """ Electrify """
    description = """The slash becomes pure lightning and has a 25% chance to stun enemies for 2 seconds."""


class Carve(Rune):
    """ Carve """
    description = """Carve a larger area in front of you, increasing the number of enemies hit."""


class Crush(Rune):
    """ Crush """
    description = """Slash gains 20% increased Critical Hit Chance."""


class Zeal(Rune):
    """ Zeal """
    description = """Gain 1% increased Attack Speed for every enemy hit for 3 seconds. This effect stacks up to 10 times."""


class Guard(Rune):
    """ Guard """
    description = """Gain 5% increased armor for each enemy hit. This effect stacks up to 5 times."""


class Slash(Active):
    """ Slash """
    category = "active"
    description = """Generate: 5 Wrath per attack

Ignite the air in front of you, dealing 230% weapon damage as Fire."""
    url = r'https://us.diablo3.com//en/class/crusader/active/slash'
    runes = [Electrify, Carve, Crush, Zeal, Guard]


class Divine_Verdict(Rune):
    """ Divine Verdict """
    description = """Blinded enemies take 20% more damage for 4 seconds."""


class Uncertainty(Rune):
    """ Uncertainty """
    description = """Enemies caught in the glare have a 50% chance to be charmed and fight for you for 8 seconds."""


class Zealous_Glare(Rune):
    """ Zealous Glare """
    description = """Gain 9 Wrath for each enemy Blinded."""


class Emblazoned_Shield(Rune):
    """ Emblazoned Shield """
    description = """Enemies with health lower than 25% have a 50% chance to explode when Blinded, dealing 60% weapon damage to enemies within 8 yards."""


class Subdue(Rune):
    """ Subdue """
    description = """Enemies hit by the glare are Slowed by 80% for 6 seconds."""


class Shield_Glare(Active):
    """ Shield Glare """
    category = "active"
    description = """Cooldown: 12 seconds

Light erupts from your shield, Blinding all enemies up to 30 yards in front of you for 4 seconds.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/shield-glare'
    runes = [Divine_Verdict, Uncertainty, Zealous_Glare, Emblazoned_Shield, Subdue]


class Blazing_Sweep(Rune):
    """ Blazing Sweep """
    description = """Enemies hit by the attack will catch on fire for 120% weapon damage over 2 seconds."""


class Trip_Attack(Rune):
    """ Trip Attack """
    description = """Enemies hit by the sweep attack have a 50% chance to be tripped and Stunned for 2 seconds."""


class Holy_Shock(Rune):
    """ Holy Shock """
    description = """Heal for 5364 Life for each enemy hit."""


class Gathering_Sweep(Rune):
    """ Gathering Sweep """
    description = """Enemies caught in the sweep are pulled toward you.

Sweep Attack's damage turns into Holy."""


class Inspiring_Sweep(Rune):
    """ Inspiring Sweep """
    description = """Sweep Attack increases your Armor by 20% for 3 seconds."""


class Sweep_Attack(Active):
    """ Sweep Attack """
    category = "active"
    description = """Cost: 20 Wrath

Sweep a mystical flail through enemies up to 18 yards before you, dealing 480% weapon damage.

Requires Weapon"""
    url = r'https://us.diablo3.com//en/class/crusader/active/sweep-attack'
    runes = [Blazing_Sweep, Trip_Attack, Holy_Shock, Gathering_Sweep, Inspiring_Sweep]


class Reflective_Skin(Rune):
    """ Reflective Skin """
    description = """While active, your Thorns is increased by 300%."""


class Steel_Skin(Rune):
    """ Steel Skin """
    description = """Increase the duration to 7 seconds."""


class Explosive_Skin(Rune):
    """ Explosive Skin """
    description = """When Iron Skin expires the metal explodes off, dealing 1400% weapon damage to enemies within 12 yards."""


class Charged_Up(Rune):
    """ Charged Up """
    description = """Your metal skin is electrified, giving you a 20% chance to Stun enemies within 10 yards for 2 seconds."""


class Flash(Rune):
    """ Flash """
    description = """If you take damage while Iron Skin is active, your movement speed is increased by 60% for 5 seconds and you can move through enemies unhindered."""


class Iron_Skin(Active):
    """ Iron Skin """
    category = "active"
    description = """Cooldown: 30 seconds

Your skin turns to iron, absorbing 50% of all incoming damage for 4 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/iron-skin'
    runes = [Reflective_Skin, Steel_Skin, Explosive_Skin, Charged_Up, Flash]


class Cleanse(Rune):
    """ Cleanse """
    description = """For each enemy successfully taunted, you gain 1073 additional Life on Hit for 5 seconds.  """


class Flee_Fool(Rune):
    """ Flee Fool """
    description = """Provoke no longer taunts, but instead causes enemies to flee in Fear for 8 seconds."""


class Too_Scared_to_Run(Rune):
    """ Too Scared to Run """
    description = """Taunted enemies have their attack speed reduced by 50% and movement speed Slowed by 80% for 4 seconds."""


class Charged_Up(Rune):
    """ Charged Up """
    description = """For 4 seconds after casting Provoke, any damage you deal will also deal 50% weapon damage as Lightning."""


class Hit_Me(Rune):
    """ Hit Me """
    description = """Gain 50% increased Block Chance for 4 seconds after casting Provoke."""


class Provoke(Active):
    """ Provoke """
    category = "active"
    description = """Cooldown: 20 seconds
Generate: 30 Wrath

Taunt all nearby enemies and instantly generate an additional 5 Wrath for every enemy taunted. Taunted enemies will focus their attention on you for 4 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/provoke'
    runes = [Cleanse, Flee_Fool, Too_Scared_to_Run, Charged_Up, Hit_Me]


class Shatter(Rune):
    """ Shatter """
    description = """The holy chains explode dealing 60% weapon damage as Holy to enemies within 3 yards."""


class Shackle(Rune):
    """ Shackle """
    description = """Enemies hit by the chains have a 20% chance to be Immobilized in place for 1 second."""


class Surge(Rune):
    """ Surge """
    description = """Increase the number of additional enemies hit to 5."""


class Reaping(Rune):
    """ Reaping """
    description = """Gain 6437 increased Life regeneration for 2 seconds for every enemy hit by the chains. This effect stacks up to 4 times."""


class Shared_Fate(Rune):
    """ Shared Fate """
    description = """The chains bind those they hit, causing them to share one another's fate. Enemies who share fate will be stunned for 2 seconds if they move 15 yards away from each other."""


class Smite(Active):
    """ Smite """
    category = "active"
    description = """Generate: 5 Wrath per attack

Smite enemies up to 30 yards away with holy chains that deal 175% weapon damage as Holy. The chains break off and strike up to 3 additional enemies within 20 yards for 150% weapon damage as Holy."""
    url = r'https://us.diablo3.com//en/class/crusader/active/smite'
    runes = [Shatter, Shackle, Surge, Reaping, Shared_Fate]


class Burning_Wrath(Rune):
    """ Burning Wrath """
    description = """The hammer is engulfed in fire and has a 25% chance to scorch the ground over which it passes. Enemies who pass through the scorched ground take 330% weapon damage as Fire per second."""


class Thunderstruck(Rune):
    """ Thunderstruck """
    description = """The hammer is charged with lightning that occasionally arcs between you and the hammer as it spirals through the air, dealing 60% weapon damage as Lightning to enemies caught in the arcs. """


class Limitless(Rune):
    """ Limitless """
    description = """Increase the damage of Blessed Hammer to 640% weapon damage as Holy and increase its area of effect by 20 yards."""


class Brute_Force(Rune):
    """ Brute Force """
    description = """The hammer Slows enemies it passes through and has a 35% chance to explode on impact, dealing 460% weapon damage as Physical and Stunning enemies within 6 yards for 1 second."""


class Dominion(Rune):
    """ Dominion """
    description = """The Hammer now orbits you as you move."""


class Blessed_Hammer(Active):
    """ Blessed Hammer """
    category = "active"
    description = """Cost: 10 Wrath

Summon a blessed hammer that spins around you, dealing 320% weapon damage as Holy to all enemies hit."""
    url = r'https://us.diablo3.com//en/class/crusader/active/blessed-hammer'
    runes = [Burning_Wrath, Thunderstruck, Limitless, Brute_Force, Dominion]


class Spiked_Barding(Rune):
    """ Spiked Barding """
    description = """The war horse deals 500% of your Thorns every second to enemies through which you ride."""


class Nightmare(Rune):
    """ Nightmare """
    description = """The war horse is engulfed in righteous fire, scorching all who cross its path for 550% weapon damage per second as Fire."""


class Rejuvenation(Rune):
    """ Rejuvenation """
    description = """While riding the war horse, you recover 15% of your maximum Life."""


class Endurance(Rune):
    """ Endurance """
    description = """Increase the duration to 3 seconds."""


class Draw_and_Quarter(Rune):
    """ Draw and Quarter """
    description = """Bind 5 monsters near you with chains and drag them as you ride, dealing 185% weapon damage as Holy every second."""


class Steed_Charge(Active):
    """ Steed Charge """
    category = "active"
    description = """Cooldown: 16 seconds

Mount a celestial war horse that allows you to ride through enemies unhindered for 2 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/steed-charge'
    runes = [Spiked_Barding, Nightmare, Rejuvenation, Endurance, Draw_and_Quarter]


class Invincible(Rune):
    """ Invincible """
    description = """Active: Empowering the Law also increases your Life on Hit by 21,457."""


class Frozen_in_Terror(Rune):
    """ Frozen in Terror """
    description = """Active: Empowering the Law also grants you a 100% chance to Stun all enemies within 10 yards for 5 seconds."""


class Critical(Rune):
    """ Critical """
    description = """Active: Empowering the Law also increases your Critical Hit Damage by 50%."""


class Unstoppable_Force(Rune):
    """ Unstoppable Force """
    description = """Active: Empowering the law also reduces the Wrath cost of all skills by 50% for 5 seconds."""


class Answered_Prayer(Rune):
    """ Answered Prayer """
    description = """Active: While the Law is empowered, each enemy killed increases the duration by 1 second, up to a maximum of 10 seconds of increased time."""


class Laws_of_Valor(Active):
    """ Laws of Valor """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Empower the Law, granting you and your allies 15% increased Attack Speed for 5 seconds.

Passive: Recite the Law, granting you and your allies 8% increased Attack Speed.

Only one Law may be active at a time."""
    url = r'https://us.diablo3.com//en/class/crusader/active/laws-of-valor'
    runes = [Invincible, Frozen_in_Terror, Critical, Unstoppable_Force, Answered_Prayer]


class Burst(Rune):
    """ Burst """
    description = """The hammer is charged with lightning and explodes on impact, dealing 60% weapon damage as Lightning to all enemies within 10 yards. Enemies caught in the explosion have a 20% chance to be stunned for 1 second."""


class Crack(Rune):
    """ Crack """
    description = """When the hammer hits an enemy, there is an 100% chance it will crack into 2 smaller hammers that fly out and deal 245% weapon damage as Holy."""


class Hammer_of_Pursuit(Rune):
    """ Hammer of Pursuit """
    description = """The hammer seeks out nearby targets and deal 335% weapon damage."""


class Sword_of_Justice(Rune):
    """ Sword of Justice """
    description = """Hurl a sword of justice at your enemies. When the sword hits an enemy, gain 5% increased movement speed for 3 seconds. This effect stacks up to 3 times."""


class Holy_Bolt(Rune):
    """ Holy Bolt """
    description = """Throw a bolt of holy power that heals you and your allies for 2146 - 3219 Life when it hits an enemy."""


class Justice(Active):
    """ Justice """
    category = "active"
    description = """Generate: 5 Wrath per attack

Hurl a hammer of justice at your enemies, dealing 245% weapon damage."""
    url = r'https://us.diablo3.com//en/class/crusader/active/justice'
    runes = [Burst, Crack, Hammer_of_Pursuit, Sword_of_Justice, Holy_Bolt]


class Bathed_in_Light(Rune):
    """ Bathed in Light """
    description = """Increase the radius of the consecrated ground to 24 yards and increase the amount you and your allies heal for to 48,278 Life per second."""


class Bed_of_Nails(Rune):
    """ Bed of Nails """
    description = """The consecrated ground becomes covered in nails. Enemies that walk into the area take 100% of your Thorns damage every second."""


class Aegis_Purgatory(Rune):
    """ Aegis Purgatory """
    description = """The edge of the consecrated ground is surrounded by a sacred shield, preventing enemies from moving through it.

The duration of the consecration is reduced to 5 seconds."""


class Shattered_Ground(Rune):
    """ Shattered Ground """
    description = """Enemies standing on consecrated ground take 155% weapon damage as Fire per second."""


class Fearful(Rune):
    """ Fearful """
    description = """Enemies standing on consecrated ground have a 100% chance to be Feared for 3 seconds."""


class Consecration(Active):
    """ Consecration """
    category = "active"
    description = """Cooldown: 30 seconds

Consecrate the ground 20 yards around you for 10 seconds. You and your allies heal for 32,185 Life per second while standing on the consecrated ground."""
    url = r'https://us.diablo3.com//en/class/crusader/active/consecration'
    runes = [Bathed_in_Light, Bed_of_Nails, Aegis_Purgatory, Shattered_Ground, Fearful]


class Protect_the_Innocent(Rune):
    """ Protect the Innocent """
    description = """Active: Empowering the Law also redirects 20% of the damage taken by your allies to you for the next 5 seconds."""


class Immovable_Object(Rune):
    """ Immovable Object """
    description = """Active: Empowering the Law also increases Armor for you and your allies by 7000 for 5 seconds."""


class Faiths_Armor(Rune):
    """ Faith's Armor """
    description = """Active: Empowering the Law also surrounds you and your allies with shields of faith for 5 seconds. The shields absorb up to 26,821 damage."""


class Decaying_Strength(Rune):
    """ Decaying Strength """
    description = """Active: While the Law is empowered, any enemy who attacks you or your allies will have their damage reduced by 15% for 5 seconds, stacking up to a maximum of 60%."""


class Bravery(Rune):
    """ Bravery """
    description = """Active: Empowering the Law also grants immunity to control impairing effects to you and your allies for 5 seconds."""


class Laws_of_Justice(Active):
    """ Laws of Justice """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Empower the Law, granting you and your allies 490 increased resistance to all elements for 5 seconds.

Passive: Recite the Law, granting you and your allies 140 increased resistance to all elements.

Only one Law may be active at a time."""
    url = r'https://us.diablo3.com//en/class/crusader/active/laws-of-justice'
    runes = [Protect_the_Innocent, Immovable_Object, Faiths_Armor, Decaying_Strength, Bravery]


class Superheated(Rune):
    """ Superheated """
    description = """The ground you fall on becomes superheated for 6 seconds, dealing 310% weapon damage as Fire per second to all enemies who pass over it."""


class Part_the_Clouds(Rune):
    """ Part the Clouds """
    description = """You build a storm of lightning as you fall which covers the area you land on for 5 seconds. Lightning strikes random enemies under the cloud, dealing 605% weapon damage as Lightning and Stunning them for 2 seconds."""


class Rise_Brothers(Rune):
    """ Rise Brothers """
    description = """You land with such force that 3 Avatars of the Order are summoned forth to fight by your side for 5 seconds. Each Avatar attacks for 280% of your weapon damage as Physical."""


class Rapid_Descent(Rune):
    """ Rapid Descent """
    description = """Reduce the cooldown by 1 second for each enemy hit by Falling Sword.  The cooldown cannot be reduced below 10 seconds."""


class Flurry(Rune):
    """ Flurry """
    description = """A flurry of swords is summoned at the impact location, dealing 230% weapon damage as Holy, hurling enemies around and incapacitating them for 5 seconds."""


class Falling_Sword(Active):
    """ Falling Sword """
    category = "active"
    description = """Cost: 25 Wrath
Cooldown: 30 seconds

Launch yourself into the heavens and come crashing down on your enemies, dealing 1700% weapon damage to everything within 14 yards of where you land.

This ability does not start its cooldown until after its effects expire."""
    url = r'https://us.diablo3.com//en/class/crusader/active/falling-sword'
    runes = [Superheated, Part_the_Clouds, Rise_Brothers, Rapid_Descent, Flurry]


class Staggering_Shield(Rune):
    """ Staggering Shield """
    description = """The shield becomes charged with lightning and has a 25% chance to Stun the first enemy hit for 2 seconds. Each enemy hit after the first has a 5% reduced chance to be Stunned."""


class Combust(Rune):
    """ Combust """
    description = """The shield erupts in flames and has a 33% chance to explode on impact, dealing 310% weapon damage as Fire to all enemies within 10 yards."""


class Divine_Aegis(Rune):
    """ Divine Aegis """
    description = """When the shield hits an enemy, your Armor is increased by 5% and Life regeneration is increased by 5% for 4 seconds."""


class Shattering_Throw(Rune):
    """ Shattering Throw """
    description = """When the shield hits an enemy, it splits into 3 small fragments that bounce between nearby enemies, dealing 170% weapon damage as Holy to all enemies hit."""


class Piercing_Shield(Rune):
    """ Piercing Shield """
    description = """The shield no longer bounces, but pierces through all enemies with a 50% chance to knock them aside."""


class Blessed_Shield(Active):
    """ Blessed Shield """
    category = "active"
    description = """Cost: 20 Wrath

Hurl your shield, dealing 430% weapon damage as Holy plus 250% of shield Block Chance as Holy damage. The shield will ricochet to 3 nearby enemies.

Requires Shield"""
    url = r'https://us.diablo3.com//en/class/crusader/active/blessed-shield'
    runes = [Staggering_Shield, Combust, Divine_Aegis, Shattering_Throw, Piercing_Shield]


class Vacuum(Rune):
    """ Vacuum """
    description = """As the explosion charges up, it sucks in enemies. The closer it is to exploding, the more enemies it sucks in."""


class Unleashed(Rune):
    """ Unleashed """
    description = """The explosion now unleashes instantly."""


class Eternal_Retaliation(Rune):
    """ Eternal Retaliation """
    description = """Reduce the cooldown by 1 second for each enemy hit by the explosion."""


class Shattering_Explosion(Rune):
    """ Shattering Explosion """
    description = """Increase the damage radius to 20 yards."""


class Reciprocate(Rune):
    """ Reciprocate """
    description = """50% of all damage taken while the explosion is building is added to the damage of the explosion."""


class Condemn(Active):
    """ Condemn """
    category = "active"
    description = """Cooldown: 15 seconds

Build up a massive explosion, unleashing it after 3 seconds, dealing 1160% weapon damage as Holy to all enemies within 15 yards."""
    url = r'https://us.diablo3.com//en/class/crusader/active/condemn'
    runes = [Vacuum, Unleashed, Eternal_Retaliation, Shattering_Explosion, Reciprocate]


class Penitence(Rune):
    """ Penitence """
    description = """For every enemy upon whom you pass judgment, you heal for 2682 Life per second for 3 seconds."""


class Mass_Verdict(Rune):
    """ Mass Verdict """
    description = """All enemies are drawn toward the center of the judged area."""


class Deliberation(Rune):
    """ Deliberation """
    description = """Increase the duration of the Immobilize to 10 seconds."""


class Resolved(Rune):
    """ Resolved """
    description = """Damage dealt to judged enemies has an 8% increased chance to be a Critical Hit."""


class Debilitate(Rune):
    """ Debilitate """
    description = """Enemies in the judged area deal 40% reduced damage for 6 seconds."""


class Judgment(Active):
    """ Judgment """
    category = "active"
    description = """Cooldown: 20 seconds

Pass judgment on all enemies within 20 yards of the targeted location, Immobilizing them in place for 6 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/judgment'
    runes = [Penitence, Mass_Verdict, Deliberation, Resolved, Debilitate]


class Wings_of_Angels(Rune):
    """ Wings of Angels """
    description = """Active: Empowering the Law also increases movement speed for you and your allies by 50%, and allows everyone affected to run through enemies unimpeded."""


class Eternal_Hope(Rune):
    """ Eternal Hope """
    description = """Active: Empowering the Law also increases the maximum Life of you and your allies by 10%."""


class Hopeful_Cry(Rune):
    """ Hopeful Cry """
    description = """Active: Empowering the Law also reduces all Physical damage taken by 25%."""


class Faiths_Reward(Rune):
    """ Faith's Reward """
    description = """Active: Empowering the Law also heals you and your allies for 1073 Life for every point of Wrath that you spend. """


class Promise_of_Faith(Rune):
    """ Promise of Faith """
    description = """Active: Empowering the Law also reduces all non-Physical damage taken by 25%."""


class Laws_of_Hope(Active):
    """ Laws of Hope """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Empower the Law, surrounding you and your allies in a shield for 5 seconds that absorbs up to 124,128 damage.

Passive: Recite the Law, healing you and your allies for 10,728 Life per second.

Only one Law may be active at a time."""
    url = r'https://us.diablo3.com//en/class/crusader/active/laws-of-hope'
    runes = [Wings_of_Angels, Eternal_Hope, Hopeful_Cry, Faiths_Reward, Promise_of_Faith]


class Fire_Starter(Rune):
    """ Fire Starter """
    description = """Dealing damage burns enemies with the power of Akarat, dealing 460% weapon damage as Fire over 3 seconds."""


class Embodiment_of_Power(Rune):
    """ Embodiment of Power """
    description = """Increases the bonus Wrath regeneration from Akarat's Champion to 10."""


class Rally(Rune):
    """ Rally """
    description = """Using Akarat's Champion reduces the remaining cooldown of your other abilities by 12 seconds."""


class Prophet(Rune):
    """ Prophet """
    description = """Gain 150% additional Armor while Akarat's Champion is active.

The first time you take fatal damage while Akarat's Champion is active, you will be returned to full health."""


class Hasteful(Rune):
    """ Hasteful """
    description = """Gain 15% increased attack speed while Akarat's Champion is active."""


class Akarats_Champion(Active):
    """ Akarat's Champion """
    category = "active"
    description = """Cooldown: 90 seconds

Explode with the power of your order, increasing your damage by 35% and increasing your Wrath regeneration by 5 for 20 seconds."""
    url = r'https://us.diablo3.com//en/class/crusader/active/akarats-champion'
    runes = [Fire_Starter, Embodiment_of_Power, Rally, Prophet, Hasteful]


class Divine_Well(Rune):
    """ Divine Well """
    description = """The holy bolts crackle with holy lightning and zap enemies within 18 yards as they travel, dealing 40% weapon damage as Holy."""


class Heavens_Tempest(Rune):
    """ Heaven's Tempest """
    description = """Summon a fiery storm that covers a 8 yard radius for 5 seconds, dealing 100% weapon damage as Fire every second to enemies who pass underneath it."""


class Fissure(Rune):
    """ Fissure """
    description = """Creates a fissure of lightning energy that deals 410% weapon damage as Lightning over 5 seconds to nearby enemies. If there is another fissure nearby, lightning will arc between them dealing an additional 135% weapon damage as Lightning with each arc."""


class Reverberation(Rune):
    """ Reverberation """
    description = """The bolt detonates with a shockwave on impact, causing all enemies hit to be knocked away from the blast and Slowed by 80% for 4 seconds."""


class Retribution(Rune):
    """ Retribution """
    description = """Hurl a fist of Holy power that pierces through your enemies, dealing 270% weapon damage as Holy, and exploding at your target, dealing 435% weapon damage as Holy to enemies within 8 yards.

The explosion creates 6 piercing charged bolts that crawl outward, dealing 185% weapon damage as Holy to enemies through whom they pass."""


class Fist_of_the_Heavens(Active):
    """ Fist of the Heavens """
    category = "active"
    description = """Cost: 30 Wrath

Call forth a pillar of lightning from the heavens that explodes, dealing 545% weapon damage as Lightning to any enemy within 8 yards. The explosion creates 6 piercing charged bolts that arc outward and deal 255% weapon damage as Lightning."""
    url = r'https://us.diablo3.com//en/class/crusader/active/fist-of-the-heavens'
    runes = [Divine_Well, Heavens_Tempest, Fissure, Reverberation, Retribution]


class Bowmen(Rune):
    """ Bowmen """
    description = """The summoned avatars no longer march forward, but will wield bows and attack enemies, dealing 185% weapon damage. These bowmen follow you as you move for 5 seconds.

The Bowmen can only be summoned once every 15 seconds."""


class Shield_Charge(Rune):
    """ Shield Charge """
    description = """The summoned avatars charge the target and perform a shield bash, dealing an additional 180% weapon damage to enemies at that location."""


class Stampede(Rune):
    """ Stampede """
    description = """Summon warhorses that deal 490% weapon damage and have a 30% chance to Stun enemies for 2 seconds."""


class Shield_Bearers(Rune):
    """ Shield Bearers """
    description = """The avatars no longer walk forward, but stand at the summoned location, blocking all enemies from moving through.

The Avatars can only be summoned once every 15 seconds."""


class Bodyguard(Rune):
    """ Bodyguard """
    description = """Instead of sending the avatars out away from you, you summon 2 Avatars of the Order to protect you and fight by your side for 10 seconds. Each Avatar will attack for 560% of your weapon damage as Physical.

The Avatars can only be summoned once every 30 seconds."""


class Phalanx(Active):
    """ Phalanx """
    category = "active"
    description = """Cost: 30 Wrath

Summon powerful avatars who charge forward to the targeted destination. Enemies caught in the charge path take 490% weapon damage."""
    url = r'https://us.diablo3.com//en/class/crusader/active/phalanx'
    runes = [Bowmen, Shield_Charge, Stampede, Shield_Bearers, Bodyguard]


class Blessed_Ground(Rune):
    """ Blessed Ground """
    description = """The ground touched by the ray becomes blessed, scorching it and dealing 1550% weapon damage over 5 seconds to enemies who walks through."""


class Ascendancy(Rune):
    """ Ascendancy """
    description = """The ray of Holy power grows to encompass 12 yards, dealing 2766% weapon damage as Holy over 6 seconds to enemies caught within it."""


class Split_Fury(Rune):
    """ Split Fury """
    description = """The ray splits into 3 smaller beams, each dealing 1980% weapon damage as Holy over 6 seconds."""


class Thou_Shalt_Not_Pass(Rune):
    """ Thou Shalt Not Pass """
    description = """Ground touched by the ray pulses with power for 6 seconds, stopping enemies who try to pass over it."""


class Fires_of_Heaven(Rune):
    """ Fires of Heaven """
    description = """Call down a furious ray of Holy power that is focused through you in a beam across the battlefield, dealing 960% weapon damage as Holy to all enemies it hits.

The cooldown is removed. Now costs 40 Wrath."""


class Heavens_Fury(Active):
    """ Heaven's Fury """
    category = "active"
    description = """Cooldown: 20 seconds

Call down a furious ray of Holy power that deals 1710% weapon damage as Holy over 6 seconds to all enemies caught within it."""
    url = r'https://us.diablo3.com//en/class/crusader/active/heavens-fury'
    runes = [Blessed_Ground, Ascendancy, Split_Fury, Thou_Shalt_Not_Pass, Fires_of_Heaven]


class Barrels_of_Spikes(Rune):
    """ Barrels of Spikes """
    description = """In place of the burning spheres, barrels of spikes are hurled. Damage of each barrel is increased by 200% of your Thorns."""


class Annihilate(Rune):
    """ Annihilate """
    description = """Each impact has a 100% Critical Hit Chance."""


class Mine_Field(Rune):
    """ Mine Field """
    description = """Each impact scatters 2 mines onto the battlefield that explode when enemies walk near them, dealing 160% weapon damage as Fire to all enemies within 10 yards."""


class Impactful_Bombardment(Rune):
    """ Impactful Bombardment """
    description = """A single, much larger ball of explosive pitch is hurled at the targeted location dealing 3320% weapon damage to all enemies within 18 yards."""


class Targeted(Rune):
    """ Targeted """
    description = """Instead of randomly finding targets nearby, the bombardment will continue to fall on your initial target."""


class Bombardment(Active):
    """ Bombardment """
    category = "active"
    description = """Cooldown: 60 seconds

Call in an assault from afar, raining 5 spheres of burning pitch and stone onto enemies around you, dealing 2850% total weapon damage to enemies within 12 yards of the impact zone."""
    url = r'https://us.diablo3.com//en/class/crusader/active/bombardment'
    runes = [Barrels_of_Spikes, Annihilate, Mine_Field, Impactful_Bombardment, Targeted]


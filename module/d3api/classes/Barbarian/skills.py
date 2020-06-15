
""" barbarian active skills """
from datatypes import Active
from datatypes import Rune


class Frostbite(Rune):
    """ Frostbite """
    description = """Each hit Freezes the enemy for 1.5 seconds.

Enemies can be frozen by Bash once every 5 seconds."""


class Onslaught(Rune):
    """ Onslaught """
    description = """The enemy has a 10% increased chance to be Critically Hit for 3 seconds.

Bash's damage turns into Lightning."""


class Punish(Rune):
    """ Punish """
    description = """Increase your damage by 4% for 5 seconds after using Bash. This effect stacks up to 3 times."""


class Instigation(Rune):
    """ Instigation """
    description = """Increase Fury generated to 9.

Bash's damage turns into Fire."""


class Pulverize(Rune):
    """ Pulverize """
    description = """Each hit causes a shockwave that deals 100% weapon damage as Fire to enemies in a 26 yard line behind the primary enemy."""


class Bash(Active):
    """ Bash """
    category = "active"
    description = """Generate: 6 Fury per attack

Brutally smash an enemy for 320% weapon damage."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/bash'
    runes = [Frostbite, Onslaught, Punish, Instigation, Pulverize]


class Rolling_Thunder(Rune):
    """ Rolling Thunder """
    description = """Create a shockwave that deals 505% weapon damage to all enemies within 22 yards in front of you."""


class Smash(Rune):
    """ Smash """
    description = """Smash for 640% weapon damage as Fire."""


class The_Devils_Anvil(Rune):
    """ The Devil's Anvil """
    description = """Each hit creates a tremor at the point of impact for 2 seconds that Chills enemies by 80%.

Hammer of the Ancients's damage turns into Cold."""


class Thunderstrike(Rune):
    """ Thunderstrike """
    description = """When you kill an enemy with Hammer of the Ancients, other enemies within 10 yards are Stunned for 2 seconds.

Hammer of the Ancients turns into Lightning damage."""


class Birthright(Rune):
    """ Birthright """
    description = """Critical Hits heal you for 3% of your maximum Life."""


class Hammer_of_the_Ancients(Active):
    """ Hammer of the Ancients """
    category = "active"
    description = """Cost: 20 Fury

Call forth a massive hammer to smash enemies directly in front of you for 535% weapon damage. Hammer of the Ancients has a 1% increased Critical Hit Chance for every 5 Fury that you have."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/hammer-of-the-ancients'
    runes = [Rolling_Thunder, Smash, The_Devils_Anvil, Thunderstrike, Birthright]


class Rupture(Rune):
    """ Rupture """
    description = """Enemies slain by Cleave explode, causing 160% weapon damage as Fire to all other enemies within 8 yards."""


class Reaping_Swing(Rune):
    """ Reaping Swing """
    description = """Generate 1 additional Fury per enemy hit.

Cleave's damage turns into Fire."""


class Scattering_Blast(Rune):
    """ Scattering Blast """
    description = """On Critical Hits, knock enemies up into the air and deal 80% weapon damage to enemies where they land."""


class Broad_Sweep(Rune):
    """ Broad Sweep """
    description = """Swing at all enemies around you and increase damage to 235% weapon damage as Lightning."""


class Gathering_Storm(Rune):
    """ Gathering Storm """
    description = """Enemies cleaved are Chilled and take 10% increased damage from all sources for 3 seconds.

Cleave's damage turns into Cold."""


class Cleave(Active):
    """ Cleave """
    category = "active"
    description = """Generate: 6 Fury per attack

Swing your weapon in a wide arc to deal 200% weapon damage to all enemies caught in the swing."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/cleave'
    runes = [Rupture, Reaping_Swing, Scattering_Blast, Broad_Sweep, Gathering_Storm]


class Deafening_Crash(Rune):
    """ Deafening Crash """
    description = """Reduce the cooldown of Ground Stomp to 8 seconds.

Enemies in the area have their movement speed slowed by 80% for 8 seconds after they recover from being stunned."""


class Wrenching_Smash(Rune):
    """ Wrenching Smash """
    description = """Increase the area of effect to 24 yards. Enemies are pulled closer before the strike lands."""


class Trembling_Stomp(Rune):
    """ Trembling Stomp """
    description = """Enemies in the area also take 575% weapon damage as Fire."""


class Foot_of_the_Mountain(Rune):
    """ Foot of the Mountain """
    description = """Increase Fury generated to 30."""


class Jarring_Slam(Rune):
    """ Jarring Slam """
    description = """Enemies hit have a chance to drop a health globe."""


class Ground_Stomp(Active):
    """ Ground Stomp """
    category = "active"
    description = """Generate: 15 Fury
Cooldown: 12 seconds

Smash the ground, stunning all enemies within 14 yards for 4 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/ground-stomp'
    runes = [Deafening_Crash, Wrenching_Smash, Trembling_Stomp, Foot_of_the_Mountain, Jarring_Slam]


class Ravage(Rune):
    """ Ravage """
    description = """Increase the range of Rend to hit all enemies within 18 yards.

Rend's damage turns into Fire."""


class Blood_Lust(Rune):
    """ Blood Lust """
    description = """Heal for 0.5% of your maximum Life per second for each affected enemy."""


class Lacerate(Rune):
    """ Lacerate """
    description = """Increase damage to 1350% weapon damage as Lightning over 5 seconds."""


class Mutilate(Rune):
    """ Mutilate """
    description = """Affected enemies are Chilled and take 10% increased damage from all sources.

Rend's damage turns into Cold."""


class Bloodbath(Rune):
    """ Bloodbath """
    description = """Enemies killed while bleeding cause all enemies within 10 yards to begin bleeding for 1100% weapon damage as Physical over 5 seconds."""


class Rend(Active):
    """ Rend """
    category = "active"
    description = """Cost: 20 Fury

A sweeping strike causes all enemies within 12 yards to Bleed for 1100% weapon damage as Physical over 5 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/rend'
    runes = [Ravage, Blood_Lust, Lacerate, Mutilate, Bloodbath]


class Iron_Impact(Rune):
    """ Iron Impact """
    description = """Gain 150% additional Armor for 4 seconds after landing."""


class Launch(Rune):
    """ Launch """
    description = """You leap with such great force that enemies within 10 yards of the takeoff point take 180% weapon damage and are also slowed by 60% for 3 seconds."""


class Toppling_Impact(Rune):
    """ Toppling Impact """
    description = """Increase the damage of Leap to 450% and send enemies hurtling away from where you land."""


class Call_of_Arreat(Rune):
    """ Call of Arreat """
    description = """Shockwaves burst forth from the ground increasing the radius of effect to 16 yards and pulling affected enemies towards you."""


class Death_from_Above(Rune):
    """ Death from Above """
    description = """Land with such force that enemies have a 100% chance to be stunned for 3 seconds."""


class Leap(Active):
    """ Leap """
    category = "active"
    description = """Generate: 15 Fury
Cooldown: 10 seconds

Leap into the air, dealing 180% weapon damage to all enemies within 10 yards of your destination and slowing their movement speed by 60% for 3 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/leap'
    runes = [Iron_Impact, Launch, Toppling_Impact, Call_of_Arreat, Death_from_Above]


class Storm_of_Steel(Rune):
    """ Storm of Steel """
    description = """Throw up to 3 axes at nearby enemies that each deal 380% weapon damage."""


class Killing_Spree(Rune):
    """ Killing Spree """
    description = """Your Critical Hit Chance is increased by 8% for 5 seconds.

Overpower's damage turns into Lightning."""


class Crushing_Advance(Rune):
    """ Crushing Advance """
    description = """Redirect 35% of incoming melee damage back to the attacker for 5 seconds after Overpower is activated."""


class Momentum(Rune):
    """ Momentum """
    description = """Generate 5 Fury for each enemy hit by Overpower."""


class Revel(Rune):
    """ Revel """
    description = """Increase damage to 760% weapon damage as Fire."""


class Overpower(Active):
    """ Overpower """
    category = "active"
    description = """Cooldown: 12 seconds

Deal 380% weapon damage to all enemies within 9 yards.

Critical Hits have a chance to reduce the cooldown of Overpower by 1 second."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/overpower'
    runes = [Storm_of_Steel, Killing_Spree, Crushing_Advance, Momentum, Revel]


class Sidearm(Rune):
    """ Sidearm """
    description = """Each strike has a 25% chance to throw a piercing axe at a nearby enemy that deals 300% weapon damage as Cold to all enemies in its path.

Frenzy's damage turns into Cold."""


class Berserk(Rune):
    """ Berserk """
    description = """Increase Fury generated to 6.

Frenzy's damage turns into Cold."""


class Vanguard(Rune):
    """ Vanguard """
    description = """Gain 5% movement speed for each stack of Frenzy."""


class Smite(Rune):
    """ Smite """
    description = """Each hit has a 30% chance to call down a bolt of lightning from above, stunning the enemy for 1.5 seconds."""


class Maniac(Rune):
    """ Maniac """
    description = """Each Frenzy effect also increases your damage by 2.5%.

Frenzy's damage turns into Fire."""


class Frenzy(Active):
    """ Frenzy """
    category = "active"
    description = """Generate: 4 Fury per attack

Swing for 220% weapon damage. Frenzy's attack speed increases by 15% for 4 seconds with each swing. This effect stacks up to 5 times."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/frenzy'
    runes = [Sidearm, Berserk, Vanguard, Smite, Maniac]


class Stagger(Rune):
    """ Stagger """
    description = """Reduce the cost to 22 Fury.

Seismic Slam's damage turns into Lightning."""


class Shattered_Ground(Rune):
    """ Shattered Ground """
    description = """Increase damage to 735% weapon damage as Fire and knocks all enemies hit up into the air."""


class Rumble(Rune):
    """ Rumble """
    description = """Expend all remaining Fury to cause the ground to shudder after the initial strike, damaging enemies in the area for 15% weapon damage for every point of Fury expended as Physical over 2 seconds."""


class Strength_from_Earth(Rune):
    """ Strength from Earth """
    description = """Gain 1% of your maximum Life for every enemy hit."""


class Permafrost(Rune):
    """ Permafrost """
    description = """Create a sheet of frost that deals 755% weapon damage as Cold and Chills enemies by 60% for 1 second."""


class Seismic_Slam(Active):
    """ Seismic Slam """
    category = "active"
    description = """Cost: 30 Fury

Slam the ground and cause a wave of destruction that deals 620% weapon damage to enemies up to 50 yards in front of you."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/seismic-slam'
    runes = [Stagger, Shattered_Ground, Rumble, Strength_from_Earth, Permafrost]


class Blood_Law(Rune):
    """ Blood Law """
    description = """Increase healing to 6% of maximum Life for each enemy hit."""


class Best_Served_Cold(Rune):
    """ Best Served Cold """
    description = """Increase your Critical Hit Chance by 8% for 6 seconds after using Revenge.

Revenge's damage turns into Cold."""


class Retribution(Rune):
    """ Retribution """
    description = """Increase damage to 700% weapon damage as Fire."""


class Grudge(Rune):
    """ Grudge """
    description = """Knockback enemies 24 yards when using Revenge.

Revenge's damage turns into Lightning."""


class Provocation(Rune):
    """ Provocation """
    description = """Increase the maximum number of charges to 3."""


class Revenge(Active):
    """ Revenge """
    category = "active"
    description = """Cost: 1 charge

Deal 300% weapon damage to all nearby enemies. You heal 4% of your maximum Life for each enemy hit.

Revenge has a 15% chance to gain a charge each time you are hit. Maximum 2 charges."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/revenge'
    runes = [Blood_Law, Best_Served_Cold, Retribution, Grudge, Provocation]


class Intimidate(Rune):
    """ Intimidate """
    description = """Affected enemies also have their movement speed reduced by 60%."""


class Falter(Rune):
    """ Falter """
    description = """Enemies instead take 25% increased damage for 6 seconds."""


class Grim_Harvest(Rune):
    """ Grim Harvest """
    description = """Enemies are badly shaken and have a chance to drop health globes."""


class Demoralize(Rune):
    """ Demoralize """
    description = """Affected enemies are also taunted to attack you for 4 seconds."""


class Terrify(Rune):
    """ Terrify """
    description = """Enemies are severely demoralized. Each enemy has a 100% chance to flee in Fear for 3 seconds."""


class Threatening_Shout(Active):
    """ Threatening Shout """
    category = "active"
    description = """Generate: 15 Fury
Cooldown: 10 seconds

Shout with great ferocity, reducing damage done by enemies within 25 yards by 20% for 15 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/threatening-shout'
    runes = [Intimidate, Falter, Grim_Harvest, Demoralize, Terrify]


class Rush(Rune):
    """ Rush """
    description = """Increase Dodge Chance by 12% while sprinting."""


class Run_Like_the_Wind(Rune):
    """ Run Like the Wind """
    description = """Tornadoes rage in your wake, each dealing 60% weapon damage as Physical for 3 seconds to nearby enemies."""


class Marathon(Rune):
    """ Marathon """
    description = """Increase the movement speed bonus to 40% for 4 seconds."""


class Gangway(Rune):
    """ Gangway """
    description = """Slams through enemies, knocking them back and dealing 25% weapon damage."""


class Forced_March(Rune):
    """ Forced March """
    description = """Increase movement speed of allies within 50 yards by 20% for 3 seconds."""


class Sprint(Active):
    """ Sprint """
    category = "active"
    description = """Cost: 20 Fury

Increase movement speed by 30% for 3 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/sprint'
    runes = [Rush, Run_Like_the_Wind, Marathon, Gangway, Forced_March]


class Mighty_Throw(Rune):
    """ Mighty Throw """
    description = """Increase thrown weapon damage to 400% weapon damage as Lightning."""


class Ricochet(Rune):
    """ Ricochet """
    description = """The weapon ricochets to 3 enemies within 20 yards of each other.

Weapon Throw's damage turns into Fire."""


class Throwing_Hammer(Rune):
    """ Throwing Hammer """
    description = """Hurl a hammer with a 40% chance to Stun the enemy for 1 second."""


class Stupefy(Rune):
    """ Stupefy """
    description = """Aim for the head, gaining a 15% chance of causing your enemy to be Confused and attack other enemies for 3 seconds."""


class Balanced_Weapon(Rune):
    """ Balanced Weapon """
    description = """Increase Fury generated to 9.

Weapon Throw's damage turns into Fire."""


class Weapon_Throw(Active):
    """ Weapon Throw """
    category = "active"
    description = """Generate: 6 Fury per attack

Hurl a throwing weapon at an enemy dealing 275% weapon damage."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/weapon-throw'
    runes = [Mighty_Throw, Ricochet, Throwing_Hammer, Stupefy, Balanced_Weapon]


class Giants_Stride(Rune):
    """ Giant's Stride """
    description = """20 secondary tremors follow your movement and deal 300% weapon damage as Fire each."""


class Chilling_Earth(Rune):
    """ Chilling Earth """
    description = """Create an icy patch, causing Earthquake to Freeze all enemies hit and deal Cold damage."""


class The_Mountains_Call(Rune):
    """ The Mountain's Call """
    description = """Remove the Fury cost and reduce the cooldown to 30 seconds.

Earthquake's damage turns into Lightning."""


class Molten_Fury(Rune):
    """ Molten Fury """
    description = """Increase Earthquake's damage to 6000% weapon damage as Fire."""


class Cave_In(Rune):
    """ Cave-In """
    description = """All enemies within 24 yards are pulled in towards you.

Earthquake's damage turns into Physical."""


class Earthquake(Active):
    """ Earthquake """
    category = "active"
    description = """Cost: 25 Fury
Cooldown: 60 seconds

Shake the ground violently, dealing 4800% weapon damage as Fire over 8 seconds to all enemies within 18 yards."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/earthquake'
    runes = [Giants_Stride, Chilling_Earth, The_Mountains_Call, Molten_Fury, Cave_In]


class Dust_Devils(Rune):
    """ Dust Devils """
    description = """Generate harsh tornadoes that deal 180% weapon damage to enemies in their path."""


class Hurricane(Rune):
    """ Hurricane """
    description = """Pull enemies from up to 35 yards away towards you while whirlwinding.

Whirlwind's damage turns into Cold."""


class Blood_Funnel(Rune):
    """ Blood Funnel """
    description = """Critical Hits restore 1% of your maximum Life."""


class Wind_Shear(Rune):
    """ Wind Shear """
    description = """Gain 1 Fury for every enemy struck.

Whirlwind's damage turns into Lightning."""


class Volcanic_Eruption(Rune):
    """ Volcanic Eruption """
    description = """Turns Whirlwind into a torrent of magma that deals 400% weapon damage as Fire."""


class Whirlwind(Active):
    """ Whirlwind """
    category = "active"
    description = """Cost: 10 Fury

Deliver multiple attacks to everything in your path for 340% weapon damage.

While whirlwinding, you move at 100% movement speed."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/whirlwind'
    runes = [Dust_Devils, Hurricane, Blood_Funnel, Wind_Shear, Volcanic_Eruption]


class Battering_Ram(Rune):
    """ Battering Ram """
    description = """Increase the damage to 1050% weapon damage as Fire."""


class Merciless_Assault(Rune):
    """ Merciless Assault """
    description = """Recharge time is reduced by 2 seconds for every enemy hit. This effect can reduce the recharge time by up to 10 seconds."""


class Stamina(Rune):
    """ Stamina """
    description = """Generate 10 additional Fury for each enemy hit while charging."""


class Cold_Rush(Rune):
    """ Cold Rush """
    description = """All enemies hit are Frozen for 2.5 seconds.

Furious Charge's damage turns into Cold."""


class Dreadnought(Rune):
    """ Dreadnought """
    description = """Store up to 3 charges of Furious Charge.

Furious Charge's damage turns into Lightning."""


class Furious_Charge(Active):
    """ Furious Charge """
    category = "active"
    description = """Cost: 1 Charge
Generate: 15 Fury

Rush forward knocking back and dealing 600% weapon damage to enemies along your path.

You gain a charge every 10 seconds and can have up to 1 charge stored at a time."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/furious-charge'
    runes = [Battering_Ram, Merciless_Assault, Stamina, Cold_Rush, Dreadnought]


class Bravado(Rune):
    """ Bravado """
    description = """While Ignore Pain is active, gain 40% increased movement speed and knock enemies away as you run."""


class Iron_Hide(Rune):
    """ Iron Hide """
    description = """Increase duration to 7 seconds."""


class Ignorance_is_Bliss(Rune):
    """ Ignorance is Bliss """
    description = """While Ignore Pain is active, gain 5364 Life per Fury spent."""


class Mob_Rule(Rune):
    """ Mob Rule """
    description = """Allies within 50 yards also gain 25% damage reduction and Immunity to control-impairing effects for 5 seconds."""


class Contempt_for_Weakness(Rune):
    """ Contempt for Weakness """
    description = """Instantly heal for 35% of maximum Life when activating Ignore Pain."""


class Ignore_Pain(Active):
    """ Ignore Pain """
    category = "active"
    description = """Cooldown: 30 seconds

Reduce all damage taken by 50% and gain Immunity to all control-impairing effects for 5 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/ignore-pain'
    runes = [Bravado, Iron_Hide, Ignorance_is_Bliss, Mob_Rule, Contempt_for_Weakness]


class Marauders_Rage(Rune):
    """ Marauder's Rage """
    description = """Increase damage bonus to 15%."""


class Ferocity(Rune):
    """ Ferocity """
    description = """Increase movement speed by 15%."""


class Swords_to_Ploughshares(Rune):
    """ Swords to Ploughshares """
    description = """Critical Hits heal you and your pets for up to 21,457 Life."""


class Into_the_Fray(Rune):
    """ Into the Fray """
    description = """Gain 1% Critical Hit Chance for each enemy within 10 yards while under the effects of Battle Rage."""


class Bloodshed(Rune):
    """ Bloodshed """
    description = """Deal damage equal to 20% of your recent Critical Hits to enemies within 20 yards every 1 second."""


class Battle_Rage(Active):
    """ Battle Rage """
    category = "active"
    description = """Cost: 20 Fury

Enter a rage which increases your damage by 10% and Critical Hit Chance by 3%. Lasts 120 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/battle-rage'
    runes = [Marauders_Rage, Ferocity, Swords_to_Ploughshares, Into_the_Fray, Bloodshed]


class The_Council_Rises(Rune):
    """ The Council Rises """
    description = """The Ancients deal 540% weapon damage as Fire with each attack."""


class Duty_to_the_Clan(Rune):
    """ Duty to the Clan """
    description = """Enemies hit by the Ancients are Chilled for 2 seconds and have 10% increased chance to be Critically Hit.

The Ancients' damage turns into Cold."""


class Ancients_Blessing(Rune):
    """ Ancients' Blessing """
    description = """Each point of Fury you spend heals you and your Ancients for 966 Life."""


class Ancients_Fury(Rune):
    """ Ancients' Fury """
    description = """Gain 4 Fury every time an Ancient deals damage."""


class Together_as_One(Rune):
    """ Together as One """
    description = """50% of all damage dealt to you is instead divided evenly between the Ancients.

The Ancients' damage turns into Lightning."""


class Call_of_the_Ancients(Active):
    """ Call of the Ancients """
    category = "active"
    description = """Cooldown: 120 seconds

Summon the ancient Barbarians Talic, Korlic, and Madawc to fight alongside you for 20 seconds. Each deals 270% weapon damage per swing in addition to bonus abilities.

 Talic wields a sword and shield and uses Whirlwind and Leap. Korlic wields a massive polearm and uses Cleave and Furious Charge. Madawc dual-wields axes and uses Weapon Throw and Seismic Slam."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/call-of-the-ancients'
    runes = [The_Council_Rises, Duty_to_the_Clan, Ancients_Blessing, Ancients_Fury, Together_as_One]


class Ranseur(Rune):
    """ Ranseur """
    description = """Enemies hit are knocked back 5 yards."""


class Harpoon(Rune):
    """ Harpoon """
    description = """Add a chain to the spear to drag all enemies hit back to you and Slow them by 60% for 1 second."""


class Jagged_Edge(Rune):
    """ Jagged Edge """
    description = """Increase the damage to 640% weapon damage as Fire."""


class Boulder_Toss(Rune):
    """ Boulder Toss """
    description = """Expend all remaining Fury to deal 20% weapon damage for every point of Fury expended to enemies within 9 yards of the impact location."""


class Rage_Flip(Rune):
    """ Rage Flip """
    description = """Add a chain to the spear to throw all enemies hit behind you and Slow them by 60% for 1 second."""


class Ancient_Spear(Active):
    """ Ancient Spear """
    category = "active"
    description = """Cost: 25 Fury

Throw a spear that pierces enemies and deals 500% weapon damage."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/ancient-spear'
    runes = [Ranseur, Harpoon, Jagged_Edge, Boulder_Toss, Rage_Flip]


class Hardened_Wrath(Rune):
    """ Hardened Wrath """
    description = """For the first 5 seconds, gain an additional 60% increased Armor."""


class Charge_(Rune):
    """ Charge! """
    description = """Increase Fury generated to 50."""


class Invigorate(Rune):
    """ Invigorate """
    description = """Increase maximum Life by 10% and Life regeneration by 13,411 per second while affected by War Cry."""


class Veterans_Warning(Rune):
    """ Veteran's Warning """
    description = """Increase Dodge Chance by 30% while affected by War Cry."""


class Impunity(Rune):
    """ Impunity """
    description = """Increase resistance to all elements by 20% while affected by War Cry."""


class War_Cry(Active):
    """ War Cry """
    category = "active"
    description = """Generate: 20 Fury
Cooldown: 20 seconds

Unleash a rallying cry to increase Armor for you and all allies within 100 yards by 20% for 120 seconds."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/war-cry'
    runes = [Hardened_Wrath, Charge_, Invigorate, Veterans_Warning, Impunity]


class Arreats_Wail(Rune):
    """ Arreat's Wail """
    description = """Activating Wrath of the Berserker deals 3400% weapon damage as Fire to all enemies within 15 yards."""


class Insanity(Rune):
    """ Insanity """
    description = """While active, gain 50% increased damage."""


class Slaughter(Rune):
    """ Slaughter """
    description = """While active, Critical Hits have a chance to cause an eruption of blood dealing 300% weapon damage to enemies within 15 yards."""


class Striding_Giant(Rune):
    """ Striding Giant """
    description = """Reduce all damage taken by 50%."""


class Thrive_on_Chaos(Rune):
    """ Thrive on Chaos """
    description = """While active, gain 5364 Life per Fury spent."""


class Wrath_of_the_Berserker(Active):
    """ Wrath of the Berserker """
    category = "active"
    description = """Cooldown: 120 seconds

Enter a berserker rage which raises several attributes for 20 seconds.

 Critical Hit Chance: 10% Attack Speed: 25% Dodge Chance: 20% Movement Speed: 20%"""
    url = r'https://us.diablo3.com//en/class/barbarian/active/wrath-of-the-berserker'
    runes = [Arreats_Wail, Insanity, Slaughter, Striding_Giant, Thrive_on_Chaos]


class Volcano(Rune):
    """ Volcano """
    description = """Chunks of molten lava are randomly launched at nearby enemies, dealing 6600% weapon damage as Fire over 5 seconds."""


class Lahar(Rune):
    """ Lahar """
    description = """Cooldown is reduced by 1 second for every 15 Fury spent."""


class Snow_Capped_Mountain(Rune):
    """ Snow-Capped Mountain """
    description = """Cave-in from both sides pushes enemies together, dealing 2800% weapon damage as Cold and Slowing them by 60% for 3 seconds."""


class Tectonic_Rift(Rune):
    """ Tectonic Rift """
    description = """Store up to 3 charges of Avalanche."""


class Glacier(Rune):
    """ Glacier """
    description = """Giant blocks of ice hit enemies for 2400% weapon damage as Cold and Freeze them."""


class Avalanche(Active):
    """ Avalanche """
    category = "active"
    description = """Cooldown: 30 seconds

Cause a massive avalanche of rocks to fall on an area dealing 2400% weapon damage to all enemies caught in its path.

Cooldown is reduced by 1 second for every 25 Fury you spend."""
    url = r'https://us.diablo3.com//en/class/barbarian/active/avalanche'
    runes = [Volcano, Lahar, Snow_Capped_Mountain, Tectonic_Rift, Glacier]



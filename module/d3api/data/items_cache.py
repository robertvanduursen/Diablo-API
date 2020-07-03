import sys, os
sys.path.append("..\..")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datatypes import Item, Set, Set_Item
from .armor_sets import Rolands_Legacy, Aegis_of_Valor, Pestilence_Battle


class Hellfire_Ring(Item):
    """ Hellfire Ring """
    url = r'/en/artisan/jeweler/recipe/hellfire-ring'
    type = 'ring'
    text = """

	+45% Experience. (4.5% at level 70)

	Chance on hit to engulf the ground in lava, dealing 200% weapon damage per second for 6 seconds.
    """


class Hellfire_Ring(Item):
    """ Hellfire Ring """
    url = r'/en/artisan/jeweler/recipe/hellfire-ring-of-strength'
    type = 'ring'
    text = """

	+[300 - 329] Strength

	+35% Experience. (3.5% at level 70)

	Chance to launch an explosive ball of Hellfire when you attack.
    """


class Band_of_Might(Item):
    """ Band of Might """
    url = r'/en/item/band-of-might-P61_Unique_Ring_05'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 After casting Furious Charge, Ground Stomp, or Leap, take 74% reduced damage for 8 seconds.
	(Barbarian Only)
	[60 - 80]%
    """


class Circle_of_Nailujs_Evol(Item):
    """ Circle of Nailuj's Evol """
    url = r'/en/item/circle-of-nailujs-evol-P6_Unique_Ring_01'
    type = 'ring'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 
	 You now raise an additional Skeletal Mage with each cast and they last an additional 4 seconds.
	(Necromancer Only)
	[2 - 4]
    """


class Ring_of_Royal_Grandeur(Item):
    """ Ring of Royal Grandeur """
    url = r'/en/item/ring-of-royal-grandeur-Unique_Ring_107_x1'
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[7737 - 9214] Life per Hit

	Reduces the number of items needed for set bonuses by 1 (to a minimum of 2).
    """


class Pandemonium_Loop(Item):
    """ Pandemonium Loop """
    url = r'/en/item/pandemonium-loop-Unique_Ring_109_x1'
    type = 'ring'
    text = """
	 Enemies slain while Feared die in a bloody explosion and cause other nearby enemies to flee in Fear.
    """


class Avarice_Band(Item):
    """ Avarice Band """
    url = r'/en/item/avarice-band-Unique_Ring_108_x1'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[32 - 35]% Extra Gold from Monsters
	 Each time you pick up gold, increase your Gold and Health Pickup radius by 1 yard for 10 seconds, stacking up to 30 times.
    """


class Leorics_Signet(Item):
    """ Leoric's Signet """
    url = r'/en/item/leorics-signet-Unique_Ring_002_x1'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[20 - 30]% Experience. ([2.0 - 3.0]% at level 70)
    """


class Pandemonium_Loop(Item):
    """ Pandemonium Loop """
    url = r'/en/item/pandemonium-loop-Unique_Ring_109_p2'
    type = 'ring'
    text = """
	 Enemies slain while Feared die in a bloody explosion for 800% weapon damage and cause other nearby enemies to flee in Fear.
    """


class Manald_Heal(Item):
    """ Manald Heal """
    url = r'/en/item/manald-heal-P43_Unique_Ring_021_x1'
    type = 'ring'
    text = """
	 Enemies stunned with Paralysis also take 13,462% weapon damage as Lightning.
	(Wizard Only)
	[13,000 - 14,000]%
    """


class Broken_Promises(Item):
    """ Broken Promises """
    url = r'/en/item/broken-promises-Unique_Ring_006_p2'
    type = 'ring'
    text = """

	Reduces all resource costs by [5.0 - 8.0]%.
	 After 5 consecutive non-critical hits, your chance to critically hit is increased to 100% for 3 seconds.
	3
    """


class Puzzle_Ring(Item):
    """ Puzzle Ring """
    url = r'/en/item/puzzle-ring-Unique_Ring_004_x1'
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[32 - 35]% Extra Gold from Monsters
	 Summon a treasure goblin who picks up normal-quality items for you. After picking up 16 items, he drops a rare item with a chance for a legendary.
	[12 - 16]
    """


class Halo_of_Karini(Item):
    """ Halo of Karini """
    url = r'/en/item/halo-of-karini-P61_Unique_Ring_03'
    type = 'ring'
    text = """

	Sockets (1)
	 You take 74% less damage for 5 seconds after your Storm Armor electrocutes an enemy more than 15 yards away.
	(Wizard Only)
	[60 - 80]%
    """


class The_Tall_Mans_Finger(Item):
    """ The Tall Man's Finger """
    url = r'/en/item/the-tall-mans-finger-Unique_Ring_101_x1'
    type = 'ring'
    text = """
	 Zombie Dogs instead summons a single gargantuan dog with more damage and health than all other dogs combined.
	(Witch Doctor Only)
    """


class Rechels_Ring_of_Larceny(Item):
    """ Rechel's Ring of Larceny """
    url = r'/en/item/rechels-ring-of-larceny-Unique_Ring_104_x1'
    type = 'ring'
    text = """

	[1.0 - 5.1]% Chance to Fear on Hit
	 Gain 57% increased movement speed for 4 seconds after Fearing an enemy.
	[45 - 60]%
    """


class Arcstone(Item):
    """ Arcstone """
    url = r'/en/item/arcstone-P2_Unique_Ring_03'
    type = 'ring'
    text = """
	 Lightning pulses periodically between all wearers of this item, dealing 1350% weapon damage.
	[1000 - 1500]%
    """


class Band_of_the_Rue_Chambers(Item):
    """ Band of the Rue Chambers """
    url = r'/en/item/band-of-the-rue-chambers-Unique_Ring_106_x1'
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Your Spirit Generators generate 40% more Spirit.
	(Monk Only)
	[40 - 50]%
    """


class Rogars_Huge_Stone(Item):
    """ Rogar's Huge Stone """
    url = r'/en/item/rogars-huge-stone-Unique_Ring_103_x1'
    type = 'ring'
    text = """
	 Increase your Life per Second by up to 95% based on your missing Life.
	[75 - 100]%
    """


class Wyrdward(Item):
    """ Wyrdward """
    url = r'/en/item/wyrdward-Unique_Ring_102_p2'
    type = 'ring'
    text = """
	 Lightning damage has a 25% chance to Stun for 1.5 seconds.
	[25 - 35]%
    """


class The_Short_Mans_Finger(Item):
    """ The Short Man's Finger """
    url = r'/en/item/the-short-mans-finger-P61_Unique_Ring_01'
    type = 'ring'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 
	 Gargantuan instead summons three smaller gargantuans that have their damage increased by 596%.
	(Witch Doctor Only)
	[500 - 650]%
    """


class Lornelles_Sunstone(Item):
    """ Lornelle's Sunstone """
    url = r'/en/item/lornelles-sunstone-P6_Unique_Ring_04'
    type = 'ring'
    text = """
	 Your damage reduction is increased by 0.89% for every 1% Life you are missing.
	(Necromancer Only)
	[0.75 - 0.95]%
    """


class Nagelring(Item):
    """ Nagelring """
    url = r'/en/item/nagelring-Unique_Ring_018_p2'
    type = 'ring'
    text = """
	 Summons a Fallen Lunatic to your side every 10 seconds.
	[10 - 12]
    """


class Obsidian_Ring_of_the_Zodiac(Item):
    """ Obsidian Ring of the Zodiac """
    url = r'/en/item/obsidian-ring-of-the-zodiac-Unique_Ring_023_p2'
    type = 'ring'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.

	Attack Speed Increased by [5.0 - 7.0]%

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Reduces all resource costs by [5.0 - 8.0]%.

	Ignores Durability Loss
	 Reduce the remaining cooldown of one of your skills by 1 second when you hit with a resource-spending attack.
	1
    """


class Justice_Lantern(Item):
    """ Justice Lantern """
    url = r'/en/item/justice-lantern-P4_Unique_Ring_03'
    type = 'ring'
    text = """

	+[12 - 16]% Chance to Block

	Sockets (1)

	Reduces duration of control impairing effects by [35 - 50]%
	 Gain damage reduction equal to 47% of your Block Chance.
	[45 - 55]%
    """


class Bul_Kathoss_Wedding_Band(Item):
    """ Bul-Kathos's Wedding Band """
    url = r'/en/item/bulkathoss-wedding-band-Unique_Ring_020_x1'
    type = 'ring'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 
	 You drain life from enemies around you.
    """


class Eternal_Union(Item):
    """ Eternal Union """
    url = r'/en/item/eternal-union-Unique_Ring_007_p1'
    type = 'ring'
    text = """
	 Increases the duration of Phalanx avatars by 200%.
	(Crusader Only)
    """


class Krysbins_Sentence(Item):
    """ Krysbin's Sentence """
    url = r'/en/item/krysbins-sentence-P6_Unique_Ring_03'
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 You deal 95% increased damage against slowed enemies or triple this bonus against enemies afflicted by any other type of control-impairing effect.
	(Necromancer Only)
	[75 - 100]%
    """


class Halo_of_Arlyse(Item):
    """ Halo of Arlyse """
    url = r'/en/item/halo-of-arlyse-p2_Unique_Ring_Wizard_001'
    type = 'ring'
    text = """

	Sockets (1)
	 Your Ice Armor now reduces damage from melee attacks by 50% and automatically casts Frost Nova whenever you take 10% of your Life in damage.
	(Wizard Only)
	[50 - 60]%
    """


class Convention_of_Elements(Item):
    """ Convention of Elements """
    url = r'/en/item/convention-of-elements-P2_Unique_Ring_04'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Sockets (1)
	 Gain 179% increased damage to a single element for 4 seconds. This effect rotates through the elements available to your class in the following order: Arcane, Cold, Fire, Holy, Lightning, Physical, Poison.
	[150 - 200]%
    """


class Litany_of_the_Undaunted(Item):
    """ Litany of the Undaunted """
    url = r'/en/item/litany-of-the-undaunted-Unique_Ring_015_x1'
    type = 'ring'
    text = """
	(2) Set:      While this is your only Item Set bonus every Ancient item you have equipped increases your damage dealt by 750% and reduces your damage taken by 4%.
    """


class The_Compass_Rose(Item):
    """ The Compass Rose """
    url = r'/en/item/the-compass-rose-Unique_Ring_013_x1'
    type = 'ring'
    text = """
	(2) Set:      While moving, damage taken is reduced by up to 50%.     While standing still, damage dealt is increased by up to 100%.
    """


class The_Wailing_Host(Item):
    """ The Wailing Host """
    url = r'/en/item/the-wailing-host-Unique_Ring_014_x1'
    type = 'ring'
    text = """
	(2) Set:      While this is your only Item Set bonus every Ancient item you have equipped increases your damage dealt by 750% and reduces your damage taken by 4%.
    """


class Skull_Grasp(Item):
    """ Skull Grasp """
    url = r'/en/item/skull-grasp-P61_Unique_Ring_02'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Increase the damage of Whirlwind by 328%
	(Barbarian Only)
	[300 - 400]%
    """


class Band_of_Hollow_Whispers(Item):
    """ Band of Hollow Whispers """
    url = r'/en/item/band-of-hollow-whispers-Unique_Ring_001_x1'
    type = 'ring'
    text = """
	 This ring occasionally haunts nearby enemies.
    """


class Ring_of_Emptiness(Item):
    """ Ring of Emptiness """
    url = r'/en/item/ring-of-emptiness-P42_Unique_Ring_Haunt'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 You deal 279% increased damage to enemies affected by either your Haunt or Locust Swarm.
	(Witch Doctor Only)
	[250 - 300]%
    """


class Kredes_Flame(Item):
    """ Krede's Flame """
    url = r'/en/item/kredes-flame-Unique_Ring_003_x1'
    type = 'ring'
    text = """
	 Taking Fire damage restores your primary resource.
    """


class Elusive_Ring(Item):
    """ Elusive Ring """
    url = r'/en/item/elusive-ring-P4_Unique_Ring_02'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 After casting Shadow Power, Smoke Screen, or Vault, take 50% reduced damage for 8 seconds.
	(Demon Hunter Only)
	[50 - 60]%
    """


class Zunimassas_Pox(Item):
    """ Zunimassa's Pox """
    url = r'/en/item/zunimassas-pox-Unique_Ring_012_x1'
    type = 'ring'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Stone_of_Jordan(Item):
    """ Stone of Jordan """
    url = r'/en/item/stone-of-jordan-Unique_Ring_019_x1'
    type = 'ring'
    text = """

	Increases damage against elites by [25.0 - 30.0]%

	+[120 - 150] Maximum Mana
    """


class Unity(Item):
    """ Unity """
    url = r'/en/item/unity-Unique_Ring_010_x1'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Increases damage against elites by [12.0 - 15.0]%
	 All damage taken is split between wearers of this item.
    """


class Oculus_Ring(Item):
    """ Oculus Ring """
    url = r'/en/item/oculus-ring-Unique_Ring_017_p4'
    type = 'ring'
    text = """

	Sockets (1)
	 Chance to create an area of focused power on killing a monster. Damage is increased by 82% while standing in the area.
	[70 - 85]%
    """


class Natalyas_Reflection(Item):
    """ Natalya's Reflection """
    url = r'/en/item/natalyas-reflection-Unique_Ring_011_x1'
    type = 'ring'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Focus(Item):
    """ Focus """
    url = r'/en/item/focus-Unique_Ring_Set_001_x1'
    type = 'ring'
    text = """
	(2) Set:      When you hit with a resource-generating attack or primary skill, deal 50% increased damage for 5 seconds.
	(2) Set:      When you hit with a resource-spending attack, deal 50% increased damage for 5 seconds.
    """


class Briggs_Wrath(Item):
    """ Briggs' Wrath """
    url = r'/en/item/briggs-wrath-P6_Unique_Ring_02'
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Uncursed enemies are pulled to the target location when a curse is applied to them.
	(Necromancer Only)
    """


class Restraint(Item):
    """ Restraint """
    url = r'/en/item/restraint-Unique_Ring_Set_002_x1'
    type = 'ring'
    text = """
	(2) Set:      When you hit with a resource-generating attack or primary skill, deal 50% increased damage for 5 seconds.
	(2) Set:      When you hit with a resource-spending attack, deal 50% increased damage for 5 seconds.
    """


class Hellfire_Amulet(Item):
    """ Hellfire Amulet """
    url = r'/en/artisan/jeweler/recipe/hellfire-amulet-of-intelligence'
    type = 'amulet'
    text = """

	+[626 - 750] Intelligence

	Sockets (1)

	Random class passive.
    """


class Squirts_Necklace(Item):
    """ Squirt's Necklace """
    url = r'/en/item/squirts-necklace-P66_Unique_Amulet_010'
    type = 'amulet'
    text = """

	Critical Hit Damage Increased by [51.0 - 100.0]% 

	+[71 - 80]% Extra Gold from Monsters
	 While not taking damage, damage dealt is increased by up to 100% and damage taken is increased by up to 50%.
    """


class Moonlight_Ward(Item):
    """ Moonlight Ward """
    url = r'/en/item/moonlight-ward-Unique_Amulet_003_x1'
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%

	Arcane skills deal [20 - 25]% more damage.
	 Hitting an enemy within 15 yards has a chance to ward you with shards of Arcane energy that explode when enemies get close, dealing 320% weapon damage as Arcane to enemies within 15 yards.
	[240 - 320]%
    """


class Overwhelming_Desire(Item):
    """ Overwhelming Desire """
    url = r'/en/item/overwhelming-desire-Unique_Amulet_106_x1'
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Chance on hit to charm the enemy. While charmed, the enemy takes 35% increased damage.
    """


class Golden_Gorget_of_Leoric(Item):
    """ Golden Gorget of Leoric """
    url = r'/en/item/golden-gorget-of-leoric-Unique_Amulet_105_x1'
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%

	+[91 - 100] Resistance to All Elements
	 After earning a massacre bonus, 6 Skeletons are summoned to fight by your side for 10 seconds.
	[4 - 6]
    """


class Wisdom_of_Kalan(Item):
    """ Wisdom of Kalan """
    url = r'/en/item/wisdom-of-kalan-P6_Unique_Amulet_03'
    type = 'amulet'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Increases the maximum stacks of Bone Armor by 5.
	(Necromancer Only)
	5
    """


class Talisman_of_Aranoch(Item):
    """ Talisman of Aranoch """
    url = r'/en/item/talisman-of-aranoch-Unique_Amulet_012_x1'
    type = 'amulet'
    text = """
	 Prevent all Cold damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class Eye_of_Etlich(Item):
    """ Eye of Etlich """
    url = r'/en/item/eye-of-etlich-Unique_Amulet_014_x1'
    type = 'amulet'
    text = """

	Reduces damage from ranged attacks by [6.0 - 30.1]%.
    """


class Rondals_Locket(Item):
    """ Rondal's Locket """
    url = r'/en/item/rondals-locket-Unique_Amulet_009_x1'
    type = 'amulet'
    text = """

	Increases Gold and Health Pickup by [4 - 6] Yards.

	Health Globes and Potions Grant +[20,001 - 29,713] Life.
    """


class Dovu_Energy_Trap(Item):
    """ Dovu Energy Trap """
    url = r'/en/item/dovu-energy-trap-Unique_Amulet_107_x1'
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Increases duration of Stun effects by 22%.
	[20 - 25]%
    """


class Ancestors_Grace(Item):
    """ Ancestors' Grace """
    url = r'/en/item/ancestors-grace-Unique_Amulet_102_x1'
    type = 'amulet'
    text = """

	+[626 - 750] Vitality
	 When receiving fatal damage, you are instead restored to 100% of maximum Life and resources. This item is destroyed in the process.
    """


class Countess_Julias_Cameo(Item):
    """ Countess Julia's Cameo """
    url = r'/en/item/countess-julias-cameo-Unique_Amulet_103_x1'
    type = 'amulet'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Prevent all Arcane damage taken and heal yourself for 22% of the amount prevented.
	[20 - 25]%
    """


class Rakoffs_Glass_of_Life(Item):
    """ Rakoff's Glass of Life """
    url = r'/en/item/rakoffs-glass-of-life-Unique_Amulet_108_x1'
    type = 'amulet'
    text = """

	Health Globes and Potions Grant +[20,001 - 29,713] Life.
	 Enemies you kill have a 3% additional chance to drop a health globe.
	[3 - 4]%
    """


class The_Ess_of_Johan(Item):
    """ The Ess of Johan """
    url = r'/en/item/the-ess-of-johan-Unique_Amulet_104_x1'
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Chance on hit to pull in enemies toward your target and Slow them by 60%.
	[60 - 80]%
    """


class Haunt_of_Vaxo(Item):
    """ Haunt of Vaxo """
    url = r'/en/item/haunt-of-vaxo-Unique_Amulet_101_x1'
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Summons shadow clones to your aid when you Stun an enemy. This effect may occur once every 30 seconds.
	30
    """


class The_Flavor_of_Time(Item):
    """ The Flavor of Time """
    url = r'/en/item/the-flavor-of-time-P66_Unique_Amulet_001'
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.

	+[10 - 12]% Movement Speed
	 Pylon effects last twice as long.
    """


class Kymbos_Gold(Item):
    """ Kymbo's Gold """
    url = r'/en/item/kymbos-gold-Unique_Amulet_002_p1'
    type = 'amulet'
    text = """
	 Picking up gold heals you for an amount equal to the gold that was picked up.
    """


class The_Travelers_Pledge(Item):
    """ The Traveler's Pledge """
    url = r'/en/item/the-travelers-pledge-Unique_Amulet_008_x1'
    type = 'amulet'
    text = """
	(2) Set:      While moving, damage taken is reduced by up to 50%.     While standing still, damage dealt is increased by up to 100%.
    """


class Tal_Rashas_Allegiance(Item):
    """ Tal Rasha's Allegiance """
    url = r'/en/item/tal-rashas-allegiance-Unique_Amulet_007_x1'
    type = 'amulet'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Maras_Kaleidoscope(Item):
    """ Mara's Kaleidoscope """
    url = r'/en/item/maras-kaleidoscope-Unique_Amulet_015_x1'
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Prevent all Poison damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class Blackthornes_Duncraig_Cross(Item):
    """ Blackthorne's Duncraig Cross """
    url = r'/en/item/blackthornes-duncraig-cross-Unique_Amulet_016_x1'
    type = 'amulet'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class The_Star_of_Azkaranth(Item):
    """ The Star of Azkaranth """
    url = r'/en/item/the-star-of-azkaranth-Unique_Amulet_006_x1'
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Prevent all Fire damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class Xephirian_Amulet(Item):
    """ Xephirian Amulet """
    url = r'/en/item/xephirian-amulet-Unique_Amulet_004_x1'
    type = 'amulet'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Prevent all Lightning damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class The_Johnstone(Item):
    """ The Johnstone """
    url = r'/en/item/the-johnstone-P6_Unique_Amulet_01'
    type = 'amulet'
    text = """

	Critical Hit Damage Increased by [51.0 - 100.0]% 
	 When Land of the Dead expires, you are granted 50 stacks of Macabre Knowledge. Macabre Knowledge increases the damage of Corpse Lance and Corpse Explosion by 179%.
	(Necromancer Only)
	[150 - 200]%
    """


class Halcyons_Ascent(Item):
    """ Halcyon's Ascent """
    url = r'/en/item/halcyons-ascent-Unique_Amulet_109_x1_210'
    type = 'amulet'
    text = """

	Sockets (1)
    """


class Haunted_Visions(Item):
    """ Haunted Visions """
    url = r'/en/item/haunted-visions-P6_Unique_Amulet_02'
    type = 'amulet'
    text = """

	Sockets (1)
	 Simulacrum now drains 5% of your maximum life every second and lasts twice as long.
	(Necromancer Only)
	5%
    """


class Sunwukos_Shines(Item):
    """ Sunwuko's Shines """
    url = r'/en/item/sunwukos-shines-Unique_Amulet_Set_11_x1'
    type = 'amulet'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Talisman_of_Akkhan(Item):
    """ Talisman of Akkhan """
    url = r'/en/item/talisman-of-akkhan-P43_AkkhanSet_Amulet'
    type = 'amulet'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Leorics_Crown(Item):
    """ Leoric's Crown """
    url = r'/en/item/leorics-crown-Unique_Helm_002_p1'
    type = 'helm'
    text = """

	Sockets (1)

	Increase the effect of any gem socketed into this item by [75 - 100]%. This effect does not apply to Legendary Gems.
    """


class Prides_Fall(Item):
    """ Pride's Fall """
    url = r'/en/item/prides-fall-Unique_Helm_103_x1'
    type = 'helm'
    text = """

	+[626 - 750] Vitality

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your resource costs are reduced by 30% after not taking damage for 5 seconds.
    """


class Broken_Crown(Item):
    """ Broken Crown """
    url = r'/en/item/broken-crown-P2_Unique_Helm_001'
    type = 'helm'
    text = """

	Sockets (1)
	 Whenever a gem drops, a gem of the type socketed into your helmet also drops. This effect does not apply to Legendary Gems.
    """


class Cains_Memory(Item):
    """ Cain's Memory """
    url = r'/en/artisan/blacksmith/recipe/cains-memory'
    type = 'helm'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Deathseers_Cowl(Item):
    """ Deathseer's Cowl """
    url = r'/en/item/deathseers-cowl-Unique_Helm_102_x1'
    type = 'helm'
    text = """

	Sockets (1)
	 19% chance on being hit by an Undead enemy to charm it for 2 seconds.
	[15 - 20]%
    """


class Warhelm_of_Kassar(Item):
    """ Warhelm of Kassar """
    url = r'/en/item/warhelm-of-kassar-P4_Unique_Helm_102'
    type = 'helm'
    text = """

	Sockets (1)
	 Reduce the cooldown and increase the damage of Phalanx by 49%.
	(Crusader Only)
	[45 - 60]%
    """


class Visage_of_Gunes(Item):
    """ Visage of Gunes """
    url = r'/en/item/visage-of-gunes-P4_Unique_Helm_103'
    type = 'helm'
    text = """

	Sockets (1)
	 Vengeance gains the effect of the Dark Heart rune.
	(Demon Hunter Only)
    """


class Mask_of_Scarlet_Death(Item):
    """ Mask of Scarlet Death """
    url = r'/en/item/mask-of-scarlet-death-P6_Necro_Unique_Helm_21'
    type = 'helm'
    text = """

	Sockets (1)
	 Revive now consumes all corpses to raise a minion that deals 135% more damage per corpse.
	(Necromancer Only)
	[125 - 150]%
    """


class Aughilds_Peak(Item):
    """ Aughild's Peak """
    url = r'/en/artisan/blacksmith/recipe/aughilds-peak'
    type = 'helm'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Skull_of_Resonance(Item):
    """ Skull of Resonance """
    url = r'/en/item/skull-of-resonance-Unique_Helm_004_x1'
    type = 'helm'
    text = """

	+[91 - 100] Resistance to All Elements

	Sockets (1)
	 Threatening Shout has a chance to Charm enemies and cause them to join your side.
	(Barbarian Only)
    """


class Guardians_Foresight(Item):
    """ Guardian's Foresight """
    url = r'/en/artisan/blacksmith/recipe/guardians-foresight'
    type = 'helm'
    text = """
	(2) Set:      +110 Vitality     Regenerates 130 Life per Second
    """


class Mempo_of_Twilight(Item):
    """ Mempo of Twilight """
    url = r'/en/item/mempo-of-twilight-Unique_Helm_006_x1'
    type = 'helm'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[91 - 100] Resistance to All Elements

	Sockets (1)
    """


class Natalyas_Sight(Item):
    """ Natalya's Sight """
    url = r'/en/item/natalyas-sight-Unique_Helm_009_x1'
    type = 'helm'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Tal_Rashas_Guise_of_Wisdom(Item):
    """ Tal Rasha's Guise of Wisdom """
    url = r'/en/item/tal-rashas-guise-of-wisdom-Unique_Helm_010_x1'
    type = 'helm'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Sages_Orbit(Item):
    """ Sage's Orbit """
    url = r'/en/artisan/blacksmith/recipe/sages-orbit'
    type = 'helm'
    text = """
	(2) Set:      +35 Strength     +35 Dexterity     +35 Intelligence     +35 Vitality
    """


class Immortal_Kings_Triumph(Item):
    """ Immortal King's Triumph """
    url = r'/en/item/immortal-kings-triumph-Unique_Helm_008_x1'
    type = 'helm'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Andariels_Visage(Item):
    """ Andariel's Visage """
    url = r'/en/item/andariels-visage-Unique_Helm_003_p2'
    type = 'helm'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	[5 - 10]% more Fire damage taken.

	+[150 - 200] Poison Resistance
	 Attacks release a Poison Nova that deals 380% weapon damage as Poison to enemies within 10 yards.
	[350 - 450]%
    """


class Fates_Vow(Item):
    """ Fate's Vow """
    url = r'/en/item/fates-vow-P61_Necro_Unique_Helm_22'
    type = 'helm'
    text = """

	Sockets (1)
	 Army of the Dead deals an additional 207% damage and gains the effect of the Unconventional Warfare rune.
	(Necromancer Only)
	[200 - 250]%
    """


class Jade_Harvesters_Wisdom(Item):
    """ Jade Harvester's Wisdom """
    url = r'/en/item/jade-harvesters-wisdom-Unique_Helm_Set_09_x1'
    type = 'helm'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Guardians_Gaze(Item):
    """ Guardian's Gaze """
    url = r'/en/artisan/blacksmith/recipe/guardians-gaze'
    type = 'helm'
    text = """
	(2) Set:      +250 Vitality     Regenerates 8000 Life per Second
	(3) Set:      +15% Movement Speed
    """


class Sunwukos_Crown(Item):
    """ Sunwuko's Crown """
    url = r'/en/item/sunwukos-crown-Unique_Helm_Set_11_x1'
    type = 'helm'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Sages_Apogee(Item):
    """ Sage's Apogee """
    url = r'/en/artisan/blacksmith/recipe/sages-apogee'
    type = 'helm'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Vyrs_Sightless_Skull(Item):
    """ Vyr's Sightless Skull """
    url = r'/en/item/vyrs-sightless-skull-Unique_Helm_Set_13_x1'
    type = 'helm'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Cains_Insight(Item):
    """ Cain's Insight """
    url = r'/en/artisan/blacksmith/recipe/cains-insight'
    type = 'helm'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class Crown_of_the_Invoker(Item):
    """ Crown of the Invoker """
    url = r'/en/item/crown-of-the-invoker-Unique_Helm_Set_12_x1'
    type = 'helm'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Aughilds_Spike(Item):
    """ Aughild's Spike """
    url = r'/en/artisan/blacksmith/recipe/aughilds-spike'
    type = 'helm'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class The_Shadows_Mask(Item):
    """ The Shadow's Mask """
    url = r'/en/item/the-shadows-mask-Unique_Helm_Set_14_x1'
    type = 'helm'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Eyes_of_the_Earth(Item):
    """ Eyes of the Earth """
    url = r'/en/item/eyes-of-the-earth-Unique_Helm_Set_15_x1'
    type = 'helm'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Raekors_Will(Item):
    """ Raekor's Will """
    url = r'/en/item/raekors-will-Unique_Helm_Set_05_x1'
    type = 'helm'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Helm_of_the_Wastes(Item):
    """ Helm of the Wastes """
    url = r'/en/item/helm-of-the-wastes-Unique_Helm_Set_01_p2'
    type = 'helm'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Skull_of_Savages(Item):
    """ Skull of Savages """
    url = r'/en/item/skull-of-savages-P68_Unique_Helm_Set_05'
    type = 'helm'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Crown_of_the_Light(Item):
    """ Crown of the Light """
    url = r'/en/item/crown-of-the-light-Unique_Helm_Set_03_p3'
    type = 'helm'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Crown_of_Valor(Item):
    """ Crown of Valor """
    url = r'/en/item/crown-of-valor-P67_Unique_Helm_Set_01'
    type = 'helm'
    set = Aegis_of_Valor
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Rolands_Visage(Set_Item):
    """ Roland's Visage """
    url = r'/en/item/rolands-visage-Unique_Helm_Set_01_p1'
    type = 'helm'
    set = Rolands_Legacy
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Helm_of_Akkhan(Item):
    """ Helm of Akkhan """
    url = r'/en/item/helm-of-akkhan-Unique_Helm_Set_10_x1'
    type = 'helm'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Accursed_Visage(Item):
    """ Accursed Visage """
    url = r'/en/item/accursed-visage-Unique_Helm_Set_03_p2'
    type = 'helm'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Visage(Item):
    """ Marauder's Visage """
    url = r'/en/item/marauders-visage-Unique_Helm_Set_07_x1'
    type = 'helm'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Mask_of_the_Searing_Sky(Item):
    """ Mask of the Searing Sky """
    url = r'/en/item/mask-of-the-searing-sky-Unique_Helm_Set_08_x1'
    type = 'helm'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Ulianas_Spirit(Item):
    """ Uliana's Spirit """
    url = r'/en/item/ulianas-spirit-Unique_Helm_Set_01_p3'
    type = 'helm'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Decree_of_Justice(Item):
    """ Decree of Justice """
    url = r'/en/item/decree-of-justice-P67_Unique_Helm_Set_02'
    type = 'helm'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Firebirds_Plume(Item):
    """ Firebird's Plume """
    url = r'/en/item/firebirds-plume-Unique_Helm_Set_06_x1'
    type = 'helm'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Shrouded_Mask(Item):
    """ Shrouded Mask """
    url = r'/en/item/shrouded-mask-Unique_Helm_Set_02_p2'
    type = 'helm'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Typhons_Frons(Item):
    """ Typhon's Frons """
    url = r'/en/item/typhons-frons-P68_Unique_Helm_Set_03'
    type = 'helm'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Arachyrs_Visage(Item):
    """ Arachyr's Visage """
    url = r'/en/item/arachyrs-visage-Unique_Helm_Set_02_p3'
    type = 'helm'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Helltooth_Mask(Item):
    """ Helltooth Mask """
    url = r'/en/item/helltooth-mask-Unique_Helm_Set_16_x1'
    type = 'helm'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class TragOuls_Guise(Item):
    """ Trag'Oul's Guise """
    url = r'/en/item/tragouls-guise-P6_Necro_Set_2_Helm'
    type = 'helm'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Inariuss_Understanding(Item):
    """ Inarius's Understanding """
    url = r'/en/item/inariuss-understanding-P6_Necro_Set_3_Helm'
    type = 'helm'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Pestilence_Mask(Set_Item):
    """ Pestilence Mask """
    url = r'/en/item/pestilence-mask-P6_Necro_Set_4_Helm'
    type = 'helm'
    set = Pestilence_Battle
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Rathmas_Skull_Helm(Item):
    """ Rathma's Skull Helm """
    url = r'/en/item/rathmas-skull-helm-P6_Necro_Set_1_Helm'
    type = 'helm'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Homing_Pads(Item):
    """ Homing Pads """
    url = r'/en/item/homing-pads-Unique_Shoulder_001_x1'
    type = 'shoulders'
    text = """

	+[32 - 35]% Extra Gold from Monsters
	 Your Town Portal is no longer interrupted by taking damage. While casting Town Portal you gain a protective bubble that reduces damage taken by 54%.
	[50 - 65]%
    """


class Pauldrons_of_the_Skeleton_King(Item):
    """ Pauldrons of the Skeleton King """
    url = r'/en/item/pauldrons-of-the-skeleton-king-Unique_Shoulder_103_x1'
    type = 'shoulders'
    text = """

	+[416 - 500] Vitality

	+[373 - 397] Armor
	 When receiving fatal damage, there is a chance that you are instead restored to 25% of maximum Life and cause nearby enemies to flee in fear.
    """


class Razeths_Volition(Item):
    """ Razeth's Volition """
    url = r'/en/item/razeths-volition-P6_Necro_Unique_Shoulders_22'
    type = 'shoulders'
    text = """

	Reduces all resource costs by [5.0 - 8.0]%.
	 Skeletal Mage gains the effect of the Gift of Death rune.
	(Necromancer Only)
    """


class Borns_Impunity(Item):
    """ Born's Impunity """
    url = r'/en/artisan/blacksmith/recipe/borns-impunity'
    type = 'shoulders'
    text = """
	(2) Set:      +2% Life     +20% Experience. (2.0% at level 70)
    """


class Death_Watch_Mantle(Item):
    """ Death Watch Mantle """
    url = r'/en/item/death-watch-mantle-Unique_Shoulder_002_p2'
    type = 'shoulders'
    text = """
	 30% chance to explode in a fan of knives for 750-950% weapon damage when hit.
	[25 - 35]%
    """


class Corpsewhisper_Pauldrons(Item):
    """ Corpsewhisper Pauldrons """
    url = r'/en/item/corpsewhisper-pauldrons-P6_Necro_Unique_Shoulders_21'
    type = 'shoulders'
    text = """
	 Corpse Lance damage is increased by 29% for 3 seconds when you consume a corpse. Max 20 stacks.
	(Necromancer Only)
	[25 - 30]%
    """


class Lefebvres_Soliloquy(Item):
    """ Lefebvre's Soliloquy """
    url = r'/en/item/lefebvres-soliloquy-P4_Unique_Shoulder_101'
    type = 'shoulders'
    text = """
	 Cyclone Strike reduces your damage taken by 45% for 5 seconds.
	(Monk Only)
	[40 - 50]%
    """


class Mantle_of_Channeling(Item):
    """ Mantle of Channeling """
    url = r'/en/item/mantle-of-channeling-P4_Unique_Shoulder_103'
    type = 'shoulders'
    text = """

	+[416 - 500] Vitality
	 While channeling Whirlwind, Rapid Fire, Strafe, Tempest Rush, Firebats, Arcane Torrent, Disintegrate, or Ray of Frost for at least 1 second, you deal 24% increased damage and take 25% reduced damage.
	[20 - 25]%
    """


class Spaulders_of_Zakara(Item):
    """ Spaulders of Zakara """
    url = r'/en/item/spaulders-of-zakara-Unique_Shoulder_102_x1'
    type = 'shoulders'
    text = """
	 Your items become indestructible.
    """


class Fury_of_the_Ancients(Item):
    """ Fury of the Ancients """
    url = r'/en/item/fury-of-the-ancients-P67_Unique_Shoulder_102'
    type = 'shoulders'
    text = """
	 Call of the Ancients gains the effect of the Ancients' Fury rune, and your Ancients attack 100% faster.
	(Barbarian Only)
    """


class Aughilds_Reign(Item):
    """ Aughild's Reign """
    url = r'/en/artisan/blacksmith/recipe/aughilds-reign'
    type = 'shoulders'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Ashearas_Guard(Item):
    """ Asheara's Guard """
    url = r'/en/artisan/blacksmith/recipe/ashearas-guard'
    type = 'shoulders'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Vile_Ward(Item):
    """ Vile Ward """
    url = r'/en/item/vile-ward-Unique_Shoulder_003_p1'
    type = 'shoulders'
    text = """
	 Furious Charge deals 34% increased damage for every enemy hit while charging.
	(Barbarian Only)
	[30 - 35]%
    """


class Seven_Sins(Item):
    """ Seven Sins """
    url = r'/en/artisan/blacksmith/recipe/seven-sins'
    type = 'shoulders'
    text = """

	+[121 - 135] Strength

	+[121 - 135] Dexterity

	+[121 - 135] Intelligence

	+[121 - 135] Vitality

	+[81 - 100] Arcane Resistance
    """


class Demons_Flight(Item):
    """ Demon's Flight """
    url = r'/en/artisan/blacksmith/recipe/demons-flight'
    type = 'shoulders'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Burden_of_the_Invoker(Item):
    """ Burden of the Invoker """
    url = r'/en/item/burden-of-the-invoker-Unique_Shoulder_Set_12_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Spires_of_the_Earth(Item):
    """ Spires of the Earth """
    url = r'/en/item/spires-of-the-earth-Unique_Shoulder_Set_15_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Demons_Aileron(Item):
    """ Demon's Aileron """
    url = r'/en/artisan/blacksmith/recipe/demons-aileron'
    type = 'shoulders'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Aughilds_Power(Item):
    """ Aughild's Power """
    url = r'/en/artisan/blacksmith/recipe/aughilds-power'
    type = 'shoulders'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class Sunwukos_Balance(Item):
    """ Sunwuko's Balance """
    url = r'/en/item/sunwukos-balance-Unique_Shoulder_Set_11_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Corruption(Item):
    """ Corruption """
    url = r'/en/artisan/blacksmith/recipe/corruption'
    type = 'shoulders'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.

	Health Globes and Potions Grant +[14,231 - 20,000] Life.
    """


class Jade_Harvesters_Joy(Item):
    """ Jade Harvester's Joy """
    url = r'/en/item/jade-harvesters-joy-Unique_Shoulder_Set_09_x1'
    type = 'shoulders'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Borns_Privilege(Item):
    """ Born's Privilege """
    url = r'/en/artisan/blacksmith/recipe/borns-privilege'
    type = 'shoulders'
    text = """
	(2) Set:      +15% Life
	(3) Set:      Reduces cooldown of all skills by 10.0%.     +20% Experience. (2.0% at level 70)
    """


class Ashearas_Custodian(Item):
    """ Asheara's Custodian """
    url = r'/en/artisan/blacksmith/recipe/ashearas-custodian'
    type = 'shoulders'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class Vyrs_Proud_Pauldrons(Item):
    """ Vyr's Proud Pauldrons """
    url = r'/en/item/vyrs-proud-pauldrons-Unique_Shoulder_Set_13_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class The_Shadows_Burden(Item):
    """ The Shadow's Burden """
    url = r'/en/item/the-shadows-burden-Unique_Shoulder_Set_14_x1'
    type = 'shoulders'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Spines_of_Savages(Item):
    """ Spines of Savages """
    url = r'/en/item/spines-of-savages-P68_Unique_Shoulder_Set_05'
    type = 'shoulders'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Raekors_Burden(Item):
    """ Raekor's Burden """
    url = r'/en/item/raekors-burden-Unique_Shoulder_Set_05_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Pauldrons_of_the_Wastes(Item):
    """ Pauldrons of the Wastes """
    url = r'/en/item/pauldrons-of-the-wastes-Unique_Shoulder_Set_01_p2'
    type = 'shoulders'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Spaulders_of_Valor(Set_Item):
    """ Spaulders of Valor """
    url = r'/en/item/spaulders-of-valor-P67_Unique_Shoulder_Set_01'
    type = 'shoulders'
    set = Aegis_of_Valor
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Rolands_Mantle(Set_Item):
    """ Roland's Mantle """
    url = r'/en/item/rolands-mantle-Unique_Shoulder_Set_01_p1'
    type = 'shoulders'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Mountain_of_the_Light(Set_Item):
    """ Mountain of the Light """
    url = r'/en/item/mountain-of-the-light-Unique_Shoulder_Set_03_p3'
    type = 'shoulders'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Pauldrons_of_Akkhan(Set_Item):
    """ Pauldrons of Akkhan """
    url = r'/en/item/pauldrons-of-akkhan-Unique_Shoulder_Set_10_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Unsanctified_Shoulders(Item):
    """ Unsanctified Shoulders """
    url = r'/en/item/unsanctified-shoulders-Unique_Shoulder_Set_03_p2'
    type = 'shoulders'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Spines(Item):
    """ Marauder's Spines """
    url = r'/en/item/marauders-spines-Unique_Shoulder_Set_07_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Mantle_of_the_Upside_Down_Sinners(Item):
    """ Mantle of the Upside-Down Sinners """
    url = r'/en/item/mantle-of-the-upsidedown-sinners-Unique_Shoulder_Set_08_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Ulianas_Strength(Item):
    """ Uliana's Strength """
    url = r'/en/item/ulianas-strength-Unique_Shoulder_Set_01_p3'
    type = 'shoulders'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Mirrors_of_Justice(Item):
    """ Mirrors of Justice """
    url = r'/en/item/mirrors-of-justice-P67_Unique_Shoulder_Set_02'
    type = 'shoulders'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Dashing_Pauldrons_of_Despair(Item):
    """ Dashing Pauldrons of Despair """
    url = r'/en/item/dashing-pauldrons-of-despair-Unique_Shoulder_Set_02_p2'
    type = 'shoulders'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Firebirds_Pinions(Item):
    """ Firebird's Pinions """
    url = r'/en/item/firebirds-pinions-Unique_Shoulder_Set_06_x1'
    type = 'shoulders'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Typhons_Tibia(Item):
    """ Typhon's Tibia """
    url = r'/en/item/typhons-tibia-P68_Unique_Shoulder_Set_03'
    type = 'shoulders'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Mundunugus_Descendant(Item):
    """ Mundunugu's Descendant """
    url = r'/en/item/mundunugus-descendant-P68_Unique_Shoulder_Set_04'
    type = 'shoulders'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Helltooth_Mantle(Item):
    """ Helltooth Mantle """
    url = r'/en/item/helltooth-mantle-Unique_Shoulder_Set_16_x1'
    type = 'shoulders'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Mantle(Item):
    """ Arachyr's Mantle """
    url = r'/en/item/arachyrs-mantle-Unique_Shoulder_Set_02_p3'
    type = 'shoulders'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Pestilence_Defense(Item):
    """ Pestilence Defense """
    url = r'/en/item/pestilence-defense-P6_Necro_Set_4_Shoulders'
    type = 'shoulders'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Rathmas_Spikes(Item):
    """ Rathma's Spikes """
    url = r'/en/item/rathmas-spikes-P6_Necro_Set_1_Shoulders'
    type = 'shoulders'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class TragOuls_Heart(Item):
    """ Trag'Oul's Heart """
    url = r'/en/item/tragouls-heart-P6_Necro_Set_2_Shoulders'
    type = 'shoulders'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Inariuss_Martyrdom(Item):
    """ Inarius's Martyrdom """
    url = r'/en/item/inariuss-martyrdom-P6_Necro_Set_3_Shoulders'
    type = 'shoulders'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Heart_of_Iron(Item):
    """ Heart of Iron """
    url = r'/en/item/heart-of-iron-P4_Unique_Chest_018'
    type = 'torso'
    text = """

	+[416 - 500] Vitality

	+[5334 - 7696] Thorns Damage
	 Gain Thorns equal to 257% of your Vitality.
	[250 - 300]%
    """


class Borns_Heart_of_Steel(Item):
    """ Born's Heart of Steel """
    url = r'/en/artisan/blacksmith/recipe/borns-heart-of-steel'
    type = 'torso'
    text = """
	(2) Set:      +2% Life     +20% Experience. (2.0% at level 70)
    """


class Aquila_Cuirass(Item):
    """ Aquila Cuirass """
    url = r'/en/item/aquila-cuirass-P4_Unique_Chest_012'
    type = 'torso'
    text = """

	Sockets (3)
	 While above 94% primary resource, all damage taken is reduced by 50%.
	[90 - 95]%
    """


class Chaingmail(Item):
    """ Chaingmail """
    url = r'/en/item/chaingmail-Unique_Chest_010_x1'
    type = 'torso'
    text = """

	+[91 - 100] Resistance to All Elements
	 After earning a survival bonus, quickly heal to full Life.
    """


class Shi_Mizus_Haori(Item):
    """ Shi Mizu's Haori """
    url = r'/en/item/shi-mizus-haori-Unique_Chest_101_x1'
    type = 'torso'
    text = """
	 While below 24% Life, all attacks are guaranteed Critical Hits.
	[20 - 25]%
    """


class Cindercoat(Item):
    """ Cindercoat """
    url = r'/en/item/cindercoat-Unique_Chest_006_x1'
    type = 'torso'
    text = """

	Fire skills deal [15 - 20]% more damage.
	 Reduces the resource cost of Fire skills by 27%.
	[23 - 30]%
    """


class Aughilds_Dominion(Item):
    """ Aughild's Dominion """
    url = r'/en/artisan/blacksmith/recipe/aughilds-dominion'
    type = 'torso'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Goldskin(Item):
    """ Goldskin """
    url = r'/en/item/goldskin-Unique_Chest_001_x1'
    type = 'torso'
    text = """

	+[91 - 100] Resistance to All Elements

	+100% Extra Gold from Monsters
	 Chance for enemies to drop gold when you hit them.
    """


class Zunimassas_Marrow(Item):
    """ Zunimassa's Marrow """
    url = r'/en/item/zunimassas-marrow-Unique_Chest_016_x1'
    type = 'torso'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Immortal_Kings_Eternal_Reign(Item):
    """ Immortal King's Eternal Reign """
    url = r'/en/item/immortal-kings-eternal-reign-Unique_Chest_013_x1'
    type = 'torso'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Blackthornes_Surcoat(Item):
    """ Blackthorne's Surcoat """
    url = r'/en/item/blackthornes-surcoat-Unique_ChestArmor_028_x1'
    type = 'torso'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Demons_Heart(Item):
    """ Demon's Heart """
    url = r'/en/artisan/blacksmith/recipe/demons-heart'
    type = 'torso'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Tal_Rashas_Relentless_Pursuit(Item):
    """ Tal Rasha's Relentless Pursuit """
    url = r'/en/item/tal-rashas-relentless-pursuit-Unique_Chest_014_x1'
    type = 'torso'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Tyraels_Might(Item):
    """ Tyrael's Might """
    url = r'/en/item/tyraels-might-Unique_Chest_002_x1'
    type = 'torso'
    text = """

	+[91 - 100] Resistance to All Elements

	+[10 - 20]% Damage to Demons

	Ignores Durability Loss
    """


class Innas_Vast_Expanse(Item):
    """ Inna's Vast Expanse """
    url = r'/en/item/innas-vast-expanse-Unique_Chest_015_x1'
    type = 'torso'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Robes_of_the_Rydraelm(Item):
    """ Robes of the Rydraelm """
    url = r'/en/artisan/blacksmith/recipe/robes-of-the-rydraelm'
    type = 'torso'
    text = """

	Reduces damage from ranged attacks by 4.0%.

	Reduces damage from melee attacks by 4.0%

	Monster kills grant +[80 - 99] experience.
    """


class Bloodsong_Mail(Item):
    """ Bloodsong Mail """
    url = r'/en/item/bloodsong-mail-P6_Necro_Unique_Chest_21'
    type = 'torso'
    text = """

	Sockets (3)
	 While in the Land of the Dead, Command Skeletons deals 110% additional damage and gains the effect of the Enforcer, Frenzy, Dark Mending and Freezing Grasp runes.
	(Necromancer Only)
	[100 - 125]%
    """


class Jade_Harvesters_Peace(Item):
    """ Jade Harvester's Peace """
    url = r'/en/item/jade-harvesters-peace-Unique_Chest_Set_09_x1'
    type = 'torso'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Demons_Marrow(Item):
    """ Demon's Marrow """
    url = r'/en/artisan/blacksmith/recipe/demons-marrow'
    type = 'torso'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Aughilds_Rule(Item):
    """ Aughild's Rule """
    url = r'/en/artisan/blacksmith/recipe/aughilds-rule'
    type = 'torso'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class Armor_of_the_Kind_Regent(Item):
    """ Armor of the Kind Regent """
    url = r'/en/item/armor-of-the-kind-regent-Unique_Chest_102_x1'
    type = 'torso'
    text = """
	 Smite will now also be cast at a second nearby enemy.
	(Crusader Only)
    """


class Spirit_of_the_Earth(Item):
    """ Spirit of the Earth """
    url = r'/en/item/spirit-of-the-earth-Unique_Chest_Set_15_x1'
    type = 'torso'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Borns_Frozen_Soul(Item):
    """ Born's Frozen Soul """
    url = r'/en/artisan/blacksmith/recipe/borns-frozen-soul'
    type = 'torso'
    text = """
	(2) Set:      +15% Life
	(3) Set:      Reduces cooldown of all skills by 10.0%.     +20% Experience. (2.0% at level 70)
    """


class The_Shadows_Bane(Item):
    """ The Shadow's Bane """
    url = r'/en/item/the-shadows-bane-Unique_Chest_Set_14_x1'
    type = 'torso'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Sunwukos_Soul(Item):
    """ Sunwuko's Soul """
    url = r'/en/item/sunwukos-soul-Unique_Chest_Set_11_x1'
    type = 'torso'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Vyrs_Astonishing_Aura(Item):
    """ Vyr's Astonishing Aura """
    url = r'/en/item/vyrs-astonishing-aura-Unique_Chest_Set_13_x1'
    type = 'torso'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Cuirass_of_the_Wastes(Item):
    """ Cuirass of the Wastes """
    url = r'/en/item/cuirass-of-the-wastes-Unique_Chest_Set_01_p2'
    type = 'torso'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Markings_of_Savages(Item):
    """ Markings of Savages """
    url = r'/en/item/markings-of-savages-P68_Unique_Chest_Set_05'
    type = 'torso'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Raekors_Heart(Set_Item):
    """ Raekor's Heart """
    url = r'/en/item/raekors-heart-Unique_Chest_Set_05_x1'
    type = 'torso'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Rolands_Bearing(Set_Item):
    """ Roland's Bearing """
    url = r'/en/item/rolands-bearing-Unique_Chest_Set_01_p1'
    type = 'torso'
    set = Rolands_Legacy
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Breastplate_of_Akkhan(Set_Item):
    """ Breastplate of Akkhan """
    url = r'/en/item/breastplate-of-akkhan-Unique_Chest_Set_10_x1'
    type = 'torso'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Heart_of_the_Light(Set_Item):
    """ Heart of the Light """
    url = r'/en/item/heart-of-the-light-Unique_Chest_Set_03_p3'
    type = 'torso'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Brigandine_of_Valor(Set_Item):
    """ Brigandine of Valor """
    url = r'/en/item/brigandine-of-valor-P67_Unique_Chest_Set_01'
    type = 'torso'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Marauders_Carapace(Set_Item):
    """ Marauder's Carapace """
    url = r'/en/item/marauders-carapace-Unique_Chest_Set_07_x1'
    type = 'torso'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Heart_of_the_Crashing_Wave(Set_Item):
    """ Heart of the Crashing Wave """
    url = r'/en/item/heart-of-the-crashing-wave-Unique_Chest_Set_08_x1'
    type = 'torso'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Ulianas_Heart(Set_Item):
    """ Uliana's Heart """
    url = r'/en/item/ulianas-heart-Unique_Chest_Set_01_p3'
    type = 'torso'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Lamellars_of_Justice(Set_Item):
    """ Lamellars of Justice """
    url = r'/en/item/lamellars-of-justice-P67_Unique_Chest_Set_02'
    type = 'torso'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Firebirds_Breast(Set_Item):
    """ Firebird's Breast """
    url = r'/en/item/firebirds-breast-Unique_Chest_Set_06_x1'
    type = 'torso'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Typhons_Thorax(Set_Item):
    """ Typhon's Thorax """
    url = r'/en/item/typhons-thorax-P68_Unique_Chest_Set_03'
    type = 'torso'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Harness_of_Truth(Set_Item):
    """ Harness of Truth """
    url = r'/en/item/harness-of-truth-Unique_Chest_Set_02_p2'
    type = 'torso'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Mundunugus_Robe(Set_Item):
    """ Mundunugu's Robe """
    url = r'/en/item/mundunugus-robe-P68_Unique_Chest_Set_04'
    type = 'torso'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Helltooth_Tunic(Set_Item):
    """ Helltooth Tunic """
    url = r'/en/item/helltooth-tunic-Unique_Chest_Set_16_x1'
    type = 'torso'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Carapace(Item):
    """ Arachyr's Carapace """
    url = r'/en/item/arachyrs-carapace-Unique_Chest_Set_02_p3'
    type = 'torso'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class TragOuls_Scales(Item):
    """ Trag'Oul's Scales """
    url = r'/en/item/tragouls-scales-P6_Necro_Set_2_Chest'
    type = 'torso'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Rathmas_Ribcage_Plate(Item):
    """ Rathma's Ribcage Plate """
    url = r'/en/item/rathmas-ribcage-plate-P6_Necro_Set_1_Chest'
    type = 'torso'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Pestilence_Robe(Item):
    """ Pestilence Robe """
    url = r'/en/item/pestilence-robe-P6_Necro_Set_4_Chest'
    type = 'torso'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Inariuss_Conviction(Item):
    """ Inarius's Conviction """
    url = r'/en/item/inariuss-conviction-P6_Necro_Set_3_Chest'
    type = 'torso'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Requiem_Cereplate(Item):
    """ Requiem Cereplate """
    url = r'/en/item/requiem-cereplate-P6_Necro_Unique_Chest_22'
    type = 'torso'
    text = """

	Sockets (3)
	 Devour restores an additional 85% Essence and Life. In addition, when Devour restores Essence or Life above your maximum, the excess is granted over 3 seconds.
	(Necromancer Only)
	[75 - 100]%
    """


class Ashnagarrs_Blood_Bracer(Item):
    """ Ashnagarr's Blood Bracer """
    url = r'/en/item/ashnagarrs-blood-bracer-P4_Unique_Bracer_004'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Increases the potency of your shields by 85%.
	(Wizard Only)
	[75 - 100]%
    """


class Gungdo_Gear(Item):
    """ Gungdo Gear """
    url = r'/en/item/gungdo-gear-P2_Unique_Bracer_006'
    type = 'wrists'
    text = """
	 Exploding Palm's on-death explosion applies Exploding Palm.
	(Monk Only)
    """


class Cesars_Memento(Item):
    """ Cesar's Memento """
    url = r'/en/item/cesars-memento-P61_Unique_Bracer_107'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Enemies take 667% increased damage from your Tempest Rush for 5 seconds after you hit them with a Blind, Freeze, or Stun.
	(Monk Only)
	[600 - 800]%
    """


class Sanguinary_Vambraces(Item):
    """ Sanguinary Vambraces """
    url = r'/en/item/sanguinary-vambraces-Unique_Bracer_105_x1'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[2401 - 2880] Thorns Damage
	 Chance on being hit to deal 1000% of your Thorns damage to nearby enemies.
    """


class Pintos_Pride(Item):
    """ Pinto's Pride """
    url = r'/en/item/pintos-pride-P4_Unique_Bracer_105'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Wave of Light also Slows enemies by 80% for 3 seconds and deals 135% increased damage.
	(Monk Only)
	[125 - 150]%
    """


class Bindings_of_the_Lesser_Gods(Item):
    """ Bindings of the Lesser Gods """
    url = r'/en/item/bindings-of-the-lesser-gods-P4_Unique_Bracer_108'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Enemies hit by your Cyclone Strike take 157% increased damage from your Mystic Ally for 5 seconds.
	(Monk Only)
	[150 - 200]%
    """


class Akkhans_Manacles(Item):
    """ Akkhan's Manacles """
    url = r'/en/item/akkhans-manacles-P4_Unique_Bracer_103'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Blessed Shield damage is increased by 442% for the first enemy it hits.
	(Crusader Only)
	[400 - 500]%
    """


class Morticks_Brace(Item):
    """ Mortick's Brace """
    url = r'/en/item/morticks-brace-P2_Unique_Bracer_003'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Wrath of the Berserker gains the effect of every rune.
	(Barbarian Only)
    """


class Vambraces_of_Sescheron(Item):
    """ Vambraces of Sescheron """
    url = r'/en/item/vambraces-of-sescheron-P4_Unique_Bracer_106'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your primary skills heal you for 5.5% of your missing Life.
	(Barbarian Only)
	[5.0 - 6.0]%
    """


class Bracer_of_Fury(Item):
    """ Bracer of Fury """
    url = r'/en/item/bracer-of-fury-P61_Unique_Bracer_104'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Heaven's Fury deals 342% increased damage to enemies that are Blinded, Immobilized, or Stunned.
	(Crusader Only)
	[300 - 400]%
    """


class Warzechian_Armguards(Item):
    """ Warzechian Armguards """
    url = r'/en/item/warzechian-armguards-Unique_Bracer_101_x1'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Every time you destroy a wreckable object, you gain a short burst of speed.
    """


class Nemesis_Bracers(Item):
    """ Nemesis Bracers """
    url = r'/en/item/nemesis-bracers-Unique_Bracer_106_x1'
    type = 'wrists'
    text = """
	 Shrines and Pylons will spawn an enemy champion.
    """


class Custerian_Wristguards(Item):
    """ Custerian Wristguards """
    url = r'/en/item/custerian-wristguards-Unique_Bracer_107_x1'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[32 - 35]% Extra Gold from Monsters
	 Picking up gold grants experience.
    """


class Ancient_Parthan_Defenders(Item):
    """ Ancient Parthan Defenders """
    url = r'/en/item/ancient-parthan-defenders-Unique_Bracer_102_x1'
    type = 'wrists'
    text = """
	 Each stunned enemy within 25 yards reduces your damage taken by 9%.
	[9 - 12]%
    """


class Aughilds_Ultimatum(Item):
    """ Aughild's Ultimatum """
    url = r'/en/artisan/blacksmith/recipe/aughilds-ultimatum'
    type = 'wrists'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Promise_of_Glory(Item):
    """ Promise of Glory """
    url = r'/en/item/promise-of-glory-Unique_Bracer_002_x1'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 5% chance to spawn a Nephalem Glory globe when you Blind an enemy.
	[4 - 6]%
    """


class Guardians_Deflector(Item):
    """ Guardian's Deflector """
    url = r'/en/artisan/blacksmith/recipe/guardians-deflector'
    type = 'wrists'
    text = """
	(2) Set:      +110 Vitality     Regenerates 130 Life per Second
    """


class Wondrous_Deflectors(Item):
    """ Wondrous Deflectors """
    url = r'/en/artisan/blacksmith/recipe/wondrous-deflectors'
    type = 'wrists'
    text = """

	Regenerates [1128 - 2842] Life per Second

	Reduces damage from ranged attacks by 4.0%.

	+[316 - 1160] Thorns Damage
    """


class Strongarm_Bracers(Item):
    """ Strongarm Bracers """
    url = r'/en/item/strongarm-bracers-Unique_Bracer_007_x1'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[416 - 500] Vitality
	 Enemies hit by knockbacks suffer 25% increased damage for 6 seconds.
	[20 - 30]%
    """


class Demons_Revenge(Item):
    """ Demon's Revenge """
    url = r'/en/artisan/blacksmith/recipe/demons-revenge'
    type = 'wrists'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Lacuni_Prowlers(Item):
    """ Lacuni Prowlers """
    url = r'/en/item/lacuni-prowlers-Unique_Bracer_005_x1'
    type = 'wrists'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[10 - 12]% Movement Speed

	+[2401 - 2880] Thorns Damage
    """


class Coils_of_the_First_Spider(Item):
    """ Coils of the First Spider """
    url = r'/en/item/coils-of-the-first-spider-P3_Unique_Bracer_107'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Regenerates [6448 - 7678] Life per Second
	 While channeling Firebats, you gain 30% damage reduction and 71,752 Life per Hit.
	(Witch Doctor Only)
	[60,000 - 80,000]
    """


class Wraps_of_Clarity(Item):
    """ Wraps of Clarity """
    url = r'/en/item/wraps-of-clarity-P61_Unique_Bracer_103'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your Hatred Generators reduce your damage taken by 45% for 5 seconds.
	(Demon Hunter Only)
	[40 - 50]%
    """


class Jerams_Bracers(Item):
    """ Jeram's Bracers """
    url = r'/en/item/jerams-bracers-P3_Unique_Bracer_106'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Wall of Death deals 85% increased damage and can be cast up to three times within 2 seconds before the cooldown begins.
	(Witch Doctor Only)
	[75 - 100]%
    """


class Bracers_of_the_First_Men(Item):
    """ Bracers of the First Men """
    url = r'/en/item/bracers-of-the-first-men-P61_Unique_Bracer_105'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Hammer of the Ancients attacks 50% faster and deals 445% increased damage.
	(Barbarian Only)
	[375 - 500]%
    """


class Ranslors_Folly(Item):
    """ Ranslor's Folly """
    url = r'/en/item/ranslors-folly-P61_Unique_Bracer_108_x1'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 The damage of Energy Twister is increased by 249% and it periodically pulls in lesser enemies within 30 yards.
	(Wizard Only)
	[225 - 300]%
    """


class Guardians_Aversion(Item):
    """ Guardian's Aversion """
    url = r'/en/artisan/blacksmith/recipe/guardians-aversion'
    type = 'wrists'
    text = """
	(2) Set:      +250 Vitality     Regenerates 8000 Life per Second
	(3) Set:      +15% Movement Speed
    """


class Bracers_of_Destruction(Item):
    """ Bracers of Destruction """
    url = r'/en/item/bracers-of-destruction-P67_Unique_Bracer_100'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Seismic Slam deals 442% increased damage to the first 10 enemies it hits.
	(Barbarian Only)
	[400 - 500]%
    """


class Gabriels_Vambraces(Item):
    """ Gabriel's Vambraces """
    url = r'/en/item/gabriels-vambraces-P3_Unique_Bracer_101'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 When your Blessed Hammer hits 3 or fewer enemies, 85% of its Wrath Cost is refunded.
	(Crusader Only)
	[75 - 100]%
    """


class TragOul_Coils(Item):
    """ Trag'Oul Coils """
    url = r'/en/item/tragoul-coils-P42_Unique_Bracer_SpikeTrap'
    type = 'wrists'
    text = """
	 Spike Traps gain the Impaling Spines rune and are deployed twice as fast.
	(Demon Hunter Only)
    """


class Drakons_Lesson(Item):
    """ Drakon's Lesson """
    url = r'/en/item/drakons-lesson-P4_Unique_Bracer_110'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 When your Shield Bash hits 3 or fewer enemies, its damage is increased by 342% and 25% of its Wrath Cost is refunded.
	(Crusader Only)
	[300 - 400]%
    """


class Aughilds_Search(Item):
    """ Aughild's Search """
    url = r'/en/artisan/blacksmith/recipe/aughilds-search'
    type = 'wrists'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class Shackles_of_the_Invoker(Item):
    """ Shackles of the Invoker """
    url = r'/en/item/shackles-of-the-invoker-Unique_Bracer_Set_12_x1'
    type = 'wrists'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Krelms_Buff_Bracers(Item):
    """ Krelm's Buff Bracers """
    url = r'/en/item/krelms-buff-bracers-Unique_Bracer_Set_02_x1'
    type = 'wrists'
    text = """
	(2) Set:      +500 Vitality
    """


class Reapers_Wraps(Item):
    """ Reaper's Wraps """
    url = r'/en/artisan/blacksmith/recipe/reapers-wraps'
    type = 'wrists'
    text = """

	Health globes restore [25 - 30]% of your primary resource.
    """


class Demons_Animus(Item):
    """ Demon's Animus """
    url = r'/en/artisan/blacksmith/recipe/demons-animus'
    type = 'wrists'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Lakumbas_Ornament(Item):
    """ Lakumba's Ornament """
    url = r'/en/item/lakumbas-ornament-P4_Unique_Bracer_102'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Reduce all damage taken by 6% for each stack of Soul Harvest you have.
	(Witch Doctor Only)
	6%
    """


class Spirit_Guards(Item):
    """ Spirit Guards """
    url = r'/en/item/spirit-guards-P61_Unique_Bracer_109'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your Spirit Generators reduce your damage taken by 49% for 3 seconds.
	(Monk Only)
	[45 - 60]%
    """


class Skulars_Salvation(Item):
    """ Skular's Salvation """
    url = r'/en/item/skulars-salvation-P4_Unique_Bracer_101'
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Increase the damage of Ancient Spear - Boulder Toss by 100%. When your Boulder Toss hits 5 or fewer enemies, the damage is increased by 145%.
	(Barbarian Only)
	[120 - 150]%
    """


class Gloves_of_Worship(Item):
    """ Gloves of Worship """
    url = r'/en/item/gloves-of-worship-Unique_Gloves_103_x1'
    type = 'hands'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 

	+[7737 - 9214] Life per Hit
	 Shrine effects last for 10 minutes.
    """


class Grasps_of_Essence(Item):
    """ Grasps of Essence """
    url = r'/en/item/grasps-of-essence-P6_Necro_Unique_Gloves_22'
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 When an exploded corpse damages at least one enemy, your Corpse Explosion deals 85% increased damage for 6 seconds, stacking up to 5 times.
	(Necromancer Only)
	[75 - 100]%
    """


class Cains_Scribe(Item):
    """ Cain's Scribe """
    url = r'/en/artisan/blacksmith/recipe/cains-scribe'
    type = 'hands'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Stone_Gauntlets(Item):
    """ Stone Gauntlets """
    url = r'/en/item/stone-gauntlets-P66_Unique_Gloves_007'
    type = 'hands'
    text = """
	 Getting hit increases your armor by 50%, but reduces your movement speed by 15% and attack speed by 20%. This effect stacks up to 5 times.
    """


class St_Archews_Gage(Item):
    """ St. Archew's Gage """
    url = r'/en/item/st-archews-gage-Unique_Gloves_101_p2'
    type = 'hands'
    text = """
	 The first time an elite pack damages you, gain an absorb shield equal to 145% of your maximum Life for 10 seconds.
	[120 - 150]%
    """


class Magefist(Item):
    """ Magefist """
    url = r'/en/item/magefist-P41_Unique_Gloves_014'
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Fire skills deal 19% increased damage.
	[15 - 20]%
    """


class Pendergrasps(Item):
    """ Pendergrasps """
    url = r'/en/artisan/blacksmith/recipe/pendergrasps'
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [4.0 - 5.0]%

	Reduces duration of control impairing effects by [7 - 12]%
    """


class Moribund_Gauntlets(Item):
    """ Moribund Gauntlets """
    url = r'/en/item/moribund-gauntlets-P6_Necro_Unique_Gloves_21'
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Your Golem sheds a corpse every second.
	(Necromancer Only)
    """


class Gladiator_Gauntlets(Item):
    """ Gladiator Gauntlets """
    url = r'/en/item/gladiator-gauntlets-Unique_Gloves_011_x1'
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 After earning a massacre bonus, gold rains from sky.
    """


class Ashearas_Iron_Fist(Item):
    """ Asheara's Iron Fist """
    url = r'/en/artisan/blacksmith/recipe/ashearas-iron-fist'
    type = 'hands'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Zunimassas_Finger_Wraps(Item):
    """ Zunimassa's Finger Wraps """
    url = r'/en/item/zunimassas-finger-wraps-P2_Unique_Gloves_03'
    type = 'hands'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Sages_Gesture(Item):
    """ Sage's Gesture """
    url = r'/en/artisan/blacksmith/recipe/sages-gesture'
    type = 'hands'
    text = """
	(2) Set:      +35 Strength     +35 Dexterity     +35 Intelligence     +35 Vitality
    """


class Frostburn(Item):
    """ Frostburn """
    url = r'/en/item/frostburn-P41_Unique_Gloves_002'
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Cold skills deal 19% increased damage and have a 50% chance to Freeze enemies.
	[15 - 20]%
    """


class Tasker_and_Theo(Item):
    """ Tasker and Theo """
    url = r'/en/item/tasker-and-theo-Unique_Gloves_003_x1'
    type = 'hands'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Increase attack speed of your pets by 45%.
	[40 - 50]%
    """


class Natalyas_Touch(Item):
    """ Natalya's Touch """
    url = r'/en/item/natalyas-touch-P2_Unique_Gloves_01'
    type = 'hands'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Immortal_Kings_Irons(Item):
    """ Immortal King's Irons """
    url = r'/en/item/immortal-kings-irons-Unique_Gloves_008_x1'
    type = 'hands'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Innas_Hold(Item):
    """ Inna's Hold """
    url = r'/en/item/innas-hold-P2_Unique_Gloves_04'
    type = 'hands'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Tal_Rashas_Grasp(Item):
    """ Tal Rasha's Grasp """
    url = r'/en/item/tal-rashas-grasp-P2_Unique_Gloves_02'
    type = 'hands'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Cains_Scrivener(Item):
    """ Cain's Scrivener """
    url = r'/en/artisan/blacksmith/recipe/cains-scriviner'
    type = 'hands'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class The_Shadows_Grasp(Item):
    """ The Shadow's Grasp """
    url = r'/en/item/the-shadows-grasp-Unique_Gloves_Set_14_x1'
    type = 'hands'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Sunwukos_Paws(Item):
    """ Sunwuko's Paws """
    url = r'/en/item/sunwukos-paws-Unique_Gloves_Set_11_x1'
    type = 'hands'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Ashearas_Ward(Item):
    """ Asheara's Ward """
    url = r'/en/artisan/blacksmith/recipe/ashearas-ward'
    type = 'hands'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class Pride_of_the_Invoker(Item):
    """ Pride of the Invoker """
    url = r'/en/item/pride-of-the-invoker-Unique_Gloves_Set_12_x1'
    type = 'hands'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Jade_Harvesters_Mercy(Item):
    """ Jade Harvester's Mercy """
    url = r'/en/item/jade-harvesters-mercy-Unique_Gloves_Set_09_x1'
    type = 'hands'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Pull_of_the_Earth(Item):
    """ Pull of the Earth """
    url = r'/en/item/pull-of-the-earth-Unique_Gloves_Set_15_x1'
    type = 'hands'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Vyrs_Grasping_Gauntlets(Item):
    """ Vyr's Grasping Gauntlets """
    url = r'/en/item/vyrs-grasping-gauntlets-Unique_Gloves_Set_13_x1'
    type = 'hands'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Sages_Purchase(Item):
    """ Sage's Purchase """
    url = r'/en/artisan/blacksmith/recipe/sages-purchase'
    type = 'hands'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Raekors_Wraps(Item):
    """ Raekor's Wraps """
    url = r'/en/item/raekors-wraps-Unique_Gloves_Set_05_x1'
    type = 'hands'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Gauntlet_of_the_Wastes(Item):
    """ Gauntlet of the Wastes """
    url = r'/en/item/gauntlet-of-the-wastes-Unique_Gloves_Set_01_p2'
    type = 'hands'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Claws_of_Savages(Item):
    """ Claws of Savages """
    url = r'/en/item/claws-of-savages-P68_Unique_Gloves_Set_05'
    type = 'hands'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Gauntlets_of_Valor(Item):
    """ Gauntlets of Valor """
    url = r'/en/item/gauntlets-of-valor-P67_Unique_Gloves_Set_01'
    type = 'hands'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Rolands_Grasp(Set_Item):
    """ Roland's Grasp """
    url = r'/en/item/rolands-grasp-Unique_Gloves_Set_01_p1'
    type = 'hands'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Gauntlets_of_Akkhan(Item):
    """ Gauntlets of Akkhan """
    url = r'/en/item/gauntlets-of-akkhan-Unique_Gloves_Set_10_x1'
    type = 'hands'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Will_of_the_Light(Item):
    """ Will of the Light """
    url = r'/en/item/will-of-the-light-Unique_Gloves_Set_03_p3'
    type = 'hands'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Fiendish_Grips(Item):
    """ Fiendish Grips """
    url = r'/en/item/fiendish-grips-Unique_Gloves_Set_03_p2'
    type = 'hands'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Gloves(Item):
    """ Marauder's Gloves """
    url = r'/en/item/marauders-gloves-Unique_Gloves_Set_07_x1'
    type = 'hands'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Bazubands_of_Justice(Item):
    """ Bazubands of Justice """
    url = r'/en/item/bazubands-of-justice-P67_Unique_Gloves_Set_02'
    type = 'hands'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Ulianas_Fury(Item):
    """ Uliana's Fury """
    url = r'/en/item/ulianas-fury-Unique_Gloves_Set_01_p3'
    type = 'hands'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Fists_of_Thunder(Item):
    """ Fists of Thunder """
    url = r'/en/item/fists-of-thunder-Unique_Gloves_Set_08_x1'
    type = 'hands'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Fierce_Gauntlets(Item):
    """ Fierce Gauntlets """
    url = r'/en/item/fierce-gauntlets-Unique_Gloves_Set_02_p2'
    type = 'hands'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Typhons_Claws(Item):
    """ Typhon's Claws """
    url = r'/en/item/typhons-claws-P68_Unique_Gloves_Set_03'
    type = 'hands'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Firebirds_Talons(Item):
    """ Firebird's Talons """
    url = r'/en/item/firebirds-talons-Unique_Gloves_Set_06_x1'
    type = 'hands'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Arachyrs_Claws(Item):
    """ Arachyr's Claws """
    url = r'/en/item/arachyrs-claws-Unique_Gloves_Set_02_p3'
    type = 'hands'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Mundunugus_Rhythm(Item):
    """ Mundunugu's Rhythm """
    url = r'/en/item/mundunugus-rhythm-P68_Unique_Gloves_Set_04'
    type = 'hands'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Helltooth_Gauntlets(Item):
    """ Helltooth Gauntlets """
    url = r'/en/item/helltooth-gauntlets-Unique_Gloves_Set_16_x1'
    type = 'hands'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Inariuss_Will(Item):
    """ Inarius's Will """
    url = r'/en/item/inariuss-will-P6_Necro_Set_3_Gloves'
    type = 'hands'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Rathmas_Macabre_Vambraces(Item):
    """ Rathma's Macabre Vambraces """
    url = r'/en/item/rathmas-macabre-vambraces-P6_Necro_Set_1_Gloves'
    type = 'hands'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Pestilence_Gloves(Item):
    """ Pestilence Gloves """
    url = r'/en/item/pestilence-gloves-P6_Necro_Set_4_Gloves'
    type = 'hands'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class TragOuls_Claws(Item):
    """ Trag'Oul's Claws """
    url = r'/en/item/tragouls-claws-P6_Necro_Set_2_Gloves'
    type = 'hands'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Saffron_Wrap(Item):
    """ Saffron Wrap """
    url = r'/en/item/saffron-wrap-P43_Unique_Belt_001_x1'
    type = 'waist'
    text = """
	 The damage of your next Overpower is increased by 45% for each enemy hit. Max 20 enemies.
	(Barbarian Only)
	[40 - 50]%
    """


class Goldwrap(Item):
    """ Goldwrap """
    url = r'/en/item/goldwrap-Unique_Belt_010_x1'
    type = 'waist'
    text = """

	+[32 - 35]% Extra Gold from Monsters
	 On gold pickup: Gain armor for 5 seconds equal to the amount picked up.
    """


class Hellcat_Waistguard(Item):
    """ Hellcat Waistguard """
    url = r'/en/item/hellcat-waistguard-P43_Unique_Belt_005_x1'
    type = 'waist'
    text = """
	 Grenades have a chance to bounce 4 times dealing an additional 50% damage on each bounce. This bonus is increased to 800% on the final bounce.
	(Demon Hunter Only)
	[3 - 5]
    """


class Insatiable_Belt(Item):
    """ Insatiable Belt """
    url = r'/en/item/insatiable-belt-Unique_Belt_103_x1'
    type = 'waist'
    text = """

	+[416 - 500] Vitality

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Picking up a Health Globe increases your maximum Life by 5% for 15 seconds, stacking up to 5 times.
    """


class Binding_of_the_Lost(Item):
    """ Binding of the Lost """
    url = r'/en/item/binding-of-the-lost-P61_Unique_Belt_03'
    type = 'waist'
    text = """
	 Each hit with Seven-Sided Strike grants 4.0% damage reduction for 7 seconds.
	(Monk Only)
	[4.0 - 5.0]%
    """


class The_Shame_of_Delsere(Item):
    """ The Shame of Delsere """
    url = r'/en/item/the-shame-of-delsere-P4_Unique_Belt_02'
    type = 'waist'
    text = """
	 Your Signature Spells attack 50% faster and restore 9 Arcane Power.
	(Wizard Only)
	[9 - 12]
    """


class Dayntees_Binding(Item):
    """ Dayntee's Binding """
    url = r'/en/item/dayntees-binding-P61_Unique_Belt_01'
    type = 'waist'
    text = """
	 You gain an additional 45% damage reduction when there is an enemy afflicted by any of your curses.
	(Necromancer Only)
	[40 - 50]%
    """


class Kyoshiros_Soul(Item):
    """ Kyoshiro's Soul """
    url = r'/en/item/kyoshiros-soul-P4_Unique_Belt_05'
    type = 'waist'
    text = """
	 Increases Sweeping Wind Damage by [100 - 125]%
	 Sweeping Wind gains 2 stacks every second it does not deal damage to any enemies.
	(Monk Only)
	2
    """


class Sacred_Harness(Item):
    """ Sacred Harness """
    url = r'/en/item/sacred-harness-P3_Unique_Belt_01'
    type = 'waist'
    text = """
	 Judgment gains the effect of the Debilitate rune and is cast at your landing location when casting Falling Sword.
	(Crusader Only)
    """


class Quick_Draw_Belt(Item):
    """ Quick Draw Belt """
    url = r'/en/artisan/blacksmith/recipe/quick-draw-belt'
    type = 'waist'
    text = """

	Attack Speed Increased by [3.0 - 4.0]%

	+[13 - 21] Thorns Damage
    """


class String_of_Ears(Item):
    """ String of Ears """
    url = r'/en/item/string-of-ears-P4_Unique_Belt_03'
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Reduces damage from melee attacks by 29%.
	[25 - 30]%
    """


class Bakuli_Jungle_Wraps(Item):
    """ Bakuli Jungle Wraps """
    url = r'/en/item/bakuli-jungle-wraps-P61_Unique_Belt_007'
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Firebats deals 257% increased damage to enemies affected by Locust Swarm or Piranhas.
	(Witch Doctor Only)
	[250 - 300]%
    """


class Saffron_Wrap(Item):
    """ Saffron Wrap """
    url = r'/en/item/saffron-wrap-Unique_Belt_001_x1'
    type = 'waist'
    text = """

	Reduces all resource costs by [5.0 - 8.0]%.

	Reduces duration of control impairing effects by [20 - 40]%
    """


class Captain_Crimsons_Satin_Sash(Item):
    """ Captain Crimson's Satin Sash """
    url = r'/en/artisan/blacksmith/recipe/captain-crimsons-satin-sash'
    type = 'waist'
    text = """
	(2) Set:      Regenerates 20 Life per Second
	(3) Set:      +20 Resistance to All Elements
    """


class Fazulas_Improbable_Chain(Item):
    """ Fazula's Improbable Chain """
    url = r'/en/item/fazulas-improbable-chain-P4_Unique_Belt_07'
    type = 'waist'
    text = """
	 You automatically start with 45 Archon stacks when entering Archon form.
	(Wizard Only)
	[40 - 50]
    """


class Hergbrashs_Binding(Item):
    """ Hergbrash's Binding """
    url = r'/en/item/hergbrashs-binding-P4_Unique_Belt_06'
    type = 'waist'
    text = """
	 Reduces the Arcane Power cost of Arcane Torrent, Disintegrate, and Ray of Frost by 54%.
	(Wizard Only)
	[50 - 65]%
    """


class Sebors_Nightmare(Item):
    """ Sebor's Nightmare """
    url = r'/en/item/sebors-nightmare-Unique_Belt_108_p2'
    type = 'waist'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Haunt is cast on all nearby enemies when you open a chest.
    """


class Sash_of_Knives(Item):
    """ Sash of Knives """
    url = r'/en/item/sash-of-knives-Unique_Belt_102_p2'
    type = 'waist'
    text = """
	 With every attack, you throw a dagger at a nearby enemy for 622% weapon damage as Physical.
	[500 - 650]%
    """


class Omnislash(Item):
    """ Omnislash """
    url = r'/en/item/omnislash-P2_Unique_Belt_04'
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Slash attacks in all directions.
	(Crusader Only)
    """


class Haunting_Girdle(Item):
    """ Haunting Girdle """
    url = r'/en/item/haunting-girdle-P2_Unique_Belt_03'
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Haunt releases 1 extra spirit.
	(Witch Doctor Only)
	1
    """


class Sebors_Nightmare(Item):
    """ Sebor's Nightmare """
    url = r'/en/item/sebors-nightmare-Unique_Belt_108_x1'
    type = 'waist'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Haunt is cast on 5 nearby enemies when you open a chest.
    """


class Hwoj_Wrap(Item):
    """ Hwoj Wrap """
    url = r'/en/item/hwoj-wrap-Unique_Belt_107_x1'
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Locust Swarm also Slows enemies by 60%.
	(Witch Doctor Only)
	[60 - 80]%
    """


class Omryns_Chain(Item):
    """ Omryn's Chain """
    url = r'/en/item/omryns-chain-P2_Unique_Belt_06'
    type = 'waist'
    text = """
	 Drop Caltrops when using Vault.
	(Demon Hunter Only)
    """


class Cord_of_the_Sherma(Item):
    """ Cord of the Sherma """
    url = r'/en/item/cord-of-the-sherma-Unique_Belt_104_p2'
    type = 'waist'
    text = """

	+[416 - 500] Vitality

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Chance on hit to create a chaos field that Blinds and Slows enemies inside for 3 seconds.
	[3 - 4]
    """


class Harrington_Waistguard(Item):
    """ Harrington Waistguard """
    url = r'/en/item/harrington-waistguard-Unique_Belt_105_x1'
    type = 'waist'
    text = """

	+[32 - 35]% Extra Gold from Monsters
	 Opening a chest grants 116% increased damage for 10 seconds.
	[100 - 135]%
    """


class Crashing_Rain(Item):
    """ Crashing Rain """
    url = r'/en/item/crashing-rain-P2_Unique_Belt_01'
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Rain of Vengeance also summons a crashing beast that deals 3049% weapon damage.
	(Demon Hunter Only)
	[3000 - 4000]%
    """


class Chain_of_Shadows(Item):
    """ Chain of Shadows """
    url = r'/en/item/chain-of-shadows-P4_Unique_Belt_01'
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 After using Impale, Vault costs no resource for 2 seconds.
	(Demon Hunter Only)
    """


class Cord_of_the_Sherma(Item):
    """ Cord of the Sherma """
    url = r'/en/item/cord-of-the-sherma-Unique_Belt_104_x1'
    type = 'waist'
    text = """

	+[416 - 500] Vitality

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Chance on hit to create a chaos field that Blinds and Slows enemies inside for 3 seconds.
	[2 - 4]
    """


class Blessed_of_Haull(Item):
    """ Blessed of Haull """
    url = r'/en/item/blessed-of-haull-P2_Unique_Belt_05'
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Justice spawns a Blessed Hammer when it hits an enemy.
	(Crusader Only)
    """


class Belt_of_Transcendence(Item):
    """ Belt of Transcendence """
    url = r'/en/item/belt-of-transcendence-P2_Unique_Belt_02'
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Summon a Fetish Sycophant when you hit with a Mana spender.
	(Witch Doctor Only)
    """


class Razor_Strop(Item):
    """ Razor Strop """
    url = r'/en/item/razor-strop-Unique_Belt_101_x1'
    type = 'waist'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Picking up a Health Globe releases an explosion that deals 342% weapon damage as Fire to enemies within 20 yards.
	[300 - 400]%
    """


class Angel_Hair_Braid(Item):
    """ Angel Hair Braid """
    url = r'/en/item/angel-hair-braid-Unique_Belt_003_x1'
    type = 'waist'
    text = """

	+11% Chance to Block

	Ignores Durability Loss
    """


class Thundergods_Vigor(Item):
    """ Thundergod's Vigor """
    url = r'/en/item/thundergods-vigor-Unique_BarbBelt_003_x1'
    type = 'waist'
    text = """

	Lightning skills deal [10 - 15]% more damage.

	+[416 - 500] Vitality

	+[150 - 200] Lightning Resistance
	 Blocking, dodging or being hit causes you to discharge bolts of electricity that deal 129% weapon damage as Lightning.
	[100 - 130]%
    """


class Angel_Hair_Braid(Item):
    """ Angel Hair Braid """
    url = r'/en/item/angel-hair-braid-Unique_Belt_003_p1'
    type = 'waist'
    text = """
	 Punish gains the effect of every rune.
	(Crusader Only)
    """


class Guardians_Sheath(Item):
    """ Guardian's Sheath """
    url = r'/en/artisan/blacksmith/recipe/guardians-sheath'
    type = 'waist'
    text = """
	(2) Set:      +110 Vitality     Regenerates 130 Life per Second
    """


class Belt_of_the_Trove(Item):
    """ Belt of the Trove """
    url = r'/en/item/belt-of-the-trove-P2_Unique_Belt_008'
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements

	Reduces damage from melee attacks by [6.0 - 7.0]%
	 Every 7 seconds, call down Bombardment on a random nearby enemy.
	(Crusader Only)
	[6 - 8]
    """


class Innas_Favor(Item):
    """ Inna's Favor """
    url = r'/en/item/innas-favor-Unique_Belt_007_x1'
    type = 'waist'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Tal_Rashas_Brace(Item):
    """ Tal Rasha's Brace """
    url = r'/en/item/tal-rashas-brace-Unique_Belt_006_x1'
    type = 'waist'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Demons_Lock(Item):
    """ Demon's Lock """
    url = r'/en/artisan/blacksmith/recipe/demons-lock'
    type = 'waist'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Blackthornes_Notched_Belt(Item):
    """ Blackthorne's Notched Belt """
    url = r'/en/item/blackthornes-notched-belt-Unique_Belt_015_x1'
    type = 'waist'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Jangs_Envelopment(Item):
    """ Jang's Envelopment """
    url = r'/en/item/jangs-envelopment-Unique_Belt_106_x1'
    type = 'waist'
    text = """
	 Enemies damaged by Black Hole are also slowed by 60% for 3 seconds.
	(Wizard Only)
	[60 - 80]%
    """


class Sages_Ribbon(Item):
    """ Sage's Ribbon """
    url = r'/en/artisan/blacksmith/recipe/sages-ribbon'
    type = 'waist'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Demons_Restraint(Item):
    """ Demon's Restraint """
    url = r'/en/artisan/blacksmith/recipe/demons-restraint'
    type = 'waist'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Khassetts_Cord_of_Righteousness(Item):
    """ Khassett's Cord of Righteousness """
    url = r'/en/item/khassetts-cord-of-righteousness-P42_Crusader_FoH_Belt'
    type = 'waist'
    text = """
	 Fist of the Heavens costs 40% less Wrath and deals 163% more damage.
	(Crusader Only)
	[130 - 170]%
    """


class Zoeys_Secret(Item):
    """ Zoey's Secret """
    url = r'/en/item/zoeys-secret-P4_Unique_Belt_04'
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 You take 8.5% less damage for every Companion you have active.
	(Demon Hunter Only)
	[8.0 - 9.0]%
    """


class Krelms_Buff_Belt(Item):
    """ Krelm's Buff Belt """
    url = r'/en/item/krelms-buff-belt-Unique_Belt_Set_02_x1'
    type = 'waist'
    text = """
	(2) Set:      +500 Vitality
    """


class Guardians_Case(Item):
    """ Guardian's Case """
    url = r'/en/artisan/blacksmith/recipe/guardians-case'
    type = 'waist'
    text = """
	(2) Set:      +250 Vitality     Regenerates 8000 Life per Second
	(3) Set:      +15% Movement Speed
    """


class Captain_Crimsons_Silk_Girdle(Item):
    """ Captain Crimson's Silk Girdle """
    url = r'/en/artisan/blacksmith/recipe/captain-crimsons-silk-girdle'
    type = 'waist'
    text = """
	(2) Set:      Regenerates 6000 Life per Second     Reduces cooldown of all skills by 20.0%.     Reduces all resource costs by 20.0%.
	(3) Set:      Damage dealt is increased by your percentage of cooldown reduction.     Damage taken is reduced by your percentage of cost reduction.
    """


class Hunters_Wrath(Item):
    """ Hunter's Wrath """
    url = r'/en/item/hunters-wrath-P3_Unique_Belt_005'
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Your primary skills attack 30% faster and deal 49% increased damage.
	(Demon Hunter Only)
	[45 - 60]%
    """


class Pox_Faulds(Item):
    """ Pox Faulds """
    url = r'/en/item/pox-faulds-Unique_Pants_007_p2'
    type = 'pants'
    text = """
	 When 3 or more enemies are within 12 yards, you release a vile stench that deals 492% weapon damage as Poison every second for 5 seconds to enemies within 15 yards.
	[450 - 550]%
    """


class Deaths_Bargain(Item):
    """ Death's Bargain """
    url = r'/en/item/deaths-bargain-Unique_Pants_102_x1'
    type = 'pants'
    text = """

	Regenerates [4643 - 5528] Life per Second
	 Gain an aura of death that deals 792% of your Life per Second as Physical damage to enemies within 16 yards. You no longer regenerate Life.
	[750 - 1000]%
    """


class Cains_Robes(Item):
    """ Cain's Robes """
    url = r'/en/artisan/blacksmith/recipe/cains-robes'
    type = 'pants'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Golemskin_Breeches(Item):
    """ Golemskin Breeches """
    url = r'/en/item/golemskin-breeches-P61_Necro_Unique_Pants_21'
    type = 'pants'
    text = """

	Sockets (2)
	 The cooldown on Command Golem is reduced by 24 seconds and you take 30% less damage while your golem is alive.
	(Necromancer Only)
	[20 - 25]
    """


class Hammer_Jammers(Item):
    """ Hammer Jammers """
    url = r'/en/item/hammer-jammers-P4_Unique_Pants_002'
    type = 'pants'
    text = """

	Sockets (2)
	 Enemies take 342% increased damage from your Blessed Hammers for 10 seconds after you hit them with a Blind, Immobilize, or Stun.
	(Crusader Only)
	[300 - 400]%
    """


class Captain_Crimsons_Bowsprit(Item):
    """ Captain Crimson's Bowsprit """
    url = r'/en/artisan/blacksmith/recipe/captain-crimsons-bowsprit'
    type = 'pants'
    text = """
	(2) Set:      Regenerates 20 Life per Second
	(3) Set:      +20 Resistance to All Elements
    """


class Hexing_Pants_of_Mr_Yan(Item):
    """ Hexing Pants of Mr. Yan """
    url = r'/en/item/hexing-pants-of-mr-yan-Unique_Pants_101_x1'
    type = 'pants'
    text = """
	 Your resource generation and damage is increased by 25% while moving and decreased by 24% while standing still.
	[20 - 25]%
    """


class Defiler_Cuisses(Item):
    """ Defiler Cuisses """
    url = r'/en/item/defiler-cuisses-P61_Necro_Unique_Pants_22'
    type = 'pants'
    text = """

	Sockets (2)
	 Your Bone Spirit's damage is increased by 442% for every second it is active.
	(Necromancer Only)
	[400 - 500]%
    """


class Swamp_Land_Waders(Item):
    """ Swamp Land Waders """
    url = r'/en/item/swamp-land-waders-P41_Unique_Pants_001'
    type = 'pants'
    text = """

	Sockets (2)
	 Sacrifice deals 342% additional damage against enemies affected by Locust Swarm or Grasp of the Dead.
	(Witch Doctor Only)
	[300 - 400]%
    """


class Ashearas_Gait(Item):
    """ Asheara's Gait """
    url = r'/en/artisan/blacksmith/recipe/ashearas-gait'
    type = 'pants'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Tal_Rashas_Stride(Item):
    """ Tal Rasha's Stride """
    url = r'/en/item/tal-rashas-stride-P2_Unique_Pants_03'
    type = 'pants'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Depth_Diggers(Item):
    """ Depth Diggers """
    url = r'/en/item/depth-diggers-Unique_Pants_006_p1'
    type = 'pants'
    text = """

	+[91 - 100] Resistance to All Elements
	 Primary skills that generate resource deal 87% additional damage.
	[80 - 100]%
    """


class Zunimassas_Cloth(Item):
    """ Zunimassa's Cloth """
    url = r'/en/item/zunimassas-cloth-P2_Unique_Pants_04'
    type = 'pants'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Immortal_Kings_Stature(Item):
    """ Immortal King's Stature """
    url = r'/en/item/immortal-kings-stature-P2_Unique_Pants_02'
    type = 'pants'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Demons_Scale(Item):
    """ Demon's Scale """
    url = r'/en/artisan/blacksmith/recipe/demons-scale'
    type = 'pants'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Gehennas(Item):
    """ Gehennas """
    url = r'/en/artisan/blacksmith/recipe/gehennas'
    type = 'pants'
    text = """

	+[410 - 446] Armor

	+[81 - 100] Fire Resistance
    """


class Innas_Temperance(Item):
    """ Inna's Temperance """
    url = r'/en/item/innas-temperance-Unique_Pants_008_x1'
    type = 'pants'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Natalyas_Leggings(Item):
    """ Natalya's Leggings """
    url = r'/en/item/natalyas-leggings-P2_Unique_Pants_01'
    type = 'pants'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Blackthornes_Jousting_Mail(Item):
    """ Blackthorne's Jousting Mail """
    url = r'/en/item/blackthornes-jousting-mail-Unique_Pants_013_x1'
    type = 'pants'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Demons_Plate(Item):
    """ Demon's Plate """
    url = r'/en/artisan/blacksmith/recipe/demons-plate'
    type = 'pants'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Captain_Crimsons_Thrust(Item):
    """ Captain Crimson's Thrust """
    url = r'/en/artisan/blacksmith/recipe/captain-crimsons-thrust'
    type = 'pants'
    text = """
	(2) Set:      Regenerates 6000 Life per Second     Reduces cooldown of all skills by 20.0%.     Reduces all resource costs by 20.0%.
	(3) Set:      Damage dealt is increased by your percentage of cooldown reduction.     Damage taken is reduced by your percentage of cost reduction.
    """


class Renewal_of_the_Invoker(Item):
    """ Renewal of the Invoker """
    url = r'/en/item/renewal-of-the-invoker-Unique_Pants_Set_12_x1'
    type = 'pants'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Jade_Harvesters_Courage(Item):
    """ Jade Harvester's Courage """
    url = r'/en/item/jade-harvesters-courage-Unique_Pants_Set_09_x1'
    type = 'pants'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Vyrs_Fantastic_Finery(Item):
    """ Vyr's Fantastic Finery """
    url = r'/en/item/vyrs-fantastic-finery-Unique_Pants_Set_13_x1'
    type = 'pants'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Sunwukos_Leggings(Item):
    """ Sunwuko's Leggings """
    url = r'/en/item/sunwukos-leggings-Unique_Pants_Set_11_x1'
    type = 'pants'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Cains_Habit(Item):
    """ Cain's Habit """
    url = r'/en/artisan/blacksmith/recipe/cains-habit'
    type = 'pants'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class The_Shadows_Coil(Item):
    """ The Shadow's Coil """
    url = r'/en/item/the-shadows-coil-Unique_Pants_Set_14_x1'
    type = 'pants'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Weight_of_the_Earth(Item):
    """ Weight of the Earth """
    url = r'/en/item/weight-of-the-earth-Unique_Pants_Set_15_x1'
    type = 'pants'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Ashearas_Pace(Item):
    """ Asheara's Pace """
    url = r'/en/artisan/blacksmith/recipe/ashearas-pace'
    type = 'pants'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class Raekors_Breeches(Item):
    """ Raekor's Breeches """
    url = r'/en/item/raekors-breeches-Unique_Pants_Set_05_x1'
    type = 'pants'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Tasset_of_the_Wastes(Item):
    """ Tasset of the Wastes """
    url = r'/en/item/tasset-of-the-wastes-Unique_Pants_Set_01_p2'
    type = 'pants'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Leggings_of_Savages(Item):
    """ Leggings of Savages """
    url = r'/en/item/leggings-of-savages-P68_Unique_Pants_Set_05'
    type = 'pants'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Chausses_of_Valor(Item):
    """ Chausses of Valor """
    url = r'/en/item/chausses-of-valor-P67_Unique_Pants_Set_01'
    type = 'pants'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Cuisses_of_Akkhan(Item):
    """ Cuisses of Akkhan """
    url = r'/en/item/cuisses-of-akkhan-Unique_Pants_Set_10_x1'
    type = 'pants'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Towers_of_the_Light(Set_Item):
    """ Towers of the Light """
    url = r'/en/item/towers-of-the-light-Unique_Pants_Set_03_p3'
    type = 'pants'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Rolands_Determination(Set_Item):
    """ Roland's Determination """
    url = r'/en/item/rolands-determination-Unique_Pants_Set_01_p1'
    type = 'pants'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Unholy_Plates(Set_Item):
    """ Unholy Plates """
    url = r'/en/item/unholy-plates-Unique_Pants_Set_03_p2'
    type = 'pants'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Encasement(Set_Item):
    """ Marauder's Encasement """
    url = r'/en/item/marauders-encasement-Unique_Pants_Set_07_x1'
    type = 'pants'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Ulianas_Burden(Item):
    """ Uliana's Burden """
    url = r'/en/item/ulianas-burden-Unique_Pants_Set_01_p3'
    type = 'pants'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Scales_of_the_Dancing_Serpent(Item):
    """ Scales of the Dancing Serpent """
    url = r'/en/item/scales-of-the-dancing-serpent-Unique_Pants_Set_08_x1'
    type = 'pants'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Mountains_of_Justice(Item):
    """ Mountains of Justice """
    url = r'/en/item/mountains-of-justice-P67_Unique_Pants_Set_02'
    type = 'pants'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Firebirds_Down(Item):
    """ Firebird's Down """
    url = r'/en/item/firebirds-down-Unique_Pants_Set_06_x1'
    type = 'pants'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Leg_Guards_of_Mystery(Item):
    """ Leg Guards of Mystery """
    url = r'/en/item/leg-guards-of-mystery-Unique_Pants_Set_02_p2'
    type = 'pants'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Typhons_Abdomen(Item):
    """ Typhon's Abdomen """
    url = r'/en/item/typhons-abdomen-P68_Unique_Pants_Set_03'
    type = 'pants'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Helltooth_Leg_Guards(Item):
    """ Helltooth Leg Guards """
    url = r'/en/item/helltooth-leg-guards-Unique_Pants_Set_16_x1'
    type = 'pants'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Legs(Item):
    """ Arachyr's Legs """
    url = r'/en/item/arachyrs-legs-Unique_Pants_Set_02_p3'
    type = 'pants'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Mundunugus_Decoration(Item):
    """ Mundunugu's Decoration """
    url = r'/en/item/mundunugus-decoration-P68_Unique_Pants_Set_04'
    type = 'pants'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Rathmas_Skeletal_Legplates(Item):
    """ Rathma's Skeletal Legplates """
    url = r'/en/item/rathmas-skeletal-legplates-P6_Necro_Set_1_Pants'
    type = 'pants'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class TragOuls_Hide(Item):
    """ Trag'Oul's Hide """
    url = r'/en/item/tragouls-hide-P6_Necro_Set_2_Pants'
    type = 'pants'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Inariuss_Reticence(Item):
    """ Inarius's Reticence """
    url = r'/en/item/inariuss-reticence-P6_Necro_Set_3_Pants'
    type = 'pants'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Pestilence_Incantations(Item):
    """ Pestilence Incantations """
    url = r'/en/item/pestilence-incantations-P6_Necro_Set_4_Pants'
    type = 'pants'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Rivera_Dancers(Item):
    """ Rivera Dancers """
    url = r'/en/item/rivera-dancers-P4_Unique_Boots_001'
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements
	 Lashing Tail Kick attacks 50% faster and deals 257% increased damage.
	(Monk Only)
	[250 - 300]%
    """


class Lut_Socks(Item):
    """ Lut Socks """
    url = r'/en/item/lut-socks-Unique_Boots_009_x1'
    type = 'feet'
    text = """
	 Leap can be cast up to three times within 2 seconds before the cooldown begins.
	(Barbarian Only)
    """


class The_Crudest_Boots(Item):
    """ The Crudest Boots """
    url = r'/en/item/the-crudest-boots-P1_Unique_Boots_010'
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 Mystic Ally summons two Mystic Allies that fight by your side.
	(Monk Only)
    """


class Illusory_Boots(Item):
    """ Illusory Boots """
    url = r'/en/item/illusory-boots-Unique_Boots_103_x1'
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements

	+[10 - 12]% Movement Speed
	 You may move unhindered through enemies.
    """


class Boots_of_Disregard(Item):
    """ Boots of Disregard """
    url = r'/en/item/boots-of-disregard-Unique_Boots_102_x1'
    type = 'feet'
    text = """

	+[416 - 500] Vitality

	+[373 - 397] Armor

	Regenerates [4643 - 5528] Life per Second
	 Gain 10000 Life regeneration per Second for each second you stand still. This effect stacks up to 4 times.
    """


class Cains_Sandals(Item):
    """ Cain's Sandals """
    url = r'/en/artisan/blacksmith/recipe/cains-sandals'
    type = 'feet'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Captain_Crimsons_Whalers(Item):
    """ Captain Crimson's Whalers """
    url = r'/en/artisan/blacksmith/recipe/captain-crimsons-whalers'
    type = 'feet'
    text = """
	(2) Set:      Regenerates 20 Life per Second
	(3) Set:      +20 Resistance to All Elements
    """


class Irontoe_Mudsputters(Item):
    """ Irontoe Mudsputters """
    url = r'/en/item/irontoe-mudsputters-Unique_Boots_104_x1'
    type = 'feet'
    text = """

	+[416 - 500] Vitality
	 Gain up to 29% increased movement speed based on amount of Life missing.
	[25 - 30]%
    """


class Bryners_Journey(Item):
    """ Bryner's Journey """
    url = r'/en/item/bryners-journey-P6_Necro_Unique_Boots_22'
    type = 'feet'
    text = """
	 Attacking with Bone Spikes has a 25% chance to cast a Bone Nova at the target location.
	(Necromancer Only)
	[20 - 30]%
    """


class Fire_Walkers(Item):
    """ Fire Walkers """
    url = r'/en/item/fire-walkers-Unique_Boots_007_p2'
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 Burn the ground you walk on, dealing 342% weapon damage each second.
	[300 - 400]%
    """


class Fire_Walkers(Item):
    """ Fire Walkers """
    url = r'/en/item/fire-walkers-Unique_Boots_007_x1'
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 Burn the ground you walk on, dealing 100% weapon damage each second.
    """


class Lost_Boys(Item):
    """ Lost Boys """
    url = r'/en/artisan/blacksmith/recipe/lost-boys'
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed

	+[132 - 208] Thorns Damage

	Monster kills grant +[80 - 99] experience.
    """


class Ashearas_Tracks(Item):
    """ Asheara's Tracks """
    url = r'/en/artisan/blacksmith/recipe/ashearas-tracks'
    type = 'feet'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Steuarts_Greaves(Item):
    """ Steuart's Greaves """
    url = r'/en/item/steuarts-greaves-P6_Necro_Unique_Boots_21'
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 You gain 45% increased movement speed for 10 seconds after using Blood Rush.
	(Necromancer Only)
	[40 - 50]%
    """


class Steuarts_Greaves(Item):
    """ Steuart's Greaves """
    url = r'/en/item/steuarts-greaves-P61_Necro_Unique_Boots_21'
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 You gain 85% increased movement speed for 10 seconds after using Blood Rush.
	(Necromancer Only)
	[75 - 100]%
    """


class Innas_Sandals(Item):
    """ Inna's Sandals """
    url = r'/en/item/innas-sandals-P2_Unique_Boots_02'
    type = 'feet'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Zunimassas_Trail(Item):
    """ Zunimassa's Trail """
    url = r'/en/item/zunimassas-trail-Unique_Boots_013_x1'
    type = 'feet'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Natalyas_Bloody_Footprints(Item):
    """ Natalya's Bloody Footprints """
    url = r'/en/item/natalyas-bloody-footprints-Unique_Boots_011_x1'
    type = 'feet'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Blackthornes_Spurs(Item):
    """ Blackthorne's Spurs """
    url = r'/en/item/blackthornes-spurs-Unique_Boots_019_x1'
    type = 'feet'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Ice_Climbers(Item):
    """ Ice Climbers """
    url = r'/en/item/ice-climbers-Unique_Boots_008_x1'
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements

	Reduces damage from Cold attacks by [7 - 10]%.
	 Gain immunity to Freeze and Immobilize effects.
    """


class Immortal_Kings_Stride(Item):
    """ Immortal King's Stride """
    url = r'/en/item/immortal-kings-stride-Unique_Boots_012_x1'
    type = 'feet'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Nilfurs_Boast(Item):
    """ Nilfur's Boast """
    url = r'/en/item/nilfurs-boast-P61_Unique_Boots_01'
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements
	 Increase the damage of Meteor by 600%. When your Meteor hits 3 or fewer enemies, the damage is increased by 675%.
	(Wizard Only)
	[675 - 900]%
    """


class Sages_Journey(Item):
    """ Sage's Journey """
    url = r'/en/artisan/blacksmith/recipe/sages-journey'
    type = 'feet'
    text = """
	(2) Set:      +35 Strength     +35 Dexterity     +35 Intelligence     +35 Vitality
    """


class Sages_Passage(Item):
    """ Sage's Passage """
    url = r'/en/artisan/blacksmith/recipe/sages-passage'
    type = 'feet'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Jade_Harvesters_Swiftness(Item):
    """ Jade Harvester's Swiftness """
    url = r'/en/item/jade-harvesters-swiftness-Unique_Boots_Set_09_x1'
    type = 'feet'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Zeal_of_the_Invoker(Item):
    """ Zeal of the Invoker """
    url = r'/en/item/zeal-of-the-invoker-Unique_Boots_Set_12_x1'
    type = 'feet'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Ashearas_Finders(Item):
    """ Asheara's Finders """
    url = r'/en/artisan/blacksmith/recipe/ashearas-finders'
    type = 'feet'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class The_Shadows_Heels(Item):
    """ The Shadow's Heels """
    url = r'/en/item/the-shadows-heels-Unique_Boots_Set_14_x1'
    type = 'feet'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Vyrs_Swaggering_Stance(Item):
    """ Vyr's Swaggering Stance """
    url = r'/en/item/vyrs-swaggering-stance-Unique_Boots_Set_13_x1'
    type = 'feet'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Cains_Travelers(Item):
    """ Cain's Travelers """
    url = r'/en/artisan/blacksmith/recipe/cains-travelers'
    type = 'feet'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class Foundation_of_the_Earth(Item):
    """ Foundation of the Earth """
    url = r'/en/item/foundation-of-the-earth-Unique_Boots_Set_15_x1'
    type = 'feet'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Captain_Crimsons_Waders(Item):
    """ Captain Crimson's Waders """
    url = r'/en/artisan/blacksmith/recipe/captain-crimsons-waders'
    type = 'feet'
    text = """
	(2) Set:      Regenerates 6000 Life per Second     Reduces cooldown of all skills by 20.0%.     Reduces all resource costs by 20.0%.
	(3) Set:      Damage dealt is increased by your percentage of cooldown reduction.     Damage taken is reduced by your percentage of cost reduction.
    """


class Heel_of_Savages(Item):
    """ Heel of Savages """
    url = r'/en/item/heel-of-savages-P68_Unique_Boots_Set_05'
    type = 'feet'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Raekors_Striders(Item):
    """ Raekor's Striders """
    url = r'/en/item/raekors-striders-Unique_Boots_Set_05_x1'
    type = 'feet'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Sabaton_of_the_Wastes(Item):
    """ Sabaton of the Wastes """
    url = r'/en/item/sabaton-of-the-wastes-Unique_Boots_Set_01_p2'
    type = 'feet'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Rolands_Stride(Set_Item):
    """ Roland's Stride """
    url = r'/en/item/rolands-stride-Unique_Boots_Set_01_p1'
    type = 'feet'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Foundation_of_the_Light(Item):
    """ Foundation of the Light """
    url = r'/en/item/foundation-of-the-light-Unique_Boots_Set_03_p3'
    type = 'feet'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Greaves_of_Valor(Item):
    """ Greaves of Valor """
    url = r'/en/item/greaves-of-valor-P67_Unique_Boots_Set_01'
    type = 'feet'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Sabatons_of_Akkhan(Item):
    """ Sabatons of Akkhan """
    url = r'/en/item/sabatons-of-akkhan-Unique_Boots_Set_10_x1'
    type = 'feet'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Hell_Walkers(Item):
    """ Hell Walkers """
    url = r'/en/item/hell-walkers-Unique_Boots_Set_03_p2'
    type = 'feet'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Treads(Item):
    """ Marauder's Treads """
    url = r'/en/item/marauders-treads-Unique_Boots_Set_07_x1'
    type = 'feet'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Ulianas_Destiny(Item):
    """ Uliana's Destiny """
    url = r'/en/item/ulianas-destiny-Unique_Boots_Set_01_p3'
    type = 'feet'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Weaves_of_Justice(Item):
    """ Weaves of Justice """
    url = r'/en/item/weaves-of-justice-P67_Unique_Boots_Set_02'
    type = 'feet'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Eight_Demon_Boots(Item):
    """ Eight-Demon Boots """
    url = r'/en/item/eightdemon-boots-Unique_Boots_Set_08_x1'
    type = 'feet'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Striders_of_Destiny(Item):
    """ Striders of Destiny """
    url = r'/en/item/striders-of-destiny-Unique_Boots_Set_02_p2'
    type = 'feet'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Firebirds_Tarsi(Item):
    """ Firebird's Tarsi """
    url = r'/en/item/firebirds-tarsi-Unique_Boots_Set_06_x1'
    type = 'feet'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Typhons_Tarsus(Item):
    """ Typhon's Tarsus """
    url = r'/en/item/typhons-tarsus-P68_Unique_Boots_Set_03'
    type = 'feet'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Helltooth_Greaves(Item):
    """ Helltooth Greaves """
    url = r'/en/item/helltooth-greaves-Unique_Boots_Set_16_x1'
    type = 'feet'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Stride(Item):
    """ Arachyr's Stride """
    url = r'/en/item/arachyrs-stride-Unique_Boots_Set_02_p3'
    type = 'feet'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Mundunugus_Dance(Item):
    """ Mundunugu's Dance """
    url = r'/en/item/mundunugus-dance-P68_Unique_Boots_Set_04'
    type = 'feet'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Pestilence_Battle_Boots(Item):
    """ Pestilence Battle Boots """
    url = r'/en/item/pestilence-battle-boots-P6_Necro_Set_4_Boots'
    type = 'feet'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Inariuss_Perseverance(Item):
    """ Inarius's Perseverance """
    url = r'/en/item/inariuss-perseverance-P6_Necro_Set_3_Boots'
    type = 'feet'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class TragOuls_Stalwart_Greaves(Item):
    """ Trag'Oul's Stalwart Greaves """
    url = r'/en/item/tragouls-stalwart-greaves-P6_Necro_Set_2_Boots'
    type = 'feet'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Rathmas_Ossified_Sabatons(Item):
    """ Rathma's Ossified Sabatons """
    url = r'/en/item/rathmas-ossified-sabatons-P6_Necro_Set_1_Boots'
    type = 'feet'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Lost_Time(Item):
    """ Lost Time """
    url = r'/en/item/lost-time-P61_Unique_Phylactery_01'
    type = 'phylactery'
    text = """

	+[5 - 6]-[6 - 7] Damage

	+[626 - 750] Intelligence
	 Your cold skills reduce the movement speed of enemies by 30%. In addition, your movement speed is increased by 10% for 5 seconds.  Maximum 5 stacks.
	(Necromancer Only)
	[8 - 10]%
    """


class Iron_Rose(Item):
    """ Iron Rose """
    url = r'/en/item/iron-rose-P65_Unique_Phylactery_04'
    type = 'phylactery'
    text = """

	+[6 - 8]-[7 - 10] Damage

	+[626 - 750] Intelligence

	+[626 - 750] Vitality
	 Attacking with Siphon Blood has a 100% chance to cast a free Blood Nova.
	(Necromancer Only)
	100%
    """


class Legers_Disdain(Item):
    """ Leger's Disdain """
    url = r'/en/item/legers-disdain-P61_Unique_Phylactery_03'
    type = 'phylactery'
    text = """

	+[10 - 13]-[11 - 16] Damage

	+[626 - 750] Intelligence

	+[626 - 750] Vitality
	 Grim Scythe deals an additional 67% damage for each point of essence it restores.
	(Necromancer Only)
	[65 - 80]%
    """


class Bone_Ringer(Item):
    """ Bone Ringer """
    url = r'/en/item/bone-ringer-P6_Unique_Phylactery_02'
    type = 'phylactery'
    text = """

	+[105 - 131]-[106 - 157] Damage

	+[626 - 750] Intelligence

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 The damage bonus of Command Skeletons increases by 27% per second they spend attacking the same target. This effect stacks up to 60 times.
	(Necromancer Only)
	[25 - 30]%
    """


class Funerary_Pick(Item):
    """ Funerary Pick """
    url = r'/en/item/funerary-pick-P6_Unique_Scythe1H_01'
    type = 'scythe-1h'
    text = """

	+[626 - 750] Intelligence

	+[626 - 750] Vitality
	 Siphon Blood drains blood from 2 additional targets.
	(Necromancer Only)
    """


class TragOuls_Corroded_Fang(Item):
    """ Trag'Oul's Corroded Fang """
    url = r'/en/item/tragouls-corroded-fang-P6_Unique_Scythe1H_02'
    type = 'scythe-1h'
    text = """

	+[626 - 750] Intelligence
	 The Cursed Scythe rune for Grim Scythe now has a 100% chance to apply a curse and you deal 179% increased damage to cursed enemies.
	(Necromancer Only)
	[150 - 200]%
    """


class Scythe_of_the_Cycle(Item):
    """ Scythe of the Cycle """
    url = r'/en/item/scythe-of-the-cycle-P61_Unique_Scythe1H_03'
    type = 'scythe-1h'
    text = """

	+[626 - 750] Intelligence
	 Your Secondary skills deal 379% additional damage while Bone Armor is active but reduce the remaining duration of Bone Armor by 4 seconds.
	(Necromancer Only)
	[350 - 400]%
    """


class Jesseth_Skullscythe(Item):
    """ Jesseth Skullscythe """
    url = r'/en/item/jesseth-skullscythe-P6_Unique_Scythe1H_04'
    type = 'scythe-1h'
    text = """
	(2) Set:      When the target of your Command Skeletons dies, your skeletons are automatically commanded to attack a nearby target.     While your skeletons are commanded to attack a target, all of your minions deal 400% increased damage.
    """


class Reilenas_Shadowhook(Item):
    """ Reilena's Shadowhook """
    url = r'/en/item/reilenas-shadowhook-P6_Unique_Scythe2H_03'
    type = 'scythe-2h'
    text = """

	+[946 - 1125] Intelligence
	 Every point of Maximum Essence increases your damage by 0.5% and Bone Spikes generates 2 additional Essence for each enemy hit.
	(Necromancer Only)
	[2 - 5]
    """


class Maltorius_Petrified_Spike(Item):
    """ Maltorius' Petrified Spike """
    url = r'/en/item/maltorius-petrified-spike-P61_Unique_Scythe2H_01'
    type = 'scythe-2h'
    text = """

	+[946 - 1125] Intelligence

	+[6 - 10]% Damage
	 Bone Spear now costs 40 Essence and deals 646% increased damage.
	(Necromancer Only)
	[550 - 700]%
    """


class Bloodtide_Blade(Item):
    """ Bloodtide Blade """
    url = r'/en/item/bloodtide-blade-P65_Unique_Scythe2H_02'
    type = 'scythe-2h'
    text = """

	+[946 - 1125] Intelligence

	+[946 - 1125] Vitality
	 Death Nova deals 328% increased damage for every enemy within 25 yards.
	(Necromancer Only)
	[300 - 400]%
    """


class Nayrs_Black_Death(Item):
    """ Nayr's Black Death """
    url = r'/en/item/nayrs-black-death-P61_Unique_Scythe2H_04'
    type = 'scythe-2h'
    text = """

	+[946 - 1125] Intelligence
	 Each different poison skill you use increases the damage of your poison skills by 95% for 15 seconds.
	(Necromancer Only)
	[75 - 100]%
    """


class Salvation(Item):
    """ Salvation """
    url = r'/en/item/salvation-Unique_CruShield_108_x1'
    type = 'crusader-shield'
    text = """

	+11% Chance to Block
	 Blocked attacks heal you and your allies for 23% of the amount blocked.
	(Crusader Only)
	[20 - 30]%
    """


class Shield_of_Fury(Item):
    """ Shield of Fury """
    url = r'/en/item/shield-of-fury-P61_Unique_Shield_106_x1'
    type = 'crusader-shield'
    text = """
	 Each time an enemy takes damage from your Heaven's Fury, it increases the damage they take from your Heaven's Fury by 26%. This effect stacks up to 20 times.
	(Crusader Only)
	[25 - 30]%
    """


class The_Final_Witness(Item):
    """ The Final Witness """
    url = r'/en/item/the-final-witness-Unique_CruShield_107_x1'
    type = 'crusader-shield'
    text = """
	 Shield Glare now hits all enemies around you.
	(Crusader Only)
    """


class Hallowed_Bulwark(Item):
    """ Hallowed Bulwark """
    url = r'/en/item/hallowed-bulwark-Unique_CruShield_103_x1'
    type = 'crusader-shield'
    text = """
	 Iron Skin also increases your Block Amount by 52%.
	(Crusader Only)
	[45 - 60]%
    """


class Jekangbord(Item):
    """ Jekangbord """
    url = r'/en/item/jekangbord-P65_Unique_CruShield_102_x1'
    type = 'crusader-shield'
    text = """
	 Blessed Shield ricochets to 6 additional enemies and has its damage increased by 379%.
	[300 - 400]%
    """


class Sublime_Conviction(Item):
    """ Sublime Conviction """
    url = r'/en/item/sublime-conviction-Unique_CruShield_106_x1'
    type = 'crusader-shield'
    text = """

	+11% Chance to Block
	 When you block, you have up to a 16% chance to Stun the attacker for 1.5 seconds based on your current Wrath.
	(Crusader Only)
	[15 - 20]%
    """


class Akarats_Awakening(Item):
    """ Akarat's Awakening """
    url = r'/en/item/akarats-awakening-Unique_CruShield_104_x1'
    type = 'crusader-shield'
    text = """

	+11% Chance to Block
	 Every successful block has a 21% chance to reduce all cooldowns by 1 second.
	(Crusader Only)
	[20 - 25]%
    """


class Hellskull(Item):
    """ Hellskull """
    url = r'/en/item/hellskull-Unique_CruShield_105_x1'
    type = 'crusader-shield'
    text = """
	 Gain 10% increased damage while wielding a two-handed weapon.
	(Crusader Only)
    """


class Piro_Marella(Item):
    """ Piro Marella """
    url = r'/en/artisan/blacksmith/recipe/piro-marella'
    type = 'crusader-shield'
    text = """

	Reduces the Wrath cost of Shield Bash by [40 - 50]%.
    """


class Guard_of_Johanna(Item):
    """ Guard of Johanna """
    url = r'/en/item/guard-of-johanna-Unique_Shield_103_x1'
    type = 'crusader-shield'
    text = """
	 Blessed Hammer damage is increased by 204% for the first 3 enemies it hits.
	(Crusader Only)
	[200 - 250]%
    """


class Shield_of_the_Steed(Item):
    """ Shield of the Steed """
    url = r'/en/item/shield-of-the-steed-P4_Unique_Shield_Set_01_x1'
    type = 'crusader-shield'
    text = """
	(2) Set:      Increases the duration of Steed Charge by 2 seconds. In addition, killing an enemy reduces the cooldown of Steed Charge by 1 second.     Gain 100% increased damage while using Steed Charge and for 5 seconds after it ends.
    """


class Frydehrs_Wrath(Item):
    """ Frydehr's Wrath """
    url = r'/en/item/frydehrs-wrath-P61_CruShield_norm_unique_01'
    type = 'crusader-shield'
    text = """
	 Condemn has no cooldown and has its damage increased by 727%, but instead costs 40 Wrath.
	[600 - 800]%
    """


class Unrelenting_Phalanx(Item):
    """ Unrelenting Phalanx """
    url = r'/en/item/unrelenting-phalanx-P1_CruShield_norm_unique_02'
    type = 'crusader-shield'
    text = """
	 Increases Phalanx Damage by [45 - 60]%
	 Phalanx now casts twice.
	(Crusader Only)
    """


class Covens_Criterion(Item):
    """ Coven's Criterion """
    url = r'/en/item/covens-criterion-Unique_Shield_107_x1'
    type = 'shield'
    text = """

	+[626 - 750] Vitality

	+11% Chance to Block
	 You take 52% less damage from blocked attacks.
	[45 - 60]%
    """


class Denial(Item):
    """ Denial """
    url = r'/en/item/denial-P61_Unique_Shield_007'
    type = 'shield'
    text = """
	 Each enemy hit by your Sweep Attack increases the damage of your next Sweep Attack by 109%, stacking up to 5 times.
	(Crusader Only)
	[100 - 125]%
    """


class Wall_of_Bone(Item):
    """ Wall of Bone """
    url = r'/en/artisan/blacksmith/recipe/wall-of-bone'
    type = 'shield'
    text = """

	+[74 - 91] Vitality

	+[11 - 20] Resistance to All Elements

	[20 - 30]% chance to be protected by a shield of bones when you are hit.
    """


class Eberli_Charo(Item):
    """ Eberli Charo """
    url = r'/en/item/eberli-charo-Unique_Shield_102_x1'
    type = 'shield'
    text = """
	 Reduces the cooldown of Heaven's Fury by 46%.
	(Crusader Only)
	[45 - 50]%
    """


class Defender_of_Westmarch(Item):
    """ Defender of Westmarch """
    url = r'/en/item/defender-of-westmarch-Unique_Shield_101_p2'
    type = 'shield'
    text = """

	+11% Chance to Block
	 Blocks have a chance of summoning a charging wolf that deals 927% weapon damage to all enemies it passes through.
	[800 - 1000]%
    """


class Freeze_of_Deflection(Item):
    """ Freeze of Deflection """
    url = r'/en/item/freeze-of-deflection-Unique_Shield_004_x1'
    type = 'shield'
    text = """
	 Blocking an attack has a chance to Freeze the attacker for 0.8 seconds.
	[0.5 - 1.5]
    """


class VoToyias_Spiker(Item):
    """ Vo'Toyias Spiker """
    url = r'/en/item/votoyias-spiker-Unique_Shield_104_x1'
    type = 'shield'
    text = """

	+[5334 - 7696] Thorns Damage
	 Enemies affected by Provoke take double damage from Thorns.
	(Crusader Only)
    """


class Lidless_Wall(Item):
    """ Lidless Wall """
    url = r'/en/item/lidless-wall-Unique_Shield_008_x1'
    type = 'shield'
    text = """

	+[120 - 150] Maximum Mana
    """


class Ivory_Tower(Item):
    """ Ivory Tower """
    url = r'/en/item/ivory-tower-P2_Unique_Shield_002'
    type = 'shield'
    text = """

	+[626 - 750] Vitality
	 Blocks release forward a Fires of Heaven.
	(Crusader Only)
    """


class Stormshield(Item):
    """ Stormshield """
    url = r'/en/item/stormshield-Unique_Shield_009_x1'
    type = 'shield'
    text = """

	Reduces damage from melee attacks by [25.0 - 30.0]%
    """


class Hallowed_Defender(Item):
    """ Hallowed Defender """
    url = r'/en/artisan/blacksmith/recipe/hallowed-defender'
    type = 'shield'
    text = """
	(2) Set:      +40 Resistance to All Elements     Attack Speed Increased by 5.0%
    """


class Jesseth_Skullshield(Item):
    """ Jesseth Skullshield """
    url = r'/en/item/jesseth-skullshield-P6_Unique_Shield_01'
    type = 'shield'
    text = """
	(2) Set:      When the target of your Command Skeletons dies, your skeletons are automatically commanded to attack a nearby target.     While your skeletons are commanded to attack a target, all of your minions deal 400% increased damage.
    """


class Wall_of_Man(Item):
    """ Wall of Man """
    url = r'/en/artisan/blacksmith/recipe/wall-of-man'
    type = 'shield'
    text = """

	[20 - 30]% chance to be protected by a shield of bones when you are hit.
    """


class Hallowed_Barricade(Item):
    """ Hallowed Barricade """
    url = r'/en/artisan/blacksmith/recipe/hallowed-barricade'
    type = 'shield'
    text = """
	(2) Set:      +100 Resistance to All Elements     Attack Speed Increased by 10.0%
    """



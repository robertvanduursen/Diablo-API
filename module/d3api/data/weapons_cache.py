import sys
sys.path.append("..\..")
from d3api.datatypes import Item, Set, Set_Item

class Genzaniku(Item):
    """ Genzaniku """
    url = r'/en/item/genzaniku-Unique_Axe_1H_003_x1'
    type = 'axe-1h'
    text = """
	 Chance to summon a ghostly Fallen Champion when attacking.
    """


class Hack(Item):
    """ Hack """
    url = r'/en/item/hack-Unique_Axe_1H_103_x1'
    type = 'axe-1h'
    text = """
	 95% of your Thorns damage is applied on every attack.
	[75 - 100]%
    """


class The_Wedge(Item):
    """ The Wedge """
    url = r'/en/artisan/blacksmith/recipe/the-wedge'
    type = 'axe-1h'
    text = """

	+[53 - 65]-[64 - 81] Cold Damage

	Increases Attack Speed by [3 - 4]%

	+[31 - 40] Cold Resistance
    """


class The_Butchers_Sickle(Item):
    """ The Butcher's Sickle """
    url = r'/en/item/the-butchers-sickle-Unique_Axe_1H_006_x1'
    type = 'axe-1h'
    text = """
	 22% chance to drag enemies to you when attacking.
	[20 - 25]%
    """


class Hallowed_Storm(Item):
    """ Hallowed Storm """
    url = r'/en/artisan/blacksmith/recipe/hallowed-storm'
    type = 'axe-1h'
    text = """
	(2) Set:      +40 Resistance to All Elements     Attack Speed Increased by 5.0%
    """


class The_Burning_Axe_of_Sankis(Item):
    """ The Burning Axe of Sankis """
    url = r'/en/item/the-burning-axe-of-sankis-Unique_Axe_1H_007_x1'
    type = 'axe-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Fire Damage

	Fire skills deal [15 - 20]% more damage.
	 Chance to fight through the pain when enemies hit you.
    """


class Sky_Splitter(Item):
    """ Sky Splitter """
    url = r'/en/item/sky-splitter-Unique_Axe_1H_005_p2'
    type = 'axe-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Holy Damage
	 17% chance to Smite enemies for 600-750% weapon damage as Lightning when you hit them.
	[15 - 20]%
    """


class Mordullus_Promise(Item):
    """ Mordullu's Promise """
    url = r'/en/item/mordullus-promise-P4_Unique_Axe_1H_102'
    type = 'axe-1h'
    text = """
	 Firebomb generates 120 Mana.
	(Witch Doctor Only)
	[100 - 125]
    """


class Hallowed_Breach(Item):
    """ Hallowed Breach """
    url = r'/en/artisan/blacksmith/recipe/hallowed-breach'
    type = 'axe-1h'
    text = """
	(2) Set:      +100 Resistance to All Elements     Attack Speed Increased by 10.0%
    """


class Fjord_Cutter(Item):
    """ Fjord Cutter """
    url = r'/en/item/fjord-cutter-P67_Unique_Mighty_1H_006'
    type = 'mighty-weapon-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Cold Damage

	+[626 - 750] Strength

	[7.5 - 10.0]% Chance to Freeze on Hit
	 Seismic Slam attacks 50% faster and also deals 100%  increased damage against Slowed or Chilled enemies.
	[100 - 150]%
    """


class Ambos_Pride(Item):
    """ Ambo's Pride """
    url = r'/en/item/ambos-pride-P67_Unique_Mighty_1H_012'
    type = 'mighty-weapon-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage

	+[626 - 750] Strength

	[34.0 - 39.0]% chance to inflict Bleed for [300 - 400]% weapon damage over 5 seconds.
	 Attacking with Whirlwind also applies Rend, and the total damage of Rend is dealt over 1 second.
    """


class Bul_Kathoss_Warrior_Blood(Item):
    """ Bul-Kathos's Warrior Blood """
    url = r'/en/item/bulkathoss-warrior-blood-Unique_Mighty_1H_011_x1'
    type = 'mighty-weapon-1h'
    text = """
	(2) Set:      Increases Fury Generation by 15 (Barbarian Only)     During Whirlwind you gain 45% increased attack speed and movement speed.
    """


class Bul_Kathoss_Solemn_Vow(Item):
    """ Bul-Kathos's Solemn Vow """
    url = r'/en/item/bulkathoss-solemn-vow-Unique_Mighty_1H_010_x1'
    type = 'mighty-weapon-1h'
    text = """
	(2) Set:      Increases Fury Generation by 15 (Barbarian Only)     During Whirlwind you gain 45% increased attack speed and movement speed.
    """


class Blade_of_the_Warlord(Item):
    """ Blade of the Warlord """
    url = r'/en/item/blade-of-the-warlord-P4_Unique_Mighty_1H_005'
    type = 'mighty-weapon-1h'
    text = """

	+[626 - 750] Strength

	+[981 - 1199]-[1175 - 1490] Holy Damage
	 Bash consumes up to 40 Fury to deal up to 428% increased damage.
	(Barbarian Only)
	[400 - 500]%
    """


class Hallowed_Reckoning(Item):
    """ Hallowed Reckoning """
    url = r'/en/artisan/blacksmith/recipe/hallowed-reckoning'
    type = 'mighty-weapon-1h'
    text = """
	(2) Set:      +40 Resistance to All Elements     Attack Speed Increased by 5.0%
    """


class Oathkeeper(Item):
    """ Oathkeeper """
    url = r'/en/item/oathkeeper-P4_Unique_Mighty_1H_104'
    type = 'mighty-weapon-1h'
    text = """

	+[626 - 750] Strength
	 Your primary skills attack 50% faster and deal 179% increased damage.
	(Barbarian Only)
	[150 - 200]%
    """


class Hallowed_Nemesis(Item):
    """ Hallowed Nemesis """
    url = r'/en/artisan/blacksmith/recipe/hallowed-nemesis'
    type = 'mighty-weapon-1h'
    text = """
	(2) Set:      +100 Resistance to All Elements     Attack Speed Increased by 10.0%
    """


class Dishonored_Legacy(Item):
    """ Dishonored Legacy """
    url = r'/en/item/dishonored-legacy-Unique_Mighty_1H_103_x1'
    type = 'mighty-weapon-1h'
    text = """

	+[626 - 750] Strength
	 Cleave deals up to 328% increased damage based on percentage of missing Fury.
	(Barbarian Only)
	[300 - 400]%
    """


class Remorseless(Item):
    """ Remorseless """
    url = r'/en/item/remorseless-P67_Unique_Mighty_1H_102'
    type = 'mighty-weapon-1h'
    text = """

	+[626 - 750] Strength
	 While both Wrath of the Berserker and Call of the Ancients are active, Hammer of the Ancients deals 229% increased damage.
	(Barbarian Only)
	[200 - 250]%
    """


class Odyn_Son(Item):
    """ Odyn Son """
    url = r'/en/item/odyn-son-Unique_Mace_1H_002_x1'
    type = 'mace-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Lightning Damage

	Lightning skills deal [15 - 20]% more damage.
	 34% chance to Chain Lightning enemies when you hit them.
	[20 - 40]%
    """


class Mad_Monarchs_Scepter(Item):
    """ Mad Monarch's Scepter """
    url = r'/en/item/mad-monarchs-scepter-Unique_Mace_1H_101_x1'
    type = 'mace-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage

	+[6 - 10]% Damage
	 After killing 10 enemies, you release a Poison Nova that deals 1265% weapon damage as Poison to enemies within 30 yards.
	[1050 - 1400]%
    """


class Nutcracker(Item):
    """ Nutcracker """
    url = r'/en/item/nutcracker-Unique_Mace_1H_005_x1'
    type = 'mace-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage

	Critical Hit Damage Increased by [31.0 - 35.0]% 

	[5.0 - 10.0]% Chance to Stun on Hit
    """


class Solanium(Item):
    """ Solanium """
    url = r'/en/item/solanium-Unique_Mace_1H_102_x1'
    type = 'mace-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Holy Damage

	Sockets (1)
	 Critical Hits have a 3% chance to spawn a health globe.
	[3 - 4]%
    """


class Jaces_Hammer_of_Vigilance(Item):
    """ Jace's Hammer of Vigilance """
    url = r'/en/item/jaces-hammer-of-vigilance-Unique_Mace_1H_103_x1'
    type = 'mace-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Holy Damage
	 Increases Blessed Hammer Damage by [15 - 20]%
	 Increase the size of your Blessed Hammers.
	(Crusader Only)
    """


class Neanderthal(Item):
    """ Neanderthal """
    url = r'/en/item/neanderthal-Unique_Mace_1H_003_x1'
    type = 'mace-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage

	Monster kills grant +[140 - 200] experience.

	+[5334 - 7696] Thorns Damage
    """


class Nailbiter(Item):
    """ Nailbiter """
    url = r'/en/item/nailbiter-Unique_Mace_1H_008_x1'
    type = 'mace-1h'
    text = """

	+[6 - 10]% Damage

	+[981 - 1199]-[1175 - 1490] Damage

	+[5334 - 7696] Thorns Damage
    """


class Sun_Keeper(Item):
    """ Sun Keeper """
    url = r'/en/item/sun-keeper-Unique_Mace_1H_011_x1'
    type = 'mace-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Holy Damage

	Increases damage against elites by [15.0 - 30.0]%

	+[71 - 80]% Extra Gold from Monsters
    """


class Echoing_Fury(Item):
    """ Echoing Fury """
    url = r'/en/item/echoing-fury-P66_Unique_Mace_1H_001'
    type = 'mace-1h'
    text = """

	Increases Attack Speed by [5 - 7]%

	+[981 - 1199]-[1175 - 1490] Damage

	+[6 - 10]% Damage

	[10.0 - 20.0]% Chance to Fear on Hit
	 Slaying enemies engulfs the wielder into a Frenzy.
    """


class Earthshatter(Item):
    """ Earthshatter """
    url = r'/en/artisan/blacksmith/recipe/earthshatter'
    type = 'mace-1h'
    text = """

	+[4 - 7]% Damage

	[1.0 - 2.6]% Chance to Stun on Hit

	[1.0 - 2.6]% Chance to Immobilize on Hit

	[20 - 35]% chance to cause the ground to shudder when attacking.
    """


class Monster_Hunter(Item):
    """ Monster Hunter """
    url = r'/en/item/monster-hunter-Unique_Sword_1H_017_x1'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Fire Damage

	+[9 - 15]% Damage to Beasts
    """


class Wildwood(Item):
    """ Wildwood """
    url = r'/en/item/wildwood-Unique_Sword_1H_002_x1'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Poison Damage

	+[6 - 10]% Damage

	Monster kills grant +[140 - 200] experience.
    """


class Borns_Searing_Spite(Item):
    """ Born's Searing Spite """
    url = r'/en/artisan/blacksmith/recipe/borns-searing-spite'
    type = 'sword-1h'
    text = """
	(2) Set:      +2% Life     +20% Experience. (2.0% at level 70)
    """


class Rimeheart(Item):
    """ Rimeheart """
    url = r'/en/item/rimeheart-Unique_Sword_1H_109_x1'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Cold Damage
	 20% chance on hit to instantly deal 10,000% weapon damage as Cold to enemies that are Frozen.
	10,000%
    """


class Fulminator(Item):
    """ Fulminator """
    url = r'/en/item/fulminator-P3_Unique_Sword_1H_104'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Lightning Damage
	 Lightning damage has a chance to turn enemies into lightning rods, causing them to pulse 472% weapon damage as Lightning every second to nearby enemies for 6 seconds.
	[444 - 555]%
    """


class Thunderfury_Blessed_Blade_of_the_Windseeker(Item):
    """ Thunderfury, Blessed Blade of the Windseeker """
    url = r'/en/item/thunderfury-blessed-blade-of-the-windseeker-Unique_Sword_1H_101_x1'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Lightning Damage

	Sockets (1)
	 Chance on hit to blast your enemy with Lightning, dealing 355% weapon damage as Lightning and then jumping to additional nearby enemies. Each enemy hit has their attack speed and movement speed reduced by 30% for 3 seconds. Jumps up to 5 targets.
	[279 - 372]%
    """


class Sever(Item):
    """ Sever """
    url = r'/en/item/sever-Unique_Sword_1H_007_x1'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage

	+[6 - 10]% Damage

	+[5 - 10]% Damage to Demons
	 Slain enemies rest in pieces.
    """


class Skycutter(Item):
    """ Skycutter """
    url = r'/en/item/skycutter-Unique_Sword_1H_004_x1'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Holy Damage

	Holy skills deal [15 - 20]% more damage.
	 Chance to summon angelic assistance when attacking.
    """


class Devil_Tongue(Item):
    """ Devil Tongue """
    url = r'/en/item/devil-tongue-Unique_Sword_1H_011_x1'
    type = 'sword-1h'
    text = """

	+[6 - 10]% Damage

	+[981 - 1199]-[1175 - 1490] Fire Damage

	+[71 - 80]% Extra Gold from Monsters
    """


class Azurewrath(Item):
    """ Azurewrath """
    url = r'/en/item/azurewrath-P3_Unique_Sword_1H_012'
    type = 'sword-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Cold Damage

	Cold skills deal [15 - 20]% more damage.

	[20.0 - 25.0]% Chance to Freeze on Hit
	 Undead and Demon enemies within 25 yards take 565% weapon damage as Holy every second and are sometimes knocked into the air.
	[500 - 650]%
    """


class Griswolds_Masterpiece(Item):
    """ Griswold's Masterpiece """
    url = r'/en/artisan/blacksmith/recipe/griswolds-masterpiece'
    type = 'sword-1h'
    text = """

	Increases Attack Speed by [4 - 5]%

	[1.0 - 2.6]% Chance to Knockback on Hit
    """


class Sword_of_Ill_Will(Item):
    """ Sword of Ill Will """
    url = r'/en/item/sword-of-ill-will-P4_Unique_Sword_1H_01'
    type = 'sword-1h'
    text = """
	 Chakram deals 1.4% increased damage for every point of Hatred you have.
	(Demon Hunter Only)
	[1.0 - 1.4]%
    """


class Borns_Furious_Wrath(Item):
    """ Born's Furious Wrath """
    url = r'/en/artisan/blacksmith/recipe/borns-furious-wrath'
    type = 'sword-1h'
    text = """
	(2) Set:      +15% Life
	(3) Set:      Reduces cooldown of all skills by 10.0%.     +20% Experience. (2.0% at level 70)
    """


class Deathwish(Item):
    """ Deathwish """
    url = r'/en/item/deathwish-P61_Unique_Sword_1H_112_x1'
    type = 'sword-1h'
    text = """
	 While channeling Arcane Torrent, Disintegrate, or Ray of Frost for at least 1 second, all damage is increased by 294%.
	(Wizard Only)
	[250 - 325]%
    """


class Little_Rogue(Item):
    """ Little Rogue """
    url = r'/en/item/little-rogue-Unique_Sword_1H_Set_03_x1'
    type = 'sword-1h'
    text = """
	(2) Set:      Every time you spend primary resource, gain 6% increased Attack Speed, Damage, and Armor for 5 seconds. This effect stacks up to 5 times.
    """


class In_geom(Item):
    """ In-geom """
    url = r'/en/item/ingeom-Unique_Sword_1H_113_x1'
    type = 'sword-1h'
    text = """

	+[6 - 10]% Damage

	+[981 - 1199]-[1175 - 1490] Holy Damage
	 Your skill cooldowns are reduced by 10 seconds for 15 seconds after killing an elite pack.
	[8 - 10]
    """


class The_Slanderer(Item):
    """ The Slanderer """
    url = r'/en/item/the-slanderer-Unique_Sword_1H_Set_02_x1'
    type = 'sword-1h'
    text = """
	(2) Set:      Every time you spend primary resource, gain 6% increased Attack Speed, Damage, and Armor for 5 seconds. This effect stacks up to 5 times.
    """


class Shard_of_Hate(Item):
    """ Shard of Hate """
    url = r'/en/item/shard-of-hate-Unique_Sword_1H_Promo_02_x1'
    type = 'sword-1h'
    text = """
	 Elemental skills have a chance to trigger a powerful attack that deals 229% weapon damage:
			   Cold skills trigger Freezing Skull
			   Poison skills trigger Poison Nova
			   Lightning skills trigger Charged Bolt
	[200 - 250]%
    """


class The_Twisted_Sword(Item):
    """ The Twisted Sword """
    url = r'/en/item/the-twisted-sword-Unique_Sword_1H_107_x1'
    type = 'sword-1h'
    text = """
	 Energy Twister damage is increased by 145% for each Energy Twister you have out up to a maximum of 5.
	(Wizard Only)
	[125 - 150]%
    """


class Gyrfalcons_Foote(Item):
    """ Gyrfalcon's Foote """
    url = r'/en/item/gyrfalcons-foote-P61_Unique_Flail_1H_105_x1'
    type = 'flail-1h'
    text = """

	+[626 - 750] Strength
	 Removes the resource cost of Blessed Shield and increases its damage by 319%.
	(Crusader Only)
	[275 - 350]%
    """


class Justinians_Mercy(Item):
    """ Justinian's Mercy """
    url = r'/en/item/justinians-mercy-Unique_Flail_1H_102_x1'
    type = 'flail-1h'
    text = """

	Sockets (1)
	 Blessed Hammer gains the effect of the Dominion rune.
	(Crusader Only)
    """


class Darklight(Item):
    """ Darklight """
    url = r'/en/item/darklight-P67_Unique_Flail_1H_106'
    type = 'flail-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Lightning Damage

	+[626 - 750] Strength
	 Fist of the Heavens now casts twice and deals 874% more damage.
	(Crusader Only)
	[800 - 1000]%
    """


class Swiftmount(Item):
    """ Swiftmount """
    url = r'/en/item/swiftmount-Unique_Flail_1H_103_x1'
    type = 'flail-1h'
    text = """

	+[626 - 750] Strength
	 Doubles the duration of Steed Charge.
	(Crusader Only)
    """


class Kassars_Retribution(Item):
    """ Kassar's Retribution """
    url = r'/en/item/kassars-retribution-Unique_Flail_1H_104_x1'
    type = 'flail-1h'
    text = """

	+[626 - 750] Strength
	 Casting Justice increases your movement speed by 17% for 2 seconds.
	(Crusader Only)
	[15 - 20]%
    """


class Inviolable_Faith(Item):
    """ Inviolable Faith """
    url = r'/en/item/inviolable-faith-Unique_Flail_1H_107_x1'
    type = 'flail-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Holy Damage

	Sockets (1)
	 Casting Consecration also casts Consecration beneath all of your allies.
    """


class Johannas_Argument(Item):
    """ Johanna's Argument """
    url = r'/en/item/johannas-argument-P1_flail1H_norm_unique_01'
    type = 'flail-1h'
    text = """

	+[626 - 750] Strength
	 Increase the attack speed and damage of Blessed Hammer by 100%.
	(Crusader Only)
	100%
    """


class Golden_Scourge(Item):
    """ Golden Scourge """
    url = r'/en/artisan/blacksmith/recipe/golden-scourge'
    type = 'flail-1h'
    text = """

	+[981 - 1199]-[1175 - 1490] Holy Damage

	Holy skills deal [15 - 20]% more damage.

	Smite now jumps to 3 additional enemies.
    """


class Spear_of_Jairo(Item):
    """ Spear of Jairo """
    url = r'/en/item/spear-of-jairo-P6_Unique_Spear_01'
    type = 'spear'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage
	 Your Thorns is increased by 12% for every enemy afflicted by one of your curses.
	(Necromancer Only)
	[10 - 15]%
    """


class Scrimshaw(Item):
    """ Scrimshaw """
    url = r'/en/item/scrimshaw-Unique_Spear_004_p3'
    type = 'spear'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage

	+[6 - 10]% Damage
	 Increases Zombie Charger Damage by [60 - 80]%
	 Reduces the Mana cost of Zombie Charger by 40%.
	(Witch Doctor Only)
	[40 - 50]%
    """


class Arreats_Law(Item):
    """ Arreat's Law """
    url = r'/en/item/arreats-law-P3_Unique_Spear_001'
    type = 'spear'
    text = """

	+[981 - 1199]-[1175 - 1490] Damage
	 Weapon Throw generates up to 17 additional Fury based on how far away the enemy hit is. Maximum benefit when the enemy hit is 20 or more yards away.
	(Barbarian Only)
	[15 - 20]
    """


class The_Three_Hundredth_Spear(Item):
    """ The Three Hundredth Spear """
    url = r'/en/item/the-three-hundredth-spear-P4_Unique_Spear_002'
    type = 'spear'
    text = """
	 Increase the damage of Weapon Throw and Ancient Spear by 57%.
	(Barbarian Only)
	[45 - 60]%
    """


class Envious_Blade(Item):
    """ Envious Blade """
    url = r'/en/item/envious-blade-Unique_Dagger_103_x1'
    type = 'dagger'
    text = """

	+[858 - 1049]-[1028 - 1304] Poison Damage
	 Gain 100% Critical Hit Chance against enemies at full health.
    """


class Pig_Sticker(Item):
    """ Pig Sticker """
    url = r'/en/item/pig-sticker-Unique_Dagger_007_x1'
    type = 'dagger'
    text = """
	 Squeal!
    """


class Wizardspike(Item):
    """ Wizardspike """
    url = r'/en/item/wizardspike-Unique_Dagger_010_x1_210'
    type = 'dagger'
    text = """
	 Performing an attack has a 22% chance to hurl a Frozen Orb.
	[20 - 25]%
    """


class Blood_Magic_Blade(Item):
    """ Blood-Magic Blade """
    url = r'/en/artisan/blacksmith/recipe/bloodmagic-blade'
    type = 'dagger'
    text = """

	+[533 - 652]-[639 - 810] Damage

	Increases Attack Speed by [4 - 5]%

	Increases damage against elites by [4.0 - 7.0]%

	Blood oozes from you.
    """


class Karleis_Point(Item):
    """ Karlei's Point """
    url = r'/en/item/karleis-point-P61_Unique_Dagger_101_x1'
    type = 'dagger'
    text = """

	+[858 - 1049]-[1028 - 1304] Cold Damage
	 The damage of Impale is increased by 344% and it returns 15 Hatred if it hits an enemy already Impaled.
	(Demon Hunter Only)
	[300 - 375]%
    """


class Eun_jang_do(Item):
    """ Eun-jang-do """
    url = r'/en/item/eunjangdo-Unique_Dagger_104_x1'
    type = 'dagger'
    text = """

	+[858 - 1049]-[1028 - 1304] Cold Damage
	 Attacking enemies below 17% Life freezes them for 3 seconds.
	[17 - 20]%
    """


class Lord_Greenstones_Fan(Item):
    """ Lord Greenstone's Fan """
    url = r'/en/item/lord-greenstones-fan-P61_Unique_Dagger_102_x1'
    type = 'dagger'
    text = """

	+[858 - 1049]-[1028 - 1304] Cold Damage
	 Every second, gain 328% increased damage for your next Fan of Knives. Stacks up to 30 times.
	(Demon Hunter Only)
	[300 - 400]%
    """


class Blood_Magic_Edge(Item):
    """ Blood-Magic Edge """
    url = r'/en/artisan/blacksmith/recipe/bloodmagic-edge'
    type = 'dagger'
    text = """

	+[858 - 1049]-[1028 - 1304] Damage

	Increases Attack Speed by [5 - 7]%

	Blood oozes from you.
    """


class The_Executioner(Item):
    """ The Executioner """
    url = r'/en/item/the-executioner-P66_Unique_Axe_2H_003'
    type = 'axe-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Damage

	Monster kills grant +[140 - 200] experience.
	 Attacks will slay enemies with less than 7% health.
	[5 - 10]%
    """


class Burst_of_Wrath(Item):
    """ Burst of Wrath """
    url = r'/en/item/burst-of-wrath-Unique_Axe_2H_103_x1'
    type = 'axe-2h'
    text = """

	Sockets (1)
	 Killing enemies and destroying objects has a chance to grant 20% of your maximum primary resource.
    """


class Butchers_Carver(Item):
    """ Butcher's Carver """
    url = r'/en/item/butchers-carver-Unique_Axe_2H_001_x1'
    type = 'axe-2h'
    text = """
	 The Butcher still inhabits his carver.
    """


class Messerschmidts_Reaver(Item):
    """ Messerschmidt's Reaver """
    url = r'/en/item/messerschmidts-reaver-P66_Unique_Axe_2H_011'
    type = 'axe-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage

	+[9142 - 13,371] Life after Each Kill
	 Reduce the remaining cooldown of one of your skills by 1 second when you slay an enemy.
	1
    """


class Fire_Brand(Item):
    """ Fire Brand """
    url = r'/en/artisan/blacksmith/recipe/fire-brand'
    type = 'axe-2h'
    text = """

	+[732 - 894]-[877 - 1111] Fire Damage

	+[81 - 100] Fire Resistance

	[25 - 50]% chance to cast a fireball when attacking.
    """


class Skorn(Item):
    """ Skorn """
    url = r'/en/item/skorn-Unique_Axe_2H_009_x1'
    type = 'axe-2h'
    text = """

	[34.0 - 39.0]% chance to inflict Bleed for [300 - 400]% weapon damage over 5 seconds.

	Sockets (1)
    """


class Cinder_Switch(Item):
    """ Cinder Switch """
    url = r'/en/artisan/blacksmith/recipe/cinder-switch'
    type = 'axe-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage

	[25 - 50]% chance to cast a fireball when attacking.
    """


class Bastions_Revered(Item):
    """ Bastion's Revered """
    url = r'/en/item/bastions-revered-P68_Unique_Mighty_2H_004'
    type = 'mighty-weapon-2h'
    text = """

	+[946 - 1125] Strength

	+[1177 - 1439]-[1410 - 1788] Cold Damage

	Sockets (1)
	 Frenzy now stacks up to 10 times and hits an additional time per stack. Each additional hit will chain to any enemies within 15 yards, and the damage is split between all of the affected enemies.
    """


class Fury_of_the_Vanished_Peak(Item):
    """ Fury of the Vanished Peak """
    url = r'/en/item/fury-of-the-vanished-peak-P61_Unique_Mighty_2H_006'
    type = 'mighty-weapon-2h'
    text = """

	+[946 - 1125] Strength

	Gain [2500 - 3000] Life per Fury Spent
	 Reduces the Fury cost of Seismic Slam by 50% and increases its damage by 458%.
	(Barbarian Only)
	[400 - 500]%
    """


class Madawcs_Sorrow(Item):
    """ Madawc's Sorrow """
    url = r'/en/item/madawcs-sorrow-Unique_Mighty_2H_101_x1'
    type = 'mighty-weapon-2h'
    text = """

	+[946 - 1125] Strength
	 Stun enemies for 2 seconds the first time you hit them.
    """


class The_Gavel_of_Judgment(Item):
    """ The Gavel of Judgment """
    url = r'/en/item/the-gavel-of-judgment-P61_Unique_Mighty_2H_001'
    type = 'mighty-weapon-2h'
    text = """

	+[946 - 1125] Strength

	+[1177 - 1439]-[1410 - 1788] Holy Damage
	 The damage of Hammer of the Ancients is increased by 674% and it returns 25 Fury if it hits 3 or fewer enemies.
	(Barbarian Only)
	[600 - 800]%
    """


class Immortal_Kings_Boulder_Breaker(Item):
    """ Immortal King's Boulder Breaker """
    url = r'/en/item/immortal-kings-boulder-breaker-Unique_Mighty_2H_010_x1'
    type = 'mighty-weapon-2h'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Blade_of_the_Tribes(Item):
    """ Blade of the Tribes """
    url = r'/en/item/blade-of-the-tribes-P4_Unique_Mighty_2H_101'
    type = 'mighty-weapon-2h'
    text = """

	+[946 - 1125] Strength
	 Increases Earthquake Damage by [150 - 200]%
	 War Cry and Threatening Shout cause an Avalanche and Earthquake.
	(Barbarian Only)
    """


class Flail_of_the_Ascended(Item):
    """ Flail of the Ascended """
    url = r'/en/item/flail-of-the-ascended-P4_Unique_Flail_2H_002'
    type = 'flail-2h'
    text = """

	+[946 - 1125] Strength
	 Your Shield Glare deals damage equal to up to your last 5 Shield Bash casts.
	(Crusader Only)
	5
    """


class Akkhans_Addendum(Item):
    """ Akkhan's Addendum """
    url = r'/en/item/akkhans-addendum-P4_Unique_Flail_2H_001'
    type = 'flail-2h'
    text = """

	+[946 - 1125] Strength
	 Akarat's Champion gains the effects of the Prophet and Embodiment of Power runes.
	(Crusader Only)
    """


class Golden_Flense(Item):
    """ Golden Flense """
    url = r'/en/item/golden-flense-P61_Unique_Flail_2H_104'
    type = 'flail-2h'
    text = """

	+[946 - 1125] Strength
	 Sweep Attack restores 6 Wrath for each enemy hit and has its damage increased by 269%.
	(Crusader Only)
	[225 - 300]%
    """


class Baleful_Remnant(Item):
    """ Baleful Remnant """
    url = r'/en/item/baleful-remnant-Unique_Flail_2H_102_x1'
    type = 'flail-2h'
    text = """

	Sockets (1)
	 Enemies killed while Akarat's Champion is active turn into Phalanx Avatars for 10 seconds.
	(Crusader Only)
    """


class Fate_of_the_Fell(Item):
    """ Fate of the Fell """
    url = r'/en/item/fate-of-the-fell-P61_Unique_Flail_2H_103_x1'
    type = 'flail-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage

	+[946 - 1125] Strength
	 Heaven's Fury gains two additional rays and has its damage increased by 473%.
	(Crusader Only)
	[375 - 500]%
    """


class The_Mortal_Drama(Item):
    """ The Mortal Drama """
    url = r'/en/item/the-mortal-drama-Unique_Flail_2H_101_x1'
    type = 'flail-2h'
    text = """

	+[946 - 1125] Strength
	 Double the number of Bombardment impacts.
	(Crusader Only)
    """


class Flail_of_the_Charge(Item):
    """ Flail of the Charge """
    url = r'/en/item/flail-of-the-charge-P4_Unique_Flail_2H_Set_01_x1'
    type = 'flail-2h'
    text = """
	(2) Set:      Increases the duration of Steed Charge by 2 seconds. In addition, killing an enemy reduces the cooldown of Steed Charge by 1 second.     Gain 100% increased damage while using Steed Charge and for 5 seconds after it ends.
    """


class Akkhans_Leniency(Item):
    """ Akkhan's Leniency """
    url = r'/en/item/akkhans-leniency-P65_flail2H_norm_unique_01'
    type = 'flail-2h'
    text = """

	+[946 - 1125] Strength
	 Each enemy hit by your Blessed Shield increases the damage of your Blessed Shield by 37% for 3 seconds.
	(Crusader Only)
	[35 - 40]%
    """


class Arthefs_Spark_of_Life(Item):
    """ Arthef's Spark of Life """
    url = r'/en/item/arthefs-spark-of-life-Unique_Mace_2H_003_x1'
    type = 'mace-2h'
    text = """
	 Heal for 3% of your missing Life when you kill an Undead enemy.
	[3 - 4]%
    """


class Soulsmasher(Item):
    """ Soulsmasher """
    url = r'/en/item/soulsmasher-Unique_Mace_2H_104_x1'
    type = 'mace-2h'
    text = """

	+[9142 - 13,371] Life after Each Kill
	 When you kill an enemy, it explodes for 546% of your Life per Kill as damage to all enemies within 20 yards. You no longer benefit from your Life per Kill.
	[450 - 600]%
    """


class Skywarden(Item):
    """ Skywarden """
    url = r'/en/item/skywarden-Unique_Mace_2H_010_x1'
    type = 'mace-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Holy Damage
	 Every 60 seconds, gain a random Law for 60 seconds.
	(Crusader Only)
    """


class Wrath_of_the_Bone_King(Item):
    """ Wrath of the Bone King """
    url = r'/en/item/wrath-of-the-bone-king-Unique_Mace_2H_012_p1'
    type = 'mace-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Cold Damage

	Cold skills deal [25 - 30]% more damage.

	+[9142 - 13,371] Life after Each Kill
    """


class The_Furnace(Item):
    """ The Furnace """
    url = r'/en/item/the-furnace-Unique_Mace_2H_103_x1'
    type = 'mace-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage
	 Increases damage against elites by 40%.
	[40 - 50]%
    """


class Cataclysm(Item):
    """ Cataclysm """
    url = r'/en/artisan/blacksmith/recipe/cataclysm'
    type = 'mace-2h'
    text = """

	+[282 - 344]-[338 - 428] Damage

	+[3 - 5]% Damage

	Critical Hit Damage Increased by [31.0 - 35.0]% 

	[25 - 50]% chance to sunder the ground your enemies walk on when you attack.
    """


class Schaefers_Hammer(Item):
    """ Schaefer's Hammer """
    url = r'/en/item/schaefers-hammer-Unique_Mace_2H_009_p2'
    type = 'mace-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Lightning Damage

	Lightning skills deal [20 - 25]% more damage.
	 Casting a Lightning skill charges you with Lightning, causing you to deal 842% weapon damage as Lightning every second for 5 seconds to nearby enemies.
	[650 - 850]%
    """


class Sunder(Item):
    """ Sunder """
    url = r'/en/artisan/blacksmith/recipe/sunder'
    type = 'mace-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage

	[25 - 50]% chance to sunder the ground your enemies walk on when you attack.
    """


class The_Zweihander(Item):
    """ The Zweihander """
    url = r'/en/item/the-zweihander-Unique_Sword_2H_002_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Damage

	Monster kills grant +[140 - 200] experience.
    """


class Faithful_Memory(Item):
    """ Faithful Memory """
    url = r'/en/item/faithful-memory-P61_Unique_Sword_2H_012_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Holy Damage
	 Each enemy hit by Falling Sword increases the damage of Blessed Hammer by 74% for 10 seconds. Max 10 stacks.
	(Crusader Only)
	[60 - 80]%
    """


class Scourge(Item):
    """ Scourge """
    url = r'/en/item/scourge-Unique_Sword_2H_004_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Poison Damage

	Sockets (1)
	 40% chance when attacking to explode with demonic fury for 1800-2000% weapon damage as Fire.
	[20 - 45]%
    """


class Blackguard(Item):
    """ Blackguard """
    url = r'/en/item/blackguard-Unique_Sword_2H_011_x1'
    type = 'sword-2h'
    text = """

	+[6 - 10]% Damage

	+[1177 - 1439]-[1410 - 1788] Damage

	Reduces duration of control impairing effects by [20 - 40]%
    """


class Stalgards_Decimator(Item):
    """ Stalgard's Decimator """
    url = r'/en/item/stalgards-decimator-Unique_Sword_2H_101_x1'
    type = 'sword-2h'
    text = """
	 Your melee attacks throw a piercing axe at a nearby enemy, dealing 646% weapon damage as Physical.
	[550 - 700]%
    """


class The_Sultan_of_Blinding_Sand(Item):
    """ The Sultan of Blinding Sand """
    url = r'/en/item/the-sultan-of-blinding-sand-Unique_Sword_2H_008_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Holy Damage

	[20.0 - 40.0]% Chance to Blind on Hit
    """


class Blade_of_Prophecy(Item):
    """ Blade of Prophecy """
    url = r'/en/item/blade-of-prophecy-P61_Unique_Sword_2H_007_x1'
    type = 'sword-2h'
    text = """

	Reduces cooldown of all skills by [6.0 - 10.0]%.
	 Two Condemned enemies also trigger Condemn's explosion and the damage of Condemn is increased by 674%.
	(Crusader Only)
	[600 - 800]%
    """


class Warmonger(Item):
    """ Warmonger """
    url = r'/en/item/warmonger-Unique_Sword_2H_003_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Damage

	Sockets (1)
    """


class The_Grandfather(Item):
    """ The Grandfather """
    url = r'/en/item/the-grandfather-Unique_Sword_2H_001_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Damage

	+[14 - 18]% Life

	Ignores Durability Loss
    """


class Maximus(Item):
    """ Maximus """
    url = r'/en/item/maximus-Unique_Sword_2H_010_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage

	Fire skills deal [15 - 20]% more damage.
	 Chance on hit to summon a Demonic Slave.
    """


class Cams_Rebuttal(Item):
    """ Cam's Rebuttal """
    url = r'/en/item/cams-rebuttal-Unique_Sword_2H_102_x1'
    type = 'sword-2h'
    text = """
	 Falling Sword can be used again within 4 seconds before the cooldown is triggered.
	(Crusader Only)
    """


class Blood_Brother(Item):
    """ Blood Brother """
    url = r'/en/item/blood-brother-Unique_Sword_2H_103_x1'
    type = 'sword-2h'
    text = """

	+[6 - 10]% Damage
	 Grants a 17% chance to block attacks. Blocked attacks inflict 30% less damage. After blocking an attack, your next attack inflicts 30% additional damage.
	[15 - 20]%
    """


class Corrupted_Ashbringer(Item):
    """ Corrupted Ashbringer """
    url = r'/en/item/corrupted-ashbringer-Unique_Sword_2H_104_x1'
    type = 'sword-2h'
    text = """

	+[1177 - 1439]-[1410 - 1788] Poison Damage

	+[9142 - 13,371] Life after Each Kill

	+[9 - 15]% Damage to Undead
	 Chance on kill to raise a skeleton to fight for you. Upon accumulating 5 skeletons, they each explode for 1000% weapon damage and the sword transforms into Ashbringer for a short time. Attacking with Ashbringer burns your enemy for 5462% weapon damage as Holy.
	[5000 - 6000]%
    """


class Standoff(Item):
    """ Standoff """
    url = r'/en/item/standoff-P61_Unique_Polearm_01'
    type = 'polearm'
    text = """

	+[1177 - 1439]-[1410 - 1788] Cold Damage
	 Furious Charge deals increased damage equal to 428% of your bonus movement speed.
	(Barbarian Only)
	[400 - 500]%
    """


class Bovine_Bardiche(Item):
    """ Bovine Bardiche """
    url = r'/en/item/bovine-bardiche-Unique_Polearm_101_x1'
    type = 'polearm'
    text = """

	+[1177 - 1439]-[1410 - 1788] Lightning Damage
	 Chance on hit to summon a herd of murderous cows.
    """


class Heart_Slaughter(Item):
    """ Heart Slaughter """
    url = r'/en/item/heart-slaughter-Unique_Polearm_003_p1'
    type = 'polearm'
    text = """

	Physical skills deal [25 - 30]% more damage.

	+[1177 - 1439]-[1410 - 1788] Damage

	+[9142 - 13,371] Life after Each Kill
    """


class Vigilance(Item):
    """ Vigilance """
    url = r'/en/item/vigilance-Unique_Polearm_001_x1'
    type = 'polearm'
    text = """

	+[1177 - 1439]-[1410 - 1788] Holy Damage
	 Getting hit has a chance to automatically cast Inner Sanctuary.
    """


class Staff_of_Chiroptera(Item):
    """ Staff of Chiroptera """
    url = r'/en/item/staff-of-chiroptera-P61_Unique_Staff_001'
    type = 'staff'
    text = """
	 Firebats attacks 100% faster, costs 75% less Mana, and has its damage increased by 145%.
	(Witch Doctor Only)
	[125 - 150]%
    """


class The_Broken_Staff(Item):
    """ The Broken Staff """
    url = r'/en/item/the-broken-staff-Unique_Staff_001_x1'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Lightning Damage

	Sockets (1)

	Ignores Durability Loss
    """


class The_Smoldering_Core(Item):
    """ The Smoldering Core """
    url = r'/en/item/the-smoldering-core-Unique_Staff_103_x1'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage

	Sockets (1)
	 Lesser enemies are now lured to your Meteor impact areas.
	(Wizard Only)
    """


class Valtheks_Rebuke(Item):
    """ Valthek's Rebuke """
    url = r'/en/item/valtheks-rebuke-Unique_Staff_102_x1'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Arcane Damage

	Sockets (1)
	 Energy Twister now travels in a straight path.
	(Wizard Only)
    """


class SuWong_Diviner(Item):
    """ SuWong Diviner """
    url = r'/en/item/suwong-diviner-Unique_Staff_104_x1'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage
	 Increases Acid Cloud Damage by [75 - 100]%

	+[6 - 10]% Damage
	 Acid Cloud gains the effect of the Lob Blob Bomb rune.
	(Witch Doctor Only)
    """


class Ahavarion_Spear_of_Lycander(Item):
    """ Ahavarion, Spear of Lycander """
    url = r'/en/item/ahavarion-spear-of-lycander-Unique_Staff_101_x1'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Holy Damage

	Sockets (1)
	 Chance on killing a demon to gain a random Shrine effect.
    """


class The_Magi(Item):
    """ The Magi """
    url = r'/en/artisan/blacksmith/recipe/the-magi'
    type = 'staff'
    text = """

	+[64 - 78]-[77 - 97] Arcane Damage

	Reduces duration of control impairing effects by [7 - 12]%
    """


class Wormwood(Item):
    """ Wormwood """
    url = r'/en/item/wormwood-P2_Unique_Staff_003'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Poison Damage

	Poison skills deal [20 - 25]% more damage.
	 Locust Swarm continuously plagues enemies around you.
	(Witch Doctor Only)
    """


class Maloths_Focus(Item):
    """ Maloth's Focus """
    url = r'/en/item/maloths-focus-Unique_Staff_006_x1'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage
	 Enemies occasionally flee at the sight of this staff.
    """


class The_Tormentor(Item):
    """ The Tormentor """
    url = r'/en/item/the-tormentor-Unique_Staff_007_x1'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Arcane Damage
	 Chance to charm enemies when you hit them.
    """


class The_Grand_Vizier(Item):
    """ The Grand Vizier """
    url = r'/en/item/the-grand-vizier-P61_Unique_Staff_009'
    type = 'staff'
    text = """

	+[1177 - 1439]-[1410 - 1788] Fire Damage
	 Reduces the Arcane Power cost of Meteor by 50% and increases its damage by 328%.
	(Wizard Only)
	[300 - 400]%
    """


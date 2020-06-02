class Item(object):

    def get_stat_potential(self):
        print('own url', self.url)
        #https://eu.diablo3.com/en/item/axe-2h/
        pass

    def recognize(self):
        print('recognizing')
        print(self.text)
        pass

class Set(object):
    items = False
    levels = dict

    def yield_bonus(self, amount):
        bonusses = []
        for level, bonus in self.levels.items():
            if level <= amount:
                bonusses.append(bonus)
        return bonusses



class Set_Item(Item):
    set = False



class The_Legacy_of_Raekor(Set):
    """ The Legacy of Raekor """
    items = []
    levels = {
        2: 'Increase the damage per second of Rend by 500% and its duration to 15 seconds.',
        4: 'During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.',
        6: 'Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.',
    }


class Hellfire_Ring(Item):
    """ Hellfire Ring """
    type = 'ring'
    text = """
	+45% Experience. (4.5% at level 70)
	Chance on hit to engulf the ground in lava, dealing 200% weapon damage per second for 6 seconds.
    """


class Hellfire_Ring2(Item):
    """ Hellfire Ring """
    type = 'ring'
    text = """

	+[300 - 329] Strength

	+35% Experience. (3.5% at level 70)

	Chance to launch an explosive ball of Hellfire when you attack.
    """


class Band_of_Might(Item):
    """ Band of Might """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 After casting Furious Charge, Ground Stomp, or Leap, take 74% reduced damage for 8 seconds.
	(Barbarian Only)
	[60 - 80]%
    """


class Circle_of_Nailujs_Evol(Item):
    """ Circle of Nailuj's Evol """
    type = 'ring'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 
	 You now raise an additional Skeletal Mage with each cast and they last an additional 4 seconds.
	(Necromancer Only)
	[2 - 4]
    """


class Ring_of_Royal_Grandeur(Item):
    """ Ring of Royal Grandeur """
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[7737 - 9214] Life per Hit

	Reduces the number of items needed for set bonuses by 1 (to a minimum of 2).
    """


class Pandemonium_Loop(Item):
    """ Pandemonium Loop """
    type = 'ring'
    text = """
	 Enemies slain while Feared die in a bloody explosion and cause other nearby enemies to flee in Fear.
    """


class Avarice_Band(Item):
    """ Avarice Band """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[32 - 35]% Extra Gold from Monsters
	 Each time you pick up gold, increase your Gold and Health Pickup radius by 1 yard for 10 seconds, stacking up to 30 times.
    """


class Leorics_Signet(Item):
    """ Leoric's Signet """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[20 - 30]% Experience. ([2.0 - 3.0]% at level 70)
    """


class Pandemonium_Loop(Item):
    """ Pandemonium Loop """
    type = 'ring'
    text = """
	 Enemies slain while Feared die in a bloody explosion for 800% weapon damage and cause other nearby enemies to flee in Fear.
    """


class Manald_Heal(Item):
    """ Manald Heal """
    type = 'ring'
    text = """
	 Enemies stunned with Paralysis also take 13,462% weapon damage as Lightning.
	(Wizard Only)
	[13,000 - 14,000]%
    """


class Broken_Promises(Item):
    """ Broken Promises """
    type = 'ring'
    text = """

	Reduces all resource costs by [5.0 - 8.0]%.
	 After 5 consecutive non-critical hits, your chance to critically hit is increased to 100% for 3 seconds.
	3
    """


class Puzzle_Ring(Item):
    """ Puzzle Ring """
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[32 - 35]% Extra Gold from Monsters
	 Summon a treasure goblin who picks up normal-quality items for you. After picking up 16 items, he drops a rare item with a chance for a legendary.
	[12 - 16]
    """


class Halo_of_Karini(Item):
    """ Halo of Karini """
    type = 'ring'
    text = """

	Sockets (1)
	 You take 74% less damage for 5 seconds after your Storm Armor electrocutes an enemy more than 15 yards away.
	(Wizard Only)
	[60 - 80]%
    """


class The_Tall_Mans_Finger(Item):
    """ The Tall Man's Finger """
    type = 'ring'
    text = """
	 Zombie Dogs instead summons a single gargantuan dog with more damage and health than all other dogs combined.
	(Witch Doctor Only)
    """


class Rechels_Ring_of_Larceny(Item):
    """ Rechel's Ring of Larceny """
    type = 'ring'
    text = """

	[1.0 - 5.1]% Chance to Fear on Hit
	 Gain 57% increased movement speed for 4 seconds after Fearing an enemy.
	[45 - 60]%
    """


class Arcstone(Item):
    """ Arcstone """
    type = 'ring'
    text = """
	 Lightning pulses periodically between all wearers of this item, dealing 1350% weapon damage.
	[1000 - 1500]%
    """


class Band_of_the_Rue_Chambers(Item):
    """ Band of the Rue Chambers """
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Your Spirit Generators generate 40% more Spirit.
	(Monk Only)
	[40 - 50]%
    """


class Rogars_Huge_Stone(Item):
    """ Rogar's Huge Stone """
    type = 'ring'
    text = """
	 Increase your Life per Second by up to 95% based on your missing Life.
	[75 - 100]%
    """


class Wyrdward(Item):
    """ Wyrdward """
    type = 'ring'
    text = """
	 Lightning damage has a 25% chance to Stun for 1.5 seconds.
	[25 - 35]%
    """


class The_Short_Mans_Finger(Item):
    """ The Short Man's Finger """
    type = 'ring'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 
	 Gargantuan instead summons three smaller gargantuans that have their damage increased by 596%.
	(Witch Doctor Only)
	[500 - 650]%
    """


class Lornelles_Sunstone(Item):
    """ Lornelle's Sunstone """
    type = 'ring'
    text = """
	 Your damage reduction is increased by 0.89% for every 1% Life you are missing.
	(Necromancer Only)
	[0.75 - 0.95]%
    """


class Nagelring(Item):
    """ Nagelring """
    type = 'ring'
    text = """
	 Summons a Fallen Lunatic to your side every 10 seconds.
	[10 - 12]
    """


class Obsidian_Ring_of_the_Zodiac(Item):
    """ Obsidian Ring of the Zodiac """
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
    type = 'ring'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 
	 You drain life from enemies around you.
    """


class Eternal_Union(Item):
    """ Eternal Union """
    type = 'ring'
    text = """
	 Increases the duration of Phalanx avatars by 200%.
	(Crusader Only)
    """


class Krysbins_Sentence(Item):
    """ Krysbin's Sentence """
    type = 'ring'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 You deal 95% increased damage against slowed enemies or triple this bonus against enemies afflicted by any other type of control-impairing effect.
	(Necromancer Only)
	[75 - 100]%
    """


class Halo_of_Arlyse(Item):
    """ Halo of Arlyse """
    type = 'ring'
    text = """

	Sockets (1)
	 Your Ice Armor now reduces damage from melee attacks by 50% and automatically casts Frost Nova whenever you take 10% of your Life in damage.
	(Wizard Only)
	[50 - 60]%
    """


class Convention_of_Elements(Item):
    """ Convention of Elements """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Sockets (1)
	 Gain 179% increased damage to a single element for 4 seconds. This effect rotates through the elements available to your class in the following order: Arcane, Cold, Fire, Holy, Lightning, Physical, Poison.
	[150 - 200]%
    """


class Litany_of_the_Undaunted(Item):
    """ Litany of the Undaunted """
    type = 'ring'
    text = """
	(2) Set:      While this is your only Item Set bonus every Ancient item you have equipped increases your damage dealt by 750% and reduces your damage taken by 4%.
    """


class The_Compass_Rose(Item):
    """ The Compass Rose """
    type = 'ring'
    text = """
	(2) Set:      While moving, damage taken is reduced by up to 50%.     While standing still, damage dealt is increased by up to 100%.
    """


class The_Wailing_Host(Item):
    """ The Wailing Host """
    type = 'ring'
    text = """
	(2) Set:      While this is your only Item Set bonus every Ancient item you have equipped increases your damage dealt by 750% and reduces your damage taken by 4%.
    """


class Skull_Grasp(Item):
    """ Skull Grasp """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Increase the damage of Whirlwind by 328%
	(Barbarian Only)
	[300 - 400]%
    """


class Band_of_Hollow_Whispers(Item):
    """ Band of Hollow Whispers """
    type = 'ring'
    text = """
	 This ring occasionally haunts nearby enemies.
    """


class Ring_of_Emptiness(Item):
    """ Ring of Emptiness """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 You deal 279% increased damage to enemies affected by either your Haunt or Locust Swarm.
	(Witch Doctor Only)
	[250 - 300]%
    """


class Kredes_Flame(Item):
    """ Krede's Flame """
    type = 'ring'
    text = """
	 Taking Fire damage restores your primary resource.
    """


class Elusive_Ring(Item):
    """ Elusive Ring """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 After casting Shadow Power, Smoke Screen, or Vault, take 50% reduced damage for 8 seconds.
	(Demon Hunter Only)
	[50 - 60]%
    """


class Zunimassas_Pox(Item):
    """ Zunimassa's Pox """
    type = 'ring'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Stone_of_Jordan(Item):
    """ Stone of Jordan """
    type = 'ring'
    text = """

	Increases damage against elites by [25.0 - 30.0]%

	+[120 - 150] Maximum Mana
    """


class Unity(Item):
    """ Unity """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Increases damage against elites by [12.0 - 15.0]%
	 All damage taken is split between wearers of this item.
    """


class Oculus_Ring(Item):
    """ Oculus Ring """
    type = 'ring'
    text = """

	Sockets (1)
	 Chance to create an area of focused power on killing a monster. Damage is increased by 82% while standing in the area.
	[70 - 85]%
    """


class Natalyas_Reflection(Item):
    """ Natalya's Reflection """
    type = 'ring'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Focus(Item):
    """ Focus """
    type = 'ring'
    text = """
	(2) Set:      When you hit with a resource-generating attack or primary skill, deal 50% increased damage for 5 seconds.
	(2) Set:      When you hit with a resource-spending attack, deal 50% increased damage for 5 seconds.
    """


class Briggs_Wrath(Item):
    """ Briggs' Wrath """
    type = 'ring'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Uncursed enemies are pulled to the target location when a curse is applied to them.
	(Necromancer Only)
    """


class Restraint(Item):
    """ Restraint """
    type = 'ring'
    text = """
	(2) Set:      When you hit with a resource-generating attack or primary skill, deal 50% increased damage for 5 seconds.
	(2) Set:      When you hit with a resource-spending attack, deal 50% increased damage for 5 seconds.
    """


class Hellfire_Amulet(Item):
    """ Hellfire Amulet """
    type = 'amulet'
    text = """

	+[626 - 750] Intelligence

	Sockets (1)

	Random class passive.
    """


class Squirts_Necklace(Item):
    """ Squirt's Necklace """
    type = 'amulet'
    text = """

	Critical Hit Damage Increased by [51.0 - 100.0]% 

	+[71 - 80]% Extra Gold from Monsters
	 While not taking damage, damage dealt is increased by up to 100% and damage taken is increased by up to 50%.
    """


class Moonlight_Ward(Item):
    """ Moonlight Ward """
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%

	Arcane skills deal [20 - 25]% more damage.
	 Hitting an enemy within 15 yards has a chance to ward you with shards of Arcane energy that explode when enemies get close, dealing 320% weapon damage as Arcane to enemies within 15 yards.
	[240 - 320]%
    """


class Overwhelming_Desire(Item):
    """ Overwhelming Desire """
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Chance on hit to charm the enemy. While charmed, the enemy takes 35% increased damage.
    """


class Golden_Gorget_of_Leoric(Item):
    """ Golden Gorget of Leoric """
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%

	+[91 - 100] Resistance to All Elements
	 After earning a massacre bonus, 6 Skeletons are summoned to fight by your side for 10 seconds.
	[4 - 6]
    """


class Wisdom_of_Kalan(Item):
    """ Wisdom of Kalan """
    type = 'amulet'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Increases the maximum stacks of Bone Armor by 5.
	(Necromancer Only)
	5
    """


class Talisman_of_Aranoch(Item):
    """ Talisman of Aranoch """
    type = 'amulet'
    text = """
	 Prevent all Cold damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class Eye_of_Etlich(Item):
    """ Eye of Etlich """
    type = 'amulet'
    text = """

	Reduces damage from ranged attacks by [6.0 - 30.1]%.
    """


class Rondals_Locket(Item):
    """ Rondal's Locket """
    type = 'amulet'
    text = """

	Increases Gold and Health Pickup by [4 - 6] Yards.

	Health Globes and Potions Grant +[20,001 - 29,713] Life.
    """


class Dovu_Energy_Trap(Item):
    """ Dovu Energy Trap """
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Increases duration of Stun effects by 22%.
	[20 - 25]%
    """


class Ancestors_Grace(Item):
    """ Ancestors' Grace """
    type = 'amulet'
    text = """

	+[626 - 750] Vitality
	 When receiving fatal damage, you are instead restored to 100% of maximum Life and resources. This item is destroyed in the process.
    """


class Countess_Julias_Cameo(Item):
    """ Countess Julia's Cameo """
    type = 'amulet'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Prevent all Arcane damage taken and heal yourself for 22% of the amount prevented.
	[20 - 25]%
    """


class Rakoffs_Glass_of_Life(Item):
    """ Rakoff's Glass of Life """
    type = 'amulet'
    text = """

	Health Globes and Potions Grant +[20,001 - 29,713] Life.
	 Enemies you kill have a 3% additional chance to drop a health globe.
	[3 - 4]%
    """


class The_Ess_of_Johan(Item):
    """ The Ess of Johan """
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Chance on hit to pull in enemies toward your target and Slow them by 60%.
	[60 - 80]%
    """


class Haunt_of_Vaxo(Item):
    """ Haunt of Vaxo """
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Summons shadow clones to your aid when you Stun an enemy. This effect may occur once every 30 seconds.
	30
    """


class The_Flavor_of_Time(Item):
    """ The Flavor of Time """
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.

	+[10 - 12]% Movement Speed
	 Pylon effects last twice as long.
    """


class Kymbos_Gold(Item):
    """ Kymbo's Gold """
    type = 'amulet'
    text = """
	 Picking up gold heals you for an amount equal to the gold that was picked up.
    """


class The_Travelers_Pledge(Item):
    """ The Traveler's Pledge """
    type = 'amulet'
    text = """
	(2) Set:      While moving, damage taken is reduced by up to 50%.     While standing still, damage dealt is increased by up to 100%.
    """


class Tal_Rashas_Allegiance(Item):
    """ Tal Rasha's Allegiance """
    type = 'amulet'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Maras_Kaleidoscope(Item):
    """ Mara's Kaleidoscope """
    type = 'amulet'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Prevent all Poison damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class Blackthornes_Duncraig_Cross(Item):
    """ Blackthorne's Duncraig Cross """
    type = 'amulet'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class The_Star_of_Azkaranth(Item):
    """ The Star of Azkaranth """
    type = 'amulet'
    text = """

	Reduces cooldown of all skills by [5.0 - 8.0]%.
	 Prevent all Fire damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class Xephirian_Amulet(Item):
    """ Xephirian Amulet """
    type = 'amulet'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Prevent all Lightning damage taken and heal yourself for 12% of the amount prevented.
	[10 - 15]%
    """


class The_Johnstone(Item):
    """ The Johnstone """
    type = 'amulet'
    text = """

	Critical Hit Damage Increased by [51.0 - 100.0]% 
	 When Land of the Dead expires, you are granted 50 stacks of Macabre Knowledge. Macabre Knowledge increases the damage of Corpse Lance and Corpse Explosion by 179%.
	(Necromancer Only)
	[150 - 200]%
    """


class Halcyons_Ascent(Item):
    """ Halcyon's Ascent """
    type = 'amulet'
    text = """

	Sockets (1)
    """


class Haunted_Visions(Item):
    """ Haunted Visions """
    type = 'amulet'
    text = """

	Sockets (1)
	 Simulacrum now drains 5% of your maximum life every second and lasts twice as long.
	(Necromancer Only)
	5%
    """


class Sunwukos_Shines(Item):
    """ Sunwuko's Shines """
    type = 'amulet'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Talisman_of_Akkhan(Item):
    """ Talisman of Akkhan """
    type = 'amulet'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Leorics_Crown(Item):
    """ Leoric's Crown """
    type = 'helm'
    text = """

	Sockets (1)

	Increase the effect of any gem socketed into this item by [75 - 100]%. This effect does not apply to Legendary Gems.
    """


class Prides_Fall(Item):
    """ Pride's Fall """
    type = 'helm'
    text = """

	+[626 - 750] Vitality

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your resource costs are reduced by 30% after not taking damage for 5 seconds.
    """


class Broken_Crown(Item):
    """ Broken Crown """
    type = 'helm'
    text = """

	Sockets (1)
	 Whenever a gem drops, a gem of the type socketed into your helmet also drops. This effect does not apply to Legendary Gems.
    """


class Cains_Memory(Item):
    """ Cain's Memory """
    type = 'helm'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Deathseers_Cowl(Item):
    """ Deathseer's Cowl """
    type = 'helm'
    text = """

	Sockets (1)
	 19% chance on being hit by an Undead enemy to charm it for 2 seconds.
	[15 - 20]%
    """


class Warhelm_of_Kassar(Item):
    """ Warhelm of Kassar """
    type = 'helm'
    text = """

	Sockets (1)
	 Reduce the cooldown and increase the damage of Phalanx by 49%.
	(Crusader Only)
	[45 - 60]%
    """


class Visage_of_Gunes(Item):
    """ Visage of Gunes """
    type = 'helm'
    text = """

	Sockets (1)
	 Vengeance gains the effect of the Dark Heart rune.
	(Demon Hunter Only)
    """


class Mask_of_Scarlet_Death(Item):
    """ Mask of Scarlet Death """
    type = 'helm'
    text = """

	Sockets (1)
	 Revive now consumes all corpses to raise a minion that deals 135% more damage per corpse.
	(Necromancer Only)
	[125 - 150]%
    """


class Aughilds_Peak(Item):
    """ Aughild's Peak """
    type = 'helm'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Skull_of_Resonance(Item):
    """ Skull of Resonance """
    type = 'helm'
    text = """

	+[91 - 100] Resistance to All Elements

	Sockets (1)
	 Threatening Shout has a chance to Charm enemies and cause them to join your side.
	(Barbarian Only)
    """


class Guardians_Foresight(Item):
    """ Guardian's Foresight """
    type = 'helm'
    text = """
	(2) Set:      +110 Vitality     Regenerates 130 Life per Second
    """


class Mempo_of_Twilight(Item):
    """ Mempo of Twilight """
    type = 'helm'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[91 - 100] Resistance to All Elements

	Sockets (1)
    """


class Natalyas_Sight(Item):
    """ Natalya's Sight """
    type = 'helm'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Tal_Rashas_Guise_of_Wisdom(Item):
    """ Tal Rasha's Guise of Wisdom """
    type = 'helm'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Sages_Orbit(Item):
    """ Sage's Orbit """
    type = 'helm'
    text = """
	(2) Set:      +35 Strength     +35 Dexterity     +35 Intelligence     +35 Vitality
    """


class Immortal_Kings_Triumph(Set_Item):
    """ Immortal King's Triumph """
    type = 'helm'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Andariels_Visage(Item):
    """ Andariel's Visage """
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
    type = 'helm'
    text = """

	Sockets (1)
	 Army of the Dead deals an additional 207% damage and gains the effect of the Unconventional Warfare rune.
	(Necromancer Only)
	[200 - 250]%
    """


class Jade_Harvesters_Wisdom(Item):
    """ Jade Harvester's Wisdom """
    type = 'helm'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Guardians_Gaze(Item):
    """ Guardian's Gaze """
    type = 'helm'
    text = """
	(2) Set:      +250 Vitality     Regenerates 8000 Life per Second
	(3) Set:      +15% Movement Speed
    """


class Sunwukos_Crown(Item):
    """ Sunwuko's Crown """
    type = 'helm'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Sages_Apogee(Item):
    """ Sage's Apogee """
    type = 'helm'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Vyrs_Sightless_Skull(Item):
    """ Vyr's Sightless Skull """
    type = 'helm'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Cains_Insight(Item):
    """ Cain's Insight """
    type = 'helm'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class Crown_of_the_Invoker(Item):
    """ Crown of the Invoker """
    type = 'helm'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Aughilds_Spike(Item):
    """ Aughild's Spike """
    type = 'helm'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class The_Shadows_Mask(Item):
    """ The Shadow's Mask """
    type = 'helm'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Eyes_of_the_Earth(Item):
    """ Eyes of the Earth """
    type = 'helm'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Raekors_Will(Set_Item):
    """ Raekor's Will """
    set = The_Legacy_of_Raekor
    type = 'helm'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Helm_of_the_Wastes(Item):
    """ Helm of the Wastes """
    type = 'helm'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Skull_of_Savages(Item):
    """ Skull of Savages """
    type = 'helm'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Crown_of_the_Light(Item):
    """ Crown of the Light """
    type = 'helm'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Crown_of_Valor(Item):
    """ Crown of Valor """
    type = 'helm'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Rolands_Visage(Item):
    """ Roland's Visage """
    type = 'helm'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Helm_of_Akkhan(Item):
    """ Helm of Akkhan """
    type = 'helm'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Accursed_Visage(Item):
    """ Accursed Visage """
    type = 'helm'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Visage(Item):
    """ Marauder's Visage """
    type = 'helm'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Mask_of_the_Searing_Sky(Item):
    """ Mask of the Searing Sky """
    type = 'helm'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Ulianas_Spirit(Item):
    """ Uliana's Spirit """
    type = 'helm'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Decree_of_Justice(Item):
    """ Decree of Justice """
    type = 'helm'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Firebirds_Plume(Item):
    """ Firebird's Plume """
    type = 'helm'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Shrouded_Mask(Item):
    """ Shrouded Mask """
    type = 'helm'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Typhons_Frons(Item):
    """ Typhon's Frons """
    type = 'helm'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Arachyrs_Visage(Item):
    """ Arachyr's Visage """
    type = 'helm'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Helltooth_Mask(Item):
    """ Helltooth Mask """
    type = 'helm'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class TragOuls_Guise(Item):
    """ Trag'Oul's Guise """
    type = 'helm'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Inariuss_Understanding(Item):
    """ Inarius's Understanding """
    type = 'helm'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Pestilence_Mask(Item):
    """ Pestilence Mask """
    type = 'helm'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Rathmas_Skull_Helm(Item):
    """ Rathma's Skull Helm """
    type = 'helm'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Homing_Pads(Item):
    """ Homing Pads """
    type = 'shoulders'
    text = """

	+[32 - 35]% Extra Gold from Monsters
	 Your Town Portal is no longer interrupted by taking damage. While casting Town Portal you gain a protective bubble that reduces damage taken by 54%.
	[50 - 65]%
    """


class Pauldrons_of_the_Skeleton_King(Item):
    """ Pauldrons of the Skeleton King """
    type = 'shoulders'
    text = """

	+[416 - 500] Vitality

	+[373 - 397] Armor
	 When receiving fatal damage, there is a chance that you are instead restored to 25% of maximum Life and cause nearby enemies to flee in fear.
    """


class Razeths_Volition(Item):
    """ Razeth's Volition """
    type = 'shoulders'
    text = """

	Reduces all resource costs by [5.0 - 8.0]%.
	 Skeletal Mage gains the effect of the Gift of Death rune.
	(Necromancer Only)
    """


class Borns_Impunity(Item):
    """ Born's Impunity """
    type = 'shoulders'
    text = """
	(2) Set:      +2% Life     +20% Experience. (2.0% at level 70)
    """


class Death_Watch_Mantle(Item):
    """ Death Watch Mantle """
    type = 'shoulders'
    text = """
	 30% chance to explode in a fan of knives for 750-950% weapon damage when hit.
	[25 - 35]%
    """


class Corpsewhisper_Pauldrons(Item):
    """ Corpsewhisper Pauldrons """
    type = 'shoulders'
    text = """
	 Corpse Lance damage is increased by 29% for 3 seconds when you consume a corpse. Max 20 stacks.
	(Necromancer Only)
	[25 - 30]%
    """


class Lefebvres_Soliloquy(Item):
    """ Lefebvre's Soliloquy """
    type = 'shoulders'
    text = """
	 Cyclone Strike reduces your damage taken by 45% for 5 seconds.
	(Monk Only)
	[40 - 50]%
    """


class Mantle_of_Channeling(Item):
    """ Mantle of Channeling """
    type = 'shoulders'
    text = """

	+[416 - 500] Vitality
	 While channeling Whirlwind, Rapid Fire, Strafe, Tempest Rush, Firebats, Arcane Torrent, Disintegrate, or Ray of Frost for at least 1 second, you deal 24% increased damage and take 25% reduced damage.
	[20 - 25]%
    """


class Spaulders_of_Zakara(Item):
    """ Spaulders of Zakara """
    type = 'shoulders'
    text = """
	 Your items become indestructible.
    """


class Fury_of_the_Ancients(Item):
    """ Fury of the Ancients """
    type = 'shoulders'
    text = """
	 Call of the Ancients gains the effect of the Ancients' Fury rune, and your Ancients attack 100% faster.
	(Barbarian Only)
    """


class Aughilds_Reign(Item):
    """ Aughild's Reign """
    type = 'shoulders'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Ashearas_Guard(Item):
    """ Asheara's Guard """
    type = 'shoulders'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Vile_Ward(Item):
    """ Vile Ward """
    type = 'shoulders'
    text = """
	 Furious Charge deals 34% increased damage for every enemy hit while charging.
	(Barbarian Only)
	[30 - 35]%
    """


class Seven_Sins(Item):
    """ Seven Sins """
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
    type = 'shoulders'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Burden_of_the_Invoker(Item):
    """ Burden of the Invoker """
    type = 'shoulders'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Spires_of_the_Earth(Item):
    """ Spires of the Earth """
    type = 'shoulders'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Demons_Aileron(Item):
    """ Demon's Aileron """
    type = 'shoulders'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Aughilds_Power(Item):
    """ Aughild's Power """
    type = 'shoulders'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class Sunwukos_Balance(Item):
    """ Sunwuko's Balance """
    type = 'shoulders'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Corruption(Item):
    """ Corruption """
    type = 'shoulders'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.

	Health Globes and Potions Grant +[14,231 - 20,000] Life.
    """


class Jade_Harvesters_Joy(Item):
    """ Jade Harvester's Joy """
    type = 'shoulders'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Borns_Privilege(Item):
    """ Born's Privilege """
    type = 'shoulders'
    text = """
	(2) Set:      +15% Life
	(3) Set:      Reduces cooldown of all skills by 10.0%.     +20% Experience. (2.0% at level 70)
    """


class Ashearas_Custodian(Item):
    """ Asheara's Custodian """
    type = 'shoulders'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class Vyrs_Proud_Pauldrons(Item):
    """ Vyr's Proud Pauldrons """
    type = 'shoulders'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class The_Shadows_Burden(Item):
    """ The Shadow's Burden """
    type = 'shoulders'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Spines_of_Savages(Item):
    """ Spines of Savages """
    type = 'shoulders'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Raekors_Burden(Set_Item):
    """ Raekor's Burden """
    set = The_Legacy_of_Raekor
    type = 'shoulders'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Pauldrons_of_the_Wastes(Item):
    """ Pauldrons of the Wastes """
    type = 'shoulders'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Spaulders_of_Valor(Item):
    """ Spaulders of Valor """
    type = 'shoulders'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Rolands_Mantle(Item):
    """ Roland's Mantle """
    type = 'shoulders'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Mountain_of_the_Light(Item):
    """ Mountain of the Light """
    type = 'shoulders'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Pauldrons_of_Akkhan(Item):
    """ Pauldrons of Akkhan """
    type = 'shoulders'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Unsanctified_Shoulders(Item):
    """ Unsanctified Shoulders """
    type = 'shoulders'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Spines(Item):
    """ Marauder's Spines """
    type = 'shoulders'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Mantle_of_the_Upside_Down_Sinners(Item):
    """ Mantle of the Upside-Down Sinners """
    type = 'shoulders'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Ulianas_Strength(Item):
    """ Uliana's Strength """
    type = 'shoulders'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Mirrors_of_Justice(Item):
    """ Mirrors of Justice """
    type = 'shoulders'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Firebirds_Pinions(Item):
    """ Firebird's Pinions """
    type = 'shoulders'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Typhons_Tibia(Item):
    """ Typhon's Tibia """
    type = 'shoulders'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Dashing_Pauldrons_of_Despair(Item):
    """ Dashing Pauldrons of Despair """
    type = 'shoulders'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Mundunugus_Descendant(Item):
    """ Mundunugu's Descendant """
    type = 'shoulders'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Helltooth_Mantle(Item):
    """ Helltooth Mantle """
    type = 'shoulders'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Mantle(Item):
    """ Arachyr's Mantle """
    type = 'shoulders'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Pestilence_Defense(Item):
    """ Pestilence Defense """
    type = 'shoulders'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Rathmas_Spikes(Item):
    """ Rathma's Spikes """
    type = 'shoulders'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class TragOuls_Heart(Item):
    """ Trag'Oul's Heart """
    type = 'shoulders'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Inariuss_Martyrdom(Item):
    """ Inarius's Martyrdom """
    type = 'shoulders'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Heart_of_Iron(Item):
    """ Heart of Iron """
    type = 'torso'
    text = """

	+[416 - 500] Vitality

	+[5334 - 7696] Thorns Damage
	 Gain Thorns equal to 257% of your Vitality.
	[250 - 300]%
    """


class Borns_Heart_of_Steel(Item):
    """ Born's Heart of Steel """
    type = 'torso'
    text = """
	(2) Set:      +2% Life     +20% Experience. (2.0% at level 70)
    """


class Aquila_Cuirass(Item):
    """ Aquila Cuirass """
    type = 'torso'
    text = """

	Sockets (3)
	 While above 94% primary resource, all damage taken is reduced by 50%.
	[90 - 95]%
    """


class Chaingmail(Item):
    """ Chaingmail """
    type = 'torso'
    text = """

	+[91 - 100] Resistance to All Elements
	 After earning a survival bonus, quickly heal to full Life.
    """


class Shi_Mizus_Haori(Item):
    """ Shi Mizu's Haori """
    type = 'torso'
    text = """
	 While below 24% Life, all attacks are guaranteed Critical Hits.
	[20 - 25]%
    """


class Cindercoat(Item):
    """ Cindercoat """
    type = 'torso'
    text = """

	Fire skills deal [15 - 20]% more damage.
	 Reduces the resource cost of Fire skills by 27%.
	[23 - 30]%
    """


class Aughilds_Dominion(Item):
    """ Aughild's Dominion """
    type = 'torso'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Goldskin(Item):
    """ Goldskin """
    type = 'torso'
    text = """

	+[91 - 100] Resistance to All Elements

	+100% Extra Gold from Monsters
	 Chance for enemies to drop gold when you hit them.
    """


class Zunimassas_Marrow(Item):
    """ Zunimassa's Marrow """
    type = 'torso'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Immortal_Kings_Eternal_Reign(Item):
    """ Immortal King's Eternal Reign """
    type = 'torso'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Blackthornes_Surcoat(Item):
    """ Blackthorne's Surcoat """
    type = 'torso'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Demons_Heart(Item):
    """ Demon's Heart """
    type = 'torso'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Tal_Rashas_Relentless_Pursuit(Item):
    """ Tal Rasha's Relentless Pursuit """
    type = 'torso'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Tyraels_Might(Item):
    """ Tyrael's Might """
    type = 'torso'
    text = """

	+[91 - 100] Resistance to All Elements

	+[10 - 20]% Damage to Demons

	Ignores Durability Loss
    """


class Innas_Vast_Expanse(Item):
    """ Inna's Vast Expanse """
    type = 'torso'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Robes_of_the_Rydraelm(Item):
    """ Robes of the Rydraelm """
    type = 'torso'
    text = """

	Reduces damage from ranged attacks by 4.0%.

	Reduces damage from melee attacks by 4.0%

	Monster kills grant +[80 - 99] experience.
    """


class Bloodsong_Mail(Item):
    """ Bloodsong Mail """
    type = 'torso'
    text = """

	Sockets (3)
	 While in the Land of the Dead, Command Skeletons deals 110% additional damage and gains the effect of the Enforcer, Frenzy, Dark Mending and Freezing Grasp runes.
	(Necromancer Only)
	[100 - 125]%
    """


class Jade_Harvesters_Peace(Item):
    """ Jade Harvester's Peace """
    type = 'torso'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Demons_Marrow(Item):
    """ Demon's Marrow """
    type = 'torso'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Aughilds_Rule(Item):
    """ Aughild's Rule """
    type = 'torso'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class Armor_of_the_Kind_Regent(Item):
    """ Armor of the Kind Regent """
    type = 'torso'
    text = """
	 Smite will now also be cast at a second nearby enemy.
	(Crusader Only)
    """


class Spirit_of_the_Earth(Item):
    """ Spirit of the Earth """
    type = 'torso'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Borns_Frozen_Soul(Item):
    """ Born's Frozen Soul """
    type = 'torso'
    text = """
	(2) Set:      +15% Life
	(3) Set:      Reduces cooldown of all skills by 10.0%.     +20% Experience. (2.0% at level 70)
    """


class The_Shadows_Bane(Item):
    """ The Shadow's Bane """
    type = 'torso'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Sunwukos_Soul(Item):
    """ Sunwuko's Soul """
    type = 'torso'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Vyrs_Astonishing_Aura(Item):
    """ Vyr's Astonishing Aura """
    type = 'torso'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Cuirass_of_the_Wastes(Item):
    """ Cuirass of the Wastes """
    type = 'torso'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Markings_of_Savages(Item):
    """ Markings of Savages """
    type = 'torso'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Raekors_Heart(Set_Item):
    """ Raekor's Heart """
    set = The_Legacy_of_Raekor
    type = 'torso'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Rolands_Bearing(Item):
    """ Roland's Bearing """
    type = 'torso'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Breastplate_of_Akkhan(Item):
    """ Breastplate of Akkhan """
    type = 'torso'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Heart_of_the_Light(Item):
    """ Heart of the Light """
    type = 'torso'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Brigandine_of_Valor(Item):
    """ Brigandine of Valor """
    type = 'torso'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Marauders_Carapace(Item):
    """ Marauder's Carapace """
    type = 'torso'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Ulianas_Heart(Item):
    """ Uliana's Heart """
    type = 'torso'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Heart_of_the_Crashing_Wave(Item):
    """ Heart of the Crashing Wave """
    type = 'torso'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Lamellars_of_Justice(Item):
    """ Lamellars of Justice """
    type = 'torso'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Firebirds_Breast(Item):
    """ Firebird's Breast """
    type = 'torso'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Typhons_Thorax(Item):
    """ Typhon's Thorax """
    type = 'torso'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Harness_of_Truth(Item):
    """ Harness of Truth """
    type = 'torso'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Mundunugus_Robe(Item):
    """ Mundunugu's Robe """
    type = 'torso'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Helltooth_Tunic(Item):
    """ Helltooth Tunic """
    type = 'torso'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Carapace(Item):
    """ Arachyr's Carapace """
    type = 'torso'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class TragOuls_Scales(Item):
    """ Trag'Oul's Scales """
    type = 'torso'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Rathmas_Ribcage_Plate(Item):
    """ Rathma's Ribcage Plate """
    type = 'torso'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Pestilence_Robe(Item):
    """ Pestilence Robe """
    type = 'torso'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Inariuss_Conviction(Item):
    """ Inarius's Conviction """
    type = 'torso'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Requiem_Cereplate(Item):
    """ Requiem Cereplate """
    type = 'torso'
    text = """

	Sockets (3)
	 Devour restores an additional 85% Essence and Life. In addition, when Devour restores Essence or Life above your maximum, the excess is granted over 3 seconds.
	(Necromancer Only)
	[75 - 100]%
    """


class Ashnagarrs_Blood_Bracer(Item):
    """ Ashnagarr's Blood Bracer """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Increases the potency of your shields by 85%.
	(Wizard Only)
	[75 - 100]%
    """


class Gungdo_Gear(Item):
    """ Gungdo Gear """
    type = 'wrists'
    text = """
	 Exploding Palm's on-death explosion applies Exploding Palm.
	(Monk Only)
    """


class Cesars_Memento(Item):
    """ Cesar's Memento """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Enemies take 667% increased damage from your Tempest Rush for 5 seconds after you hit them with a Blind, Freeze, or Stun.
	(Monk Only)
	[600 - 800]%
    """


class Sanguinary_Vambraces(Item):
    """ Sanguinary Vambraces """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[2401 - 2880] Thorns Damage
	 Chance on being hit to deal 1000% of your Thorns damage to nearby enemies.
    """


class Pintos_Pride(Item):
    """ Pinto's Pride """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Wave of Light also Slows enemies by 80% for 3 seconds and deals 135% increased damage.
	(Monk Only)
	[125 - 150]%
    """


class Bindings_of_the_Lesser_Gods(Item):
    """ Bindings of the Lesser Gods """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Enemies hit by your Cyclone Strike take 157% increased damage from your Mystic Ally for 5 seconds.
	(Monk Only)
	[150 - 200]%
    """


class Akkhans_Manacles(Item):
    """ Akkhan's Manacles """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Blessed Shield damage is increased by 442% for the first enemy it hits.
	(Crusader Only)
	[400 - 500]%
    """


class Morticks_Brace(Item):
    """ Mortick's Brace """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Wrath of the Berserker gains the effect of every rune.
	(Barbarian Only)
    """


class Vambraces_of_Sescheron(Item):
    """ Vambraces of Sescheron """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your primary skills heal you for 5.5% of your missing Life.
	(Barbarian Only)
	[5.0 - 6.0]%
    """


class Bracer_of_Fury(Item):
    """ Bracer of Fury """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Heaven's Fury deals 342% increased damage to enemies that are Blinded, Immobilized, or Stunned.
	(Crusader Only)
	[300 - 400]%
    """


class Warzechian_Armguards(Item):
    """ Warzechian Armguards """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Every time you destroy a wreckable object, you gain a short burst of speed.
    """


class Nemesis_Bracers(Item):
    """ Nemesis Bracers """
    type = 'wrists'
    text = """
	 Shrines and Pylons will spawn an enemy champion.
    """


class Custerian_Wristguards(Item):
    """ Custerian Wristguards """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[32 - 35]% Extra Gold from Monsters
	 Picking up gold grants experience.
    """


class Ancient_Parthan_Defenders(Item):
    """ Ancient Parthan Defenders """
    type = 'wrists'
    text = """
	 Each stunned enemy within 25 yards reduces your damage taken by 9%.
	[9 - 12]%
    """


class Aughilds_Ultimatum(Item):
    """ Aughild's Ultimatum """
    type = 'wrists'
    text = """
	(2) Set:      Reduces damage from melee attacks by 2.0%
	(3) Set:      Reduces damage from ranged attacks by 2.0%.
    """


class Promise_of_Glory(Item):
    """ Promise of Glory """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 5% chance to spawn a Nephalem Glory globe when you Blind an enemy.
	[4 - 6]%
    """


class Guardians_Deflector(Item):
    """ Guardian's Deflector """
    type = 'wrists'
    text = """
	(2) Set:      +110 Vitality     Regenerates 130 Life per Second
    """


class Wondrous_Deflectors(Item):
    """ Wondrous Deflectors """
    type = 'wrists'
    text = """

	Regenerates [1128 - 2842] Life per Second

	Reduces damage from ranged attacks by 4.0%.

	+[316 - 1160] Thorns Damage
    """


class Strongarm_Bracers(Item):
    """ Strongarm Bracers """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%

	+[416 - 500] Vitality
	 Enemies hit by knockbacks suffer 25% increased damage for 6 seconds.
	[20 - 30]%
    """


class Demons_Revenge(Item):
    """ Demon's Revenge """
    type = 'wrists'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Lacuni_Prowlers(Item):
    """ Lacuni Prowlers """
    type = 'wrists'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%

	+[10 - 12]% Movement Speed

	+[2401 - 2880] Thorns Damage
    """


class Coils_of_the_First_Spider(Item):
    """ Coils of the First Spider """
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
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your Hatred Generators reduce your damage taken by 45% for 5 seconds.
	(Demon Hunter Only)
	[40 - 50]%
    """


class Jerams_Bracers(Item):
    """ Jeram's Bracers """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Wall of Death deals 85% increased damage and can be cast up to three times within 2 seconds before the cooldown begins.
	(Witch Doctor Only)
	[75 - 100]%
    """


class Bracers_of_the_First_Men(Item):
    """ Bracers of the First Men """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Hammer of the Ancients attacks 50% faster and deals 445% increased damage.
	(Barbarian Only)
	[375 - 500]%
    """


class Ranslors_Folly(Item):
    """ Ranslor's Folly """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 The damage of Energy Twister is increased by 249% and it periodically pulls in lesser enemies within 30 yards.
	(Wizard Only)
	[225 - 300]%
    """


class Guardians_Aversion(Item):
    """ Guardian's Aversion """
    type = 'wrists'
    text = """
	(2) Set:      +250 Vitality     Regenerates 8000 Life per Second
	(3) Set:      +15% Movement Speed
    """


class Bracers_of_Destruction(Item):
    """ Bracers of Destruction """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Seismic Slam deals 442% increased damage to the first 10 enemies it hits.
	(Barbarian Only)
	[400 - 500]%
    """


class Gabriels_Vambraces(Item):
    """ Gabriel's Vambraces """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 When your Blessed Hammer hits 3 or fewer enemies, 85% of its Wrath Cost is refunded.
	(Crusader Only)
	[75 - 100]%
    """


class TragOul_Coils(Item):
    """ Trag'Oul Coils """
    type = 'wrists'
    text = """
	 Spike Traps gain the Impaling Spines rune and are deployed twice as fast.
	(Demon Hunter Only)
    """


class Drakons_Lesson(Item):
    """ Drakon's Lesson """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 When your Shield Bash hits 3 or fewer enemies, its damage is increased by 342% and 25% of its Wrath Cost is refunded.
	(Crusader Only)
	[300 - 400]%
    """


class Aughilds_Search(Item):
    """ Aughild's Search """
    type = 'wrists'
    text = """
	(2) Set:      Reduces damage taken by 15%.     Increases damage dealt by 30%.
	(3) Set:      Reduces damage from elites by 30.0%     Increases damage against elites by 30.0%
    """


class Shackles_of_the_Invoker(Item):
    """ Shackles of the Invoker """
    type = 'wrists'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Krelms_Buff_Bracers(Item):
    """ Krelm's Buff Bracers """
    type = 'wrists'
    text = """
	(2) Set:      +500 Vitality
    """


class Reapers_Wraps(Item):
    """ Reaper's Wraps """
    type = 'wrists'
    text = """

	Health globes restore [25 - 30]% of your primary resource.
    """


class Demons_Animus(Item):
    """ Demon's Animus """
    type = 'wrists'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Lakumbas_Ornament(Item):
    """ Lakumba's Ornament """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Reduce all damage taken by 6% for each stack of Soul Harvest you have.
	(Witch Doctor Only)
	6%
    """


class Spirit_Guards(Item):
    """ Spirit Guards """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Your Spirit Generators reduce your damage taken by 49% for 3 seconds.
	(Monk Only)
	[45 - 60]%
    """


class Skulars_Salvation(Item):
    """ Skular's Salvation """
    type = 'wrists'
    text = """

	Critical Hit Chance Increased by [4.5 - 6.0]%
	 Increase the damage of Ancient Spear - Boulder Toss by 100%. When your Boulder Toss hits 5 or fewer enemies, the damage is increased by 145%.
	(Barbarian Only)
	[120 - 150]%
    """


class Gloves_of_Worship(Item):
    """ Gloves of Worship """
    type = 'hands'
    text = """

	Critical Hit Damage Increased by [26.0 - 50.0]% 

	+[7737 - 9214] Life per Hit
	 Shrine effects last for 10 minutes.
    """


class Grasps_of_Essence(Item):
    """ Grasps of Essence """
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 When an exploded corpse damages at least one enemy, your Corpse Explosion deals 85% increased damage for 6 seconds, stacking up to 5 times.
	(Necromancer Only)
	[75 - 100]%
    """


class Cains_Scribe(Item):
    """ Cain's Scribe """
    type = 'hands'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Stone_Gauntlets(Item):
    """ Stone Gauntlets """
    type = 'hands'
    text = """
	 Getting hit increases your armor by 50%, but reduces your movement speed by 15% and attack speed by 20%. This effect stacks up to 5 times.
    """


class St_Archews_Gage(Item):
    """ St. Archew's Gage """
    type = 'hands'
    text = """
	 The first time an elite pack damages you, gain an absorb shield equal to 145% of your maximum Life for 10 seconds.
	[120 - 150]%
    """


class Magefist(Item):
    """ Magefist """
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Fire skills deal 19% increased damage.
	[15 - 20]%
    """


class Pendergrasps(Item):
    """ Pendergrasps """
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [4.0 - 5.0]%

	Reduces duration of control impairing effects by [7 - 12]%
    """


class Moribund_Gauntlets(Item):
    """ Moribund Gauntlets """
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Your Golem sheds a corpse every second.
	(Necromancer Only)
    """


class Gladiator_Gauntlets(Item):
    """ Gladiator Gauntlets """
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 After earning a massacre bonus, gold rains from sky.
    """


class Ashearas_Iron_Fist(Item):
    """ Asheara's Iron Fist """
    type = 'hands'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Zunimassas_Finger_Wraps(Item):
    """ Zunimassa's Finger Wraps """
    type = 'hands'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Sages_Gesture(Item):
    """ Sage's Gesture """
    type = 'hands'
    text = """
	(2) Set:      +35 Strength     +35 Dexterity     +35 Intelligence     +35 Vitality
    """


class Frostburn(Item):
    """ Frostburn """
    type = 'hands'
    text = """

	Critical Hit Chance Increased by [8.0 - 10.0]%
	 Cold skills deal 19% increased damage and have a 50% chance to Freeze enemies.
	[15 - 20]%
    """


class Tasker_and_Theo(Item):
    """ Tasker and Theo """
    type = 'hands'
    text = """

	Attack Speed Increased by [5.0 - 7.0]%
	 Increase attack speed of your pets by 45%.
	[40 - 50]%
    """


class Natalyas_Touch(Item):
    """ Natalya's Touch """
    type = 'hands'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Immortal_Kings_Irons(Item):
    """ Immortal King's Irons """
    type = 'hands'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Innas_Hold(Item):
    """ Inna's Hold """
    type = 'hands'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Tal_Rashas_Grasp(Item):
    """ Tal Rasha's Grasp """
    type = 'hands'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Cains_Scrivener(Item):
    """ Cain's Scrivener """
    type = 'hands'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class The_Shadows_Grasp(Item):
    """ The Shadow's Grasp """
    type = 'hands'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Sunwukos_Paws(Item):
    """ Sunwuko's Paws """
    type = 'hands'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Ashearas_Ward(Item):
    """ Asheara's Ward """
    type = 'hands'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class Pride_of_the_Invoker(Item):
    """ Pride of the Invoker """
    type = 'hands'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Jade_Harvesters_Mercy(Item):
    """ Jade Harvester's Mercy """
    type = 'hands'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Pull_of_the_Earth(Item):
    """ Pull of the Earth """
    type = 'hands'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Vyrs_Grasping_Gauntlets(Item):
    """ Vyr's Grasping Gauntlets """
    type = 'hands'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Sages_Purchase(Item):
    """ Sage's Purchase """
    type = 'hands'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Raekors_Wraps(Set_Item):
    """ Raekor's Wraps """
    set = The_Legacy_of_Raekor
    type = 'hands'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Gauntlet_of_the_Wastes(Item):
    """ Gauntlet of the Wastes """
    type = 'hands'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Claws_of_Savages(Item):
    """ Claws of Savages """
    type = 'hands'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Gauntlets_of_Valor(Item):
    """ Gauntlets of Valor """
    type = 'hands'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Rolands_Grasp(Item):
    """ Roland's Grasp """
    type = 'hands'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Gauntlets_of_Akkhan(Item):
    """ Gauntlets of Akkhan """
    type = 'hands'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Will_of_the_Light(Item):
    """ Will of the Light """
    type = 'hands'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Fiendish_Grips(Item):
    """ Fiendish Grips """
    type = 'hands'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Gloves(Item):
    """ Marauder's Gloves """
    type = 'hands'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Ulianas_Fury(Item):
    """ Uliana's Fury """
    type = 'hands'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Fists_of_Thunder(Item):
    """ Fists of Thunder """
    type = 'hands'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Bazubands_of_Justice(Item):
    """ Bazubands of Justice """
    type = 'hands'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Fierce_Gauntlets(Item):
    """ Fierce Gauntlets """
    type = 'hands'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Typhons_Claws(Item):
    """ Typhon's Claws """
    type = 'hands'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Firebirds_Talons(Item):
    """ Firebird's Talons """
    type = 'hands'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Arachyrs_Claws(Item):
    """ Arachyr's Claws """
    type = 'hands'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Mundunugus_Rhythm(Item):
    """ Mundunugu's Rhythm """
    type = 'hands'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Helltooth_Gauntlets(Item):
    """ Helltooth Gauntlets """
    type = 'hands'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class TragOuls_Claws(Item):
    """ Trag'Oul's Claws """
    type = 'hands'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Pestilence_Gloves(Item):
    """ Pestilence Gloves """
    type = 'hands'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Rathmas_Macabre_Vambraces(Item):
    """ Rathma's Macabre Vambraces """
    type = 'hands'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Inariuss_Will(Item):
    """ Inarius's Will """
    type = 'hands'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Saffron_Wrap(Item):
    """ Saffron Wrap """
    type = 'waist'
    text = """
	 The damage of your next Overpower is increased by 45% for each enemy hit. Max 20 enemies.
	(Barbarian Only)
	[40 - 50]%
    """


class Goldwrap(Item):
    """ Goldwrap """
    type = 'waist'
    text = """

	+[32 - 35]% Extra Gold from Monsters
	 On gold pickup: Gain armor for 5 seconds equal to the amount picked up.
    """


class Hellcat_Waistguard(Item):
    """ Hellcat Waistguard """
    type = 'waist'
    text = """
	 Grenades have a chance to bounce 4 times dealing an additional 50% damage on each bounce. This bonus is increased to 800% on the final bounce.
	(Demon Hunter Only)
	[3 - 5]
    """


class Insatiable_Belt(Item):
    """ Insatiable Belt """
    type = 'waist'
    text = """

	+[416 - 500] Vitality

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Picking up a Health Globe increases your maximum Life by 5% for 15 seconds, stacking up to 5 times.
    """


class Binding_of_the_Lost(Item):
    """ Binding of the Lost """
    type = 'waist'
    text = """
	 Each hit with Seven-Sided Strike grants 4.0% damage reduction for 7 seconds.
	(Monk Only)
	[4.0 - 5.0]%
    """


class The_Shame_of_Delsere(Item):
    """ The Shame of Delsere """
    type = 'waist'
    text = """
	 Your Signature Spells attack 50% faster and restore 9 Arcane Power.
	(Wizard Only)
	[9 - 12]
    """


class Dayntees_Binding(Item):
    """ Dayntee's Binding """
    type = 'waist'
    text = """
	 You gain an additional 45% damage reduction when there is an enemy afflicted by any of your curses.
	(Necromancer Only)
	[40 - 50]%
    """


class Kyoshiros_Soul(Item):
    """ Kyoshiro's Soul """
    type = 'waist'
    text = """
	 Increases Sweeping Wind Damage by [100 - 125]%
	 Sweeping Wind gains 2 stacks every second it does not deal damage to any enemies.
	(Monk Only)
	2
    """


class Sacred_Harness(Item):
    """ Sacred Harness """
    type = 'waist'
    text = """
	 Judgment gains the effect of the Debilitate rune and is cast at your landing location when casting Falling Sword.
	(Crusader Only)
    """


class Quick_Draw_Belt(Item):
    """ Quick Draw Belt """
    type = 'waist'
    text = """

	Attack Speed Increased by [3.0 - 4.0]%

	+[13 - 21] Thorns Damage
    """


class String_of_Ears(Item):
    """ String of Ears """
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Reduces damage from melee attacks by 29%.
	[25 - 30]%
    """


class Bakuli_Jungle_Wraps(Item):
    """ Bakuli Jungle Wraps """
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Firebats deals 257% increased damage to enemies affected by Locust Swarm or Piranhas.
	(Witch Doctor Only)
	[250 - 300]%
    """


class Saffron_Wrap(Item):
    """ Saffron Wrap """
    type = 'waist'
    text = """

	Reduces all resource costs by [5.0 - 8.0]%.

	Reduces duration of control impairing effects by [20 - 40]%
    """


class Captain_Crimsons_Satin_Sash(Item):
    """ Captain Crimson's Satin Sash """
    type = 'waist'
    text = """
	(2) Set:      Regenerates 20 Life per Second
	(3) Set:      +20 Resistance to All Elements
    """


class Fazulas_Improbable_Chain(Item):
    """ Fazula's Improbable Chain """
    type = 'waist'
    text = """
	 You automatically start with 45 Archon stacks when entering Archon form.
	(Wizard Only)
	[40 - 50]
    """


class Hergbrashs_Binding(Item):
    """ Hergbrash's Binding """
    type = 'waist'
    text = """
	 Reduces the Arcane Power cost of Arcane Torrent, Disintegrate, and Ray of Frost by 54%.
	(Wizard Only)
	[50 - 65]%
    """


class Sebors_Nightmare(Item):
    """ Sebor's Nightmare """
    type = 'waist'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Haunt is cast on all nearby enemies when you open a chest.
    """


class Sash_of_Knives(Item):
    """ Sash of Knives """
    type = 'waist'
    text = """
	 With every attack, you throw a dagger at a nearby enemy for 622% weapon damage as Physical.
	[500 - 650]%
    """


class Omnislash(Item):
    """ Omnislash """
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Slash attacks in all directions.
	(Crusader Only)
    """


class Haunting_Girdle(Item):
    """ Haunting Girdle """
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Haunt releases 1 extra spirit.
	(Witch Doctor Only)
	1
    """


class Sebors_Nightmare(Item):
    """ Sebor's Nightmare """
    type = 'waist'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Haunt is cast on 5 nearby enemies when you open a chest.
    """


class Hwoj_Wrap(Item):
    """ Hwoj Wrap """
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Locust Swarm also Slows enemies by 60%.
	(Witch Doctor Only)
	[60 - 80]%
    """


class Omryns_Chain(Item):
    """ Omryn's Chain """
    type = 'waist'
    text = """
	 Drop Caltrops when using Vault.
	(Demon Hunter Only)
    """


class Cord_of_the_Sherma(Item):
    """ Cord of the Sherma """
    type = 'waist'
    text = """

	+[416 - 500] Vitality

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Chance on hit to create a chaos field that Blinds and Slows enemies inside for 3 seconds.
	[3 - 4]
    """


class Harrington_Waistguard(Item):
    """ Harrington Waistguard """
    type = 'waist'
    text = """

	+[32 - 35]% Extra Gold from Monsters
	 Opening a chest grants 116% increased damage for 10 seconds.
	[100 - 135]%
    """


class Crashing_Rain(Item):
    """ Crashing Rain """
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Rain of Vengeance also summons a crashing beast that deals 3049% weapon damage.
	(Demon Hunter Only)
	[3000 - 4000]%
    """


class Chain_of_Shadows(Item):
    """ Chain of Shadows """
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 After using Impale, Vault costs no resource for 2 seconds.
	(Demon Hunter Only)
    """


class Cord_of_the_Sherma(Item):
    """ Cord of the Sherma """
    type = 'waist'
    text = """

	+[416 - 500] Vitality

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Chance on hit to create a chaos field that Blinds and Slows enemies inside for 3 seconds.
	[2 - 4]
    """


class Blessed_of_Haull(Item):
    """ Blessed of Haull """
    type = 'waist'
    text = """

	+[91 - 100] Resistance to All Elements
	 Justice spawns a Blessed Hammer when it hits an enemy.
	(Crusader Only)
    """


class Belt_of_Transcendence(Item):
    """ Belt of Transcendence """
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Summon a Fetish Sycophant when you hit with a Mana spender.
	(Witch Doctor Only)
    """


class Razor_Strop(Item):
    """ Razor Strop """
    type = 'waist'
    text = """

	Increases Gold and Health Pickup by [1 - 2] Yards.
	 Picking up a Health Globe releases an explosion that deals 342% weapon damage as Fire to enemies within 20 yards.
	[300 - 400]%
    """


class Angel_Hair_Braid(Item):
    """ Angel Hair Braid """
    type = 'waist'
    text = """

	+11% Chance to Block

	Ignores Durability Loss
    """


class Thundergods_Vigor(Item):
    """ Thundergod's Vigor """
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
    type = 'waist'
    text = """
	 Punish gains the effect of every rune.
	(Crusader Only)
    """


class Guardians_Sheath(Item):
    """ Guardian's Sheath """
    type = 'waist'
    text = """
	(2) Set:      +110 Vitality     Regenerates 130 Life per Second
    """


class Belt_of_the_Trove(Item):
    """ Belt of the Trove """
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
    type = 'waist'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Tal_Rashas_Brace(Item):
    """ Tal Rasha's Brace """
    type = 'waist'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Demons_Lock(Item):
    """ Demon's Lock """
    type = 'waist'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Blackthornes_Notched_Belt(Item):
    """ Blackthorne's Notched Belt """
    type = 'waist'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Jangs_Envelopment(Item):
    """ Jang's Envelopment """
    type = 'waist'
    text = """
	 Enemies damaged by Black Hole are also slowed by 60% for 3 seconds.
	(Wizard Only)
	[60 - 80]%
    """


class Sages_Ribbon(Item):
    """ Sage's Ribbon """
    type = 'waist'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Demons_Restraint(Item):
    """ Demon's Restraint """
    type = 'waist'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Khassetts_Cord_of_Righteousness(Item):
    """ Khassett's Cord of Righteousness """
    type = 'waist'
    text = """
	 Fist of the Heavens costs 40% less Wrath and deals 163% more damage.
	(Crusader Only)
	[130 - 170]%
    """


class Zoeys_Secret(Item):
    """ Zoey's Secret """
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 You take 8.5% less damage for every Companion you have active.
	(Demon Hunter Only)
	[8.0 - 9.0]%
    """


class Krelms_Buff_Belt(Item):
    """ Krelm's Buff Belt """
    type = 'waist'
    text = """
	(2) Set:      +500 Vitality
    """


class Guardians_Case(Item):
    """ Guardian's Case """
    type = 'waist'
    text = """
	(2) Set:      +250 Vitality     Regenerates 8000 Life per Second
	(3) Set:      +15% Movement Speed
    """


class Captain_Crimsons_Silk_Girdle(Item):
    """ Captain Crimson's Silk Girdle """
    type = 'waist'
    text = """
	(2) Set:      Regenerates 6000 Life per Second     Reduces cooldown of all skills by 20.0%.     Reduces all resource costs by 20.0%.
	(3) Set:      Damage dealt is increased by your percentage of cooldown reduction.     Damage taken is reduced by your percentage of cost reduction.
    """


class Hunters_Wrath(Item):
    """ Hunter's Wrath """
    type = 'waist'
    text = """

	+[416 - 500] Vitality
	 Your primary skills attack 30% faster and deal 49% increased damage.
	(Demon Hunter Only)
	[45 - 60]%
    """


class Pox_Faulds(Item):
    """ Pox Faulds """
    type = 'pants'
    text = """
	 When 3 or more enemies are within 12 yards, you release a vile stench that deals 492% weapon damage as Poison every second for 5 seconds to enemies within 15 yards.
	[450 - 550]%
    """


class Deaths_Bargain(Item):
    """ Death's Bargain """
    type = 'pants'
    text = """

	Regenerates [4643 - 5528] Life per Second
	 Gain an aura of death that deals 792% of your Life per Second as Physical damage to enemies within 16 yards. You no longer regenerate Life.
	[750 - 1000]%
    """


class Cains_Robes(Item):
    """ Cain's Robes """
    type = 'pants'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Golemskin_Breeches(Item):
    """ Golemskin Breeches """
    type = 'pants'
    text = """

	Sockets (2)
	 The cooldown on Command Golem is reduced by 24 seconds and you take 30% less damage while your golem is alive.
	(Necromancer Only)
	[20 - 25]
    """


class Hammer_Jammers(Item):
    """ Hammer Jammers """
    type = 'pants'
    text = """

	Sockets (2)
	 Enemies take 342% increased damage from your Blessed Hammers for 10 seconds after you hit them with a Blind, Immobilize, or Stun.
	(Crusader Only)
	[300 - 400]%
    """


class Captain_Crimsons_Bowsprit(Item):
    """ Captain Crimson's Bowsprit """
    type = 'pants'
    text = """
	(2) Set:      Regenerates 20 Life per Second
	(3) Set:      +20 Resistance to All Elements
    """


class Hexing_Pants_of_Mr_Yan(Item):
    """ Hexing Pants of Mr. Yan """
    type = 'pants'
    text = """
	 Your resource generation and damage is increased by 25% while moving and decreased by 24% while standing still.
	[20 - 25]%
    """


class Defiler_Cuisses(Item):
    """ Defiler Cuisses """
    type = 'pants'
    text = """

	Sockets (2)
	 Your Bone Spirit's damage is increased by 442% for every second it is active.
	(Necromancer Only)
	[400 - 500]%
    """


class Swamp_Land_Waders(Item):
    """ Swamp Land Waders """
    type = 'pants'
    text = """

	Sockets (2)
	 Sacrifice deals 342% additional damage against enemies affected by Locust Swarm or Grasp of the Dead.
	(Witch Doctor Only)
	[300 - 400]%
    """


class Ashearas_Gait(Item):
    """ Asheara's Gait """
    type = 'pants'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Tal_Rashas_Stride(Item):
    """ Tal Rasha's Stride """
    type = 'pants'
    text = """
	(2) Set:      Damaging enemies with Arcane, Cold, Fire or Lightning will cause a Meteor of the same damage type to fall from the sky. There is an 8 second cooldown for each damage type.
	(4) Set:      Arcane, Cold, Fire, and Lightning attacks each increase all of your resistances by 25% for 8 seconds.
	(6) Set:      Attacks increase your damage by 2000% for 8 seconds. Arcane, Cold, Fire, and Lightning attacks each add one stack. At 4 stacks, each different elemental attack extends the duration by 2 seconds, up to a maximum of 8 seconds.
    """


class Depth_Diggers(Item):
    """ Depth Diggers """
    type = 'pants'
    text = """

	+[91 - 100] Resistance to All Elements
	 Primary skills that generate resource deal 87% additional damage.
	[80 - 100]%
    """


class Zunimassas_Cloth(Item):
    """ Zunimassa's Cloth """
    type = 'pants'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Immortal_Kings_Stature(Item):
    """ Immortal King's Stature """
    type = 'pants'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Demons_Scale(Item):
    """ Demon's Scale """
    type = 'pants'
    text = """
	(2) Set:      +999 Fire Thorns Damage
	(3) Set:      1.1% Chance to Fear on Hit
	(4) Set:      +3% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Gehennas(Item):
    """ Gehennas """
    type = 'pants'
    text = """

	+[410 - 446] Armor

	+[81 - 100] Fire Resistance
    """


class Innas_Temperance(Item):
    """ Inna's Temperance """
    type = 'pants'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Natalyas_Leggings(Item):
    """ Natalya's Leggings """
    type = 'pants'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Blackthornes_Jousting_Mail(Item):
    """ Blackthorne's Jousting Mail """
    type = 'pants'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Demons_Plate(Item):
    """ Demon's Plate """
    type = 'pants'
    text = """
	(2) Set:      +6000 Fire Thorns Damage
	(3) Set:      Chance to Deal 25% Area Damage on Hit.
	(4) Set:      +15% Damage to Demons     Chance to reflect projectiles when you are hit by enemies.
    """


class Captain_Crimsons_Thrust(Item):
    """ Captain Crimson's Thrust """
    type = 'pants'
    text = """
	(2) Set:      Regenerates 6000 Life per Second     Reduces cooldown of all skills by 20.0%.     Reduces all resource costs by 20.0%.
	(3) Set:      Damage dealt is increased by your percentage of cooldown reduction.     Damage taken is reduced by your percentage of cost reduction.
    """


class Renewal_of_the_Invoker(Item):
    """ Renewal of the Invoker """
    type = 'pants'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Jade_Harvesters_Courage(Item):
    """ Jade Harvester's Courage """
    type = 'pants'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Vyrs_Fantastic_Finery(Item):
    """ Vyr's Fantastic Finery """
    type = 'pants'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Sunwukos_Leggings(Item):
    """ Sunwuko's Leggings """
    type = 'pants'
    text = """
	(2) Set:      Your damage taken is reduced by 50% while Sweeping Wind is active.
	(4) Set:      Every second Sweeping Wind spawns a decoy next to the last enemy you hit that taunts nearby enemies and then explodes for 1000% weapon damage for each stack of Sweeping Wind you have.
	(6) Set:      Lashing Tail Kick, Tempest Rush, and Wave of Light have their damage increased by 1500% for each stack of Sweeping Wind you have.
    """


class Cains_Habit(Item):
    """ Cain's Habit """
    type = 'pants'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class The_Shadows_Coil(Item):
    """ The Shadow's Coil """
    type = 'pants'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Weight_of_the_Earth(Item):
    """ Weight of the Earth """
    type = 'pants'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Ashearas_Pace(Item):
    """ Asheara's Pace """
    type = 'pants'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class Raekors_Breeches(Set_Item):
    """ Raekor's Breeches """
    set = ''
    type = 'pants'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Tasset_of_the_Wastes(Item):
    """ Tasset of the Wastes """
    type = 'pants'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Leggings_of_Savages(Item):
    """ Leggings of Savages """
    type = 'pants'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Chausses_of_Valor(Item):
    """ Chausses of Valor """
    type = 'pants'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Cuisses_of_Akkhan(Item):
    """ Cuisses of Akkhan """
    type = 'pants'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Towers_of_the_Light(Item):
    """ Towers of the Light """
    type = 'pants'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Rolands_Determination(Item):
    """ Roland's Determination """
    type = 'pants'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Unholy_Plates(Item):
    """ Unholy Plates """
    type = 'pants'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Encasement(Item):
    """ Marauder's Encasement """
    type = 'pants'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Scales_of_the_Dancing_Serpent(Item):
    """ Scales of the Dancing Serpent """
    type = 'pants'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Mountains_of_Justice(Item):
    """ Mountains of Justice """
    type = 'pants'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Ulianas_Burden(Item):
    """ Uliana's Burden """
    type = 'pants'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Firebirds_Down(Item):
    """ Firebird's Down """
    type = 'pants'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Leg_Guards_of_Mystery(Item):
    """ Leg Guards of Mystery """
    type = 'pants'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Typhons_Abdomen(Item):
    """ Typhon's Abdomen """
    type = 'pants'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Helltooth_Leg_Guards(Item):
    """ Helltooth Leg Guards """
    type = 'pants'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Legs(Item):
    """ Arachyr's Legs """
    type = 'pants'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Mundunugus_Decoration(Item):
    """ Mundunugu's Decoration """
    type = 'pants'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Rathmas_Skeletal_Legplates(Item):
    """ Rathma's Skeletal Legplates """
    type = 'pants'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class TragOuls_Hide(Item):
    """ Trag'Oul's Hide """
    type = 'pants'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Inariuss_Reticence(Item):
    """ Inarius's Reticence """
    type = 'pants'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class Pestilence_Incantations(Item):
    """ Pestilence Incantations """
    type = 'pants'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Lut_Socks(Item):
    """ Lut Socks """
    type = 'feet'
    text = """
	 Leap can be cast up to three times within 2 seconds before the cooldown begins.
	(Barbarian Only)
    """


class Rivera_Dancers(Item):
    """ Rivera Dancers """
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements
	 Lashing Tail Kick attacks 50% faster and deals 257% increased damage.
	(Monk Only)
	[250 - 300]%
    """


class The_Crudest_Boots(Item):
    """ The Crudest Boots """
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 Mystic Ally summons two Mystic Allies that fight by your side.
	(Monk Only)
    """


class Illusory_Boots(Item):
    """ Illusory Boots """
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements

	+[10 - 12]% Movement Speed
	 You may move unhindered through enemies.
    """


class Boots_of_Disregard(Item):
    """ Boots of Disregard """
    type = 'feet'
    text = """

	+[416 - 500] Vitality

	+[373 - 397] Armor

	Regenerates [4643 - 5528] Life per Second
	 Gain 10000 Life regeneration per Second for each second you stand still. This effect stacks up to 4 times.
    """


class Cains_Sandals(Item):
    """ Cain's Sandals """
    type = 'feet'
    text = """
	(2) Set:      Attack Speed Increased by 2.0%
	(3) Set:      10% Better Chance of Finding Magical Items     +50% Experience. (5.0% at level 70)
    """


class Captain_Crimsons_Whalers(Item):
    """ Captain Crimson's Whalers """
    type = 'feet'
    text = """
	(2) Set:      Regenerates 20 Life per Second
	(3) Set:      +20 Resistance to All Elements
    """


class Irontoe_Mudsputters(Item):
    """ Irontoe Mudsputters """
    type = 'feet'
    text = """

	+[416 - 500] Vitality
	 Gain up to 29% increased movement speed based on amount of Life missing.
	[25 - 30]%
    """


class Bryners_Journey(Item):
    """ Bryner's Journey """
    type = 'feet'
    text = """
	 Attacking with Bone Spikes has a 25% chance to cast a Bone Nova at the target location.
	(Necromancer Only)
	[20 - 30]%
    """


class Fire_Walkers(Item):
    """ Fire Walkers """
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 Burn the ground you walk on, dealing 342% weapon damage each second.
	[300 - 400]%
    """


class Fire_Walkers(Item):
    """ Fire Walkers """
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 Burn the ground you walk on, dealing 100% weapon damage each second.
    """


class Lost_Boys(Item):
    """ Lost Boys """
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed

	+[132 - 208] Thorns Damage

	Monster kills grant +[80 - 99] experience.
    """


class Ashearas_Tracks(Item):
    """ Asheara's Tracks """
    type = 'feet'
    text = """
	(2) Set:      +30 Resistance to All Elements
	(3) Set:      2.50% of Damage Dealt Is Converted to Life     +300 Holy Thorns Damage
    """


class Steuarts_Greaves(Item):
    """ Steuart's Greaves """
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 You gain 45% increased movement speed for 10 seconds after using Blood Rush.
	(Necromancer Only)
	[40 - 50]%
    """


class Steuarts_Greaves(Item):
    """ Steuart's Greaves """
    type = 'feet'
    text = """

	+[10 - 12]% Movement Speed
	 You gain 85% increased movement speed for 10 seconds after using Blood Rush.
	(Necromancer Only)
	[75 - 100]%
    """


class Zunimassas_Trail(Item):
    """ Zunimassa's Trail """
    type = 'feet'
    text = """
	(2) Set:      Your Fetish Army lasts until they die and the cooldown of your Fetish Army is reduced by 80%.
	(4) Set:      You and your pets take 3% less damage for every Fetish you have alive.
	(6) Set:      Enemies hit by your Mana spenders take 15,000% increased damage from your pets for 8 seconds.
    """


class Innas_Sandals(Item):
    """ Inna's Sandals """
    type = 'feet'
    text = """
	(2) Set:      Increase the passive effect of your Mystic Ally and the base passive effect of your Mantra by 100%.
	(4) Set:      Gain the base effect of all four Mantras at all times.
	(6) Set:      Gain the five runed Mystic Allies at all times and your damage is increased by 750% for each Mystic Ally you have out.
    """


class Natalyas_Bloody_Footprints(Item):
    """ Natalya's Bloody Footprints """
    type = 'feet'
    text = """
	(2) Set:      Reduce the cooldown of Rain of Vengeance by 4 seconds when you hit with a Hatred-generating attack or Hatred-spending attack.
	(4) Set:      Rain of Vengeance deals 100% increased damage.
	(6) Set:      After casting Rain of Vengeance, deal 14,000% increased damage and take 60% reduced damage for 10 seconds.
    """


class Nilfurs_Boast(Item):
    """ Nilfur's Boast """
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements
	 Increase the damage of Meteor by 600%. When your Meteor hits 3 or fewer enemies, the damage is increased by 675%.
	(Wizard Only)
	[675 - 900]%
    """


class Ice_Climbers(Item):
    """ Ice Climbers """
    type = 'feet'
    text = """

	+[91 - 100] Resistance to All Elements

	Reduces damage from Cold attacks by [7 - 10]%.
	 Gain immunity to Freeze and Immobilize effects.
    """


class Sages_Journey(Item):
    """ Sage's Journey """
    type = 'feet'
    text = """
	(2) Set:      +35 Strength     +35 Dexterity     +35 Intelligence     +35 Vitality
    """


class Blackthornes_Spurs(Item):
    """ Blackthorne's Spurs """
    type = 'feet'
    text = """
	(2) Set:      +250 Vitality     Increases damage against elites by 10.0%
	(3) Set:      Reduces damage from elites by 10.0%     +25% Extra Gold from Monsters
	(4) Set:      You are immune to Desecrator, Molten, and Plagued monster ground effects.
    """


class Immortal_Kings_Stride(Item):
    """ Immortal King's Stride """
    type = 'feet'
    text = """
	(2) Set:      Call of the Ancients last until they die.
	(4) Set:      Reduce the cooldown of Wrath of the Berserker and Call of the Ancients by 3 seconds for every 10 Fury you spend with an attack.
	(6) Set:      While both Wrath of the Berserker and Call of the Ancients is active, you deal 4000% increased damage.
    """


class Sages_Passage(Item):
    """ Sage's Passage """
    type = 'feet'
    text = """
	(2) Set:      +250 Strength     +250 Dexterity     +250 Intelligence     +250 Vitality
	(3) Set:      Double the amount of Death's Breath that drop.
    """


class Jade_Harvesters_Swiftness(Item):
    """ Jade Harvester's Swiftness """
    type = 'feet'
    text = """
	(2) Set:      When Haunt lands on an enemy already affected by Haunt, it instantly deals 3500 seconds worth of Haunt damage.
	(4) Set:      Soul Harvest gains the effect of every rune and has its cooldown reduced by 1 second every time you cast Haunt or Locust Swarm.
	(6) Set:      Soul Harvest reduces damage taken by 50% for 12 seconds and consumes your damage over time effects on enemies, instantly dealing 10,000 seconds worth of remaining damage.
    """


class Zeal_of_the_Invoker(Item):
    """ Zeal of the Invoker """
    type = 'feet'
    text = """
	(2) Set:      Your Thorns damage now hits all enemies in a 15 yard radius around you. Each time you hit an enemy with Punish, Slash, or block an attack your Thorns is increased by 350% for 2 seconds.
	(4) Set:      You take 50% less damage for 20 seconds after damaging an enemy with Bombardment.
	(6) Set:      The attack speed of Punish and Slash are increased by 50% and deal 15,000% of your Thorns damage to the first enemy hit.
    """


class Ashearas_Finders(Item):
    """ Asheara's Finders """
    type = 'feet'
    text = """
	(2) Set:      +100 Resistance to All Elements
	(3) Set:      +20% Life
	(4) Set:      Attacks cause your followers to occasionally come to your aid.
    """


class The_Shadows_Heels(Item):
    """ The Shadow's Heels """
    type = 'feet'
    text = """
	(2) Set:      While equipped with a melee weapon, your damage is increased by 6000%.
	(4) Set:      Shadow Power gains the effect of every rune and lasts forever.
	(6) Set:      Impale deals an additional 75,000% weapon damage to the first enemy hit.
    """


class Vyrs_Swaggering_Stance(Item):
    """ Vyr's Swaggering Stance """
    type = 'feet'
    text = """
	(2) Set:      Archon gains the effect of every rune.
	(4) Set:      Archon stacks also increase your Attack Speed, Armor, and Resistances by 1%.
	(6) Set:      You gain 1 Archon stack when you hit with an Archon ability and Archon stacks also reduce damage taken by 0.15% and have their damage bonus increased to 100%.
    """


class Captain_Crimsons_Waders(Item):
    """ Captain Crimson's Waders """
    type = 'feet'
    text = """
	(2) Set:      Regenerates 6000 Life per Second     Reduces cooldown of all skills by 20.0%.     Reduces all resource costs by 20.0%.
	(3) Set:      Damage dealt is increased by your percentage of cooldown reduction.     Damage taken is reduced by your percentage of cost reduction.
    """


class Foundation_of_the_Earth(Item):
    """ Foundation of the Earth """
    type = 'feet'
    text = """
	(2) Set:      Reduce the cooldown of Earthquake, Avalanche, Leap, and Ground Stomp by 1 second for every 30 Fury you spend with an attack.
	(4) Set:      Leap causes an Earthquake when you land. Additionally, Leap gains the effect of the Iron Impact rune and the rune's effect and duration are increased by 150%.
	(6) Set:      Increase the damage of Earthquake, Avalanche, Leap, Ground Stomp, Ancient Spear and Seismic Slam by 20,000%.
    """


class Cains_Travelers(Item):
    """ Cain's Travelers """
    type = 'feet'
    text = """
	(2) Set:      Attack Speed Increased by 8.0%     +50% Experience. (5.0% at level 70)
	(3) Set:      When a Greater Rift Keystone drops, there is a 25% chance for an extra one to drop.
    """


class Heel_of_Savages(Item):
    """ Heel of Savages """
    type = 'feet'
    text = """
	(2) Set:      Double the effectiveness of shouts. You deal double damage to Feared, Frozen, or Stunned enemies.
	(4) Set:      Each Frenzy stack reduces damage taken by 6%. Frenzy lasts twice as long.
	(6) Set:      Frenzy deals 1000% increased damage per stack.
    """


class Raekors_Striders(Set_Item):
    """ Raekor's Striders """
    set = The_Legacy_of_Raekor
    type = 'feet'
    text = """
	(2) Set:      Furious Charge refunds a charge if it hits only 1 enemy.
	(4) Set:      Furious Charge gains the effect of every rune and deals 1000% increased damage.
	(6) Set:      Every use of Furious Charge increases the damage of your next Fury-spending attack by 5500%. This effect stacks. Every use of a Fury-spending attack consumes up to 5 stacks.
    """


class Sabaton_of_the_Wastes(Item):
    """ Sabaton of the Wastes """
    type = 'feet'
    text = """
	(2) Set:      Increase the damage per second of Rend by 500% and its duration to 15 seconds.
	(4) Set:      During Whirlwind and for 3 seconds after, you gain 50% damage reduction and your applied Rends deal triple damage.
	(6) Set:      Whirlwind gains the effect of the Dust Devils rune and all Whirlwind and Rend damage is increased by 10,000%.
    """


class Rolands_Stride(Item):
    """ Roland's Stride """
    type = 'feet'
    text = """
	(2) Set:      Every use of Shield Bash and Sweep Attack reduces the cooldowns of your Laws and Defensive Skills by 1 second.
	(4) Set:      Increase the damage of Shield Bash and Sweep Attack by 13,000%.
	(6) Set:      Every use of Shield Bash or Sweep Attack that hits an enemy grants 75% increased Attack Speed and 15% damage reduction for 8 seconds. This effect stacks up to 5 times.
    """


class Foundation_of_the_Light(Item):
    """ Foundation of the Light """
    type = 'feet'
    text = """
	(2) Set:      Every use of Blessed Hammer that hits an enemy reduces the cooldown of Falling Sword and Provoke by 1 second.
	(4) Set:      You take 50% less damage for 8 seconds after landing with Falling Sword.
	(6) Set:      Increase the damage of Blessed Hammer by 12,000% and Falling Sword by 1000%.
    """


class Greaves_of_Valor(Item):
    """ Greaves of Valor """
    type = 'feet'
    text = """
	(2) Set:      Attacking with Fists of the Heavens empowers you, allowing Heaven's Fury to deal 100% increased damage for 5 seconds. Stacks up to 3 times multiplicatively.
	(4) Set:      Hitting with Fist of the Heavens returns 5 Wrath and reduces damage taken by 1% for 10 seconds. Stacks up to 50 times.
	(6) Set:      Increase the damage of Fist of the Heavens and Heaven's Fury by 20,000%.
    """


class Sabatons_of_Akkhan(Item):
    """ Sabatons of Akkhan """
    type = 'feet'
    text = """
	(2) Set:      Reduce the cost of all abilities by 50% while Akarat's Champion is active.
	(4) Set:      Reduce the cooldown of Akarat's Champion by 50%.
	(6) Set:      While Akarat's Champion is active, you deal 1500% increased damage and take 50% less damage.
    """


class Hell_Walkers(Item):
    """ Hell Walkers """
    type = 'feet'
    text = """
	(2) Set:      Your generators generate 2 additional Hatred and 1 Discipline.
	(4) Set:      Gain 60% damage reduction and deal 60% increased damage for 8 seconds if no enemy is within 10 yards of you.
	(6) Set:      Your generators, Multishot, and Vengeance deal 350% increased damage for every point of Discipline you have.
    """


class Marauders_Treads(Item):
    """ Marauder's Treads """
    type = 'feet'
    text = """
	(2) Set:      Companion calls all companions to your side.
	(4) Set:      Sentries deal 400% increased damage and cast Elemental Arrow, Chakram, Impale, Multishot, and Cluster Arrow when you do.
	(6) Set:      Your primary skills, Elemental Arrow, Chakram, Impale, Multishot, Cluster Arrow, Companions, and Vengeance deal 12,000% increased damage for every active Sentry.
    """


class Weaves_of_Justice(Item):
    """ Weaves of Justice """
    type = 'feet'
    text = """
	(2) Set:      Sweeping Wind gains the effect of every rune, and movement speed is increased by 5% for each stack of Sweeping Wind.
	(4) Set:      Attacking with Tempest Rush reduces your damage taken by 50% and increases Spirit Regeneration by 50.
	(6) Set:      Hitting with Tempest Rush while Sweeping Wind is active increases the size of Sweeping Wind and also increases all damage dealt by 15,000%.
    """


class Eight_Demon_Boots(Item):
    """ Eight-Demon Boots """
    type = 'feet'
    text = """
	(2) Set:      Your Spirit Generators have 25% increased attack speed and 400% increased damage.
	(4) Set:      Dashing Strike spends 75 Spirit, but refunds a Charge when it does.
	(6) Set:      Your Spirit Generators increase the weapon damage of Dashing Strike to 60,000% for 6 seconds and Dashing Strike increases the damage of your Spirit Generators by 6000% for 6 seconds.
    """


class Ulianas_Destiny(Item):
    """ Uliana's Destiny """
    type = 'feet'
    text = """
	(2) Set:      Every third hit of your Spirit Generators applies Exploding Palm.
	(4) Set:      Your Seven-Sided Strike deals 777% its total damage with each hit.
	(6) Set:      Increase the damage of your Exploding Palm by 9000% and your Seven-Sided Strike detonates your Exploding Palm.
    """


class Striders_of_Destiny(Item):
    """ Striders of Destiny """
    type = 'feet'
    text = """
	(2) Set:      Casting Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, or Wave of Force reduces the cooldown of Slow Time by 3 seconds.
	(4) Set:      You take 60% reduced damage while you have a Slow Time active. Allies inside your Slow Time gain half benefit.
	(6) Set:      Enemies affected by your Slow Time and for 5 seconds after exiting take 8500% increased damage from your Arcane Orb, Energy Twister, Explosive Blast, Magic Missile, Shock Pulse, Spectral Blade, and Wave of Force abilities.
    """


class Typhons_Tarsus(Item):
    """ Typhon's Tarsus """
    type = 'feet'
    text = """
	(2) Set:      Double the duration of Hydras and increase the number of heads on multi-headed Hydras by two.
	(4) Set:      Damage taken is reduced by 8% for each Hydra head alive. Each time you take damage, a head dies. A head cannot die more than once every 2 seconds.
	(6) Set:      Hydras deal 1300% increased damage for each Hydra head alive.
    """


class Firebirds_Tarsi(Item):
    """ Firebird's Tarsi """
    type = 'feet'
    text = """
	(2) Set:      When you die, a meteor falls from the sky and revives you. This effect has a 60 second cooldown.
	(4) Set:      Dealing Fire damage with one of your skills causes the enemy to take 1000% weapon damage as Fire per second for 3 seconds. This effect can be repeated a second and third time by different skills. If an enemy is burning due to three different skills simultaneously the enemy will Ignite, taking 3000% weapon damage per second until they die.
	(6) Set:      Your damage is increased by 200% and damage taken reduced by 3% for each enemy that is Ignited. This effect can stack up to 20 times. You always receive the maximum bonus whenever a nearby Elite monster is Ignited.
    """


class Helltooth_Greaves(Item):
    """ Helltooth Greaves """
    type = 'feet'
    text = """
	(2) Set:      Enemies hit by your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, or Wall of Death are afflicted by Necrosis, becoming Slowed and taking 3000% weapon damage every second for 10 seconds.
	(4) Set:      After applying Necrosis to an enemy, you take 60% reduced damage for 10 seconds.
	(6) Set:      After casting Wall of Death, gain 9000% increased damage for 15 seconds to your primary skills, Acid Cloud, Firebats, Zombie Charger, Zombie Dogs, Gargantuan, Grasp of the Dead, Piranhas, and Wall of Death.
    """


class Arachyrs_Stride(Item):
    """ Arachyr's Stride """
    type = 'feet'
    text = """
	(2) Set:      Summon a permanent Spider Queen who leaves behind webs that deal 4000% weapon damage over 5 seconds and Slows enemies. The Spider Queen is commanded to move to where you cast your Corpse Spiders.
	(4) Set:      Hex gains the effect of the Toad of Hugeness rune. After summoning a Toad of Hugeness, you gain 50% damage reduction and heal for 10% of your maximum Life per second for 15 seconds.
	(6) Set:      The damage of your creature skills is increased by 9000%. Creature skills are Corpse Spiders, Plague of Toads, Firebats, Locust Swarm, Hex, and Piranhas.
    """


class Mundunugus_Dance(Item):
    """ Mundunugu's Dance """
    type = 'feet'
    text = """
	(2) Set:      Big Bad Voodoo now follows you and lasts twice as long.
	(4) Set:      Gain 60% damage reduction for 30 seconds when you enter the spirit realm.
	(6) Set:      Spirit Barrage deals 20,000% increased damage plus an additional % equal to 5 times your Mana Regeneration/Second.
    """


class Pestilence_Battle_Boots(Item):
    """ Pestilence Battle Boots """
    type = 'feet'
    text = """
	(2) Set:      Each corpse you consume fires a Corpse Lance at a nearby enemy.
	(4) Set:      Each enemy you hit with Bone Spear, Corpse Lance and Corpse Explosion reduces your damage taken by 2%, up to a maximum of 50%.  Lasts 15 seconds.
	(6) Set:      Each corpse you consume grants you an Empowered Bone Spear charge that increases the damage of your next Bone Spear by 3300%. In addition, Corpse Lance and Corpse Explosion damage is increased by 1650%.
    """


class Inariuss_Perseverance(Item):
    """ Inarius's Perseverance """
    type = 'feet'
    text = """
	(2) Set:      Bone Armor damage is increased by 1000%.
	(4) Set:      Bone Armor grants an additional 2% damage reduction per enemy hit.
	(6) Set:      Bone Armor also activates a swirling tornado of bone, damaging nearby enemies for 1000% weapon damage and increasing the damage they take from the Necromancer by 10,000%.
    """


class TragOuls_Stalwart_Greaves(Item):
    """ Trag'Oul's Stalwart Greaves """
    type = 'feet'
    text = """
	(2) Set:      Blood Rush gains the effect of every rune.
	(4) Set:      While at full Life, your healing from skills is added to your maximum Life for 45 seconds, up to 100% more.
	(6) Set:      Your Life-spending abilities deal 3800% increased damage and your healing from skills is increased by 100%.
    """


class Rathmas_Ossified_Sabatons(Item):
    """ Rathma's Ossified Sabatons """
    type = 'feet'
    text = """
	(2) Set:      Your minions have a chance to reduce the cooldown of Army of the Dead by 1 second each time they deal damage.
	(4) Set:      You gain 1% damage reduction for 15 seconds each time one of your minions deal damage. Max 50 stacks.
	(6) Set:      Each active Skeletal Mage increases the damage of your minions and Army of the Dead by 1000% up to a max of 4000%.
    """


class Lost_Time(Item):
    """ Lost Time """
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
    type = 'scythe-1h'
    text = """

	+[626 - 750] Intelligence

	+[626 - 750] Vitality
	 Siphon Blood drains blood from 2 additional targets.
	(Necromancer Only)
    """


class TragOuls_Corroded_Fang(Item):
    """ Trag'Oul's Corroded Fang """
    type = 'scythe-1h'
    text = """

	+[626 - 750] Intelligence
	 The Cursed Scythe rune for Grim Scythe now has a 100% chance to apply a curse and you deal 179% increased damage to cursed enemies.
	(Necromancer Only)
	[150 - 200]%
    """


class Scythe_of_the_Cycle(Item):
    """ Scythe of the Cycle """
    type = 'scythe-1h'
    text = """

	+[626 - 750] Intelligence
	 Your Secondary skills deal 379% additional damage while Bone Armor is active but reduce the remaining duration of Bone Armor by 4 seconds.
	(Necromancer Only)
	[350 - 400]%
    """


class Jesseth_Skullscythe(Item):
    """ Jesseth Skullscythe """
    type = 'scythe-1h'
    text = """
	(2) Set:      When the target of your Command Skeletons dies, your skeletons are automatically commanded to attack a nearby target.     While your skeletons are commanded to attack a target, all of your minions deal 400% increased damage.
    """


class Reilenas_Shadowhook(Item):
    """ Reilena's Shadowhook """
    type = 'scythe-2h'
    text = """

	+[946 - 1125] Intelligence
	 Every point of Maximum Essence increases your damage by 0.5% and Bone Spikes generates 2 additional Essence for each enemy hit.
	(Necromancer Only)
	[2 - 5]
    """


class Maltorius_Petrified_Spike(Item):
    """ Maltorius' Petrified Spike """
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
    type = 'scythe-2h'
    text = """

	+[946 - 1125] Intelligence
	 Each different poison skill you use increases the damage of your poison skills by 95% for 15 seconds.
	(Necromancer Only)
	[75 - 100]%
    """

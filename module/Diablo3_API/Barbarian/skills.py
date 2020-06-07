class Skill(object):
    category = False
    description = False
    url = False
    runes = False

    @property
    def data(self):
        print('name: {}'.format(self.__class__.__doc__))
        if self.category:
            print('category: {}'.format(self.category))
        if self.description:
            print('description: {}'.format(self.description))
        if self.runes:
            print('runes: {}'.format(self.runes))

        return True


class Bash(Skill):
    """ Bash """
    category = "active"
    description = """
    Generate: 6 Fury per attack

    Brutally smash an enemy for 320% weapon damage.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/bash'


    runes = """
	 Frostbite
		Each hit Freezes the enemy for 1.5 seconds.

        Enemies can be frozen by Bash once every 5 seconds.

	 Onslaught
		 The enemy has a 10% increased chance to be Critically Hit for 3 seconds.

        Bash's damage turns into Lightning.

	 Punish
		 Increase your damage by 4% for 5 seconds after using Bash. This effect stacks up to 3 times.

	 Instigation
		 Increase Fury generated to 9.

        Bash's damage turns into Fire.

	 Pulverize
		 Each hit causes a shockwave that deals 100% weapon damage as Fire to enemies in a 26 yard line behind the primary enemy.

    """


class Hammer_of_the_Ancients(Skill):
    """ Hammer of the Ancients """
    category = "active"
    description = """
    Cost: 20 Fury

    Call forth a massive hammer to smash enemies directly in front of you for 535% weapon damage. Hammer of the Ancients has a 1% increased Critical Hit Chance for every 5 Fury that you have.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/hammer-of-the-ancients'


    runes = """
	 Rolling Thunder
		 Create a shockwave that deals 505% weapon damage to all enemies within 22 yards in front of you.

	 Smash
		 Smash for 640% weapon damage as Fire.

	 The Devil's Anvil
		 Each hit creates a tremor at the point of impact for 2 seconds that Chills enemies by 80%.

        Hammer of the Ancients's damage turns into Cold.

	 Thunderstrike
		 When you kill an enemy with Hammer of the Ancients, other enemies within 10 yards are Stunned for 2 seconds.

        Hammer of the Ancients turns into Lightning damage.

	 Birthright
		 Critical Hits heal you for 3% of your maximum Life.

    """


class Cleave(Skill):
    """ Cleave """
    category = "active"
    description = """
    Generate: 6 Fury per attack

    Swing your weapon in a wide arc to deal 200% weapon damage to all enemies caught in the swing.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/cleave'


    runes = """
	 Rupture
		 Enemies slain by Cleave explode, causing 160% weapon damage as Fire to all other enemies within 8 yards.

	 Reaping Swing
		 Generate 1 additional Fury per enemy hit.

        Cleave's damage turns into Fire.

	 Scattering Blast
		 On Critical Hits, knock enemies up into the air and deal 80% weapon damage to enemies where they land.

	 Broad Sweep
		 Swing at all enemies around you and increase damage to 235% weapon damage as Lightning.

	 Gathering Storm
		 Enemies cleaved are Chilled and take 10% increased damage from all sources for 3 seconds.

        Cleave's damage turns into Cold.

    """


class Ground_Stomp(Skill):
    """ Ground Stomp """
    category = "active"
    description = """
    Generate: 15 Fury
    Cooldown: 12 seconds

    Smash the ground, stunning all enemies within 14 yards for 4 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/ground-stomp'


    runes = """
	Deafening Crash
		 Reduce the cooldown of Ground Stomp to 8 seconds.

         Enemies in the area have their movement speed slowed by 80% for 8 seconds after they recover from being stunned.

	 Wrenching Smash
		 Increase the area of effect to 24 yards. Enemies are pulled closer before the strike lands.

	 Trembling Stomp
		 Enemies in the area also take 575% weapon damage as Fire.

	 Foot of the Mountain
		 Increase Fury generated to 30.

	 Jarring Slam
		 Enemies hit have a chance to drop a health globe.

    """


class Rend(Skill):
    """ Rend """
    category = "active"
    description = """
    Cost: 20 Fury

    A sweeping strike causes all enemies within 12 yards to Bleed for 1100% weapon damage as Physical over 5 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/rend'


    runes = """
	 Ravage
		 Increase the range of Rend to hit all enemies within 18 yards.

         Rend's damage turns into Fire.

	 Blood Lust
		 Heal for 0.5% of your maximum Life per second for each affected enemy.

	 Lacerate
		 Increase damage to 1350% weapon damage as Lightning over 5 seconds.

	 Mutilate
		 Affected enemies are Chilled and take 10% increased damage from all sources.

         Rend's damage turns into Cold.

	 Bloodbath
		 Enemies killed while bleeding cause all enemies within 10 yards to begin bleeding for 1100% weapon damage as Physical over 5 seconds.

    """


class Leap(Skill):
    """ Leap """
    category = "active"
    description = """
    Generate: 15 Fury
    Cooldown: 10 seconds

    Leap into the air, dealing 180% weapon damage to all enemies within 10 yards of your destination and slowing their movement speed by 60% for 3 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/leap'


    runes = """
	Iron Impact
		 Gain 150% additional Armor for 4 seconds after landing.

	 Launch
		 You leap with such great force that enemies within 10 yards of the takeoff point take 180% weapon damage and are also slowed by 60% for 3 seconds.

	 Toppling Impact
		 Increase the damage of Leap to 450% and send enemies hurtling away from where you land.

	 Call of Arreat
		 Shockwaves burst forth from the ground increasing the radius of effect to 16 yards and pulling affected enemies towards you.

	 Death from Above
		 Land with such force that enemies have a 100% chance to be stunned for 3 seconds.

    """


class Overpower(Skill):
    """ Overpower """
    category = "active"
    description = """
    Cooldown: 12 seconds

    Deal 380% weapon damage to all enemies within 9 yards.

    Critical Hits have a chance to reduce the cooldown of Overpower by 1 second.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/overpower'


    runes = """
	 Storm of Steel
		 Throw up to 3 axes at nearby enemies that each deal 380% weapon damage.

	 Killing Spree
		 Your Critical Hit Chance is increased by 8% for 5 seconds.

         Overpower's damage turns into Lightning.

	 Crushing Advance
		 Redirect 35% of incoming melee damage back to the attacker for 5 seconds after Overpower is activated.

	 Momentum
		 Generate 5 Fury for each enemy hit by Overpower.

	 Revel
		 Increase damage to 760% weapon damage as Fire.

    """


class Frenzy(Skill):
    """ Frenzy """
    category = "active"
    description = """
    Generate: 4 Fury per attack

    Swing for 220% weapon damage. Frenzy's attack speed increases by 15% for 4 seconds with each swing. This effect stacks up to 5 times.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/frenzy'


    runes = """
	Sidearm
		 Each strike has a 25% chance to throw a piercing axe at a nearby enemy that deals 300% weapon damage as Cold to all enemies in its path.

         Frenzy's damage turns into Cold.

	 Berserk
		 Increase Fury generated to 6.

         Frenzy's damage turns into Cold.

	 Vanguard
		 Gain 5% movement speed for each stack of Frenzy.

	 Smite
		 Each hit has a 30% chance to call down a bolt of lightning from above, stunning the enemy for 1.5 seconds.

	 Maniac
		 Each Frenzy effect also increases your damage by 2.5%.

         Frenzy's damage turns into Fire.

    """


class Seismic_Slam(Skill):
    """ Seismic Slam """
    category = "active"
    description = """
    Cost: 30 Fury

    Slam the ground and cause a wave of destruction that deals 620% weapon damage to enemies up to 50 yards in front of you.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/seismic-slam'

    runes = """
	Stagger
		 Reduce the cost to 22 Fury.

        Seismic Slam's damage turns into Lightning.

	 Shattered Ground
		 Increase damage to 735% weapon damage as Fire and knocks all enemies hit up into the air.

	 Rumble
		 Expend all remaining Fury to cause the ground to shudder after the initial strike, damaging enemies in the area for 15% weapon damage for every point of Fury expended as Physical over 2 seconds.

	 Strength from Earth
		 Gain 1% of your maximum Life for every enemy hit.

	 Permafrost
		 Create a sheet of frost that deals 755% weapon damage as Cold and Chills enemies by 60% for 1 second.

    """


class Revenge(Skill):
    """ Revenge """
    category = "active"
    description = """
    Cost: 1 charge

    Deal 300% weapon damage to all nearby enemies. You heal 4% of your maximum Life for each enemy hit.

    Revenge has a 15% chance to gain a charge each time you are hit. Maximum 2 charges.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/revenge'


    runes = """
	 Blood Law
		 Increase healing to 6% of maximum Life for each enemy hit.

	 Best Served Cold
		 Increase your Critical Hit Chance by 8% for 6 seconds after using Revenge.

         Revenge's damage turns into Cold.

	 Retribution
		 Increase damage to 700% weapon damage as Fire.

	 Grudge
		 Knockback enemies 24 yards when using Revenge.

        Revenge's damage turns into Lightning.

	 Provocation
		 Increase the maximum number of charges to 3.

    """


class Threatening_Shout(Skill):
    """ Threatening Shout """
    category = "active"
    description = """
    Generate: 15 Fury
    Cooldown: 10 seconds

    Shout with great ferocity, reducing damage done by enemies within 25 yards by 20% for 15 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/threatening-shout'


    runes = """
	 Intimidate
		 Affected enemies also have their movement speed reduced by 60%.

	 Falter
		 Enemies instead take 25% increased damage for 6 seconds.

	 Grim Harvest
		 Enemies are badly shaken and have a chance to drop health globes.

	 Demoralize
		 Affected enemies are also taunted to attack you for 4 seconds.

	 Terrify
		 Enemies are severely demoralized. Each enemy has a 100% chance to flee in Fear for 3 seconds.

    """


class Sprint(Skill):
    """ Sprint """
    category = "active"
    description = """
    Cost: 20 Fury
    Increase movement speed by 30% for 3 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/sprint'


    runes = """
	 Rush
		 Increase Dodge Chance by 12% while sprinting.

	 Run Like the Wind
		 Tornadoes rage in your wake, each dealing 60% weapon damage as Physical for 3 seconds to nearby enemies.

	 Marathon
		 Increase the movement speed bonus to 40% for 4 seconds.

	 Gangway
		 Slams through enemies, knocking them back and dealing 25% weapon damage.

	 Forced March
		 Increase movement speed of allies within 50 yards by 20% for 3 seconds.

    """


class Weapon_Throw(Skill):
    """ Weapon Throw """
    category = "active"
    description = """
    Generate: 6 Fury per attack

    Hurl a throwing weapon at an enemy dealing 275% weapon damage.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/weapon-throw'


    runes = """
	 Mighty Throw
		 Increase thrown weapon damage to 400% weapon damage as Lightning.

	 Ricochet
		 The weapon ricochets to 3 enemies within 20 yards of each other.

         Weapon Throw's damage turns into Fire.

	 Throwing Hammer
		 Hurl a hammer with a 40% chance to Stun the enemy for 1 second.

	 Stupefy
		 Aim for the head, gaining a 15% chance of causing your enemy to be Confused and attack other enemies for 3 seconds.

	 Balanced Weapon
		 Increase Fury generated to 9.

        Weapon Throw's damage turns into Fire.

    """


class Earthquake(Skill):
    """ Earthquake """
    category = "active"
    description = """
    Cost: 25 Fury
    Cooldown: 60 seconds

    Shake the ground violently, dealing 4800% weapon damage as Fire over 8 seconds to all enemies within 18 yards.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/earthquake'


    runes = """
	 Giant's Stride
		 20 secondary tremors follow your movement and deal 300% weapon damage as Fire each.

	 Chilling Earth
		 Create an icy patch, causing Earthquake to Freeze all enemies hit and deal Cold damage.

	 The Mountain's Call
		 Remove the Fury cost and reduce the cooldown to 30 seconds.

         Earthquake's damage turns into Lightning.

	 Molten Fury
		 Increase Earthquake's damage to 6000% weapon damage as Fire.

	 Cave-In
		 All enemies within 24 yards are pulled in towards you.

         Earthquake's damage turns into Physical.

    """


class Whirlwind(Skill):
    """ Whirlwind """
    category = "active"
    description = """
    Cost: 10 Fury

    Deliver multiple attacks to everything in your path for 340% weapon damage.

    While whirlwinding, you move at 100% movement speed.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/whirlwind'


    runes = """
	 Dust Devils
		 Generate harsh tornadoes that deal 180% weapon damage to enemies in their path.

	 Hurricane
		 Pull enemies from up to 35 yards away towards you while whirlwinding.

        Whirlwind's damage turns into Cold.

	 Blood Funnel
		 Critical Hits restore 1% of your maximum Life.

	 Wind Shear
		 Gain 1 Fury for every enemy struck.

         Whirlwind's damage turns into Lightning.

	 Volcanic Eruption
		 Turns Whirlwind into a torrent of magma that deals 400% weapon damage as Fire.

    """


class Furious_Charge(Skill):
    """ Furious Charge """
    category = "active"
    description = """
    Cost: 1 Charge
    Generate: 15 Fury

    Rush forward knocking back and dealing 600% weapon damage to enemies along your path.

    You gain a charge every 10 seconds and can have up to 1 charge stored at a time.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/furious-charge'


    runes = """
	 Battering Ram
		 Increase the damage to 1050% weapon damage as Fire.

	 Merciless Assault
		 Recharge time is reduced by 2 seconds for every enemy hit. This effect can reduce the recharge time by up to 10 seconds.

	 Stamina
		 Generate 10 additional Fury for each enemy hit while charging.

	 Cold Rush
		 All enemies hit are Frozen for 2.5 seconds.

         Furious Charge's damage turns into Cold.

	 Dreadnought
		 Store up to 3 charges of Furious Charge.

         Furious Charge's damage turns into Lightning.

    """


class Ignore_Pain(Skill):
    """ Ignore Pain """
    category = "active"
    description = """
    Cooldown: 30 seconds

    Reduce all damage taken by 50% and gain Immunity to all control-impairing effects for 5 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/ignore-pain'


    runes = """
	 Bravado
		 While Ignore Pain is active, gain 40% increased movement speed and knock enemies away as you run.

	 Iron Hide
		 Increase duration to 7 seconds.

	 Ignorance is Bliss
		 While Ignore Pain is active, gain 5364 Life per Fury spent.

	 Mob Rule
		 Allies within 50 yards also gain 25% damage reduction and Immunity to control-impairing effects for 5 seconds.

	 Contempt for Weakness
		 Instantly heal for 35% of maximum Life when activating Ignore Pain.

    """


class Battle_Rage(Skill):
    """ Battle Rage """
    category = "active"
    description = """
    Cost: 20 Fury

    Enter a rage which increases your damage by 10% and Critical Hit Chance by 3%. Lasts 120 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/battle-rage'


    runes = """
	 Marauder's Rage
		 Increase damage bonus to 15%.

	 Ferocity
		 Increase movement speed by 15%.

	 Swords to Ploughshares
		 Critical Hits heal you and your pets for up to 21,457 Life.

	 Into the Fray
		 Gain 1% Critical Hit Chance for each enemy within 10 yards while under the effects of Battle Rage.

	 Bloodshed
		 Deal damage equal to 20% of your recent Critical Hits to enemies within 20 yards every 1 second.

    """


class Call_of_the_Ancients(Skill):
    """ Call of the Ancients """
    category = "active"
    description = """
    Cooldown: 120 seconds

    Summon the ancient Barbarians Talic, Korlic, and Madawc to fight alongside you for 20 seconds. Each deals 270% weapon damage per swing in addition to bonus abilities.

    Talic wields a sword and shield and uses Whirlwind and Leap. Korlic wields a massive polearm and uses Cleave and Furious Charge. Madawc dual-wields axes and uses Weapon Throw and Seismic Slam.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/call-of-the-ancients'


    runes = """
	 The Council Rises
		 The Ancients deal 540% weapon damage as Fire with each attack.

	 Duty to the Clan
		 Enemies hit by the Ancients are Chilled for 2 seconds and have 10% increased chance to be Critically Hit.

         The Ancients' damage turns into Cold.

	 Ancients' Blessing
		 Each point of Fury you spend heals you and your Ancients for 966 Life.

	 Ancients' Fury
		 Gain 4 Fury every time an Ancient deals damage.

	 Together as One
		 50% of all damage dealt to you is instead divided evenly between the Ancients.

         The Ancients' damage turns into Lightning.

    """


class Ancient_Spear(Skill):
    """ Ancient Spear """
    category = "active"
    description = """
    Cost: 25 Fury

    Throw a spear that pierces enemies and deals 500% weapon damage.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/ancient-spear'


    runes = """
	 Ranseur
		 Enemies hit are knocked back 5 yards.

	 Harpoon
		 Add a chain to the spear to drag all enemies hit back to you and Slow them by 60% for 1 second.

	 Jagged Edge
		 Increase the damage to 640% weapon damage as Fire.

	 Boulder Toss
		 Expend all remaining Fury to deal 20% weapon damage for every point of Fury expended to enemies within 9 yards of the impact location.

	 Rage Flip
		 Add a chain to the spear to throw all enemies hit behind you and Slow them by 60% for 1 second.

    """


class War_Cry(Skill):
    """ War Cry """
    category = "active"
    description = """
    Generate: 20 Fury
    Cooldown: 20 seconds
    Unleash a rallying cry to increase Armor for you and all allies within 100 yards by 20% for 120 seconds.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/war-cry'


    """
	 Hardened Wrath
		 For the first 5 seconds, gain an additional 60% increased Armor.

	 Charge!
		 Increase Fury generated to 50.

	 Invigorate
		 Increase maximum Life by 10% and Life regeneration by 13,411 per second while affected by War Cry.

	 Veteran's Warning
		 Increase Dodge Chance by 30% while affected by War Cry.

	 Impunity
		 Increase resistance to all elements by 20% while affected by War Cry.

    """


class Wrath_of_the_Berserker(Skill):
    """ Wrath of the Berserker """
    category = "active"
    description = """
    Cooldown: 120 seconds

    Enter a berserker rage which raises several attributes for 20 seconds.

    Critical Hit Chance: 10% Attack Speed: 25% Dodge Chance: 20% Movement Speed: 20%
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/wrath-of-the-berserker'


    """
	 Arreat's Wail
		 Activating Wrath of the Berserker deals 3400% weapon damage as Fire to all enemies within 15 yards.

	 Insanity
		 While active, gain 50% increased damage.

	 Slaughter
		 While active, Critical Hits have a chance to cause an eruption of blood dealing 300% weapon damage to enemies within 15 yards.

	 Striding Giant
		 Reduce all damage taken by 50%.

	 Thrive on Chaos
		 While active, gain 5364 Life per Fury spent.

    """


class Avalanche(Skill):
    """ Avalanche """
    category = "active"
    description = """
    Cooldown: 30 seconds

    Cause a massive avalanche of rocks to fall on an area dealing 2400% weapon damage to all enemies caught in its path.

    Cooldown is reduced by 1 second for every 25 Fury you spend.
    """
    url = r'https://us.diablo3.com//en/class/barbarian/active/avalanche'


    """
	 Volcano
		 Chunks of molten lava are randomly launched at nearby enemies, dealing 6600% weapon damage as Fire over 5 seconds.

	 Lahar
		 Cooldown is reduced by 1 second for every 15 Fury spent.

	 Snow-Capped Mountain
		 Cave-in from both sides pushes enemies together, dealing 2800% weapon damage as Cold and Slowing them by 60% for 3 seconds.

	 Tectonic Rift
		 Store up to 3 charges of Avalanche.

	 Glacier
		 Giant blocks of ice hit enemies for 2400% weapon damage as Cold and Freeze them.

    """


""" Classes.MONK active skills """
from datatypes import Active
from datatypes import Rune


class Thunderclap(Rune):
    """ Thunderclap """
    description = """Release an electric shockwave with every punch that hits all enemies within 6 yards of your primary enemy for 120% weapon damage as Lightning and causes knockback with every third hit."""


class Wind_Blast(Rune):
    """ Wind Blast """
    description = """Every third hit Freezes enemies for 2 seconds.

Fists of Thunder's damage turns into Cold."""


class Static_Charge(Rune):
    """ Static Charge """
    description = """Fists of Thunder applies Static Charge to enemies hit for 6 seconds. Each time an enemy with Static Charge gets hit by you, there is a chance that every other enemy with Static Charge within 40 yards takes 40% weapon damage as Lightning."""


class Quickening(Rune):
    """ Quickening """
    description = """Increase Spirit generated to 20.

Fists of Thunder's damage turns into Physical."""


class Bounding_Light(Rune):
    """ Bounding Light """
    description = """Every third hit also releases arcs of holy power, dealing 240% weapon damage as Holy to up to 3 additional enemies."""


class Fists_of_Thunder(Active):
    """ Fists of Thunder """
    category = "active"
    description = """Generate: 14 Spirit per attack

Teleport to your target and unleash a series of extremely fast punches that deal 200% weapon damage as Lightning.

Every third hit deals 400% weapon damage as Lightning split between all enemies in front of you."""
    url = r'https://us.diablo3.com//en/class/monk/active/fists-of-thunder'
    runes = [Thunderclap, Wind_Blast, Static_Charge, Quickening, Bounding_Light]


class Vulture_Claw_Kick(Rune):
    """ Vulture Claw Kick """
    description = """Release a torrent of fire that burns enemies within 10 yards for 755% weapon damage as Fire and an additional 230% weapon damage as Fire over 3 seconds."""


class Sweeping_Armada_(Rune):
    """ Sweeping Armada  """
    description = """Unleash a large roundhouse kick that deals 825% weapon damage as Physical to enemies within 15 yards."""


class Spinning_Flame_Kick(Rune):
    """ Spinning Flame Kick """
    description = """Hurl a column of fire that burns through enemies, causing 755% weapon damage as Fire to each enemy it strikes."""


class Scorpion_Sting(Rune):
    """ Scorpion Sting """
    description = """Enemies hit are stunned for 2 seconds.

Lashing Tail Kick's damage turns into Lightning."""


class Hand_of_Ytar(Rune):
    """ Hand of Ytar """
    description = """Enemies are chilled at long range, Slowing them by 80% for 3 seconds.

Lashing Tail Kick's damage turns into Cold."""


class Lashing_Tail_Kick(Active):
    """ Lashing Tail Kick """
    category = "active"
    description = """Cost: 50 Spirit

Unleash a deadly roundhouse kick that deals 755% weapon damage as Physical."""
    url = r'https://us.diablo3.com//en/class/monk/active/lashing-tail-kick'
    runes = [Vulture_Claw_Kick, Sweeping_Armada_, Spinning_Flame_Kick, Scorpion_Sting, Hand_of_Ytar]


class Piercing_Trident(Rune):
    """ Piercing Trident """
    description = """Increases chance to knock enemies up into the air to 100% and the second and third hits gain increased area of effect."""


class Searing_Grasp(Rune):
    """ Searing Grasp """
    description = """Increase damage to 260% weapon damage as Fire."""


class Scattered_Blows(Rune):
    """ Scattered Blows """
    description = """Every third hit randomly damages enemies within 25 yards for 215% weapon damage as Lightning."""


class Strike_from_Beyond(Rune):
    """ Strike from Beyond """
    description = """Each enemy hit with the third hit reduces the Spirit cost of your next Spirit Spender by 8%.

Deadly Reach's damage turns into Cold."""


class Foresight(Rune):
    """ Foresight """
    description = """Every third hit also increases the damage of all your attacks by 15% for 5 seconds."""


class Deadly_Reach(Active):
    """ Deadly Reach """
    category = "active"
    description = """Generate: 12 Spirit per attack

Project lines of pure force over a short distance for 150% weapon damage as Physical.

Every third hit has a 50% chance to knock enemies up into the air."""
    url = r'https://us.diablo3.com//en/class/monk/active/deadly-reach'
    runes = [Piercing_Trident, Searing_Grasp, Scattered_Blows, Strike_from_Beyond, Foresight]


class Self_Reflection(Rune):
    """ Self Reflection """
    description = """Increase the duration enemies are blinded to 6 seconds."""


class Mystifying_Light(Rune):
    """ Mystifying Light """
    description = """Blinded enemies are also slowed by 80% for 5 seconds."""


class Replenishing_Light(Rune):
    """ Replenishing Light """
    description = """Each enemy you Blind restores 10 Spirit."""


class Crippling_Light(Rune):
    """ Crippling Light """
    description = """Enemies that are Blinded deal 25% reduced damage for 5 seconds after the Blind wears off."""


class Faith_in_the_Light(Rune):
    """ Faith in the Light """
    description = """You deal 29% increased damage for 3 seconds after using Blinding Flash."""


class Blinding_Flash(Active):
    """ Blinding Flash """
    category = "active"
    description = """Cooldown: 15 seconds

Create a flash of light that blinds all enemies within 20 yards for 3 seconds. Elite enemies recover faster, but suffer a 30% chance to miss with attacks."""
    url = r'https://us.diablo3.com//en/class/monk/active/blinding-flash'
    runes = [Self_Reflection, Mystifying_Light, Replenishing_Light, Crippling_Light, Faith_in_the_Light]


class Northern_Breeze(Rune):
    """ Northern Breeze """
    description = """Reduce the Spirit cost of Tempest Rush to 25 Spirit and increase its damage to 500% weapon damage as Holy."""


class Tailwind(Rune):
    """ Tailwind """
    description = """Increases your movement speed while using Tempest Rush by 25%."""


class Flurry(Rune):
    """ Flurry """
    description = """After you stop channeling Tempest Rush, you cause an icy blast to all enemies within 15 yards. The damage of the explosion increases by 90% weapon damage as Cold while channeling.

Tempest Rush's damage turns into Cold."""


class Electric_Field(Rune):
    """ Electric Field """
    description = """Enemies within 20 yards take an additional 135% weapon damage as Lightning every second.

Tempest Rush's damage turns into Lightning."""


class Bluster(Rune):
    """ Bluster """
    description = """Enemies hit are knocked back and deal 20% reduced damage for 4 seconds.

Tempest Rush's damage turns into Fire."""


class Tempest_Rush(Active):
    """ Tempest Rush """
    category = "active"
    description = """Cost: 30 Spirit

Charge directly through your enemies, dealing 390% weapon damage while running."""
    url = r'https://us.diablo3.com//en/class/monk/active/tempest-rush'
    runes = [Northern_Breeze, Tailwind, Flurry, Electric_Field, Bluster]


class Circle_of_Scorn(Rune):
    """ Circle of Scorn """
    description = """Breath of Heaven also sears enemies for 505% weapon damage as Holy. """


class Circle_of_Life(Rune):
    """ Circle of Life """
    description = """Increase the healing power of Breath of Heaven to 139,469 - 182,383 Life.

Heal amount is increased by 30% of your Health Globe Healing Bonus."""


class Blazing_Wrath(Rune):
    """ Blazing Wrath """
    description = """Breath of Heaven increases the damage of your attacks by 10% for 9 seconds."""


class Infused_with_Light(Rune):
    """ Infused with Light """
    description = """Gain 14 additional Spirit from Spirit generating attacks for 5 seconds after using Breath of Heaven."""


class Zephyr(Rune):
    """ Zephyr """
    description = """Allies healed by Breath of Heaven have their movement speed increased by 30% for 3 seconds."""


class Breath_of_Heaven(Active):
    """ Breath of Heaven """
    category = "active"
    description = """Cooldown: 15 seconds

A blast of divine energy heals you and all allies within 12 yards for 69,735 - 91,192 Life.

Heal amount is increased by 30% of your Health Globe Healing Bonus."""
    url = r'https://us.diablo3.com//en/class/monk/active/breath-of-heaven'
    runes = [Circle_of_Scorn, Circle_of_Life, Blazing_Wrath, Infused_with_Light, Zephyr]


class Way_of_the_Falling_Star(Rune):
    """ Way of the Falling Star """
    description = """Gain 20% increased movement speed for 4 seconds after using Dashing Strike.

Dashing Strike's damage turns into Holy."""


class Blinding_Speed(Rune):
    """ Blinding Speed """
    description = """Gain 40% increased chance to Dodge for 4 seconds after using Dashing Strike.

Dashing Strike's damage turns into Cold."""


class Quicksilver(Rune):
    """ Quicksilver """
    description = """Increases maximum charges to 3.

Dashing Strike's damage turns into Lightning."""


class Radiance(Rune):
    """ Radiance """
    description = """Gain 15% increased attack speed for 4 seconds after using Dashing Strike.

Dashing Strike's damage turns into Fire."""


class Barrage(Rune):
    """ Barrage """
    description = """The last enemy you dash through is obliterated with a barrage of strikes, taking an additional 975% weapon damage as Physical over 2 seconds."""


class Dashing_Strike(Active):
    """ Dashing Strike """
    category = "active"
    description = """Cost: 1 Charge

Quickly dash up to 50 yards, striking enemies along the way for 370% weapon damage as Physical.

You gain a charge every 8 seconds and can have up to 2 charges stored at a time."""
    url = r'https://us.diablo3.com//en/class/monk/active/dashing-strike'
    runes = [Way_of_the_Falling_Star, Blinding_Speed, Quicksilver, Radiance, Barrage]


class Mangle(Rune):
    """ Mangle """
    description = """Increase damage to 255% weapon damage as Fire."""


class Concussion(Rune):
    """ Concussion """
    description = """Enemies hit by Crippling Wave deal 20% less damage for 3 seconds."""


class Rising_Tide(Rune):
    """ Rising Tide """
    description = """Each enemy hit generates 2.5 additional Spirit.

Crippling Wave's damage turns into Holy."""


class Tsunami(Rune):
    """ Tsunami """
    description = """Crippling Wave's third attack has its range increased to 17 yards and Freezes enemies for 1 second.

Crippling Wave's damage turns into Cold."""


class Breaking_Wave(Rune):
    """ Breaking Wave """
    description = """Enemies hit by Crippling Wave take 10% additional damage from all attacks for 3 seconds."""


class Crippling_Wave(Active):
    """ Crippling Wave """
    category = "active"
    description = """Generate: 12 Spirit per attack

Unleash a series of large sweeping attacks that deal 155% weapon damage as Physical to all enemies in front of you.

Every third hit also dazes enemies within 11 yards, slowing their movement speed by 30% and attack speed by 20% for 3 seconds."""
    url = r'https://us.diablo3.com//en/class/monk/active/crippling-wave'
    runes = [Mangle, Concussion, Rising_Tide, Tsunami, Breaking_Wave]


class Wall_of_Light(Rune):
    """ Wall of Light """
    description = """Wave of Light Stuns enemies for 1 second.

Wave of Light's damage turns into Physical."""


class Explosive_Light(Rune):
    """ Explosive Light """
    description = """Release bursts of energy that deal 830% weapon damage as Fire to nearby enemies."""


class Empowered_Wave(Rune):
    """ Empowered Wave """
    description = """Increases the damage of Wave of Light to 1045% weapon damage as Holy."""


class Shattering_Light(Rune):
    """ Shattering Light """
    description = """Wave of Light deals an additional 820% weapon damage as Cold in a line."""


class Pillar_of_the_Ancients(Rune):
    """ Pillar of the Ancients """
    description = """Summon an ancient pillar that deals 635% weapon damage as Lightning, followed by 785% weapon damage as Lightning over 3 seconds to enemies who remain in the area."""


class Wave_of_Light(Active):
    """ Wave of Light """
    category = "active"
    description = """Cost: 75 Spirit

Focus a wave of light that crushes enemies for 835% weapon damage as Holy."""
    url = r'https://us.diablo3.com//en/class/monk/active/wave-of-light'
    runes = [Wall_of_Light, Explosive_Light, Empowered_Wave, Shattering_Light, Pillar_of_the_Ancients]


class The_Flesh_is_Weak(Rune):
    """ The Flesh is Weak """
    description = """Enemies hit take 15% additional damage for 9 seconds."""


class Strong_Spirit(Rune):
    """ Strong Spirit """
    description = """If the enemy explodes after bleeding, gain 15 Spirit for each enemy caught in the blast.

Exploding Palm's damage turns into Holy."""


class Impending_Doom(Rune):
    """ Impending Doom """
    description = """Exploding Palm no longer causes the enemy to bleed, but if the enemy dies while affected by Exploding Palm, they explode for 6305% weapon damage as Cold."""


class Shocking_Grasp(Rune):
    """ Shocking Grasp """
    description = """Exploding Palm arcs up to 15 yards to another target.

Exploding Palm's damage turns into Lightning."""


class Essence_Burn(Rune):
    """ Essence Burn """
    description = """Instead of bleeding, the enemy will burn for 1875% weapon damage as Fire over 9 seconds. If the enemy dies while burning, it explodes causing all nearby enemies to burn for 3260% weapon damage as Fire over 3 seconds."""


class Exploding_Palm(Active):
    """ Exploding Palm """
    category = "active"
    description = """Cost: 40 Spirit

Cause an enemy to Bleed for 1200% weapon damage as Physical over 9 seconds. If the enemy dies while bleeding, it explodes and deals 2770% weapon damage as Physical damage to all nearby enemies."""
    url = r'https://us.diablo3.com//en/class/monk/active/exploding-palm'
    runes = [The_Flesh_is_Weak, Strong_Spirit, Impending_Doom, Shocking_Grasp, Essence_Burn]


class Eye_of_the_Storm(Rune):
    """ Eye of the Storm """
    description = """Reduce the Spirit cost of Cyclone Strike to 26 Spirit.

Cyclone Strike's damage turns into Lightning."""


class Implosion(Rune):
    """ Implosion """
    description = """Increase the distance enemies will be pulled towards you to 34 yards."""


class Sunburst(Rune):
    """ Sunburst """
    description = """Blast enemies with an explosion that deals 454% weapon damage as Fire."""


class Wall_of_Wind(Rune):
    """ Wall of Wind """
    description = """Enemies are Frozen for 1.5 seconds after being pulled in.

Cyclone Strike's damage turns into Cold."""


class Soothing_Breeze(Rune):
    """ Soothing Breeze """
    description = """Cyclone Strike heals you and all allies within 24 yards for 31,036 Life.

Heal amount is increased by 17% of your Health Globe Healing Bonus."""


class Cyclone_Strike(Active):
    """ Cyclone Strike """
    category = "active"
    description = """Cost: 50 Spirit

Pull up to 16 enemies within 24 yards towards you, followed by a furious blast of energy that deals 261% weapon damage as Holy."""
    url = r'https://us.diablo3.com//en/class/monk/active/cyclone-strike'
    runes = [Eye_of_the_Storm, Implosion, Sunburst, Wall_of_Wind, Soothing_Breeze]


class Hands_of_Lightning(Rune):
    """ Hands of Lightning """
    description = """Increase the number of hits in the second strike from 7 to 10 and increasing damage to 423% weapon damage as Lightning."""


class Blazing_Fists(Rune):
    """ Blazing Fists """
    description = """Critical Hits increase your attack speed and movement speed by 5% for 5 seconds. This effect can stack up to 3 times.

Way of the Hundred Fists's damage turns into Fire."""


class Fists_of_Fury(Rune):
    """ Fists of Fury """
    description = """Perform a short dash with the first attack and enemies hit take an additional 60% weapon damage as Holy over 3 seconds. Fists of Fury damage can stack multiple times on the same enemy."""


class Assimilation(Rune):
    """ Assimilation """
    description = """Each enemy hit with the third hit increases your damage by 5% for 5 seconds."""


class Windforce_Flurry(Rune):
    """ Windforce Flurry """
    description = """Every third hit also generates a wave of wind that deals 500% weapon damage as Cold to enemies directly ahead of you.

Way of the Hundred Fists's damage turns into Cold."""


class Way_of_the_Hundred_Fists(Active):
    """ Way of the Hundred Fists """
    category = "active"
    description = """Generate: 12 Spirit per attack

Unleash a rapid series of punches that strike enemies for 190% weapon damage as Physical."""
    url = r'https://us.diablo3.com//en/class/monk/active/way-of-the-hundred-fists'
    runes = [Hands_of_Lightning, Blazing_Fists, Fists_of_Fury, Assimilation, Windforce_Flurry]


class Peaceful_Repose(Rune):
    """ Peaceful Repose """
    description = """When activated, Serenity heals you for 93,874 - 120,695 Life.

Heal amount is increased by 40% of your Health Globe Healing Bonus."""


class Unwelcome_Disturbance(Rune):
    """ Unwelcome Disturbance """
    description = """While under the effects of Serenity, enemies within 20 yards take 438% weapon damage as Physical every second."""


class Tranquility(Rune):
    """ Tranquility """
    description = """Protect allies within 45 yards with a shield that removes control impairing effects and redirects up to 120,158 damage to you for 3 seconds.

Shield amount is increased by 40% of your Health Globe Healing Bonus."""


class Ascension(Rune):
    """ Ascension """
    description = """Increase the duration of Serenity to 4 seconds. """


class Instant_Karma(Rune):
    """ Instant Karma """
    description = """While under the effects of Serenity, your movement is unhindered."""


class Serenity(Active):
    """ Serenity """
    category = "active"
    description = """Cooldown: 16 seconds

You are enveloped in a protective shield that absorbs all incoming damage for 3 seconds and grants immunity to all control impairing effects.

This ability does not start its cooldown until after its effects expire."""
    url = r'https://us.diablo3.com//en/class/monk/active/serenity'
    runes = [Peaceful_Repose, Unwelcome_Disturbance, Tranquility, Ascension, Instant_Karma]


class Sudden_Assault(Rune):
    """ Sudden Assault """
    description = """Teleport to the enemy and increase damage dealt to 8285% weapon damage as Lightning over 7 strikes."""


class Incinerate(Rune):
    """ Incinerate """
    description = """Seven-Sided Strike causes enemies to burn for 630% weapon damage as Fire over 3 seconds."""


class Pandemonium(Rune):
    """ Pandemonium """
    description = """Removes the Spirit cost and enemies hit by Seven-Sided Strike are Frozen for 7 seconds."""


class Sustained_Attack(Rune):
    """ Sustained Attack """
    description = """Reduce the cooldown to 14 seconds."""


class Fulminating_Onslaught(Rune):
    """ Fulminating Onslaught """
    description = """Each strike explodes, dealing 877% weapon damage as Holy in a 7 yard radius around the enemy."""


class Seven_Sided_Strike(Active):
    """ Seven-Sided Strike """
    category = "active"
    description = """Cost: 50 Spirit
Cooldown: 30 seconds

Dash rapidly between nearby enemies, dealing 5677% weapon damage over 7 strikes.

This ability does not start its cooldown until after its effects expire."""
    url = r'https://us.diablo3.com//en/class/monk/active/sevensided-strike'
    runes = [Sudden_Assault, Incinerate, Pandemonium, Sustained_Attack, Fulminating_Onslaught]


class Hard_Target(Rune):
    """ Hard Target """
    description = """Passive: Mantra of Salvation also increases Armor by 20%."""


class Divine_Protection(Rune):
    """ Divine Protection """
    description = """Passive: Mantra of Salvation also protects you and your allies when reduced below 25% Life, granting a shield that reduces damage taken by 80% for 3 seconds.

Each target may be protected by this effect once every 90 seconds."""


class Wind_through_the_Reeds(Rune):
    """ Wind through the Reeds """
    description = """Passive: Mantra of Salvation also increases movement speed by 10%."""


class Perseverance(Rune):
    """ Perseverance """
    description = """Passive: Increases the resistance to all elements bonus to 40%."""


class Agility(Rune):
    """ Agility """
    description = """Passive: Mantra of Salvation also increases Dodge Chance by 35%."""


class Mantra_of_Salvation(Active):
    """ Mantra of Salvation """
    category = "active"
    description = """Cost: 50 Spirit

Active: You and nearby allies gain an additional 20% increased resistance to all elements for 3 seconds.

Passive: You and your allies within 60 yards gain 20% increased resistance to all elements.

Only one Mantra may be active at a time."""
    url = r'https://us.diablo3.com//en/class/monk/active/mantra-of-salvation'
    runes = [Hard_Target, Divine_Protection, Wind_through_the_Reeds, Perseverance, Agility]


class Master_of_Wind(Rune):
    """ Master of Wind """
    description = """While your vortex is at 3 or more stacks, enemies damaged by Sweeping Wind for 3 consecutive seconds are Frozen for 2 seconds.

Enemies cannot be frozen by Sweeping Wind more than once every 3 seconds.

Sweeping Wind's damage turns into Cold."""


class Blade_Storm(Rune):
    """ Blade Storm """
    description = """Intensify the vortex, increasing the damage per stack to 145% weapon damage. This increases the damage with 3 stacks to 435% weapon damage."""


class Fire_Storm(Rune):
    """ Fire Storm """
    description = """Increase the radius of the vortex to 14 yards.

Sweeping Wind's damage turns into Fire."""


class Inner_Storm(Rune):
    """ Inner Storm """
    description = """As long as your vortex is at 3 or more stacks, you gain 8 Spirit per second.

Sweeping Wind's damage turns into Holy."""


class Cyclone(Rune):
    """ Cyclone """
    description = """While your vortex is at 3 or more stacks, Critical Hits have a chance to spawn a lightning tornado that periodically electrocutes nearby enemies for 95% weapon damage as Lightning. Each spawned lightning tornado lasts 3 seconds.

Sweeping Wind's damage turns into Lightning."""


class Sweeping_Wind(Active):
    """ Sweeping Wind """
    category = "active"
    description = """Cost: 75 Spirit

Surround yourself in a vortex that continuously deals 105% weapon damage to all enemies within 10 yards. The vortex lasts 6 seconds and is refreshed each time you strike an enemy with a melee attack. Landing a Critical Hit has a chance to increase the vortex effect up to 3 stacks for a total of 315% weapon damage."""
    url = r'https://us.diablo3.com//en/class/monk/active/sweeping-wind'
    runes = [Master_of_Wind, Blade_Storm, Fire_Storm, Inner_Storm, Cyclone]


class Retaliation(Rune):
    """ Retaliation """
    description = """Passive: Increase the amount of damage inflicted by Mantra of Retribution to 202% weapon damage as Fire."""


class Transgression(Rune):
    """ Transgression """
    description = """Passive: Mantra of Retribution also increases attack speed by 10% for you and your allies."""


class Indignation(Rune):
    """ Indignation """
    description = """Passive: Enemies damaged by Mantra of Retribution have a 20% chance to be stunned for 3 seconds."""


class Against_All_Odds(Rune):
    """ Against All Odds """
    description = """Passive: Mantra of Retribution has a chance to restore 3 Spirit when dealing damage."""


class Collateral_Damage(Rune):
    """ Collateral Damage """
    description = """Passive: Enemies damaged by Mantra of Retribution have a 75% chance to suffer a feedback blast, dealing 101% weapon damage as Holy to itself and nearby enemies."""


class Mantra_of_Retribution(Active):
    """ Mantra of Retribution """
    category = "active"
    description = """Cost: 50 Spirit

Active: Increase the amount of damage dealt to 202% for 3 seconds.

Passive: You and your allies within 60 yards deal 101% of your weapon damage as Holy to attackers when blocking, dodging or getting hit.

Only one Mantra may be active at a time."""
    url = r'https://us.diablo3.com//en/class/monk/active/mantra-of-retribution'
    runes = [Retaliation, Transgression, Indignation, Against_All_Odds, Collateral_Damage]


class Sanctified_Ground(Rune):
    """ Sanctified Ground """
    description = """Inner Sanctuary duration is increased to 8 seconds and cannot be passed by enemies."""


class Safe_Haven(Rune):
    """ Safe Haven """
    description = """Allies inside Inner Sanctuary are healed for 35,779 every second.

Heal amount is increased by 7% of your Life per Second."""


class Temple_of_Protection(Rune):
    """ Temple of Protection """
    description = """Allies inside Inner Sanctuary are also immune to control impairing effects."""


class Intervene(Rune):
    """ Intervene """
    description = """Dash to the target location, granting a shield that absorbs up to 107,284 damage for 3 seconds to allies within 11 yards and then creating Inner Sanctuary.

Absorb amount is increased by 28% of your Health Globe Healing Bonus."""


class Forbidden_Palace(Rune):
    """ Forbidden Palace """
    description = """Enemies inside Inner Sanctuary have their movement speed reduced by 80%."""


class Inner_Sanctuary(Active):
    """ Inner Sanctuary """
    category = "active"
    description = """Cooldown: 20 seconds

Create a runic circle of protection on the ground for 6 seconds that reduces all damage taken by 55% for all allies inside."""
    url = r'https://us.diablo3.com//en/class/monk/active/inner-sanctuary'
    runes = [Sanctified_Ground, Safe_Haven, Temple_of_Protection, Intervene, Forbidden_Palace]


class Water_Ally(Rune):
    """ Water Ally """
    description = """Active: Your mystic ally performs 7 wave attacks in quick succession, each dealing 625% weapon damage as Cold and Freezing enemies for 3 seconds.

Passive: A mystic ally fights by your side that infuses your attacks to Slow enemies by 60% for 3 seconds."""


class Fire_Ally(Rune):
    """ Fire Ally """
    description = """Active: Your mystic ally splits into 5 allies that explode for 480% weapon damage as Fire.

Passive: A mystic ally fights by your side that increases your damage by 10%."""


class Air_Ally(Rune):
    """ Air Ally """
    description = """Active: You gain 100 Spirit.

Passive: A mystic ally fights by your side that increases your Spirit Regeneration by 4."""


class Enduring_Ally(Rune):
    """ Enduring Ally """
    description = """Active: Your mystic ally sacrifices itself to heal you for 100% of your maximum Life. The cooldown on Mystic Ally is increased to 50 seconds.

Passive: A mystic ally fights by your side that increases your Life per Second by 10,728. The heal amount is increased by 7% of your Life per Second."""


class Earth_Ally(Rune):
    """ Earth Ally """
    description = """Active: Your mystic ally turns into a boulder for 8 seconds. The boulder deals 380% weapon damage as Physical every second and rolls toward nearby enemies, knocking them up.

Passive: A mystic ally fights by your side that increases your Life by 20%."""


class Mystic_Ally(Active):
    """ Mystic Ally """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Your mystic ally has its damage increased by 50% for 10 seconds.

Passive: A mystic ally fights by your side. The ally deals 130% of your weapon damage as Physical per swing. When the ally dies, it is reborn after 5 seconds."""
    url = r'https://us.diablo3.com//en/class/monk/active/mystic-ally'
    runes = [Water_Ally, Fire_Ally, Air_Ally, Enduring_Ally, Earth_Ally]


class Sustenance(Rune):
    """ Sustenance """
    description = """Passive: Increase the Life regeneration granted by Mantra of Healing to 21,457 Life per Second.

Heal amount is increased by 7% of your Life per Second."""


class Circular_Breathing(Rune):
    """ Circular Breathing """
    description = """Passive: Mantra of Healing also regenerates 3 Spirit per second."""


class Boon_of_Inspiration(Rune):
    """ Boon of Inspiration """
    description = """Passive: Mantra of Healing also heals 3576 Life when hitting an enemy.

Heal amount is increased by 20% of your Life per Hit."""


class Heavenly_Body(Rune):
    """ Heavenly Body """
    description = """Passive: Mantra of Healing also increases maximum Life by 20%. """


class Time_of_Need(Rune):
    """ Time of Need """
    description = """Passive: Mantra of Healing also reduces damage taken by 30% when below 50% Life."""


class Mantra_of_Healing(Active):
    """ Mantra of Healing """
    category = "active"
    description = """Cost: 50 Spirit

Active: Shroud you and your allies with a mystical shield that absorbs up to 62,064 damage for 3 seconds. Absorb amount is increased by 15% of your Health Globe Healing Bonus.

Passive: You and your allies within 60 yards gain 10,728 increased Life regeneration. The heal amount is increased by 7% of your Life per Second.

Only one Mantra may be active at a time."""
    url = r'https://us.diablo3.com//en/class/monk/active/mantra-of-healing'
    runes = [Sustenance, Circular_Breathing, Boon_of_Inspiration, Heavenly_Body, Time_of_Need]


class Overawe(Rune):
    """ Overawe """
    description = """Passive: Increase the strength of Mantra of Conviction so that enemies take 12% increased damage."""


class Intimidation(Rune):
    """ Intimidation """
    description = """Passive: Enemies affected by Mantra of Conviction deal 15% less damage."""


class Dishearten(Rune):
    """ Dishearten """
    description = """Passive: Mantra of Conviction also slows the movement speed of enemies by 80%."""


class Annihilation(Rune):
    """ Annihilation """
    description = """Passive: Killing an enemy that is affected by Mantra of Conviction grants you and your allies 30% increased movement speed for 3 seconds."""


class Submission(Rune):
    """ Submission """
    description = """Passive: Enemies affected by Mantra of Conviction take 38% weapon damage per second as Holy."""


class Mantra_of_Conviction(Active):
    """ Mantra of Conviction """
    category = "active"
    description = """Cost: 50 Spirit

Active: Damage bonus is increased to 16% for 3 seconds.

Passive: Enemies within 30 yards of you take 8% increased damage.

Only one Mantra may be active at a time."""
    url = r'https://us.diablo3.com//en/class/monk/active/mantra-of-conviction'
    runes = [Overawe, Intimidation, Dishearten, Annihilation, Submission]


class Desert_Shroud(Rune):
    """ Desert Shroud """
    description = """Infuse yourself with sand, reducing damage taken by 50%."""


class Ascendance(Rune):
    """ Ascendance """
    description = """Charge yourself with Lightning, causing your next attack after moving 10 yards to Stun enemies for 1.5 seconds."""


class Soothing_Mist(Rune):
    """ Soothing Mist """
    description = """Imbue yourself with water, causing your abilities to heal yourself and allies within 30 yards for 16,093 Life.

Heal amount is increased by 4% of your Health Globe Healing Bonus."""


class Insight(Rune):
    """ Insight """
    description = """Increases the bonus Spirit regeneration from Epiphany to 45."""


class Inner_Fire(Rune):
    """ Inner Fire """
    description = """Engulf yourself in flames, causing your attacks to assault enemies for 353% weapon damage as Fire."""


class Epiphany(Active):
    """ Epiphany """
    category = "active"
    description = """Cooldown: 60 seconds

Have an Epiphany, increasing your Spirit Regeneration per Second by 20 and enabling your melee attacks to instantly dash to your target for 15 seconds."""
    url = r'https://us.diablo3.com//en/class/monk/active/epiphany'
    runes = [Desert_Shroud, Ascendance, Soothing_Mist, Insight, Inner_Fire]

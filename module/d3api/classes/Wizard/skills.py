""" wizard active skills """
from datatypes import Active
from datatypes import Rune


class Charged_Blast(Rune):
    """ Charged Blast """
    description = """Increase the damage of Magic Missile to 325% weapon damage as Arcane."""


class Glacial_Spike(Rune):
    """ Glacial Spike """
    description = """Cast out a shard of ice that explodes on impact, causing enemies within 4.5 yards to take 175% weapon damage as Cold and be Frozen for 1 second.

Enemies cannot be Frozen by Glacial Spike more than once every 5 seconds."""


class Split(Rune):
    """ Split """
    description = """Fire 3 missiles that each deal 80% weapon damage as Arcane."""


class Seeker(Rune):
    """ Seeker """
    description = """Missiles track the nearest enemy. Missile damage is increased to 285% weapon damage as Arcane."""


class Conflagrate(Rune):
    """ Conflagrate """
    description = """The missile pierces through enemies and causes them to burn for 130% weapon damage as Fire over 3 seconds.

Burn damage stacks up to 3 times and any Fire damage taken from your other spells refresh all stacks to their maximum duration."""


class Magic_Missile(Active):
    """ Magic Missile """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Launch a missile of magic energy, dealing 230% weapon damage as Arcane."""
    url = r'https://us.diablo3.com//en/class/wizard/active/magic-missile'
    runes = [Charged_Blast, Glacial_Spike, Split, Seeker, Conflagrate]


class Cold_Blood(Rune):
    """ Cold Blood """
    description = """Reduce channeling cost to 11 Arcane Power."""


class Numb(Rune):
    """ Numb """
    description = """Ray of Frost has a 10% chance to Freeze enemies for 1 second and increases the Slow amount to 80% for 3 seconds."""


class Black_Ice(Rune):
    """ Black Ice """
    description = """Enemies killed by Ray of Frost leave behind a patch of ice that deals 1625% weapon damage as Cold to enemies moving through it over 3 seconds."""


class Sleet_Storm(Rune):
    """ Sleet Storm """
    description = """Create a swirling storm around you that grows up to a 22 yard radius, dealing 300% weapon damage as Cold to all enemies caught within it.

Ray of Frost damage is increased by 220% weapon damage every second, up to a maximum total of 740% weapon damage as Cold."""


class Snow_Blast(Rune):
    """ Snow Blast """
    description = """Enemies hit by Ray of Frost take 15% increased damage from Cold for 4 seconds."""


class Ray_of_Frost(Active):
    """ Ray of Frost """
    category = "active"
    description = """Cost: 16 Arcane Power

Project a beam of frozen ice that blasts enemies within 5 yards of the first enemy hit for 430% weapon damage as Cold and Slows their movement by 60% for 3 seconds.

Ray of Frost damage is increased by 405% weapon damage every second, up to a maximum total of 1240% weapon damage as Cold."""
    url = r'https://us.diablo3.com//en/class/wizard/active/ray-of-frost'
    runes = [Cold_Blood, Numb, Black_Ice, Sleet_Storm, Snow_Blast]


class Explosive_Bolts(Rune):
    """ Explosive Bolts """
    description = """Slain enemies explode, dealing 184% weapon damage as Cold to every enemy within 10 yards.

Shock Pulse's damage turns into Cold."""


class Fire_Bolts(Rune):
    """ Fire Bolts """
    description = """Cast 3 bolts of fire that each deal 274% weapon damage as Fire."""


class Piercing_Orb(Rune):
    """ Piercing Orb """
    description = """Merge the bolts in a single giant orb that oscillates forward dealing 214% weapon damage as Lightning to everything it hits."""


class Power_Affinity(Rune):
    """ Power Affinity """
    description = """Gain 2 Arcane Power for each enemy hit.

Shock Pulse's damage turns into Arcane."""


class Living_Lightning(Rune):
    """ Living Lightning """
    description = """Conjure a being of lightning that drifts forward, electrocuting nearby enemies for 165% weapon damage as Lightning."""


class Shock_Pulse(Active):
    """ Shock Pulse """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Release a medium range pulse of 3 unpredictable charges of electricity that deal 194% weapon damage as Lightning."""
    url = r'https://us.diablo3.com//en/class/wizard/active/shock-pulse'
    runes = [Explosive_Bolts, Fire_Bolts, Piercing_Orb, Power_Affinity, Living_Lightning]


class Shatter(Rune):
    """ Shatter """
    description = """A frozen enemy that is killed has a 100% chance of releasing another Frost Nova."""


class Cold_Snap(Rune):
    """ Cold Snap """
    description = """Reduce the cooldown to 7.5 seconds and increase the Freeze duration to 3 seconds."""


class Frozen_Mist(Rune):
    """ Frozen Mist """
    description = """Frost Nova no longer freezes enemies, but instead leaves behind a mist of frost that deals 915% weapon damage as Cold over 8 seconds."""


class Deep_Freeze(Rune):
    """ Deep Freeze """
    description = """Gain a 10% bonus to Critical Hit Chance for 11 seconds if Frost Nova hits 5 or more enemies."""


class Bone_Chill(Rune):
    """ Bone Chill """
    description = """Enemies take 33% more damage while frozen or chilled by Frost Nova."""


class Frost_Nova(Active):
    """ Frost Nova """
    category = "active"
    description = """Cooldown: 11 seconds

Blast nearby enemies with an explosion of ice and freeze them for 2 seconds."""
    url = r'https://us.diablo3.com//en/class/wizard/active/frost-nova'
    runes = [Shatter, Cold_Snap, Frozen_Mist, Deep_Freeze, Bone_Chill]


class Obliteration(Rune):
    """ Obliteration """
    description = """Increase the speed of the orb and its damage to 700% weapon damage as Arcane, but reduce the area of effect to 8 yards."""


class Arcane_Orbit(Rune):
    """ Arcane Orbit """
    description = """Create 4 Arcane Orbs that orbit you, exploding for 265% weapon damage as Arcane when enemies get close. """


class Spark(Rune):
    """ Spark """
    description = """Lob an electrified orb over enemies that zaps them for 349% weapon damage as Lightning and increases the damage of the next Lightning spell you cast by 2% for every enemy hit up to a maximum of 15."""


class Scorch(Rune):
    """ Scorch """
    description = """Launch a burning orb that deals 221% weapon damage as Fire. The orb leaves behind a wall of Fire that deals 734% weapon damage as Fire over 5 seconds."""


class Frozen_Orb(Rune):
    """ Frozen Orb """
    description = """Create an orb of frozen death that shreds an area with ice bolts, dealing 950% weapon damage as Cold."""


class Arcane_Orb(Active):
    """ Arcane Orb """
    category = "active"
    description = """Cost: 30 Arcane Power

Hurl an orb of pure energy that explodes on contact, dealing 435% weapon damage as Arcane to all enemies within 15 yards."""
    url = r'https://us.diablo3.com//en/class/wizard/active/arcane-orb'
    runes = [Obliteration, Arcane_Orbit, Spark, Scorch, Frozen_Orb]


class Crystal_Shell(Rune):
    """ Crystal Shell """
    description = """Increase the maximum amount of damage absorbed to 80% of your Life."""


class Prism(Rune):
    """ Prism """
    description = """Reduce the Arcane Power cost of all skills by 9 while Diamond Skin is active."""


class Sleek_Shell(Rune):
    """ Sleek Shell """
    description = """Increases your movement speed by 30% while Diamond Skin is active."""


class Enduring_Skin(Rune):
    """ Enduring Skin """
    description = """Increase the duration of Diamond Skin to 6 seconds."""


class Diamond_Shards(Rune):
    """ Diamond Shards """
    description = """When Diamond Skin fades, diamond shards explode in all directions dealing 863% weapon damage as Arcane to nearby enemies."""


class Diamond_Skin(Active):
    """ Diamond Skin """
    category = "active"
    description = """Cooldown: 15 seconds

Transform your skin to diamond for 3 seconds, absorbing up to 40% of your Life in damage from incoming attacks."""
    url = r'https://us.diablo3.com//en/class/wizard/active/diamond-skin'
    runes = [Crystal_Shell, Prism, Sleek_Shell, Enduring_Skin, Diamond_Shards]


class Impactful_Wave(Rune):
    """ Impactful Wave """
    description = """Wave of Force repels projectiles back toward their shooter, knocks back nearby enemies and Slows them by 60% for 3 seconds.

Wave of Force gains a 5 second cooldown."""


class Debilitating_Force(Rune):
    """ Debilitating Force """
    description = """Enemies hit deal 20% reduced damage for 4 seconds."""


class Arcane_Attunement(Rune):
    """ Arcane Attunement """
    description = """Each enemy hit increases the damage of your next Arcane spell by 4%."""


class Static_Pulse(Rune):
    """ Static Pulse """
    description = """Each enemy hit restores 1 Arcane Power.

Wave of Force's damage turns into Lightning."""


class Heat_Wave(Rune):
    """ Heat Wave """
    description = """Increase the damage to 475% weapon damage as Fire."""


class Wave_of_Force(Active):
    """ Wave of Force """
    category = "active"
    description = """Cost: 25 Arcane Power

Discharge a wave of pure energy that deals 390% weapon damage as Arcane to nearby enemies."""
    url = r'https://us.diablo3.com//en/class/wizard/active/wave-of-force'
    runes = [Impactful_Wave, Debilitating_Force, Arcane_Attunement, Static_Pulse, Heat_Wave]


class Flame_Blades(Rune):
    """ Flame Blades """
    description = """Each enemy hit increases the damage of your Fire spells by 1%, up to a maximum of 30%, for 5 seconds."""


class Siphoning_Blade(Rune):
    """ Siphoning Blade """
    description = """Gain 2 Arcane Power for each enemy hit."""


class Thrown_Blade(Rune):
    """ Thrown Blade """
    description = """Extend the reach of Spectral Blade to 20 yards and increase its damage to 231% weapon damage as Lightning."""


class Barrier_Blades(Rune):
    """ Barrier Blades """
    description = """With each cast, gain a protective shield for 3 seconds that absorbs 4% of your Life in damage."""


class Ice_Blades(Rune):
    """ Ice Blades """
    description = """Chilled enemies have a 5% chance to be Frozen and Frozen enemies have a 5% increased chance to be critically hit by Spectral Blade."""


class Spectral_Blade(Active):
    """ Spectral Blade """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Summon a spectral blade that strikes all enemies up to 15 yards in front of you for 168% weapon damage as Arcane."""
    url = r'https://us.diablo3.com//en/class/wizard/active/spectral-blade'
    runes = [Flame_Blades, Siphoning_Blade, Thrown_Blade, Barrier_Blades, Ice_Blades]


class Flame_Ward(Rune):
    """ Flame Ward """
    description = """You take 15% less damage from attacks while channeling. Every second you channel increases this amount by 5%, up to a maximum total of 25% damage reduction.

Arcane Torrent's damage turns into Fire."""


class Death_Blossom(Rune):
    """ Death Blossom """
    description = """Unleash a torrent of power beyond your control. You no longer direct where the projectiles go, but their damage is greatly increased to 1215% weapon damage as Arcane.

Arcane Torrent damage is increased by 640% weapon damage every second, up to a maximum total of 2495% weapon damage as Arcane."""


class Arcane_Mines(Rune):
    """ Arcane Mines """
    description = """Lay Arcane mines that arm after 2 seconds. These mines explode when an enemy approaches, dealing 825% weapon damage as Arcane. Enemies caught in the explosion have their movement and attack speeds reduced by 60% for 3 seconds."""


class Static_Discharge(Rune):
    """ Static Discharge """
    description = """Each missile explodes into 2 piercing bolts of electricity that each deal 150% weapon damage as Lightning."""


class Cascade(Rune):
    """ Cascade """
    description = """Enemies hit by Arcane Torrent have a 12.5% chance to fire a new missile at a nearby enemy dealing 582% weapon damage as Arcane."""


class Arcane_Torrent(Active):
    """ Arcane Torrent """
    category = "active"
    description = """Cost: 16 Arcane Power

Hurl a barrage of arcane projectiles that deal 400% weapon damage as Arcane to all enemies near the impact location.

Arcane Torrent damage is increased by 305% weapon damage every second, up to a maximum total of 1010% weapon damage as Arcane."""
    url = r'https://us.diablo3.com//en/class/wizard/active/arcane-torrent'
    runes = [Flame_Ward, Death_Blossom, Arcane_Mines, Static_Discharge, Cascade]


class Mistral_Breeze(Rune):
    """ Mistral Breeze """
    description = """Reduce the casting cost of Energy Twister to 25 Arcane Power.

Energy Twister's damage turns into Cold."""


class Gale_Force(Rune):
    """ Gale Force """
    description = """Enemies hit by Energy Twister take 15% increased damage from Fire for 4 seconds."""


class Raging_Storm(Rune):
    """ Raging Storm """
    description = """When two Energy Twisters collide, they merge into a tornado with increased area of effect that causes 3200% weapon damage as Arcane over 6 seconds."""


class Wicked_Wind(Rune):
    """ Wicked Wind """
    description = """Energy Twister no longer travels but spins in place, dealing 835% weapon damage as Arcane over 6 seconds to everything caught in it."""


class Storm_Chaser(Rune):
    """ Storm Chaser """
    description = """Each cast of Energy Twister grants you a Lightning Charge. You can store up to 3 Lightning Charges at a time. Casting a Signature spell releases all Lightning Charges as a bolt of Lightning that deals 196% weapon damage as Lightning per Lightning Charge.

Energy Twister's damage turns into Lightning.

The following skills are Signature spells: Magic Missile Shock Pulse Spectral Blade Electrocute"""


class Energy_Twister(Active):
    """ Energy Twister """
    category = "active"
    description = """Cost: 35 Arcane Power

Unleash a twister of pure energy that deals 1525% weapon damage as Arcane over 6 seconds to everything in its path."""
    url = r'https://us.diablo3.com//en/class/wizard/active/energy-twister'
    runes = [Mistral_Breeze, Gale_Force, Raging_Storm, Wicked_Wind, Storm_Chaser]


class Chilling_Aura(Rune):
    """ Chilling Aura """
    description = """Lower the temperature of the air around you. Nearby enemies are chilled, slowing their movement speed by 80%."""


class Crystallize(Rune):
    """ Crystallize """
    description = """When you are struck by a melee attack, your Armor is increased by 20% for 30 seconds. This effect stacks up to 3 times."""


class Jagged_Ice(Rune):
    """ Jagged Ice """
    description = """Melee attackers also take 189% weapon damage as Cold."""


class Ice_Reflect(Rune):
    """ Ice Reflect """
    description = """Melee attacks have a 40% chance to create a Frost Nova centered on the attacker, dealing 75% weapon damage as Cold."""


class Frozen_Storm(Rune):
    """ Frozen Storm """
    description = """A whirling storm of ice builds around you, dealing 80% weapon damage as Cold every second."""


class Ice_Armor(Active):
    """ Ice Armor """
    category = "active"
    description = """Cost: 25 Arcane Power

Surround yourself in a barrier of ice that reduces damage from melee attacks by 12%. Melee attackers are either Chilled or Frozen for 3 seconds. Lasts 10 minutes.

Only one Armor may be active at a time."""
    url = r'https://us.diablo3.com//en/class/wizard/active/ice-armor'
    runes = [Chilling_Aura, Crystallize, Jagged_Ice, Ice_Reflect, Frozen_Storm]


class Chain_Lightning(Rune):
    """ Chain Lightning """
    description = """Increase the maximum number of enemies that can be electrocuted to 10."""


class Forked_Lightning(Rune):
    """ Forked Lightning """
    description = """Critical Hits release 4 charged bolts in random directions, dealing 44% weapon damage as Fire to any enemies hit."""


class Lightning_Blast(Rune):
    """ Lightning Blast """
    description = """Create streaks of lightning that pierce through enemies for 140% weapon damage as Lightning."""


class Surge_of_Power(Rune):
    """ Surge of Power """
    description = """Gain 1 Arcane Power for each enemy hit."""


class Arc_Lightning(Rune):
    """ Arc Lightning """
    description = """Blast a cone of lightning that deals 310% weapon damage as Lightning to all affected enemies."""


class Electrocute(Active):
    """ Electrocute """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Lightning arcs from your fingertips, dealing 138% weapon damage as Lightning. The lightning can jump, hitting up to 2 additional enemies."""
    url = r'https://us.diablo3.com//en/class/wizard/active/electrocute'
    runes = [Chain_Lightning, Forked_Lightning, Lightning_Blast, Surge_of_Power, Arc_Lightning]


class Time_Shell(Rune):
    """ Time Shell """
    description = """Increase the potency of the movement speed reduction to 80% and reduces the cooldown to 12 seconds."""


class Exhaustion(Rune):
    """ Exhaustion """
    description = """Enemies caught by Slow Time deal 25% less damage."""


class Time_Warp(Rune):
    """ Time Warp """
    description = """Enemies caught in the bubble of warped time take 15% more damage."""


class Point_of_No_Return(Rune):
    """ Point of No Return """
    description = """Enemies that enter or leave the Slow Time area are stunned for 5 seconds."""


class Stretch_Time(Rune):
    """ Stretch Time """
    description = """Time is sped up for any allies standing in the area, increasing their attack speed by 10%."""


class Slow_Time(Active):
    """ Slow Time """
    category = "active"
    description = """Cooldown: 15 seconds

Invoke a bubble of warped time and space at your target location up to 60 yards away for 15 seconds, reducing enemy attack speed by 20% and movement speed by 60%. This bubble also slows the speed of enemy projectiles by 90%."""
    url = r'https://us.diablo3.com//en/class/wizard/active/slow-time'
    runes = [Time_Shell, Exhaustion, Time_Warp, Point_of_No_Return, Stretch_Time]


class Reactive_Armor(Rune):
    """ Reactive Armor """
    description = """Ranged and melee attackers are shocked for 189% weapon damage as Lightning."""


class Power_of_the_Storm(Rune):
    """ Power of the Storm """
    description = """Reduce the Arcane Power cost of all skills by 3 while Storm Armor is active."""


class Thunder_Storm(Rune):
    """ Thunder Storm """
    description = """Increase the damage of the shock to 315% weapon damage as Lightning. """


class Scramble(Rune):
    """ Scramble """
    description = """Increase your movement speed by 25% for 3 seconds when you are hit by melee or ranged attacks."""


class Shocking_Aspect(Rune):
    """ Shocking Aspect """
    description = """Critical Hits have a chance to electrocute a nearby enemy for 425% weapon damage as Lightning."""


class Storm_Armor(Active):
    """ Storm Armor """
    category = "active"
    description = """Cost: 25 Arcane Power

Bathe yourself in electrical energy, periodically shocking a nearby enemy for 175% weapon damage as Lightning. Lasts 10 minutes.

Only one Armor may be active at a time."""
    url = r'https://us.diablo3.com//en/class/wizard/active/storm-armor'
    runes = [Reactive_Armor, Power_of_the_Storm, Thunder_Storm, Scramble, Shocking_Aspect]


class Unleashed(Rune):
    """ Unleashed """
    description = """Increases the damage of Explosive Blast to 1485%."""


class Flash(Rune):
    """ Flash """
    description = """Reduce the cooldown of Explosive Blast to 3 seconds.

Explosive Blast's damage turns into Lightning."""


class Short_Fuse(Rune):
    """ Short Fuse """
    description = """Immediately release the energy of Explosive Blast for 909% weapon damage as Fire."""


class Obliterate(Rune):
    """ Obliterate """
    description = """Release an enormous Explosive Blast that deals 990% weapon damage as Cold to all enemies within 18 yards."""


class Chain_Reaction(Rune):
    """ Chain Reaction """
    description = """Instead of a single explosion, release a chain of 3 consecutive explosions, each dealing 520% weapon damage as Fire."""


class Explosive_Blast(Active):
    """ Explosive Blast """
    category = "active"
    description = """Cost: 20 Arcane Power
Cooldown: 6 seconds

Gather an infusion of energy around you that explodes after 1.5 seconds for 945% weapon damage as Arcane to all enemies within 12 yards."""
    url = r'https://us.diablo3.com//en/class/wizard/active/explosive-blast'
    runes = [Unleashed, Flash, Short_Fuse, Obliterate, Chain_Reaction]


class Electrify(Rune):
    """ Electrify """
    description = """Attacks have a chance to cause lightning to arc to 3 nearby enemies, dealing 61% weapon damage as Lightning."""


class Force_Weapon(Rune):
    """ Force Weapon """
    description = """Increase the damage bonus of Magic Weapon to 20% damage."""


class Conduit(Rune):
    """ Conduit """
    description = """Enemies hit by your attacks restore up to 3 Arcane Power."""


class Ignite(Rune):
    """ Ignite """
    description = """Attacks have a chance to burn enemies, dealing 300% weapon damage as Fire over 3 seconds."""


class Deflection(Rune):
    """ Deflection """
    description = """When you perform an attack, gain a protective shield for 3 seconds that absorbs 4% of your Life in damage."""


class Magic_Weapon(Active):
    """ Magic Weapon """
    category = "active"
    description = """Cost: 25 Arcane Power

Imbue your weapon with magical energy, granting it 10% increased damage. Lasts 10 minutes.

Requires Weapon"""
    url = r'https://us.diablo3.com//en/class/wizard/active/magic-weapon'
    runes = [Electrify, Force_Weapon, Conduit, Ignite, Deflection]


class Arcane_Hydra(Rune):
    """ Arcane Hydra """
    description = """Summon an Arcane Hydra that spits Arcane Orbs that explode on impact, dealing 205% weapon damage as Arcane to enemies near the explosion."""


class Lightning_Hydra(Rune):
    """ Lightning Hydra """
    description = """Summon a Lightning Hydra that electrocutes enemies for 255% weapon damage as Lightning."""


class Blazing_Hydra(Rune):
    """ Blazing Hydra """
    description = """Summon a Blazing Hydra that spits bolts of Fire that burn enemies near the point of impact, dealing 155% weapon damage as Fire over 3 seconds. Burn damage can stack multiple times on the same enemy."""


class Frost_Hydra(Rune):
    """ Frost Hydra """
    description = """Summon a Frost Hydra that breathes a short range cone of frost, causing 255% weapon damage as Cold to all enemies in the cone."""


class Mammoth_Hydra(Rune):
    """ Mammoth Hydra """
    description = """Summon a Mammoth Hydra that breathes a river of flame at nearby enemies, dealing 330% weapon damage per second as Fire to enemies caught on the burning ground."""


class Hydra(Active):
    """ Hydra """
    category = "active"
    description = """Cost: 15 Arcane Power

Summon a multi-headed Hydra for 15 seconds that attacks enemies with bolts of fire dealing 165% weapon damage as Fire.

Only one Hydra may be active at a time."""
    url = r'https://us.diablo3.com//en/class/wizard/active/hydra'
    runes = [Arcane_Hydra, Lightning_Hydra, Blazing_Hydra, Frost_Hydra, Mammoth_Hydra]


class Convergence(Rune):
    """ Convergence """
    description = """Increase the width of the beam allowing it to hit more enemies.

Disintegrate's damage turns into Fire."""


class Volatility(Rune):
    """ Volatility """
    description = """Enemies killed by the beam have a 35% chance to explode causing 750% weapon damage as Arcane to all enemies within 8 yards."""


class Entropy(Rune):
    """ Entropy """
    description = """The beam fractures into a short-ranged cone that deals 435% weapon damage as Arcane.

Disintegrate damage is increased by 340% weapon damage every second, up to a maximum total of 1115% weapon damage as Arcane."""


class Chaos_Nexus(Rune):
    """ Chaos Nexus """
    description = """While channeling the beam you become charged with energy and discharge at nearby enemies dealing 115% weapon damage as Arcane."""


class Intensify(Rune):
    """ Intensify """
    description = """Enemies hit by Disintegrate take 15% increased damage from Arcane for 4 seconds."""


class Disintegrate(Active):
    """ Disintegrate """
    category = "active"
    description = """Cost: 18 Arcane Power

Channel a beam of pure energy, dealing 390% weapon damage as Arcane.

Disintegrate damage is increased by 250% weapon damage every second, up to a maximum total of 890% weapon damage as Arcane."""
    url = r'https://us.diablo3.com//en/class/wizard/active/disintegrate'
    runes = [Convergence, Volatility, Entropy, Chaos_Nexus, Intensify]


class Sparkflint(Rune):
    """ Sparkflint """
    description = """Summon a fiery Familiar that grants you 10% increased damage."""


class Icicle(Rune):
    """ Icicle """
    description = """The Familiar's projectiles have a 35% chance to Freeze the enemy for 1 second."""


class Ancient_Guardian(Rune):
    """ Ancient Guardian """
    description = """Summon a protective Familiar. When you are below 50% Life the Familiar will absorb damage from 1 attack every 6 seconds."""


class Arcanot(Rune):
    """ Arcanot """
    description = """While the Familiar is active, you regenerate 4.5 Arcane Power every second."""


class Cannoneer(Rune):
    """ Cannoneer """
    description = """The Familiar's projectiles explode on impact, dealing 240% weapon damage as Arcane to all enemies within 6 yards."""


class Familiar(Active):
    """ Familiar """
    category = "active"
    description = """Cost: 20 Arcane Power

Summon a Familiar that attacks your enemies for 240% weapon damage as Arcane. This companion cannot be targeted or damaged by enemies. Lasts 10 minutes."""
    url = r'https://us.diablo3.com//en/class/wizard/active/familiar'
    runes = [Sparkflint, Icicle, Ancient_Guardian, Arcanot, Cannoneer]


class Safe_Passage(Rune):
    """ Safe Passage """
    description = """For 5 seconds after you Teleport, you will take 25% less damage."""


class Wormhole(Rune):
    """ Wormhole """
    description = """After casting Teleport, you have 3 seconds to Teleport 1 additional time."""


class Reversal(Rune):
    """ Reversal """
    description = """Casting Teleport again within 5 seconds will instantly return you to your original location and set the remaining cooldown to 1 second."""


class Fracture(Rune):
    """ Fracture """
    description = """Summon 2 decoys for 6 seconds after teleporting."""


class Calamity(Rune):
    """ Calamity """
    description = """Cast a short range Wave of Force upon arrival, dealing 175% weapon damage as Arcane to all nearby enemies and stunning them for 1 second."""


class Teleport(Active):
    """ Teleport """
    category = "active"
    description = """Cooldown: 11 seconds

Teleport through the ether to the selected location up to 50 yards away."""
    url = r'https://us.diablo3.com//en/class/wizard/active/teleport'
    runes = [Safe_Passage, Wormhole, Reversal, Fracture, Calamity]


class Hard_Light(Rune):
    """ Hard Light """
    description = """Increase the Life of your Mirror Images to 200% of your own."""


class Duplicates(Rune):
    """ Duplicates """
    description = """Summon 4 Mirror Images that taunt nearby enemies for 1 second and each have 50% of your Life."""


class Mocking_Demise(Rune):
    """ Mocking Demise """
    description = """When a Mirror Image is destroyed, it explodes, dealing 309% weapon damage as Arcane with a 50% chance to Stun for 2 seconds."""


class Extension_of_Will(Rune):
    """ Extension of Will """
    description = """Increase the duration of your Mirror Images to 10 seconds and their Life to 100% of your Life."""


class Mirror_Mimics(Rune):
    """ Mirror Mimics """
    description = """Spells cast by your Mirror Images will deal 20% of the damage of your own spells."""


class Mirror_Image(Active):
    """ Mirror Image """
    category = "active"
    description = """Cooldown: 15 seconds

Summon 2 illusionary duplicates of yourself that taunt nearby enemies for 1 second, last for 7 seconds and have 50% of your Life.

Spells cast by your Mirror Images will deal 10% of the damage of your own spells."""
    url = r'https://us.diablo3.com//en/class/wizard/active/mirror-image'
    runes = [Hard_Light, Duplicates, Mocking_Demise, Extension_of_Will, Mirror_Mimics]


class Thunder_Crash(Rune):
    """ Thunder Crash """
    description = """Removes the delay before Meteor comes crashing down.

Meteor's damage turns into Lightning."""


class Star_Pact(Rune):
    """ Star Pact """
    description = """Expend all remaining Arcane Power. Each point of extra Arcane Power spent increases the impact damage of Meteor by 20% weapon damage as Arcane."""


class Comet(Rune):
    """ Comet """
    description = """Summon a Comet that deals 740% weapon damage as Cold and freezes chilled enemies for 1 second upon impact.

The impact site is covered in an icy mist that deals 235% weapon damage as Cold over 3 seconds."""


class Meteor_Shower(Rune):
    """ Meteor Shower """
    description = """Unleash a volley of 7 small Meteors that each strike for 277% weapon damage as Fire."""


class Molten_Impact(Rune):
    """ Molten Impact """
    description = """Greatly increases the size and increases the damage of the Meteor impact to 1648% weapon damage as Fire and the molten fire to 625% weapon damage as Fire over 3 seconds.

Adds a 15 second cooldown."""


class Meteor(Active):
    """ Meteor """
    category = "active"
    description = """Cost: 40 Arcane Power

Summon an immense Meteor that plummets from the sky, crashing into enemies for 740% weapon damage as Fire. The ground it hits is scorched with molten fire that deals 235% weapon damage as Fire over 3 seconds."""
    url = r'https://us.diablo3.com//en/class/wizard/active/meteor'
    runes = [Thunder_Crash, Star_Pact, Comet, Meteor_Shower, Molten_Impact]


class Lightning_Storm(Rune):
    """ Lightning Storm """
    description = """Enemies affected by Blizzard take 15% increased damage from Lightning."""


class Frozen_Solid(Rune):
    """ Frozen Solid """
    description = """Enemies caught in the Blizzard have a 100% chance to be Frozen for 2.5 seconds."""


class Snowbound(Rune):
    """ Snowbound """
    description = """Reduce the casting cost of Blizzard to 10 Arcane Power."""


class Apocalypse(Rune):
    """ Apocalypse """
    description = """Increase the area of effect of Blizzard to a 30 yard radius.

Blizzard's damage turns into Fire."""


class Unrelenting_Storm(Rune):
    """ Unrelenting Storm """
    description = """Increase the duration and damage of Blizzard to deal 1810% weapon damage as Cold over 8 seconds."""


class Blizzard(Active):
    """ Blizzard """
    category = "active"
    description = """Cost: 40 Arcane Power

Call down shards of ice that deal 1075% weapon damage as Cold over 6 seconds to enemies in a 12 yard radius. Multiple casts in the same area from the same caster do not stack."""
    url = r'https://us.diablo3.com//en/class/wizard/active/blizzard'
    runes = [Lightning_Storm, Frozen_Solid, Snowbound, Apocalypse, Unrelenting_Storm]


class Absorption(Rune):
    """ Absorption """
    description = """You have a chance to gain 4 Arcane Power when you are hit by a ranged or melee attack."""


class Pinpoint_Barrier(Rune):
    """ Pinpoint Barrier """
    description = """Energy Armor also increases your Critical Hit Chance by 5%."""


class Energy_Tap(Rune):
    """ Energy Tap """
    description = """Rather than decreasing your maximum Arcane Power, Energy Armor increases it by 20."""


class Force_Armor(Rune):
    """ Force Armor """
    description = """Incoming attacks that would deal more than 35% of your maximum Life are reduced to deal 35% of your maximum Life instead.

The amount absorbed cannot exceed 100% of your maximum Life."""


class Prismatic_Armor(Rune):
    """ Prismatic Armor """
    description = """Energy Armor also increases your resistance to all damage types 25%."""


class Energy_Armor(Active):
    """ Energy Armor """
    category = "active"
    description = """Cost: 25 Arcane Power

Focus your energies, increasing your Armor by 35% but decreasing your maximum Arcane Power by 20. Lasts 10 minutes.

Only one Armor may be active at a time."""
    url = r'https://us.diablo3.com//en/class/wizard/active/energy-armor'
    runes = [Absorption, Pinpoint_Barrier, Energy_Tap, Force_Armor, Prismatic_Armor]


class Combustion(Rune):
    """ Combustion """
    description = """An explosion erupts around you when you transform, dealing 3680% weapon damage as Fire to all enemies within 15 yards.

Archon abilities deal Fire damage instead of Arcane."""


class Teleport(Rune):
    """ Teleport """
    description = """Archon form can cast Teleport with a 2 second cooldown."""


class Pure_Power(Rune):
    """ Pure Power """
    description = """Decrease the cooldown of Archon to 100 seconds.

Archon abilities deal Lightning damage instead of Arcane."""


class Slow_Time(Rune):
    """ Slow Time """
    description = """Archon form can cast a Slow Time that follows you and your Arcane Blast and Arcane Strike abilities Freeze enemies for 1 second.

Archon abilities deal Cold damage instead of Arcane."""


class Improved_Archon(Rune):
    """ Improved Archon """
    description = """Increase the damage of all Archon abilities by 50%."""


class Archon(Active):
    """ Archon """
    category = "active"
    description = """Cooldown: 120 seconds

Transform into a being of pure arcane energy for 20 seconds. While in Archon form, your normal abilities are replaced by powerful Archon abilities, your damage is increased by 30%, and your Armor and resistances are increased by 150%.

Each enemy killed while in Archon form increases your damage by 6% for the remaining duration of Archon."""
    url = r'https://us.diablo3.com//en/class/wizard/active/archon'
    runes = [Combustion, Teleport, Pure_Power, Slow_Time, Improved_Archon]


class Supermassive(Rune):
    """ Supermassive """
    description = """Increases the Black Hole radius to 20 yards and damage to 1290% weapon damage as Lightning over 2 seconds."""


class Absolute_Zero(Rune):
    """ Absolute Zero """
    description = """Each enemy hit increases the damage of your Cold spells by 3% for 10 seconds.

Black Hole's damage turns into Cold."""


class Event_Horizon(Rune):
    """ Event Horizon """
    description = """The Black Hole also absorbs enemy projectiles and objects from Elite monster affixes within 15 yards."""


class Blazar(Rune):
    """ Blazar """
    description = """Conjure a Black Hole at the target location that draws enemies to it and deals 700% weapon damage as Fire over 2 seconds to all enemies within 15 yards.

After the Black Hole disappears, an explosion occurs that deals 725% weapon damage as Fire to enemies within 15 yards."""


class Spellsteal(Rune):
    """ Spellsteal """
    description = """Enemies hit by Black Hole deal 10% reduced damage for 5 seconds. Each enemy hit by Black Hole grants you 3% increased damage for 5 seconds."""


class Black_Hole(Active):
    """ Black Hole """
    category = "active"
    description = """Cost: 20 Arcane Power
Cooldown: 12 seconds

Conjure a Black Hole at the target location that draws enemies to it and deals 700% weapon damage as Arcane over 2 seconds to all enemies within 15 yards."""
    url = r'https://us.diablo3.com//en/class/wizard/active/black-hole'
    runes = [Supermassive, Absolute_Zero, Event_Horizon, Blazar, Spellsteal]



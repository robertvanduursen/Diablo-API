""" Classes.DEMON_HUNTER active skills """
from datatypes import Active
from datatypes import Rune


class Puncturing_Arrow(Rune):
    """ Puncturing Arrow """
    description = """Increase the chance for the arrow to pierce to 50%."""


class Serrated_Arrow(Rune):
    """ Serrated Arrow """
    description = """Increase Hatred generated to 7.

Hungering Arrow's damage turns into Fire."""


class Shatter_Shot(Rune):
    """ Shatter Shot """
    description = """If the arrow successfully pierces the first enemy, the arrow splits into 3 arrows.

Hungering Arrow's damage turns into Lightning."""


class Devouring_Arrow(Rune):
    """ Devouring Arrow """
    description = """Each consecutive pierce increases the damage of the arrow by 70%.

Hungering Arrow's damage turns into Cold."""


class Spray_of_Teeth(Rune):
    """ Spray of Teeth """
    description = """Critical Hits cause a burst of bone to explode from the enemy, dealing 60% weapon damage to enemies within 10 yards."""


class Hungering_Arrow(Active):
    """ Hungering Arrow """
    category = "active"
    description = """Generate: 4 Hatred

Fire a magically imbued arrow that seeks out enemies for 155% weapon damage and has a 35% chance to pierce through them.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/hungering-arrow'
    runes = [Puncturing_Arrow, Serrated_Arrow, Shatter_Shot, Devouring_Arrow, Spray_of_Teeth]


class Impact(Rune):
    """ Impact """
    description = """The impact causes Knockback and has a 100% chance to Stun for 1.5 seconds."""


class Chemical_Burn(Rune):
    """ Chemical Burn """
    description = """The enemy also burns for 500% weapon damage as Fire over 2 seconds."""


class Overpenetration(Rune):
    """ Overpenetration """
    description = """The knife pierces through all enemies in a straight line for Cold damage."""


class Ricochet(Rune):
    """ Ricochet """
    description = """The knife ricochets to 2 additional nearby enemies within 20 yards of each other.

Impale's damage turns into Lightning."""


class Grievous_Wounds(Rune):
    """ Grievous Wounds """
    description = """Critical Hits deal 330% additional damage."""


class Impale(Active):
    """ Impale """
    category = "active"
    description = """Cost: 20 Hatred

Throw a knife that impales an enemy for 750% weapon damage."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/impale'
    runes = [Impact, Chemical_Burn, Overpenetration, Ricochet, Grievous_Wounds]


class Chain_Gang(Rune):
    """ Chain Gang """
    description = """Entangle and Slow up to 4 enemies with each shot."""


class Shock_Collar(Rune):
    """ Shock Collar """
    description = """Entangled enemies take 80% weapon damage as Lightning over 2 seconds."""


class Heavy_Burden(Rune):
    """ Heavy Burden """
    description = """Increase the Slow duration to 4 seconds.

Entangling Shot's damage turns into Cold."""


class Justice_is_Served(Rune):
    """ Justice is Served """
    description = """Increase Hatred generated to 7.

Entangling Shot's damage turns into Fire."""


class Bounty_Hunter(Rune):
    """ Bounty Hunter """
    description = """Increase the Slow amount to 80%."""


class Entangling_Shot(Active):
    """ Entangling Shot """
    category = "active"
    description = """Generate: 4 Hatred

Imbue an arrow with shadow energy that deals 200% weapon damage to the primary enemy and entangles up to 2 enemies, slowing their movement by 60% for 2 seconds.

When Entangling Shot hits an enemy, the Slow effect on all entangled enemies is refreshed.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/entangling-shot'
    runes = [Chain_Gang, Shock_Collar, Heavy_Burden, Justice_is_Served, Bounty_Hunter]


class Hooked_Spines(Rune):
    """ Hooked Spines """
    description = """Increase the slowing amount to 80%."""


class Torturous_Ground(Rune):
    """ Torturous Ground """
    description = """When the trap is sprung, all enemies in the area are immobilized for 2 seconds."""


class Jagged_Spikes(Rune):
    """ Jagged Spikes """
    description = """Enemies in the area also take 270% weapon damage as Physical over 6 seconds."""


class Carved_Stakes(Rune):
    """ Carved Stakes """
    description = """Reduce the cost of Caltrops to 3 Discipline."""


class Bait_the_Trap(Rune):
    """ Bait the Trap """
    description = """Become empowered while standing in the area of effect, gaining an additional 10% Critical Hit Chance."""


class Caltrops(Active):
    """ Caltrops """
    category = "active"
    description = """Cost: 6 Discipline

Lay a trap of caltrops on the ground that activates when an enemy approaches. Once sprung, the caltrops Slow the movement of enemies within 12 yards by 60%. This trap lasts 6 seconds."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/caltrops'
    runes = [Hooked_Spines, Torturous_Ground, Jagged_Spikes, Carved_Stakes, Bait_the_Trap]


class Withering_Fire(Rune):
    """ Withering Fire """
    description = """Reduce the initial Hatred cost to 10 and ignite your arrows, causing them to deal Fire damage."""


class Frost_Shots(Rune):
    """ Frost Shots """
    description = """Enemies hit by Rapid Fire are Chilled by 80% for 2 seconds.

Rapid Fire's damage turns into Cold."""


class Fire_Support(Rune):
    """ Fire Support """
    description = """While channeling Rapid Fire, launch 2 homing rockets every second. Each rocket deals 145% weapon damage as Physical to nearby enemies."""


class High_Velocity(Rune):
    """ High Velocity """
    description = """Fire lightning arrows that have a 50% chance to pierce through enemies."""


class Bombardment(Rune):
    """ Bombardment """
    description = """Rapidly fire grenades that explode for 545% weapon damage as Fire to all enemies within a 8 yard radius."""


class Rapid_Fire(Active):
    """ Rapid Fire """
    category = "active"
    description = """Cost: 20 Hatred initially, and an additional 6 Hatred while channeling

Rapidly fire for 685% weapon damage as Physical.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/rapid-fire'
    runes = [Withering_Fire, Frost_Shots, Fire_Support, High_Velocity, Bombardment]


class Displacement(Rune):
    """ Displacement """
    description = """Gain 100% movement speed while invisible."""


class Lingering_Fog(Rune):
    """ Lingering Fog """
    description = """Increase the duration to 1.5 seconds."""


class Healing_Vapors(Rune):
    """ Healing Vapors """
    description = """Regenerate 15% Life while invisible."""


class Special_Recipe(Rune):
    """ Special Recipe """
    description = """Reduce the cost to 8 Discipline."""


class Vanishing_Powder(Rune):
    """ Vanishing Powder """
    description = """Remove the Discipline cost but increase the cooldown to 6 seconds."""


class Smoke_Screen(Active):
    """ Smoke Screen """
    category = "active"
    description = """Cost: 14 Discipline
Cooldown: 1.5 seconds

Vanish behind a wall of smoke, becoming momentarily invisible for 1 second.

This ability does not start its cooldown until after its effects expire."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/smoke-screen'
    runes = [Displacement, Lingering_Fog, Healing_Vapors, Special_Recipe, Vanishing_Powder]


class Action_Shot(Rune):
    """ Action Shot """
    description = """While Vaulting, shoot 4 arrows for 75% weapon damage at nearby enemies. These shots are guaranteed Critical Hits."""


class Rattling_Roll(Rune):
    """ Rattling Roll """
    description = """Enemies you vault through are knocked away and Stunned for 1.5 seconds."""


class Tumble(Rune):
    """ Tumble """
    description = """After using Vault, your next Vault within 6 seconds has its Discipline cost reduced by 50%."""


class Acrobatics(Rune):
    """ Acrobatics """
    description = """Remove the Discipline cost but add an 6 second cooldown."""


class Trail_of_Cinders(Rune):
    """ Trail of Cinders """
    description = """Leave a trail of fire in your wake that deals 300% weapon damage as Fire over 3 seconds."""


class Vault(Active):
    """ Vault """
    category = "active"
    description = """Cost: 8 Discipline

Tumble acrobatically 35 yards."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/vault'
    runes = [Action_Shot, Rattling_Roll, Tumble, Acrobatics, Trail_of_Cinders]


class Volatile_Explosives(Rune):
    """ Volatile Explosives """
    description = """Increase the explosion radius to 20 yards."""


class Thunder_Ball(Rune):
    """ Thunder Ball """
    description = """Increase Hatred generated to 7."""


class Freezing_Strike(Rune):
    """ Freezing Strike """
    description = """Shoot 3 bolas that each deal 160% weapon damage as Cold. The bolas no longer explode for area damage to nearby enemies.

Enemies hit have a 50% chance to be Frozen for 1 second."""


class Bitter_Pill(Rune):
    """ Bitter Pill """
    description = """When the bola explodes, you have a 15% chance to gain 2 Discipline.

Bolas's damage turns into Lightning."""


class Imminent_Doom(Rune):
    """ Imminent Doom """
    description = """Augment the bola to deal 216% weapon damage as Fire to the enemy and 148% weapon damage as Fire to all other enemies within 14 yards, but increases the explosion delay to 2 seconds."""


class Bolas(Active):
    """ Bolas """
    category = "active"
    description = """Generate: 4 Hatred

Shoot out an explosive bola that wraps itself around the enemy. After 1 second, the bola explodes dealing 160% weapon damage as Fire to the enemy and an additional 110% weapon damage as Fire to all other enemies within 14 yards."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/bolas'
    runes = [Volatile_Explosives, Thunder_Ball, Freezing_Strike, Bitter_Pill, Imminent_Doom]


class Twin_Chakrams(Rune):
    """ Twin Chakrams """
    description = """A second Chakram mirrors the first. Each Chakram deals 220% weapon damage as Fire."""


class Serpentine(Rune):
    """ Serpentine """
    description = """The Chakram follows a slow curve, dealing 500% weapon damage as Cold to enemies along the path."""


class Razor_Disk(Rune):
    """ Razor Disk """
    description = """The Chakram spirals out from the targeted location dealing 380% weapon damage as Physical to enemies along the path."""


class Boomerang(Rune):
    """ Boomerang """
    description = """The Chakram path turns into a loop, dealing 400% weapon damage as Lightning to enemies along its path."""


class Shuriken_Cloud(Rune):
    """ Shuriken Cloud """
    description = """Surround yourself with a cloud of spinning Chakrams, dealing 200% weapon damage per second as Physical to nearby enemies. Lasts 10 minutes."""


class Chakram(Active):
    """ Chakram """
    category = "active"
    description = """Cost: 10 Hatred

Fire a swirling Chakram that deals 380% weapon damage as Physical to enemies along its path."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/chakram'
    runes = [Twin_Chakrams, Serpentine, Razor_Disk, Boomerang, Shuriken_Cloud]


class Invigoration(Rune):
    """ Invigoration """
    description = """Passive: Permanently increase maximum Discipline by 20."""


class Punishment(Rune):
    """ Punishment """
    description = """Restore 75 Hatred.

Preparation has a 20 second cooldown."""


class Battle_Scars(Rune):
    """ Battle Scars """
    description = """Gain 40% Life when using Preparation."""


class Focused_Mind(Rune):
    """ Focused Mind """
    description = """Gain 45 Discipline over 15 seconds instead of restoring it immediately."""


class Backup_Plan(Rune):
    """ Backup Plan """
    description = """There is a 30% chance that Preparation's cooldown will not be triggered."""


class Preparation(Active):
    """ Preparation """
    category = "active"
    description = """Cooldown: 45 seconds

Instantly restore 30 Discipline."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/preparation'
    runes = [Invigoration, Punishment, Battle_Scars, Focused_Mind, Backup_Plan]


class Pinpoint_Accuracy(Rune):
    """ Pinpoint Accuracy """
    description = """Increase cooldown to 15 seconds and increase damage to 1600% weapon damage as Lightning."""


class Bladed_Armor(Rune):
    """ Bladed Armor """
    description = """Gain 40% additional armor for 6 seconds.

Fan of Knives' damage turns into Cold."""


class Knives_Expert(Rune):
    """ Knives Expert """
    description = """Remove the cooldown but add a 30 Hatred cost.

Fan of Knives' damage turns into Fire."""


class Fan_of_Daggers(Rune):
    """ Fan of Daggers """
    description = """Enemies hit are Stunned for 3 seconds.

Fan of Knives' damage turns into Fire."""


class Assassins_Knives(Rune):
    """ Assassin's Knives """
    description = """Also throw long-range knives that deal 620% weapon damage to 5 additional enemies."""


class Fan_of_Knives(Active):
    """ Fan of Knives """
    category = "active"
    description = """Cooldown: 10 seconds

Throw knives out in a spiral around you, dealing 620% weapon damage to all enemies within 20 yards. Your knives will also Slow the movement of enemies by 60% for 1 second."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/fan-of-knives'
    runes = [Pinpoint_Accuracy, Bladed_Armor, Knives_Expert, Fan_of_Daggers, Assassins_Knives]


class Hardened(Rune):
    """ Hardened """
    description = """Instead of backflipping, your Armor is increased by 25% for 3 seconds."""


class Parting_Gift(Rune):
    """ Parting Gift """
    description = """Whenever a backflip is triggered, leave a bomb behind that explodes for 150% weapon damage as Physical in a 12 yard radius after 0.6 seconds."""


class Covering_Fire(Rune):
    """ Covering Fire """
    description = """Increase the damage of side bolts to 200% weapon damage as Fire."""


class Focus(Rune):
    """ Focus """
    description = """Instead of backflipping, increase Hatred generated to 7.

Evasive Fire's damage turns into Cold."""


class Surge(Rune):
    """ Surge """
    description = """Increase the backflip distance to 15 yards.

Evasive Fire's damage turns into Lightning."""


class Evasive_Fire(Active):
    """ Evasive Fire """
    category = "active"
    description = """Generate: 4 Hatred

Shoot a spread of bolts that hits the primary enemy for 200% weapon damage and two additional enemies for 100% weapon damage.

If an enemy is in front of you at close range, you will backflip away 5 yards.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/evasive-fire'
    runes = [Hardened, Parting_Gift, Covering_Fire, Focus, Surge]


class Tinkerer(Rune):
    """ Tinkerer """
    description = """Increase Hatred generated to 7."""


class Cluster_Grenades(Rune):
    """ Cluster Grenades """
    description = """Throw cluster grenades that deal 200% weapon damage as Fire over a 9 yard radius."""


class Grenade_Cache(Rune):
    """ Grenade Cache """
    description = """Throw out 3 grenades that explode for 160% weapon damage as Fire each."""


class Stun_Grenade(Rune):
    """ Stun Grenade """
    description = """Hurl a Lightning grenade that has a 20% chance to Stun enemies for 1.5 seconds."""


class Cold_Grenade(Rune):
    """ Cold Grenade """
    description = """Throw a grenade that explodes for 160% weapon damage as Cold and leaves a cloud that deals an additional 120% weapon damage as Cold over 3 seconds to enemies who stand in the area and Chills them."""


class Grenade(Active):
    """ Grenade """
    category = "active"
    description = """Generate: 4 Hatred

Throw a grenade that bounces and explodes for 160% weapon damage as Fire."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/grenade'
    runes = [Tinkerer, Cluster_Grenades, Grenade_Cache, Stun_Grenade, Cold_Grenade]


class Night_Bane(Rune):
    """ Night Bane """
    description = """Slow the movement speed of enemies within 30 yards by 80% for 5 seconds."""


class Blood_Moon(Rune):
    """ Blood Moon """
    description = """Double the total amount of Life per Hit gained."""


class Well_of_Darkness(Rune):
    """ Well of Darkness """
    description = """Reduce the cost to 8 Discipline."""


class Gloom(Rune):
    """ Gloom """
    description = """Reduce damage taken by 35% while Shadow Power is active."""


class Shadow_Glide(Rune):
    """ Shadow Glide """
    description = """Gain 30% increased movement speed while Shadow Power is active."""


class Shadow_Power(Active):
    """ Shadow Power """
    category = "active"
    description = """Cost: 14 Discipline

Draw in the power of the shadows, gaining 26,821 Life per Hit for 5 seconds.

Life per Hit gained is increased by 25% of your Life per Kill."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/shadow-power'
    runes = [Night_Bane, Blood_Moon, Well_of_Darkness, Gloom, Shadow_Glide]


class Echoing_Blast(Rune):
    """ Echoing Blast """
    description = """Increase to 2020% weapon damage as Cold.

On detonation, the blast slows any targets hit for 3 seconds."""


class Custom_Trigger(Rune):
    """ Custom Trigger """
    description = """Increase to 1900% weapon damage as Fire.

Hatred generators will now detonate traps."""


class Impaling_Spines(Rune):
    """ Impaling Spines """
    description = """Increases damage to 1930% weapon damage.

When deployed, enemies within range are instantly immobilized for 3 seconds."""


class Lightning_Rod(Rune):
    """ Lightning Rod """
    description = """When triggered lightning chain hits up to 3 enemies within 10 yards.

Lightning will also arc from any triggered trap to any armed traps within 25 yards.
All enemies are hit for 2020% weapon damage as Lightning over 3 hits."""


class Scatter(Rune):
    """ Scatter """
    description = """Simultaneously lay 2 traps."""


class Spike_Trap(Active):
    """ Spike Trap """
    category = "active"
    description = """Cost: 15 Hatred

Lay a trap that remains dormant until another Hatred spender is used to detonate the trap. When detonated, the trap and all other traps will explode in a chain reaction for 1160% weapon damage as Fire to all enemies within 8 yards of each trap.

You can have a maximum of 4 Spike Traps active at one time."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/spike-trap'
    runes = [Echoing_Blast, Custom_Trigger, Impaling_Spines, Lightning_Rod, Scatter]


class Spider_Companion(Rune):
    """ Spider Companion """
    description = """Active: Your spider throws webs at all enemies within 25 yards of you and him, Slowing them by 80% for 5 seconds.

Passive: Summons a spider companion that attacks enemies in front of him for 140% weapon damage as Physical.

The spider's attacks Slow enemies by 60% for 3 seconds."""


class Bat_Companion(Rune):
    """ Bat Companion """
    description = """Active: Instantly gain 50 Hatred.

Passive: Summons a bat companion that attacks for 60% of your weapon damage as Physical.

The bat grants you 1 Hatred per second."""


class Boar_Companion(Rune):
    """ Boar Companion """
    description = """Active: Your boar charges to you, then taunts all enemies within 20 yards for 5 seconds.

Passive: Summons a boar companion that attacks enemies for 50% of your weapon damage as Physical.

The boar increases your and your party's Life regeneration by 10,728 and resistance to all elements by 20%."""


class Ferret_Companion(Rune):
    """ Ferret Companion """
    description = """Active: Instantly pick up all health globes and gold within 60 yards.

Passive: Summons a pair of ferret companions that each attack for 50% of your weapon damage as Physical.

The ferrets collect gold for you, increase gold found on monsters by 10%, and increase your movement speed by 10%."""


class Wolf_Companion(Rune):
    """ Wolf Companion """
    description = """Active: Your wolf howls, granting you and your allies within 60 yards 15% increased damage for 10 seconds.

Passive: Summons a wolf companion that attacks enemies in front of him for 150% of your weapon damage as Physical."""


class Companion(Active):
    """ Companion """
    category = "active"
    description = """Cooldown: 30 seconds

Active: Your raven deals an additional 500% damage on its next attack.

Passive: Summons a raven companion that pecks at enemies for 100% of your weapon damage as Physical."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/companion'
    runes = [Spider_Companion, Bat_Companion, Boar_Companion, Ferret_Companion, Wolf_Companion]


class Icy_Trail(Rune):
    """ Icy Trail """
    description = """Leave an icy trail in your wake that deals 300% weapon damage as Cold over 3 seconds and Chills enemies for 3 seconds."""


class Drifting_Shadow(Rune):
    """ Drifting Shadow """
    description = """Movement speed increased to 100% of normal running speed while strafing.

Strafe's damage turns into Lightning."""


class Stinging_Steel(Rune):
    """ Stinging Steel """
    description = """Throw out knives rather than arrows that deal an extra 140% damage on Critical Hits."""


class Rocket_Storm(Rune):
    """ Rocket Storm """
    description = """In addition to regular shots, shoot off homing rockets for 130% weapon damage as Fire."""


class Demolition(Rune):
    """ Demolition """
    description = """Throw out bouncy grenades that explode for 460% weapon damage as Fire to enemies within 9 yards."""


class Strafe(Active):
    """ Strafe """
    category = "active"
    description = """Cost: 12 Hatred

Shoot at random nearby enemies for 675% weapon damage while moving at 75% of normal movement speed.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/strafe'
    runes = [Icy_Trail, Drifting_Shadow, Stinging_Steel, Rocket_Storm, Demolition]


class Ball_Lightning(Rune):
    """ Ball Lightning """
    description = """Shoot a ball of lightning that electrocutes enemies along its path for 300% weapon damage as Lightning."""


class Frost_Arrow(Rune):
    """ Frost Arrow """
    description = """Shoot a frost arrow that hits an enemy for 330% weapon damage as Cold then splits into up to 10 additional frost arrows. Enemies hit are Chilled by 60% for 1 second."""


class Immolation_Arrow(Rune):
    """ Immolation Arrow """
    description = """Shoot a fiery arrow that hits an enemy for 300% weapon damage as Fire and explodes, immolating the ground for 315% weapon damage as Fire over 2 seconds to enemies within 10 yards."""


class Lightning_Bolts(Rune):
    """ Lightning Bolts """
    description = """Shoot an electrified bolt for 300% weapon damage as Lightning that Stuns enemies for 1 second on a Critical Hit."""


class Nether_Tentacles(Rune):
    """ Nether Tentacles """
    description = """Shoot a shadow tentacle that deals 300% weapon damage as Physical to enemies along its path and returns 0.4% of your maximum Life for each enemy hit."""


class Elemental_Arrow(Active):
    """ Elemental Arrow """
    category = "active"
    description = """Cost: 10 Hatred

Shoot a fire arrow that deals 300% weapon damage as Fire to all enemies it passes through.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/elemental-arrow'
    runes = [Ball_Lightning, Frost_Arrow, Immolation_Arrow, Lightning_Bolts, Nether_Tentacles]


class Contagion(Rune):
    """ Contagion """
    description = """When the enemy is killed, the mark spreads to the closest 3 enemies within 30 yards. This effect can chain repeatedly."""


class Valley_of_Death(Rune):
    """ Valley of Death """
    description = """Mark an area on the ground of 15 yard radius for 15 seconds. Enemies in the area take 15% additional damage."""


class Grim_Reaper(Rune):
    """ Grim Reaper """
    description = """15% of damage dealt to the marked enemy is also divided evenly among all enemies within 20 yards."""


class Mortal_Enemy(Rune):
    """ Mortal Enemy """
    description = """Attacks you make against the marked enemy generate 4 Hatred."""


class Death_Toll(Rune):
    """ Death Toll """
    description = """Attackers heal for up to 3% of their maximum Life when damaging the marked enemy."""


class Marked_for_Death(Active):
    """ Marked for Death """
    category = "active"
    description = """Cost: 3 Discipline

Mark an enemy. The marked enemy takes 15% additional damage for the next 30 seconds."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/marked-for-death'
    runes = [Contagion, Valley_of_Death, Grim_Reaper, Mortal_Enemy, Death_Toll]


class Fire_at_Will(Rune):
    """ Fire at Will """
    description = """Reduce the Hatred cost to 18.

Multishot's damage turns into Lightning."""


class Wind_Chill(Rune):
    """ Wind Chill """
    description = """Enemies hit are Chilled and have 8% increased chance to be Critically Hit for 3 seconds."""


class Suppression_Fire(Rune):
    """ Suppression Fire """
    description = """Knockback the first 4 enemies hit."""


class Full_Broadside(Rune):
    """ Full Broadside """
    description = """Increase the damage of Multishot to 500% weapon damage."""


class Arsenal(Rune):
    """ Arsenal """
    description = """Every time you fire, launch 3 rockets at nearby enemies that each deal 300% weapon damage as Fire."""


class Multishot(Active):
    """ Multishot """
    category = "active"
    description = """Cost: 25 Hatred

Fire a massive volley of arrows dealing 360% weapon damage to all enemies in the area.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/multishot'
    runes = [Fire_at_Will, Wind_Chill, Suppression_Fire, Full_Broadside, Arsenal]


class Spitfire_Turret(Rune):
    """ Spitfire Turret """
    description = """The turret will also fire homing rockets at random nearby enemies for 120% weapon damage as Fire."""


class Impaling_Bolt(Rune):
    """ Impaling Bolt """
    description = """The turret now fires piercing bolts."""


class Chain_of_Torment(Rune):
    """ Chain of Torment """
    description = """Create a chain between you and the Sentry and between each Sentry that deals 300% weapon damage every second to each enemy it touches."""


class Polar_Station(Rune):
    """ Polar Station """
    description = """The turret Chills all nearby enemies within 16 yards, Slowing their movement speed by 60%."""


class Guardian_Turret(Rune):
    """ Guardian Turret """
    description = """The turret also creates a shield that reduces damage taken by allies by 25%."""


class Sentry(Active):
    """ Sentry """
    category = "active"
    description = """Cost: 20 Hatred

Summon a turret that fires at nearby enemies for 280% weapon damage. Lasts 30 seconds.

You may have 2 turrets active at a time.

You gain a charge every 8 seconds and can have up to 2 charges stored at a time."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/sentry'
    runes = [Spitfire_Turret, Impaling_Bolt, Chain_of_Torment, Polar_Station, Guardian_Turret]


class Dazzling_Arrow(Rune):
    """ Dazzling Arrow """
    description = """Enemies hit by the grenades have a 100% chance to be stunned for 1.5 seconds.

Cluster Arrow's damage turns into Lightning."""


class Shooting_Stars(Rune):
    """ Shooting Stars """
    description = """Instead of releasing grenades, release up to 2 rockets at nearby enemies that each deal 600% weapon damage as Physical."""


class Maelstrom(Rune):
    """ Maelstrom """
    description = """Instead of releasing grenades, release up to 3 rockets at nearby enemies that each deal 450% weapon damage as Cold. You gain 2% Life per enemy hit."""


class Cluster_Bombs(Rune):
    """ Cluster Bombs """
    description = """Launch a cluster through the air, dropping grenades in a straight line that each explode for 650% weapon damage as Fire."""


class Loaded_for_Bear(Rune):
    """ Loaded for Bear """
    description = """Increase the damage of the explosion at the impact location to 850% weapon damage as Fire."""


class Cluster_Arrow(Active):
    """ Cluster Arrow """
    category = "active"
    description = """Cost: 40 Hatred

Fire a cluster arrow that explodes for 650% weapon damage as Fire into a series of 4 additional grenades that each explode for 250% weapon damage as Fire.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/cluster-arrow'
    runes = [Dazzling_Arrow, Shooting_Stars, Maelstrom, Cluster_Bombs, Loaded_for_Bear]


class Dark_Cloud(Rune):
    """ Dark Cloud """
    description = """Launch a volley of guided arrows that rain down on enemies for 3500% weapon damage over 8 seconds."""


class Shade(Rune):
    """ Shade """
    description = """Fire a massive volley of arrows at a large area. Arrows fall from the sky dealing 2800% weapon damage as Lightning over 5 seconds to all enemies in the area."""


class Stampede(Rune):
    """ Stampede """
    description = """Summon a wave of 10 Shadow Beasts to tear across the ground, knocking back enemies and dealing 4600% total weapon damage as Fire over 3 seconds."""


class Anathema(Rune):
    """ Anathema """
    description = """Summon a Shadow Beast that drops grenades from the sky dealing 5800% weapon damage as Fire over 2 seconds."""


class Flying_Strike(Rune):
    """ Flying Strike """
    description = """Call a group of 8 Shadow Beasts to plummet from the sky at a targeted location dealing 3800% total weapon damage as Cold over 5 seconds and Freezing enemies hit for 2 seconds."""


class Rain_of_Vengeance(Active):
    """ Rain of Vengeance """
    category = "active"
    description = """Cooldown: 30 seconds

Fire a massive volley of arrows at a large area. Arrows fall from the sky dealing 1500% weapon damage over 5 seconds to all enemies in the area.

Requires Bow"""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/rain-of-vengeance'
    runes = [Dark_Cloud, Shade, Stampede, Anathema, Flying_Strike]


class Personal_Mortar(Rune):
    """ Personal Mortar """
    description = """Instead of Homing Rockets, launch 2 Grenades at random enemies outside melee range on every attack that explode for 150% weapon damage each as Fire."""


class Dark_Heart(Rune):
    """ Dark Heart """
    description = """Vengeance fills your heart, reducing all damage taken by 50%."""


class Side_Cannons(Rune):
    """ Side Cannons """
    description = """Instead of Homing Rockets, the side guns are powered up into slower-firing cannons that deal 225% weapon damage and heal you for 3.0% of maximum Life per enemy hit."""


class Seethe(Rune):
    """ Seethe """
    description = """Gain 10 Hatred per second."""


class From_the_Shadows(Rune):
    """ From the Shadows """
    description = """Instead of Homing Rockets, summon allies from the shadows that attack for 120% weapon damage as Cold and Freeze your enemies for 3 seconds."""


class Vengeance(Active):
    """ Vengeance """
    category = "active"
    description = """Cooldown: 90 seconds

Turn into the physical embodiment of Vengeance for 20 seconds.

 Side Guns: Gain 4 additional piercing shots for 60% weapon damage each on every attack. Homing Rockets: Shoot 2 rockets at nearby enemies for 80% weapon damage each on every attack. Vengeance: Gain 40% increased damage."""
    url = r'https://us.diablo3.com//en/class/demon-hunter/active/vengeance'
    runes = [Personal_Mortar, Dark_Heart, Side_Cannons, Seethe, From_the_Shadows]

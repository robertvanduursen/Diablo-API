""" necromancer active skills """
from datatypes import Active
from datatypes import Rune


class Sudden_Impact(Rune):
    """ Sudden Impact """
    description = """Bone spikes stun enemies for 1 second."""


class Bone_Pillars(Rune):
    """ Bone Pillars """
    description = """Instead strikes the target and up to two nearby enemies with large bone pillars for 225% weapon damage per second as Poison."""


class Frost_Spikes(Rune):
    """ Frost Spikes """
    description = """Leaves a frost patch that reduces the movement speed of enemies by 60% for 2 secs.

Bone Spikes' damage turns into Cold."""


class Path_of_Bones(Rune):
    """ Path of Bones """
    description = """Now unleashes a line of spikes that deals 100% weapon damage as Physical. Damage is increased by up to 100% for those further away."""


class Blood_Spikes(Rune):
    """ Blood Spikes """
    description = """Enemies hit bleed for 50% weapon damage as Physical over 2 seconds and heal you for 0.5% of your total life over the duration."""


class Bone_Spikes(Active):
    """ Bone Spikes """
    category = "active"
    description = """Generate: 24 Essence

Summon bone spikes from the ground dealing 150% weapon damage as Physical per second."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/bone-spikes'
    runes = [Sudden_Impact, Bone_Pillars, Frost_Spikes, Path_of_Bones, Blood_Spikes]


class Blighted_Marrow(Rune):
    """ Blighted Marrow """
    description = """Damage is increased by 15% for each enemy Bone Spear passes through.

Bone Spear's damage turns into Poison."""


class Teeth(Rune):
    """ Teeth """
    description = """Launch razor sharp teeth that deal 300% weapon damage as Physical to enemies in front of you."""


class Crystallization(Rune):
    """ Crystallization """
    description = """Each enemy hit has their attack speed reduced by 20% and your attack speed is increased by 3% for 3 seconds stacking up to 10 times.

Bone Spear's damage turns into Cold."""


class Shatter(Rune):
    """ Shatter """
    description = """Instead of piercing now detonates on the first enemy hit dealing 500% weapon damage as Physical to all enemies within 15 yards."""


class Blood_Spear(Rune):
    """ Blood Spear """
    description = """Bone Spear turns into Blood Spear. Damage is increased to 650% weapon damage as Physical at the cost of 10% Health."""


class Bone_Spear(Active):
    """ Bone Spear """
    category = "active"
    description = """Cost: 20 Essence

Summon a piercing projectile that causes 500% weapon damage as Physical to all enemies it passes through."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/bone-spear'
    runes = [Blighted_Marrow, Teeth, Crystallization, Shatter, Blood_Spear]


class Execution(Rune):
    """ Execution """
    description = """Enemies below 20% health have a 5% chance to be decapitated and instantly killed."""


class Dual_Scythes(Rune):
    """ Dual Scythes """
    description = """Generate: 12 Essence per enemy hit

Slash with two summoned Scythes in front of you dealing 150% weapon damage as Physical and push enemies together."""


class Cursed_Scythe(Rune):
    """ Cursed Scythe """
    description = """Enemies hit by the scythe have a 15% chance to be inflicted with a random curse.

Grim Scythe's damage turns into Poison."""


class Frost_Scythe(Rune):
    """ Frost Scythe """
    description = """Each enemy hit increases your attack speed by 1% for 5 seconds. Max 15 stacks.

Grim Scythe's damage turns into Cold."""


class Blood_Scythe(Rune):
    """ Blood Scythe """
    description = """Heal for 1% of your health per enemy hit."""


class Grim_Scythe(Active):
    """ Grim Scythe """
    category = "active"
    description = """Generate: 12 Essence per enemy hit

Slash with a summoned Scythe in front of you dealing 150% weapon damage as Physical."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/grim-scythe'
    runes = [Execution, Dual_Scythes, Cursed_Scythe, Frost_Scythe, Blood_Scythe]


class Bloody_Mess(Rune):
    """ Bloody Mess """
    description = """Explosion radius is increased to 25 yards."""


class Close_Quarters(Rune):
    """ Close Quarters """
    description = """Now explodes up to 5 corpses close to you, dealing 525% weapon damage as Poison to enemies within 20 yards."""


class Shrapnel(Rune):
    """ Shrapnel """
    description = """Corpses now explode away from you, hitting all targets in a cone.

Corpse Explosion's damage turns into Poison."""


class Dead_Cold(Rune):
    """ Dead Cold """
    description = """Freeze all enemies caught in the explosion for 2 seconds.

Corpse Explosion's damage turns into Cold."""


class Final_Embrace(Rune):
    """ Final Embrace """
    description = """Corpses pull themselves towards the nearest enemy before exploding, but Corpse Explosion now costs 2% life per corpse."""


class Corpse_Explosion(Active):
    """ Corpse Explosion """
    category = "active"
    description = """Target an area exploding up to 5 corpses within 11 yards dealing 350% weapon damage as Physical to enemies within 20 yards."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/corpse-explosion'
    runes = [Bloody_Mess, Close_Quarters, Shrapnel, Dead_Cold, Final_Embrace]


class Gift_of_Death(Rune):
    """ Gift of Death """
    description = """Risen mages leave a corpse behind when they die or expire."""


class Contamination(Rune):
    """ Contamination """
    description = """Raise a contaminated mage that channels an aura of decay for 100% weapon damage as Poison for its duration."""


class Skeleton_Archer(Rune):
    """ Skeleton Archer """
    description = """Raise a Skeleton Archer that deals 400% weapon damage as Cold.

Skeleton Archers increase your attack speed by 3% for 5 seconds each time they deal damage. Max 10 stacks."""


class Singularity(Rune):
    """ Singularity """
    description = """Consumes all Essence to summon a powerful minion. The minion's damage is increased by 3% for every point of Essence consumed."""


class Life_Support(Rune):
    """ Life Support """
    description = """Risen mages cost 10% health to cast but last an additional 2 seconds."""


class Skeletal_Mage(Active):
    """ Skeletal Mage """
    category = "active"
    description = """Cost: 40 Essence

Raise a skeleton from the ground to attack your foes dealing 400% weapon damage as Physical over two attacks. Lasts 6 seconds."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/skeletal-mage'
    runes = [Gift_of_Death, Contamination, Skeleton_Archer, Singularity, Life_Support]


class Shredding_Splinters(Rune):
    """ Shredding Splinters """
    description = """Each lance slows the target by 10% and reduces its damage by 6% for 10 seconds. Stacks up to 5 times.

Corpse Lance's damage turns into Poison."""


class Brittle_Touch(Rune):
    """ Brittle Touch """
    description = """Enemies become brittle increasing their chance to be crit by 5% for 5 seconds each time they are hit with Corpse Lance.

Corpse Lance's damage turns into Cold."""


class Ricochet(Rune):
    """ Ricochet """
    description = """Corpse Lance has a 20% chance to ricochet to one additional target.

Corpse Lance's damage turns into Poison."""


class Visceral_Impact(Rune):
    """ Visceral Impact """
    description = """Stuns the target for 3 seconds."""


class Blood_Lance(Rune):
    """ Blood Lance """
    description = """Spend 2% of your total health to launch an additional lance from yourself towards the target that deals 525% weapon damage as Physical."""


class Corpse_Lance(Active):
    """ Corpse Lance """
    category = "active"
    description = """Target an enemy to summon projectiles from nearby corpses that cause 1750% weapon damage as Physical to the target."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/corpse-lance'
    runes = [Shredding_Splinters, Brittle_Touch, Ricochet, Visceral_Impact, Blood_Lance]


class Enforcer(Rune):
    """ Enforcer """
    description = """Reduces the active Essence cost to 25."""


class Frenzy(Rune):
    """ Frenzy """
    description = """Commanded skeletons go into a frenzy, gaining 25% increased attack speed while they attack the target."""


class Dark_Mending(Rune):
    """ Dark Mending """
    description = """Skeletal minions will heal you for 0.5% of your total health per hit while being commanded."""


class Freezing_Grasp(Rune):
    """ Freezing Grasp """
    description = """The target of your command is frozen for 3 seconds.

Command Skeletons' damage is turned to Cold."""


class Kill_Command(Rune):
    """ Kill Command """
    description = """Now commands your skeletons to explode, dealing 215% weapon damage as Poison to enemies within 15 yards."""


class Command_Skeletons(Active):
    """ Command Skeletons """
    category = "active"
    description = """Cost: 50 Essence

Active: Command your skeletal minions to attack the target and increase their damage against it by 50%.

Passive: Raise skeletons from the ground every 2 seconds to a max of 7 skeletons. Skeletal minions deal 50% weapon damage as Physical per attack."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/command-skeletons'
    runes = [Enforcer, Frenzy, Dark_Mending, Freezing_Grasp, Kill_Command]


class Blood_Sucker(Rune):
    """ Blood Sucker """
    description = """You pull in all health globes within 40 yards while siphoning."""


class Suppress(Rune):
    """ Suppress """
    description = """Enemies are also slowed by 75% while you siphon blood from them.

Siphon Blood's damage turns into Cold."""


class Power_Shift(Rune):
    """ Power Shift """
    description = """Damage is increased by 10% each time damage is dealt. Max 10 stacks.

Siphon Blood's damage turns into Poison."""


class Purity_of_Essence(Rune):
    """ Purity of Essence """
    description = """Essence gained is increased to 20 while you are at full health."""


class Drain_Life(Rune):
    """ Drain Life """
    description = """Increases the amount of health restored to 6% but no longer restores Essence."""


class Siphon_Blood(Active):
    """ Siphon Blood """
    category = "active"
    description = """Generate: 15 Essence each time damage is dealt

Siphon the blood from the targeted enemy dealing 300% weapon damage as Physical.

Siphon Blood heals you for 2% of your total health every second while channeled."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/siphon-blood'
    runes = [Blood_Sucker, Suppress, Power_Shift, Purity_of_Essence, Drain_Life]


class Unstable_Compound(Rune):
    """ Unstable Compound """
    description = """Each cast increases the radius of your next Nova by 5 yards up to 2 times."""


class Tendril_Nova(Rune):
    """ Tendril Nova """
    description = """Now heals you for 1% of your health per target hit and reduces damage dealt to 225% weapon damage as Physical."""


class Blight(Rune):
    """ Blight """
    description = """Leave a lingering patch of blight on the ground slowing enemies by 60% and causing them to deal 15% less damage for 1 second."""


class Bone_Nova(Rune):
    """ Bone Nova """
    description = """Spines radiate outward and deal 475% weapon damage as Physical within 12 yards."""


class Blood_Nova(Rune):
    """ Blood Nova """
    description = """Spend 10% health to unleash a Blood Nova that deals 450% weapon damage as Physical to all nearby enemies within 25 yards."""


class Death_Nova(Active):
    """ Death Nova """
    category = "active"
    description = """Cost: 20 Essence

Unleash a Nova that deals 350% weapon damage as Poison to all enemies within 25 yards."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/death-nova'
    runes = [Unstable_Compound, Tendril_Nova, Blight, Bone_Nova, Blood_Nova]


class Flesh_Golem(Rune):
    """ Flesh Golem """
    description = """Active: Command the Golem to the targeted location where it collapses into a pile of 8 corpses."""


class Ice_Golem(Rune):
    """ Ice Golem """
    description = """Active: Command the Golem to launch an icy blast at the targeted location, freezing enemies for 3 seconds and increasing their chance to be critically struck by 10% for 10 seconds.

Command Golem's damage turns into Cold."""


class Bone_Golem(Rune):
    """ Bone Golem """
    description = """Active: The Golem becomes a tornado of bone carrying all nearby enemies to the targeted location, stuns them for 2 seconds and deals 2000% weapon damage as Physical over the duration."""


class Decay_Golem(Rune):
    """ Decay Golem """
    description = """Active: The Golem consumes corpses at the targeted location increasing its damage by 30% per corpse.

Command Golem's damage turns into Poison."""


class Blood_Golem(Rune):
    """ Blood Golem """
    description = """Active: The Golem sacrifices itself healing you for 25% of your health and reconstructs at the targeted location. As the Golem reconstructs, veiny tendrils damage nearby enemies for 450% weapon damage as Physical."""


class Command_Golem(Active):
    """ Command Golem """
    category = "active"
    description = """Cooldown: 45 seconds

Active: Command the Golem to the targeted location where it collapses into a pile of 5 corpses.

Passive: Raise a Flesh Golem to fight for you. Flesh Golem deals 450% weapon damage as Physical per attack."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/command-golem'
    runes = [Flesh_Golem, Ice_Golem, Bone_Golem, Decay_Golem, Blood_Golem]


class Dizzying_Curse(Rune):
    """ Dizzying Curse """
    description = """Cursed enemies have a 10% chance to be stunned for 2 seconds when hit."""


class Enfeeblement(Rune):
    """ Enfeeblement """
    description = """Increase the potency of the movement speed reduction to 100% and decaying to normal potency over 5 seconds."""


class Opportunist(Rune):
    """ Opportunist """
    description = """Gain a 3% movement speed increase for every enemy cursed, up to a maximum of 30%."""


class Wither(Rune):
    """ Wither """
    description = """Damage reduction increased to 40%, but no longer reduces movement speed."""


class Borrowed_Time(Rune):
    """ Borrowed Time """
    description = """Gain 1% cooldown reduction for every enemy cursed, up to a maximum of 20%."""


class Decrepify(Active):
    """ Decrepify """
    category = "active"
    description = """Cost: 10 Essence

A crippling curse that reduces the enemy units' movement speed by 75% and reduces damage of affected enemies by 30% for 30 seconds."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/decrepify'
    runes = [Dizzying_Curse, Enfeeblement, Opportunist, Wither, Borrowed_Time]


class Satiated(Rune):
    """ Satiated """
    description = """Increases maximum life by 2% for 2 seconds for each corpse devoured."""


class Ruthless(Rune):
    """ Ruthless """
    description = """Additionally consumes your minions for 10 Essence per minion killed."""


class Devouring_Aura(Rune):
    """ Devouring Aura """
    description = """Becomes an aura that consumes all corpses within 15 yards to restore 11 Essence per corpse.

The range of this effect is increased by 50% of your gold pickup radius."""


class Voracious(Rune):
    """ Voracious """
    description = """Reduces all essence costs by 2% for each corpse consumed for 5 seconds."""


class Cannibalize_(Rune):
    """ Cannibalize  """
    description = """Each corpse consumed also restores 3% health."""


class Devour(Active):
    """ Devour """
    category = "active"
    description = """Consume corpses within 60 yards to restore 10 Essence per corpse."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/devour'
    runes = [Satiated, Ruthless, Devouring_Aura, Voracious, Cannibalize_]


class Transmittable(Rune):
    """ Transmittable """
    description = """Enemies that die while cursed will spread the curse to a nearby unaffected target."""


class Osmosis(Rune):
    """ Osmosis """
    description = """Each cursed enemy increases your life regeneration by 751 per second, up to 20 enemies."""


class Blood_Flask(Rune):
    """ Blood Flask """
    description = """Whenever a cursed enemy dies your potion cooldown is reduced by 1 second."""


class Sanguine_End(Rune):
    """ Sanguine End """
    description = """Whenever a cursed enemy dies, you are healed for 200% of your Life per Kill."""


class Cursed_Ground(Rune):
    """ Cursed Ground """
    description = """Now curses the ground, healing you for 1.0% of your maximum life every second for each enemy in the cursed area."""


class Leech(Active):
    """ Leech """
    category = "active"
    description = """Cost: 10 Essence

Curse the target area. Cursed enemies heal the attacker for 2% of their total health when they are struck. Lasts 30 seconds."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/leech'
    runes = [Transmittable, Osmosis, Blood_Flask, Sanguine_End, Cursed_Ground]


class Vengeful_Armaments(Rune):
    """ Vengeful Armaments """
    description = """Increases the damage dealt to 145% weapon damage."""


class Dislocation(Rune):
    """ Dislocation """
    description = """Enemies hit are also stunned for 2 seconds.

Bone Armor's damage is turned into Poison."""


class Limited_Immunity(Rune):
    """ Limited Immunity """
    description = """Cooldown: 45 seconds

Your armor absorbs all incoming damage and grants immunity to all control impairing effects but only lasts for 5 seconds."""


class Harvest_of_Anguish(Rune):
    """ Harvest of Anguish """
    description = """Bone Armor also increases your movement speed by 1% for each enemy hit.

Bone Armor's damage is turned into Cold."""


class Thy_Flesh_Sustained(Rune):
    """ Thy Flesh Sustained """
    description = """Cost: 20% Health

Increases your Life per Second by 10% per target hit. """


class Bone_Armor(Active):
    """ Bone Armor """
    category = "active"
    description = """Cooldown: 10 seconds

Rip bones from nearby enemies, dealing 125% weapon damage as Physical, and create armor that reduces damage taken by 3% per enemy hit up to a maximum of 10 enemies. Lasts for 60 secs."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/bone-armor'
    runes = [Vengeful_Armaments, Dislocation, Limited_Immunity, Harvest_of_Anguish, Thy_Flesh_Sustained]


class Blighted_Grasp(Rune):
    """ Blighted Grasp """
    description = """Skeletal hands raise from the ground damaging enemies within 15 yards for 14,000% weapon damage as Poison. Lasts 5 seconds."""


class Death_Valley(Rune):
    """ Death Valley """
    description = """The skeletal army knocks all affected enemies towards the center."""


class Unconventional_Warfare(Rune):
    """ Unconventional Warfare """
    description = """Skeletons will rise from the ground and attack random targets for 50,000% total weapon damage as Physical over 4 seconds."""


class Frozen_Army(Rune):
    """ Frozen Army """
    description = """Raise a massive skeletal army to pummel all enemies in a line dealing 12,000% weapon damage as Cold."""


class Dead_Storm(Rune):
    """ Dead Storm """
    description = """Cost: 20% health

Raise a storm of the dead that surround you damaging enemies for 15,500% weapon damage as Physical over 5 seconds."""


class Army_of_the_Dead(Active):
    """ Army of the Dead """
    category = "active"
    description = """Cooldown: 120 seconds

Raise a massive skeletal army to pummel the targeted location dealing 12,000% weapon damage as Physical in a 15 yard radius."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/army-of-the-dead'
    runes = [Blighted_Grasp, Death_Valley, Unconventional_Warfare, Frozen_Army, Dead_Storm]


class Scent_of_Blood(Rune):
    """ Scent of Blood """
    description = """Cursed enemies take 15% increased damage from your minions."""


class Volatile_Death(Rune):
    """ Volatile Death """
    description = """Cursed enemies explode for 100% weapon damage on death."""


class Aura_of_Frailty(Rune):
    """ Aura of Frailty """
    description = """Becomes an aura that curses all enemies within 15 yards.

The range of this effect is increased by 50% of your gold pickup radius."""


class Harvest_Essence(Rune):
    """ Harvest Essence """
    description = """Gain 2 Essence when a cursed enemy dies."""


class Early_Grave(Rune):
    """ Early Grave """
    description = """Triggers at 18% life but costs 10% of your life."""


class Frailty(Active):
    """ Frailty """
    category = "active"
    description = """Cost: 10 Essence

A crippling curse that kills enemies with less than 15% health.  Lasts 30 seconds."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/frailty'
    runes = [Scent_of_Blood, Volatile_Death, Aura_of_Frailty, Harvest_Essence, Early_Grave]


class Personal_Army(Rune):
    """ Personal Army """
    description = """Damage taken is reduced by 1% for each revived minion active."""


class Horrific_Return(Rune):
    """ Horrific Return """
    description = """When you revive a corpse, enemies within 20 yards run in fear for 3 seconds. Damage dealt is turned into Poison."""


class Purgatory(Rune):
    """ Purgatory """
    description = """Revived minions degenerate back into a usable corpse at the end of their duration."""


class Recklessness(Rune):
    """ Recklessness """
    description = """Revived minions deal an additional 25% damage but last 10 seconds. Damage dealt is turned into Cold."""


class Oblation(Rune):
    """ Oblation """
    description = """Increases the damage of revived creatures by 20% but each Revive now costs 3% health."""


class Revive(Active):
    """ Revive """
    category = "active"
    description = """Target an area reviving up to 10 corpses within 20 yards for 15 seconds."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/revive'
    runes = [Personal_Army, Horrific_Return, Purgatory, Recklessness, Oblation]


class Astral_Projection(Rune):
    """ Astral Projection """
    description = """Damage is increased by 15% for each enemy that Bone Spirit passes through while seeking its target. Damage turns into Cold."""


class Panic_Attack(Rune):
    """ Panic Attack """
    description = """Enemies within 10 yards are feared for 2 seconds when Bone Spirit detonates. Damage turns into Poison."""


class Poltergeist(Rune):
    """ Poltergeist """
    description = """Increases the maximum number of charges to 4."""


class Unfinished_Business(Rune):
    """ Unfinished Business """
    description = """Bone Spirit explodes dealing 1250% weapon damage as Cold to all enemies within 10 yards on detonation."""


class Possession(Rune):
    """ Possession """
    description = """Bone Spirit will now charm the target for 10 seconds at the cost of 5% health."""


class Bone_Spirit(Active):
    """ Bone Spirit """
    category = "active"
    description = """Launch a Bone Spirit that will seek enemies. Deals 4000% weapon damage as Physical on impact.

You gain a charge every 15 seconds and can store up to 3 charges. Recharge time is reduced by 1 second for each corpse you consume."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/bone-spirit'
    runes = [Astral_Projection, Panic_Attack, Poltergeist, Unfinished_Business, Possession]


class Potency(Rune):
    """ Potency """
    description = """Increases your armor by 100% for 2 seconds after casting."""


class Transfusion(Rune):
    """ Transfusion """
    description = """Heals for 2% of your maximum health for every enemy passed through."""


class Molting(Rune):
    """ Molting """
    description = """Leaves a corpse at your original location when used."""


class Hemostasis(Rune):
    """ Hemostasis """
    description = """Removes the health cost."""


class Metabolism(Rune):
    """ Metabolism """
    description = """Provides an additional charge but doubles the health cost."""


class Blood_Rush(Active):
    """ Blood Rush """
    category = "active"
    description = """Cost: 5% Health
Cooldown: 5 seconds

Shed your mortal flesh and reappear up to 50 yards away."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/blood-rush'
    runes = [Potency, Transfusion, Molting, Hemostasis, Metabolism]


class Frozen_Lands(Rune):
    """ Frozen Lands """
    description = """Enemies in the Land of the Dead are periodically frozen."""


class Plaguelands(Rune):
    """ Plaguelands """
    description = """Enemies in Land of the Dead suffer 100% weapon damage as Poison each second, up to a maximum of 10,000% weapon damage total."""


class Shallow_Graves(Rune):
    """ Shallow Graves """
    description = """Every 10 enemies killed extends the duration by 1 second up to a maximum of 2 seconds.  """


class Invigoration(Rune):
    """ Invigoration """
    description = """Your skills do not cost essence while Land of the Dead is active."""


class Land_of_Plenty(Rune):
    """ Land of Plenty """
    description = """You are healed for 2% of your maximum life whenever you kill an enemy while Land of the Dead is active."""


class Land_of_the_Dead(Active):
    """ Land of the Dead """
    category = "active"
    description = """Cooldown: 120 seconds

All corpse skills can be used at will for 10 seconds."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/land-of-the-dead'
    runes = [Frozen_Lands, Plaguelands, Shallow_Graves, Invigoration, Land_of_Plenty]


class Cursed_Form(Rune):
    """ Cursed Form """
    description = """While active, your curse skills now apply all three curses."""


class Reservoir(Rune):
    """ Reservoir """
    description = """Your maximum essence is increased by 100% while your Simulacrum is active."""


class Self_Sacrifice(Rune):
    """ Self Sacrifice """
    description = """If you would die with a Simulacrum active, instead the Simulacrum is destroyed and you are fully healed."""


class Blood_Debt(Rune):
    """ Blood Debt """
    description = """Life costs for skills are reduced by 75% while Simulacrum is active."""


class Blood_and_Bone(Rune):
    """ Blood and Bone """
    description = """Now also creates a Simulacrum of Bone, but the duration is reduced to 10 seconds."""


class Simulacrum(Active):
    """ Simulacrum """
    category = "active"
    description = """Cost: 25% Health
Cooldown: 120 seconds

Create a Simulacrum made of blood that will duplicate your Secondary skills for 15 seconds."""
    url = r'https://us.diablo3.com//en/class/necromancer/active/simulacrum'
    runes = [Cursed_Form, Reservoir, Self_Sacrifice, Blood_Debt, Blood_and_Bone]


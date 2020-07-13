""" Classes.WITCH_DOCTOR active skills """
from datatypes import Active
from datatypes import Rune


class Splinters(Rune):
    """ Splinters """
    description = """Shoot 3 Poison Darts that deal 110% weapon damage as Poison each."""


class Numbing_Dart(Rune):
    """ Numbing Dart """
    description = """Shoot a Cold dart that will Slow the enemy by 60% for 2 seconds."""


class Spined_Dart(Rune):
    """ Spined Dart """
    description = """Gain 50 Mana every time a Poison Dart hits an enemy. Converts the damage type to Physical."""


class Flaming_Dart(Rune):
    """ Flaming Dart """
    description = """Ignite the dart, dealing 565% weapon damage as Fire over 4 seconds."""


class Snake_to_the_Face(Rune):
    """ Snake to the Face """
    description = """Transform your Poison Dart into a snake that has a 35% chance to Stun the enemy for 1.5 seconds."""


class Poison_Dart(Active):
    """ Poison Dart """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Shoot a deadly Poison Dart that deals 185% weapon damage as Poison and an additional 40% weapon damage as Poison over 2 seconds."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/poison-dart'
    runes = [Splinters, Numbing_Dart, Spined_Dart, Flaming_Dart, Snake_to_the_Face]


class Unbreakable_Grasp(Rune):
    """ Unbreakable Grasp """
    description = """Removes the Mana cost and increases the amount enemies are Slowed to 80%.

Damage type is changed to Cold."""


class Groping_Eels(Rune):
    """ Groping Eels """
    description = """Increase the damage done to 1360% weapon damage as Physical."""


class Death_Is_Life(Rune):
    """ Death Is Life """
    description = """Enemies who die while in the area of Grasp of the Dead have a 70% chance to summon a Zombie Dog.

Damage type is changed to Poison."""


class Desperate_Grasp(Rune):
    """ Desperate Grasp """
    description = """Reduce the cooldown of Grasp of the Dead to 4 seconds.

Damage type is changed to Poison."""


class Rain_of_Corpses(Rune):
    """ Rain of Corpses """
    description = """Corpses also fall from the sky, dealing 420% weapon damage as Physical over 3 seconds to nearby enemies."""


class Grasp_of_the_Dead(Active):
    """ Grasp of the Dead """
    category = "active"
    description = """Cost: 150 Mana
Cooldown: 8 seconds

Ghoulish hands reach out from the ground, slowing enemy movement by 60% and dealing 760% weapon damage as Physical over 8 seconds."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/grasp-of-the-dead'
    runes = [Unbreakable_Grasp, Groping_Eels, Death_Is_Life, Desperate_Grasp, Rain_of_Corpses]


class Leaping_Spiders(Rune):
    """ Leaping Spiders """
    description = """Throw a jar with jumping spiders that leap up to 25 yards to reach their enemy and attack for a total of 645% weapon damage as Poison."""


class Spider_Queen(Rune):
    """ Spider Queen """
    description = """Throw a jar with a spider queen that births spiderlings, dealing 2625% weapon damage as Poison over 15 seconds.

You may have one spider queen summoned at a time."""


class Widowmakers(Rune):
    """ Widowmakers """
    description = """Throw a jar with widowmaker spiders deal a total of 700% weapon damage as Physical."""


class Medusa_Spiders(Rune):
    """ Medusa Spiders """
    description = """Throw a jar with paralyzing spiders that have a 100% chance to Slow enemies by 60% with every attack."""


class Blazing_Spiders(Rune):
    """ Blazing Spiders """
    description = """Throw a jar with fire spiders that return 3 Mana to you per hit."""


class Corpse_Spiders(Active):
    """ Corpse Spiders """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Throw a jar with 4 spiders that attack nearby enemies for a total of 576% weapon damage as Physical before dying."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/corpse-spiders'
    runes = [Leaping_Spiders, Spider_Queen, Widowmakers, Medusa_Spiders, Blazing_Spiders]


class Rabid_Dogs(Rune):
    """ Rabid Dogs """
    description = """Your Zombie Dogs gain an infectious bite that deals 120% of your weapon damage as Poison over 3 seconds."""


class Chilled_to_the_Bone(Rune):
    """ Chilled to the Bone """
    description = """Enemies who hit or are hit by your Zombie Dogs are Chilled for 3 seconds."""


class Life_Link(Rune):
    """ Life Link """
    description = """Your Zombie Dogs absorb 10% of all damage done to you."""


class Burning_Dogs(Rune):
    """ Burning Dogs """
    description = """Your Zombie Dogs burst into flames, burning nearby enemies for 80% of your weapon damage as Fire every second."""


class Leeching_Beasts(Rune):
    """ Leeching Beasts """
    description = """Your Zombie Dogs heal you for 100% of your Life On Hit with every attack."""


class Summon_Zombie_Dogs(Active):
    """ Summon Zombie Dogs """
    category = "active"
    description = """Cooldown: 45 seconds

Summon 3 Zombie Dogs from the depths to fight by your side. Each dog deals 120% of your weapon damage as Physical per hit."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/summon-zombie-dogs'
    runes = [Rabid_Dogs, Chilled_to_the_Bone, Life_Link, Burning_Dogs, Leeching_Beasts]


class Dire_Bats(Rune):
    """ Dire Bats """
    description = """Summon fewer but larger bats that travel a long distance and deal 500% weapon damage as Fire."""


class Vampire_Bats(Rune):
    """ Vampire Bats """
    description = """Firebats has an initial Mana cost of 250 mana but no longer has a channeling cost.

Firebats' damage type turns into Physical."""


class Plague_Bats(Rune):
    """ Plague Bats """
    description = """Diseased bats fly towards the enemy and infect them. Damage is slow at first, but can increase over time to a maximum of 720% weapon damage as Poison."""


class Hungry_Bats(Rune):
    """ Hungry Bats """
    description = """Rapidly summon two bats that each seek out a nearby enemy for 750% weapon damage as Fire."""


class Cloud_of_Bats(Rune):
    """ Cloud of Bats """
    description = """Call forth a swirl of bats that damage nearby enemies for 425% weapon damage as Fire. The damage of the bats increases every second, up to a maximum of 850% weapon damage after 3 seconds."""


class Firebats(Active):
    """ Firebats """
    category = "active"
    description = """Cost: 125 Mana

Call forth a swarm of fiery bats to burn enemies in front of you for 475% weapon damage as Fire."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/firebats'
    runes = [Dire_Bats, Vampire_Bats, Plague_Bats, Hungry_Bats, Cloud_of_Bats]


class Phobia(Rune):
    """ Phobia """
    description = """Enemies are no longer Immobilized and will instead run in Fear for 5 seconds."""


class Stalker(Rune):
    """ Stalker """
    description = """Increase movement speed by 20% for 4 seconds after casting Horrify."""


class Face_of_Death(Rune):
    """ Face of Death """
    description = """Increase the radius of Horrify to 24 yards. """


class Frightening_Aspect(Rune):
    """ Frightening Aspect """
    description = """Gain 50% additional Armor for 8 seconds after casting Horrify."""


class Ruthless_Terror(Rune):
    """ Ruthless Terror """
    description = """Gain 55 Mana for every horrified enemy."""


class Horrify(Active):
    """ Horrify """
    category = "active"
    description = """Cooldown: 10 seconds

Don a spectral mask that horrifies all enemies within 18 yards, causing them to tremor in Fear and be Immobilized for 3 seconds."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/horrify'
    runes = [Phobia, Stalker, Face_of_Death, Frightening_Aspect, Ruthless_Terror]


class Swallow_Your_Soul(Rune):
    """ Swallow Your Soul """
    description = """Gain mana and increase maximum Mana by 5% for each enemy harvested."""


class Siphon(Rune):
    """ Siphon """
    description = """Gain 32,185 Life for every harvested enemy."""


class Languish(Rune):
    """ Languish """
    description = """Increase your Armor by 10% per harvested enemy and reduce their movement speed by 80% for 5 seconds."""


class Soul_to_Waste(Rune):
    """ Soul to Waste """
    description = """Gain 5% increased movement speed for each enemy harvested."""


class Vengeful_Spirit(Rune):
    """ Vengeful Spirit """
    description = """Harvested enemies also take 640% weapon damage as Physical."""


class Soul_Harvest(Active):
    """ Soul Harvest """
    category = "active"
    description = """Cooldown: 12 seconds

Feed on the life force of enemies within 18 yards. Gain 3% Intelligence for 30 seconds for each affected enemy. This effect stacks up to 5 times."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/soul-harvest'
    runes = [Swallow_Your_Soul, Siphon, Languish, Soul_to_Waste, Vengeful_Spirit]


class Explosive_Toads(Rune):
    """ Explosive Toads """
    description = """Mutate to fire bullfrogs that explode for 245% weapon damage as Fire."""


class Piercing_Toads(Rune):
    """ Piercing Toads """
    description = """Mutate to frogs that pierce through enemies for 130% weapon damage as Physical."""


class Rain_of_Toads(Rune):
    """ Rain of Toads """
    description = """Cause toads to rain from the sky that deal 182% weapon damage as Poison to enemies in the area over 2 seconds."""


class Addling_Toads(Rune):
    """ Addling Toads """
    description = """Mutate to yellow toads that deal 190% weapon damage as Poison and have a 15% chance to Confuse affected enemies for 4 seconds."""


class Toad_Affinity(Rune):
    """ Toad Affinity """
    description = """Gain 9 Mana every time a toad hits an enemy.

Plague of Toads' damage turns into Cold."""


class Plague_of_Toads(Active):
    """ Plague of Toads """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Release a handful of toads that deal 190% weapon damage as Poison to enemies they come in contact with."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/plague-of-toads'
    runes = [Explosive_Toads, Piercing_Toads, Rain_of_Toads, Addling_Toads, Toad_Affinity]


class Consuming_Spirit(Rune):
    """ Consuming Spirit """
    description = """The spirit returns 4291 Life per second.

Haunt's damage turns into Fire."""


class Resentful_Spirits(Rune):
    """ Resentful Spirits """
    description = """Release two spirits with every cast."""


class Lingering_Spirit(Rune):
    """ Lingering Spirit """
    description = """If there are no enemies left, the spirit will linger for up to 10 seconds looking for new enemies."""


class Poisoned_Spirit(Rune):
    """ Poisoned Spirit """
    description = """Haunted enemies take 20% more damage from your attacks.

Haunt's damage turns into Poison."""


class Draining_Spirit(Rune):
    """ Draining Spirit """
    description = """The spirit returns 12 Mana per second.

Haunt's damage turns into Physical."""


class Haunt(Active):
    """ Haunt """
    category = "active"
    description = """Cost: 50 Mana

Haunt an enemy with a spirit, dealing 4000% weapon damage as Cold over 12 seconds. If the enemy dies, the spirit will haunt another nearby enemy.

An enemy can only be affected by one Haunt at a time."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/haunt'
    runes = [Consuming_Spirit, Resentful_Spirits, Lingering_Spirit, Poisoned_Spirit, Draining_Spirit]


class Black_Blood(Rune):
    """ Black Blood """
    description = """Ichor erupts from the corpse of the Zombie Dog and Stuns enemies for 3 seconds."""


class Next_of_Kin(Rune):
    """ Next of Kin """
    description = """Each Zombie Dog you sacrifice has a 35% chance to resurrect as a new Zombie Dog."""


class Pride(Rune):
    """ Pride """
    description = """Gain 280 Mana for each Zombie Dog you sacrifice."""


class For_the_Master(Rune):
    """ For the Master """
    description = """Command all of your Zombie Dogs to charge the target at the same time, each dealing 1300% weapon damage as Physical."""


class Provoke_the_Pack(Rune):
    """ Provoke the Pack """
    description = """Gain 20% increased damage done for 5 seconds after using Sacrifice."""


class Sacrifice(Active):
    """ Sacrifice """
    category = "active"
    description = """Banish one of your active Zombie Dogs causing it to explode, dealing 1090% of your weapon damage as Physical to all enemies within 12 yards."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/sacrifice'
    runes = [Black_Blood, Next_of_Kin, Pride, For_the_Master, Provoke_the_Pack]


class Pile_On(Rune):
    """ Pile On """
    description = """Summon a tower of zombies that falls over, dealing 880% weapon damage as Physical to any enemies it hits."""


class Undeath(Rune):
    """ Undeath """
    description = """If the Zombie Charger kills any enemies, it will reanimate and charge nearby enemies for 480% weapon damage as Poison. This effect can repeat up to 2 times."""


class Lumbering_Cold(Rune):
    """ Lumbering Cold """
    description = """Zombie winter bears crawl out of the ground and run in all directions, dealing 280% weapon damage as Cold to nearby enemies."""


class Explosive_Beast(Rune):
    """ Explosive Beast """
    description = """Summon an explosive Zombie Dog that streaks toward the enemy before exploding, dealing 680% weapon damage as Fire to all enemies within 12 yards."""


class Zombie_Bears(Rune):
    """ Zombie Bears """
    description = """Summon zombie bears that stampede towards your enemy. Each bear deals 520% weapon damage as Poison to enemies in the area."""


class Zombie_Charger(Active):
    """ Zombie Charger """
    category = "active"
    description = """Cost: 150 Mana

Call forth a reckless, suicidal zombie that deals 560% weapon damage as Poison to all enemies in its path before decomposing."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/zombie-charger'
    runes = [Pile_On, Undeath, Lumbering_Cold, Explosive_Beast, Zombie_Bears]


class Jaunt(Rune):
    """ Jaunt """
    description = """Increase the duration of Spirit Walk to 3 seconds."""


class Honored_Guest(Rune):
    """ Honored Guest """
    description = """Gain 20% of your maximum Mana when you activate Spirit Walk."""


class Umbral_Shock(Rune):
    """ Umbral Shock """
    description = """When Spirit Walk ends, your physical body erupts for 750% weapon damage as Fire to all enemies within 10 yards."""


class Severance(Rune):
    """ Severance """
    description = """Increase your movement speed by an additional 100% while in the spirit realm."""


class Healing_Journey(Rune):
    """ Healing Journey """
    description = """Gain 15% of your maximum Life when you activate Spirit Walk."""


class Spirit_Walk(Active):
    """ Spirit Walk """
    category = "active"
    description = """Cooldown: 10 seconds

Leave your physical body and enter the spirit realm for 2 seconds. While in the spirit realm, your movement is unhindered.

This ability does not start its cooldown until after its effects expire."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/spirit-walk'
    runes = [Jaunt, Honored_Guest, Umbral_Shock, Severance, Healing_Journey]


class The_Spirit_Is_Willing(Rune):
    """ The Spirit Is Willing """
    description = """Gain 12 Mana each time Spirit Barrage hits."""


class Well_of_Souls(Rune):
    """ Well of Souls """
    description = """An additional 3 spirits seek out other enemies and deal 65% weapon damage as Fire."""


class Phantasm(Rune):
    """ Phantasm """
    description = """Summon a spectre that deals 750% weapon damage as Cold over 5 seconds to all enemies within 10 yards.

You can have a maximum of 3 Phantasms out at one time."""


class Phlebotomize(Rune):
    """ Phlebotomize """
    description = """Gain 6437 Life each time Spirit Barrage hits."""


class Manitou(Rune):
    """ Manitou """
    description = """Summon a spectre that hovers over you, unleashing spirit bolts at nearby enemies for 6000% weapon damage as Cold over 20 seconds."""


class Spirit_Barrage(Active):
    """ Spirit Barrage """
    category = "active"
    description = """Cost: 100 Mana

Bombard an enemy with 4 spirit bolts that deal a total of 600% weapon damage as Cold."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/spirit-barrage'
    runes = [The_Spirit_Is_Willing, Well_of_Souls, Phantasm, Phlebotomize, Manitou]


class Humongoid(Rune):
    """ Humongoid """
    description = """The Gargantuan gains the Cleave ability, allowing its attacks to hit multiple enemies for 585% of your weapon damage as Cold."""


class Restless_Giant(Rune):
    """ Restless Giant """
    description = """When the Gargantuan encounters an elite enemy or is near 5 enemies, it enrages for 15 seconds gaining:
  20% movement speed
  35% attack speed
  200% Physical damage

This effect cannot occur more than once every 45 seconds. Elite enemies include champions, rares, bosses, and other players."""


class Wrathful_Protector(Rune):
    """ Wrathful Protector """
    description = """Summon a more powerful Gargantuan to fight for you for 15 seconds. The Gargantuan's fists burn with fire, dealing 575% of your weapon damage as Fire and knocking enemies into the air."""


class Big_Stinker(Rune):
    """ Big Stinker """
    description = """The Gargantuan is surrounded by a poison cloud that deals 135% weapon damage as Poison per second to nearby enemies."""


class Bruiser(Rune):
    """ Bruiser """
    description = """The Gargantuan gains the ability to periodically slam enemies, dealing 200% of your weapon damage as Fire and stunning them for 3 seconds."""


class Gargantuan(Active):
    """ Gargantuan """
    category = "active"
    description = """Cooldown: 60 seconds

Summon a Gargantuan zombie to fight for you. The Gargantuan attacks for 450% of your weapon damage as Physical."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/gargantuan'
    runes = [Humongoid, Restless_Giant, Wrathful_Protector, Big_Stinker, Bruiser]


class Pestilence(Rune):
    """ Pestilence """
    description = """Locust Swarm has a 100% chance to jump to two additional enemies instead of one. """


class Devouring_Swarm(Rune):
    """ Devouring Swarm """
    description = """Gain 25 Mana a second while the first enemy hit by a Locust Swarm cast is still affected by that swarm. """


class Cloud_of_Insects(Rune):
    """ Cloud of Insects """
    description = """Enemies affected deal 25% reduced damage."""


class Diseased_Swarm(Rune):
    """ Diseased Swarm """
    description = """Enemies killed while affected by Locust Swarm leave behind a cloud of locusts that deal 750% weapon damage as Poison over 3 seconds to enemies who stand in the area."""


class Searing_Locusts(Rune):
    """ Searing Locusts """
    description = """Engulf the enemy with burning locusts that deal 1480% weapon damage as Fire over 8 seconds."""


class Locust_Swarm(Active):
    """ Locust Swarm """
    category = "active"
    description = """Cost: 300 Mana

Unleash a plague of locusts that swarms an enemy, dealing 1040% weapon damage as Poison over 8 seconds.

The locusts will jump to additional nearby enemies."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/locust-swarm'
    runes = [Pestilence, Devouring_Swarm, Cloud_of_Insects, Diseased_Swarm, Searing_Locusts]


class Flash_Fire(Rune):
    """ Flash Fire """
    description = """Rather than exploding for area damage, each Firebomb can bounce to up to 6 additional enemies. Damage is reduced by 15% per bounce."""


class Roll_the_Bones(Rune):
    """ Roll the Bones """
    description = """The skull can bounce up to 2 times."""


class Fire_Pit(Rune):
    """ Fire Pit """
    description = """The explosion creates a pool of fire that deals 60% weapon damage as Fire over 3 seconds."""


class Pyrogeist(Rune):
    """ Pyrogeist """
    description = """Create a column of flame that spews fire at the closest enemy for 880% weapon damage as Fire over 6 seconds.

You may have up to 3 Pyrogeists active at a time."""


class Ghost_Bomb(Rune):
    """ Ghost Bomb """
    description = """In addition to the base explosion, the skull creates a larger blast that deals an additional 30% weapon damage as Cold to all other enemies within 28 yards."""


class Firebomb(Active):
    """ Firebomb """
    category = "active"
    description = """This is a Signature spell. Signature spells are free to cast.

Lob an explosive skull that deals 155% weapon damage as Fire to all enemies within 8 yards."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/firebomb'
    runes = [Flash_Fire, Roll_the_Bones, Fire_Pit, Pyrogeist, Ghost_Bomb]


class Hedge_Magic(Rune):
    """ Hedge Magic """
    description = """The Fetish Shaman will periodically heal allies for 32,185 Life."""


class Jinx(Rune):
    """ Jinx """
    description = """Hexed enemies take 15% additional damage."""


class Angry_Chicken(Rune):
    """ Angry Chicken """
    description = """Transform into an angry chicken for up to 2 seconds that can explode for 1350% weapon damage as Poison to all enemies within 12 yards."""


class Toad_of_Hugeness(Rune):
    """ Toad of Hugeness """
    description = """Summon a giant toad that pulls in enemies, briefly swallows them whole, then spits them back out with a layer of goo that deals 750% weapon damage as Poison over 5 seconds, Slows them, and increases their damage taken by 15%."""


class Unstable_Form(Rune):
    """ Unstable Form """
    description = """Hexed enemies explode when killed, dealing 500% weapon damage as Fire to all enemies within 8 yards."""


class Hex(Active):
    """ Hex """
    category = "active"
    description = """Cooldown: 15 seconds

Summon a Fetish Shaman for 12 seconds that will hex groups of enemies into chickens. Hexed enemies are unable to perform offensive actions."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/hex'
    runes = [Hedge_Magic, Jinx, Angry_Chicken, Toad_of_Hugeness, Unstable_Form]


class Acid_Rain(Rune):
    """ Acid Rain """
    description = """Increase the initial area of effect of Acid Cloud to 24 yards."""


class Lob_Blob_Bomb(Rune):
    """ Lob Blob Bomb """
    description = """The acid on the ground forms into a slime that irradiates nearby enemies for 600% weapon damage as Poison over 5 seconds."""


class Slow_Burn(Rune):
    """ Slow Burn """
    description = """Create pools of frost to deal 720% weapon damage as Cold over 6 seconds."""


class Kiss_of_Death(Rune):
    """ Kiss of Death """
    description = """Spit a cloud of acid that deals 333% weapon damage as Poison, followed by 400% weapon damage as Poison over 3 seconds."""


class Corpse_Bomb(Rune):
    """ Corpse Bomb """
    description = """Raise a corpse from the ground that explodes for 700% weapon damage as Fire to enemies in the area."""


class Acid_Cloud(Active):
    """ Acid Cloud """
    category = "active"
    description = """Cost: 175 Mana

Cause acid to rain down, dealing an initial 300% weapon damage as Poison, followed by 360% weapon damage as Poison over 3 seconds to enemies who remain in the area."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/acid-cloud'
    runes = [Acid_Rain, Lob_Blob_Bomb, Slow_Burn, Kiss_of_Death, Corpse_Bomb]


class Unstable_Realm(Rune):
    """ Unstable Realm """
    description = """Reduce the cooldown of Mass Confusion to 30 seconds."""


class Devolution(Rune):
    """ Devolution """
    description = """Enemies killed while Confused have a 100% chance to spawn a Zombie Dog."""


class Mass_Hysteria(Rune):
    """ Mass Hysteria """
    description = """Up to 10 enemies who are not Confused become Stunned for 3 seconds."""


class Paranoia(Rune):
    """ Paranoia """
    description = """All enemies in the area of Mass Confusion deal 30% less damage for 12 seconds."""


class Mass_Hallucination(Rune):
    """ Mass Hallucination """
    description = """Amid the confusion, a giant spirit rampages through enemies, dealing 400% weapon damage per second as Physical to enemies it passes through."""


class Mass_Confusion(Active):
    """ Mass Confusion """
    category = "active"
    description = """Cooldown: 60 seconds

Incite paranoia in enemies, confusing them and causing some to be Charmed and fight for you for 12 seconds."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/mass-confusion'
    runes = [Unstable_Realm, Devolution, Mass_Hysteria, Paranoia, Mass_Hallucination]


class Jungle_Drums(Rune):
    """ Jungle Drums """
    description = """Increase the duration of the ritual to 30 seconds."""


class Rain_Dance(Rune):
    """ Rain Dance """
    description = """The ritual restores 250 Mana per second while standing in the ritual area."""


class Slam_Dance(Rune):
    """ Slam Dance """
    description = """The Fetish increases the damage of all nearby allies by 15%."""


class Ghost_Trance(Rune):
    """ Ghost Trance """
    description = """The ritual heals all nearby allies for 5% of their maximum Life per second and reduces all damage taken by 20%."""


class Boogie_Man(Rune):
    """ Boogie Man """
    description = """Enemies who die in the ritual area have a 50% chance to resurrect as a Zombie Dog."""


class Big_Bad_Voodoo(Active):
    """ Big Bad Voodoo """
    category = "active"
    description = """Cooldown: 120 seconds

Conjure a Fetish that begins a ritual dance that increases the attack speed and movement speed of all nearby allies by 15% for 20 seconds."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/big-bad-voodoo'
    runes = [Jungle_Drums, Rain_Dance, Slam_Dance, Ghost_Trance, Boogie_Man]


class Ring_of_Poison(Rune):
    """ Ring of Poison """
    description = """Summon a deadly ring for 5 seconds that poisons nearby enemies for 1200% weapon damage as Poison over 8 seconds."""


class Wall_of_Zombies(Rune):
    """ Wall of Zombies """
    description = """Increase the width of the wall to 50 yards. All enemies in front of you are knocked back behind the wall."""


class Surrounded_by_Death(Rune):
    """ Surrounded by Death """
    description = """Raise a circle of zombies from the ground that traps and attacks nearby enemies for 1250% weapon damage as Physical over 5 seconds."""


class Fire_Wall(Rune):
    """ Fire Wall """
    description = """Raise a wall of flame 40 yards wide for 8 seconds that burns enemies who walk through, causing them to take 1100% weapon damage as Fire over 4 seconds."""


class Communing_with_Spirits(Rune):
    """ Communing with Spirits """
    description = """Summon a circle of spirits for 6 seconds that deals 1200% weapon damage as Cold, Chills nearby enemies by 60%, and reduces their damage dealt by 25% for 3 seconds."""


class Wall_of_Death(Active):
    """ Wall of Death """
    category = "active"
    description = """Cooldown: 8 seconds

Raise a wall of zombies 28 yards wide from the ground that blocks enemies and attacks them for 1200% weapon damage as Physical over 6 seconds."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/wall-of-death'
    runes = [Ring_of_Poison, Wall_of_Zombies, Surrounded_by_Death, Fire_Wall, Communing_with_Spirits]


class Fetish_Ambush(Rune):
    """ Fetish Ambush """
    description = """Each Fetish deals 680% weapon damage as Cold to any nearby enemy as it is summoned."""


class Devoted_Following(Rune):
    """ Devoted Following """
    description = """Decrease the cooldown of Fetish Army to 90 seconds."""


class Legion_of_Daggers(Rune):
    """ Legion of Daggers """
    description = """Increase number of dagger-wielding Fetishes summoned by 3."""


class Tiki_Torchers(Rune):
    """ Tiki Torchers """
    description = """Summon an additional 2 Fetish casters who breathe fire in a cone in front of them and deal 85% of your weapon damage as Fire."""


class Head_Hunters(Rune):
    """ Head Hunters """
    description = """Summon an additional 2 Hunter Fetishes that shoot blowdarts at enemies, dealing 130% of your weapon damage as Poison."""


class Fetish_Army(Active):
    """ Fetish Army """
    category = "active"
    description = """Cooldown: 120 seconds

Summon an army of 5 dagger-wielding Fetishes to fight by your side for 20 seconds. The Fetishes attack for 180% of your weapon damage as Physical."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/fetish-army'
    runes = [Fetish_Ambush, Devoted_Following, Legion_of_Daggers, Tiki_Torchers, Head_Hunters]


class Bogadile(Rune):
    """ Bogadile """
    description = """A giant bogadile emerges from the pool of water, Stuns, and bites a monster dealing 1100% weapon damage as Physical."""


class Zombie_Piranhas(Rune):
    """ Zombie Piranhas """
    description = """Turn the piranhas into zombie piranhas.  The piranhas will leap out from the pool savagely at nearby enemies"""


class Piranhado(Rune):
    """ Piranhado """
    description = """The pool of piranhas becomes a tornado of piranhas that lasts 4 seconds.  Nearby enemies are periodically sucked into the tornado.

Increases the cooldown to 16 seconds."""


class Wave_of_Mutilation(Rune):
    """ Wave of Mutilation """
    description = """Turn each cast into a wave of piranhas that crash forward dealing 475% weapon damage and causing all enemies affected to take 15% increased damage for 8 seconds. """


class Frozen_Piranhas(Rune):
    """ Frozen Piranhas """
    description = """Changes the damage dealt to 400% weapon damage as Cold over 8 seconds, chilling enemies for the entire duration."""


class Piranhas(Active):
    """ Piranhas """
    category = "active"
    description = """Cost: 250 Mana
Cooldown: 8 seconds

Summons a pool of deadly piranhas that deals 400% weapon damage as Poison over 8 seconds.  Affected enemies will also take 15% increased damage."""
    url = r'https://us.diablo3.com//en/class/witch-doctor/active/piranhas'
    runes = [Bogadile, Zombie_Piranhas, Piranhado, Wave_of_Mutilation, Frozen_Piranhas]

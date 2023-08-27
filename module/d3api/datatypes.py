# from data import items_cache
# from data import weapons_cache
import re

class Item(object):
    text = ''

    def get_stat_potential(self):
        print('own url', self.url)
        print('https://eu.diablo3.com{}'.format(self.url))
        # https://eu.diablo3.com/en/item/axe-2h/
        pass

    def recognize(self):
        print('recognizing')
        print(self.text)
        pass

    @property
    def range(self):
        return range(1, 10)

    def gemSlots(self):
        """ return derived gemslots """
        return 0

    def visit(self):
        import webbrowser
        webbrowser.open('https://eu.diablo3.com{}'.format(self.url))
        print('visiting')

    def interpret(self):
        """ returns a list of tokens found in the items text """
        import re

        with open(r'G:\projects\Diablo-API\module\d3api\data\tokens.txt', 'r') as token_file:
            tokens = [x[:-1] for x in token_file.readlines() if x[:-1] != '']

        found_tokens = []
        for token in tokens:
            if re.search(r"[( ]"+token+"[) .,s]", self.text):
                found_tokens.append(token)

        return found_tokens





    def damage_increase(self):
        import re
        result = re.search(r"damage.* (\d+?)%", self.text)
        if result:
            return int(result.groups()[0])
        return 0

    def help(self):
        """ print a textual version of the objects functions and attributes """
        import inspect
        for name, attr in inspect.getmembers(self):
            if not name.startswith('__'):
                print("{} {} -> {}: {}".format(name, ' ' * (20-len(name)), type(attr), attr))
                if inspect.ismethod(attr):
                    print("'''{}'''".format(attr.__doc__))
                print()




class Set(object):
    items = False
    levels = dict
    _class = False
    pieces = None

    def yield_bonus(self, amount):
        bonusses = []
        for level, bonus in self.levels.items():
            if level <= amount:
                bonusses.append(bonus)
        return bonusses


class Set_Item(Item):
    set = False

    def howTo(self):
        return 'N/A'


class BloodShard:
    """ Blood Shard """
    pass

    def farming(self):
        '''

        :return:
        '''
        return '''
        For the most blood shards you should be farming greater rifts that you can complete in 5ish minutes. Honestly blood shards aren't the best way to get new gear if you already have every piece you need and are looking to upgrade to ancient versions (which my guess would be what you are doing if you can complete gr 65). Good news is the best way to get ancients is to reforge a legendary, which would result in you doing the same thing, because farming grs is the best way to get legendaries also. Make sure you don't reforge the one you have equipped though because the reroll can make it worse, so keep an extra piece on your bank and just reroll the worse of the two until you get a better piece.
        '''

    def howTo(self):
        return '''
        https://www.reddit.com/r/diablo3/comments/bagr92/fastest_way_to_farm_blood_shards/
        https://www.icy-veins.com/d3/how-to-farm-legendary-and-set-items-guide
        '''


class Rare_Item:
    def howTo(self):
        return 'N/A'


class Legendary_Item:
    def howTo(self):
        return 'N/A'


class Legendary_power:
    """ the extracted power Effect"""

    # @property
    # def requires(self) -> Kanai.KanaisCube:
    #     return Kanai.KanaisCube


# Legendary crafting items ---------------------------------------------------------------------------------------------

class Khanduran_Rune:
    """ Legendary Crafting Material """

    def howTo(self):
        return 'Obtained from Act I Horadric Caches.'


class CALDEUM_NIGHTSHADE:
    """ Legendary Crafting Material """

    def howTo(self):
        return 'Obtained from Act II Horadric Caches.'


class ARREAT_WAR_TAPESTRY:
    """ Legendary Crafting Material """

    def howTo(self):
        return 'Obtained from Act III Horadric Caches.'


class CORRUPTED_ANGEL_FLESH:
    """ Legendary Crafting Material """

    def howTo(self):
        return 'Obtained from Act IV Horadric Caches.'


class WESTMARCH_HOLY_WATER:
    """ Legendary Crafting Material """

    def howTo(self):
        return 'Obtained from Act V Horadric Caches.'


class Deaths_Breath:
    """ Unique Crafting Material"""

    def howTo(self):
        return 'Found on the most challenging monsters. Used by Artisans to craft and modify items.'

    def farming(self):
        return '''
        https://www.gamecmd.com/diablo-3-deaths-breath-farming/
        '''


class REUSABLE_PARTS:
    """ Crafting Material """

    def howTo(self):
        return 'Obtained by using the Blacksmith to salvage normal weapons and armor.'


class ARCANE_DUST:
    """ Magic Crafting Material """

    def howTo(self):
        return 'Obtained by using the Blacksmith to salvage magic weapons and armor.'


class VEILED_CRYSTAL:
    """ Rare Crafting Material """

    def howTo(self):
        return 'Obtained by using the Blacksmith to salvage rare weapons and armor.'


class FORGOTTEN_SOUL:
    """ Legendary Crafting Material """

    def howTo(self):
        return 'Obtained by using the Blacksmith to salvage legendary weapons and armor.'


# Objects --------------------------------------------------------------------------------------------------------------

class Rift(object):
    level = 1
    greater = False

    def __init__(self):
        pass

    def source_of(self) -> [BloodShard]:
        amount = [BloodShard()] * 10
        return amount


# todo: how to express a Source-Of-<type> best?

class Horadric_Cache:
    """ Horadric Cache """
    '''
    # Each Horadric Cache obtained at level 70 is also guaranteed to have the corresponding Crafting Material (last entry in each section). Drop rates depend on difficulty at which the Cache was acquired:
    #
    # 3 per cache (Normal – Master)
    # 6 per cache (Torment I – VI)  # correct
    #
    # 8 per cache (Torment VII – IX)
    # 10 per cache (Torment X)
    # 12 per cache (Torment XI)
    # 14 per cache (Torment XII)
    # 16 per cache (Torment XIII)
    # 18 per cache (Torment XIV)
    # 20 per cache (Torment XV)
    # 22 per cache (Torment XVI)
    '''


class KanaisCube:
    source = r"https://eu.diablo3.com/en/game/guide/items/kanais-cube"

    slots = False

    def __init__(self):
        self.slots = [] * 3

    def calcIngredients(self, wants):
        return []

    class transmute:

        def EXTRACT_LEGENDARY_POWER(self, input):
            input[Legendary_Item] -= 1
            input[Khanduran_Rune] -= 1
            input[CALDEUM_NIGHTSHADE] -= 1
            input[ARREAT_WAR_TAPESTRY] -= 1
            input[CORRUPTED_ANGEL_FLESH] -= 1
            input[WESTMARCH_HOLY_WATER] -= 1

            input[Deaths_Breath] -= 5

        # todo: note: how do you express a Required / Threshold / Activation function style in Python?
        #  as in 'you need X or this function will assert?' or 'will not function unless X'
        #  there has got to be a
        def UPGRADE_RARE_ITEM(self, input: Rare_Item) -> Legendary_Item:
            """ Hope of Cain
            Upgrades a level 70 item of Rare quality into a level 70 Legendary of the same item type. For example, upgrading a Rare one-handed sword will result in a random Legendary one-handed sword.
            """

            input[Legendary_Item] -= 1
            input[REUSABLE_PARTS] -= 50
            input[ARCANE_DUST] -= 50
            input[VEILED_CRYSTAL] -= 50
            input[Deaths_Breath] -= 25

            return Legendary_Item

        def CONVERT_CRAFTING_MATERIALS(self, input):
            pass

        def CONVERT_SET_ITEM(self, input: Set_Item) -> Set_Item:
            """ Skill of Nilfur
            Transforms a Set item into another item belonging to the same Set. This recipe only works on Sets containing 3 or more pieces. For example, Natalya's Embrace would be transformed into another random piece of the Natalya’s Vengeance set.
            """
            return Set_Item

        def CONVERT_GEMS(self, input):
            pass

        def REMOVE_LEVEL_REQUIREMENT_ON_AN_ITEM(self, input):
            pass

        def REFORGE_LEGENDARY_OR_SET_ITEM(self, input):
            """ Law of Kulle
            Sacrificing great quantities of magical ingredients, the Horadric incantation known as the Law of Kulle
            allows you to reforge any Legendary or Set item. This process will grant your item different attributes,
            and may transform it into an Ancient or Primal Ancient version of the same item.

            Be warned; reforging an Ancient or Primal Ancient Legendary or Set item might
            result in the loss of the Ancient or Primal Ancient property.
            """
            pass

        def AUGMENT_ANCIENT_OR_PRIMAL_ANCIENT_ITEM(self, input):
            pass



        #todo
        '''
        challenge:
        circular imports
        # '''
        # weapon_powers = [
        #     weapons_cache.Ahavarion_Spear_of_Lycander,
        #     weapons_cache.Arthefs_Spark_of_Life,
        #     weapons_cache.Azurewrath,
        #     weapons_cache.Blood_Brother,
        #     items_cache.Bloodtide_Blade,
        #     items_cache.Bone_Ringer,
        #     weapons_cache.Burst_of_Wrath,
        #     weapons_cache.Butchers_Carver,
        #     weapons_cache.Cinder_Switch,
        #     items_cache.Covens_Criterion,
        #     items_cache.Defender_of_Westmarch,
        #     weapons_cache.Echoing_Fury,
        #     weapons_cache.Envious_Blade,
        #     weapons_cache.Eun_jang_do,
        #     items_cache.Freeze_of_Deflection,
        #     weapons_cache.Fulminator,
        #     items_cache.Funerary_Pick,
        #     weapons_cache.Genzaniku,
        #
        #     weapons_cache.Hack,
        #     weapons_cache.In_geom,
        #     items_cache.Iron_Rose,
        #     items_cache.Legers_Disdain,
        #     items_cache.Lost_Time,
        #     weapons_cache.Mad_Monarchs_Scepter,
        #     weapons_cache.Maloths_Focus,
        #     items_cache.Maltorius_Petrified_Spike,
        #     weapons_cache.Maximus,
        #     weapons_cache.Messerschmidts_Reaver,
        #     items_cache.Nayrs_Black_Death,
        #     weapons_cache.Odyn_Son,
        #     items_cache.Reilenas_Shadowhook,
        #     weapons_cache.Rimeheart,
        #     weapons_cache.Schaefers_Hammer,
        #     weapons_cache.Scourge,
        #     items_cache.Scythe_of_the_Cycle,
        #     weapons_cache.Sever,
        #
        #     weapons_cache.Shard_of_Hate,
        #     weapons_cache.Sky_Splitter,
        #     weapons_cache.Skycutter,
        #     weapons_cache.Solanium,
        #     weapons_cache.Soulsmasher,
        #     weapons_cache.Spear_of_Jairo,
        #     weapons_cache.Stalgards_Decimator,
        #     weapons_cache.Sunder,
        #     weapons_cache.The_Burning_Axe_of_Sankis,
        #     weapons_cache.The_Butchers_Sickle,
        #     weapons_cache.The_Executioner,
        #     weapons_cache.The_Furnace,
        #     weapons_cache.The_Tormentor,
        #     weapons_cache.Thunderfury_Blessed_Blade_of_the_Windseeker,
        #     items_cache.TragOuls_Corroded_Fang,
        #     items_cache.Wall_of_Man,
        #     weapons_cache.Wizardspike,
        #
        # ]
        # # 53
        #
        # armor_powers = [
        #     items_cache.Ancient_Parthan_Defenders,
        #     items_cache.Andariels_Visage,
        #     items_cache.Aquila_Cuirass,
        #     items_cache.Bloodsong_Mail,
        #     items_cache.Boots_of_Disregard,
        #     items_cache.Broken_Crown,
        #     items_cache.Bryners_Journey,
        #     items_cache.Chaingmail,
        #     items_cache.Cindercoat,
        #     items_cache.Cord_of_the_Sherma,
        #     items_cache.Corpsewhisper_Pauldrons,
        #     items_cache.Custerian_Wristguards,
        #     items_cache.Dayntees_Binding,
        #     items_cache.Death_Watch_Mantle,
        #     items_cache.Deaths_Bargain,
        #     items_cache.Deathseers_Cowl,
        #     items_cache.Defiler_Cuisses,
        #     items_cache.Depth_Diggers,
        #
        #     items_cache.Fates_Vow,
        #     items_cache.Fire_Walkers,
        #     items_cache.Frostburn,
        #     items_cache.Gladiator_Gauntlets,
        #     items_cache.Gloves_of_Worship,
        #     items_cache.Goldskin,
        #     items_cache.Goldwrap,
        #     items_cache.Golemskin_Breeches,
        #     items_cache.Grasps_of_Essence,
        #     items_cache.Harrington_Waistguard,
        #     items_cache.Heart_of_Iron,
        #     items_cache.Hexing_Pants_of_Mr_Yan,
        #     items_cache.Homing_Pads,
        #     items_cache.Ice_Climbers,
        #     items_cache.Illusory_Boots,
        #     items_cache.Insatiable_Belt,
        #     items_cache.Irontoe_Mudsputters,
        #     items_cache.Krelms_Buff_Belt,
        #
        #     items_cache.Krelms_Buff_Bracers,
        #     items_cache.Leorics_Crown,
        #     items_cache.Magefist,
        #     items_cache.Mantle_of_Channeling,
        #     items_cache.Mask_of_Scarlet_Death,
        #     items_cache.Moribund_Gauntlets,
        #     items_cache.Nemesis_Bracers,
        #     items_cache.Pauldrons_of_the_Skeleton_King,
        #     items_cache.Pox_Faulds,
        #     items_cache.Prides_Fall,
        #     items_cache.Promise_of_Glory,
        #     items_cache.Razeths_Volition,
        #     items_cache.Razor_Strop,
        #     items_cache.Reapers_Wraps,
        #     items_cache.Requiem_Cereplate,
        #     items_cache.Sanguinary_Vambraces,
        #     items_cache.Sash_of_Knives,
        #     items_cache.Sebors_Nightmare,
        #
        #     items_cache.Shi_Mizus_Haori,
        #     items_cache.Spaulders_of_Zakara,
        #     items_cache.St_Archews_Gage,
        #     items_cache.Steuarts_Greaves,
        #     items_cache.Stone_Gauntlets,
        #     items_cache.String_of_Ears,
        #     items_cache.Strongarm_Bracers,
        #     items_cache.Tasker_and_Theo,
        #     items_cache.Thundergods_Vigor,
        #     items_cache.Warzechian_Armguards
        # ]
        #
        # trinket_powers = [
        #     items_cache.Arcstone,
        #     items_cache.Avarice_Band,
        #     items_cache.Band_of_Hollow_Whispers,
        #     items_cache.Briggs_Wrath,
        #     items_cache.Broken_Crown,
        #     items_cache.Bul_Kathoss_Wedding_Band,
        #     items_cache.Circle_of_Nailujs_Evol,
        #     items_cache.Convention_of_Elements,
        #     items_cache.Countess_Julias_Cameo,
        #     items_cache.Dovu_Energy_Trap,
        #     items_cache.Golden_Gorget_of_Leoric,
        #     items_cache.Haunt_of_Vaxo,
        #     items_cache.Haunted_Visions,
        #     items_cache.Hellfire_Ring,
        #     items_cache.Justice_Lantern,
        #     items_cache.Kredes_Flame,
        #     items_cache.Krysbins_Sentence,
        #     items_cache.Kymbos_Gold,
        #
        #     items_cache.Lornelles_Sunstone,
        #     items_cache.Maras_Kaleidoscope,
        #     items_cache.Moonlight_Ward,
        #     items_cache.Nagelring,
        #     items_cache.Obsidian_Ring_of_the_Zodiac,
        #     items_cache.Oculus_Ring,
        #     items_cache.Overwhelming_Desire,
        #     items_cache.Pandemonium_Loop,
        #     items_cache.Puzzle_Ring,
        #     items_cache.Rakoffs_Glass_of_Life,
        #     items_cache.Rechels_Ring_of_Larceny,
        #     items_cache.Ring_of_Royal_Grandeur,
        #     items_cache.Rogars_Huge_Stone,
        #     items_cache.Squirts_Necklace,
        #     items_cache.Stone_of_Jordan,
        #     items_cache.Talisman_of_Aranoch,
        #     items_cache.The_Ess_of_Johan,
        #     items_cache.The_Flavor_of_Time,
        #
        #     items_cache.The_Johnstone,
        #     items_cache.The_Star_of_Azkaranth,
        #     items_cache.Unity,
        #     items_cache.Wisdom_of_Kalan,
        #     items_cache.Wyrdward,
        #     items_cache.Xephirian_Amulet
        # ]


class attribute:
    def __init__(self, val):
        pass


Intel = attribute


class Gear:
    gemSlots = 0

    def __init__(self, slots):
        self.gemSlots = slots


class Armour:
    pass


class Gem:
    def __init__(self, type):
        pass

    @property
    def max(self):
        return Intel(280)


import enum


class Classes(enum.Enum):
    """ utility class to make name look-up's easier """
    BARBARIAN = 'Barbarian'
    WIZARD = 'Wizard'
    WITCH_DOCTOR = 'Witch Doctor'
    DEMON_HUNTER = 'Demon Hunter'
    NECROMANCER = 'Necromancer'
    CRUSADER = 'Crusader'
    MONK = 'Monk'

    from types import DynamicClassAttribute

    @DynamicClassAttribute
    def low(self):
        """The name of the Enum member."""
        return self._value_.lower()

    @DynamicClassAttribute
    def internet(self):
        """The name of the Enum member."""
        return self._value_.replace(' ', '-').lower()

    @DynamicClassAttribute
    def os_name(self):
        """The name of the Enum member."""
        return self._value_.replace(' ', '_')

    @staticmethod
    def names():
        return [obj.value for n, obj in Classes._value2member_map_.items()]

    @staticmethod
    def items():
        return [obj for n, obj in Classes._value2member_map_.items()]

    @staticmethod
    def find(cls):
        if cls in Classes._value2member_map_:
            return Classes._value2member_map_[cls]
        else:
            print('{} not found in Classes'.format(cls))

def isGenerator(obj):
    """ assert when object generates the primary resource """
    import inspect
    if inspect.isclass(obj):
        class_str = inspect.getsource(obj).lower()
        if 'generate' in class_str and 'wrath' in class_str:
            return True

    # if hasattr(obj, 'description') and obj.description:
    #     if 'Generate' in obj.description:
    #         return True
    return False


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

    @property
    def isGenerator(self):
        if 'Generate' in self.description:
            return True
        return False

    @property
    def tags(self):
        # derivisions of skill text
        desc = self.description.lower()
        lookup = {
            'cause': 'trigger',
            'rocks': 'falling objects',
            'area': 'area of effect',
            'weapon damage': 'weapon damage',
            'in its path': 'directional',
            'hurl.*at': 'directional',
            'cooldown is reduced': 'cooldown stacker',
            'whirlwind': 'all round damage',
            '\d{1,6}% movement speed': 'speed increase',
            'cost: \d{1,6} fury': 'fury spender',
            'cooldown:  \d{1,4} seconds': 'has cooldown',
            'raises.*attributes': 'temp attr bumper',
            'summon.': 'adds minions',
        }
        _tags = []
        for tag, concept in lookup.items():
            if re.search(tag, desc):
                _tags.append(concept)

        return _tags


class Passive(Skill):
    pass


class Active(Skill):
    pass


class Rune:

    Head = 'Helm'
    Hands = 'Gloves'
    Torso = 'Chest Armor'
    Waist = 'Belt'
    Legs = 'Pants'
    Feet = 'Boots'
    Shoulders = 'Shoulders'

    def __add__(self, other):
        pass


if __name__ == '__main__':
    try:
        print(KanaisCube.transmute().UPGRADE_RARE_ITEM())
    except TypeError as t:
        print(t)
        print(t.args)
        print('typed')
    except Exception as e:

        print(e)
    print('after')

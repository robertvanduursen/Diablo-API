class Item(object):

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
    BARBARIAN = 'barbarian'
    WIZARD = 'wizard'
    WITCH_DOCTOR = 'witch doctor'
    DEMON_HUNTER = 'demon hunter'
    NECROMANCER = 'necromancer'
    CRUSADER = 'crusader'
    MONK = 'monk'


classes = [
    'barbarian',
    'wizard',
    'witch doctor',
    'demon hunter',
    'necromancer',
    'crusader',
    'monk',
]


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


class Passive(Skill):
    pass


class Active(Skill):
    pass


class Rune:
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

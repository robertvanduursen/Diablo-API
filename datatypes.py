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


class Rare_Item:
    def howTo(self):
        return 'N/A'

class Legendary_Item:
    def howTo(self):
        return 'N/A'

class Set_Item:
    def howTo(self):
        return 'N/A'


class LEGENDARY_POWER:
    """ the extracted power Effect"""

    # @property
    # def requires(self) -> Kanai.KanaisCube:
    #     return Kanai.KanaisCube


class KHANDURAN_RUNE:
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


class DEATHS_BREATH:
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


from Resources import BloodShard


class Rift(object):
    level = 1
    greater = False

    def __init__(self):
        pass

    def source_of(self) -> [BloodShard]:
        amount = [BloodShard()] * 10
        return amount








# todo: how to express a Source-Of-<type> best?


from Resources import *


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
            input[KHANDURAN_RUNE] -= 1
            input[CALDEUM_NIGHTSHADE] -= 1
            input[ARREAT_WAR_TAPESTRY] -= 1
            input[CORRUPTED_ANGEL_FLESH] -= 1
            input[WESTMARCH_HOLY_WATER] -= 1

            input[DEATHS_BREATH] -= 5

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
            input[DEATHS_BREATH] -= 25

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


try:
    print(KanaisCube.transmute().UPGRADE_RARE_ITEM())
except TypeError as t:
    print(t)
    print(t.args)
    print('typed')
except Exception as e:

    print(e)
print('after')
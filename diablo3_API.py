# test
class Legendary_Item:
    def howTo(self):
        return 'N/A'

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

############################################################################
############################################################################
############################################################################

class KanaisCube:
    source = r"https://eu.diablo3.com/en/game/guide/items/kanais-cube"

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


        def UPGRADE_RARE_ITEM(self, input):
            input[Legendary_Item] -= 1
            input[REUSABLE_PARTS] -= 50
            input[ARCANE_DUST] -= 50
            input[VEILED_CRYSTAL] -= 50
            input[DEATHS_BREATH] -= 25


        def CONVERT_CRAFTING_MATERIALS(self, input):
            pass


        def CONVERT_SET_ITEM(self, input):
            pass

        def CONVERT_GEMS(self, input):
            pass

        def REMOVE_LEVEL_REQUIREMENT_ON_AN_ITEM(self, input):
            pass

        def REFORGE_LEGENDARY_OR_SET_ITEM(self, input):
            pass

        def AUGMENT_ANCIENT_OR_PRIMAL_ANCIENT_ITEM(self, input):
            pass


# for name, typ in list(globals().items()): print(name)

ingredients = {
    Legendary_Item : 0,

    KHANDURAN_RUNE : 4,
    CALDEUM_NIGHTSHADE : 5,
    ARREAT_WAR_TAPESTRY : 5,
    CORRUPTED_ANGEL_FLESH : 5,
    WESTMARCH_HOLY_WATER : 0,

    DEATHS_BREATH : 22,

    REUSABLE_PARTS : 1686,
    ARCANE_DUST : 2924,
    VEILED_CRYSTAL : 2839,

    FORGOTTEN_SOUL : 43,
}

KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)
KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)
KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)
KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)


for item, quanitity in ingredients.items():
    print(item.__name__, '-->', 'still need %s more' % abs(quanitity) if quanitity < 0.0 else quanitity, '\t\t', item().howTo() )

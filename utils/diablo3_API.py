# test
from Kanai import Legendary_Item, KHANDURAN_RUNE, CALDEUM_NIGHTSHADE, ARREAT_WAR_TAPESTRY, CORRUPTED_ANGEL_FLESH, \
    WESTMARCH_HOLY_WATER, DEATHS_BREATH, REUSABLE_PARTS, ARCANE_DUST, VEILED_CRYSTAL, FORGOTTEN_SOUL, KanaisCube

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


# for name, typ in list(globals().items()): print(name)

ingredients = {
    Legendary_Item: 0,

    KHANDURAN_RUNE: 4,
    CALDEUM_NIGHTSHADE: 5,
    ARREAT_WAR_TAPESTRY: 5,
    CORRUPTED_ANGEL_FLESH: 5,
    WESTMARCH_HOLY_WATER: 0,

    DEATHS_BREATH: 22,

    REUSABLE_PARTS: 1686,
    ARCANE_DUST: 2924,
    VEILED_CRYSTAL: 2839,

    FORGOTTEN_SOUL: 43,
}

KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)
KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)
KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)
KanaisCube().transmute().UPGRADE_RARE_ITEM(ingredients)


for item, quanitity in ingredients.items():
    print(item.__name__, '-->', 'still need %s more' % abs(quanitity) if quanitity < 0.0 else quanitity, '\t\t', item().howTo() )

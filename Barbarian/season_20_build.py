"""

Season 20 Barbarian build

"""


class Immortal_Kings_Call:
    """ Immortal King's Call armor set """


    class Head:
        """ Helms """
        type = 'Helms'
        name = "Immortal King's Triumph"
        url = r'https://us.diablo3.com/en/item/immortal-kings-triumph-Unique_Helm_008_x1'


    class Hands:
        """ Gloves """
        type = 'Gloves'
        name = "Immortal King's Irons"
        url = r'https://us.diablo3.com/en/item/immortal-kings-irons-Unique_Gloves_008_x1'


    class Torso:
        """ Chest Armor """
        type = 'Chest Armor'
        name = "Immortal King's Eternal Reign"
        url = r'https://us.diablo3.com/en/item/immortal-kings-eternal-reign-Unique_Chest_013_x1'


    class Waist:
        """ Mighty Belts """
        type = 'Mighty Belts'
        name = "Immortal King's Tribal Binding"
        url = r'https://us.diablo3.com/en/item/immortal-kings-tribal-binding-Unique_BarbBelt_009_x1'


    class Legs:
        """ Pants """
        type = 'Pants'
        name = "Immortal King's Stature"
        url = r'https://us.diablo3.com/en/item/immortal-kings-stature-P2_Unique_Pants_02'


    class Feet:
        """ Boots """
        type = 'Boots'
        name = "Immortal King's Stride"
        url = r'https://us.diablo3.com/en/item/immortal-kings-stride-Unique_Boots_012_x1'


    class Two_Handed:
        """ Mighty Weapons """
        type = 'Mighty Weapons'
        name = "Immortal King's Boulder Breaker"
        url = r'https://us.diablo3.com/en/item/immortal-kings-boulder-breaker-Unique_Mighty_2H_010_x1'


from Diablo.Diablo3_webScraper import get_part_from_url


for _url in [
    'https://us.diablo3.com/en/item/immortal-kings-triumph-Unique_Helm_008_x1',
    'https://us.diablo3.com/en/item/immortal-kings-irons-Unique_Gloves_008_x1',
    'https://us.diablo3.com/en/item/immortal-kings-eternal-reign-Unique_Chest_013_x1',
    'https://us.diablo3.com/en/item/immortal-kings-tribal-binding-Unique_BarbBelt_009_x1',
    'https://us.diablo3.com/en/item/immortal-kings-stature-P2_Unique_Pants_02',
    'https://us.diablo3.com/en/item/immortal-kings-stride-Unique_Boots_012_x1',
    'https://us.diablo3.com/en/item/immortal-kings-boulder-breaker-Unique_Mighty_2H_010_x1',
    ]:

    test = get_part_from_url(_url)
    if not test : assert False
    else: print(test)

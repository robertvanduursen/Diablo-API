"""

Diablo playstyle


"""

'''

Necromancer

'''
import inspect
import requests, re


class Class_Info:
    def __init__(self, className):
        self.className = className
        # break_down & get_skills -> took 22 min

    def get_skills(self):

        from lxml import html
        import requests

        url = r'https://us.diablo3.com/en/class/{}/active/'.format(self.className)
        print(url)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        # //*[@id="table-skills-active"]/div/div/table/tbody/tr[1]/td[2]/div/h3/a
        _test = '//*[@class="skill-details"]'
        skills = tree.xpath(_test)
        total = 0
        for idx, skill in enumerate(skills):

            title = skill.xpath('h3[1]/a[1]')

            name = title[0].text_content()
            url = r'https://us.diablo3.com/{}'.format(title[0].attrib['href'])
            page = requests.get(url)
            tree = html.fromstring(page.content)

            _test = '//*[@class="skill-desc"]'
            desc = tree.xpath(_test)
            desc = desc[0].text_content().strip()

            template = '''
            class {name}:
                """ {title} """
                category = "active"
                description = """{desc}"""
                url = r'{url}'

            '''.format(name=name.replace(' ', '_'), url=url, title=name, desc=desc)

            print(template.lstrip())

            print('"""')
            _test = '//*[@class="table rune-list"]'
            runes = tree.xpath(_test)
            for y in runes:
                rune = y.xpath('table[1]/tbody[1]//*[@class="rune-details"]')  #
                for data in rune:
                    name = data.xpath('h3[1]')
                    print('\t', name[0].text_content())
                    desc = data.xpath('div[2]')
                    print('\t\t', desc[0].text_content())
                    print()
            print('"""')
            print()



        print(total)
        return True

    def get_passives(self):

        from lxml import html
        import requests

        url = r'https://us.diablo3.com/en/class/{}/passive/'.format(self.className)
        print('fetching {}'.format(url))
        page = requests.get(url)
        tree = html.fromstring(page.content)
        _test = '//*[@class="skill-details"]'
        skills = tree.xpath(_test)

        for idx, skill in enumerate(skills):
            title = skill.xpath('h3[1]/a[1]')
            url = r'https://us.diablo3.com/{}'.format(title[0].attrib['href'])

            name = title[0].text_content()

            page = requests.get(url)
            tree = html.fromstring(page.content)

            _test = '//*[@class="skill-desc"]'
            desc = tree.xpath(_test)
            desc = desc[0].text_content().strip()

            part_name = 'passive'

            template = '''
            class {name}:
                """ {title} """
                category = "{part_name}"
                description = """{desc}"""
                url = r'{url}'
    
            '''.format(name=name.replace(' ', '_'), url=url, part_name=part_name, title=name, desc=desc)

            print(template)
        return True


item_template = '''
class {class_name}(Item):
    """ {name} """
    type = '{type}'
    text = """
{text}
    """

'''


class Armour_miner:
    armorTypes = [
        'ring',
        'amulet',
        'helm',
        'shoulders',
        'torso',
        'wrists',
        'hands',
        'waist',
        'pants',
        'feet',
        'phylactery',
        'scythe-1h',
        'scythe-2h',

        # 'jewelry',
        # 'off-hand',
        # 'one-handed',
        # 'two-handed',
        # 'ranged',
    ]

    def __init__(self, className):
        self.className = className
        # break_down & get_skills -> took 22 min

    def get_piece(self, url=r'https://eu.diablo3.com/en/item/tragouls-scales-P6_Necro_Set_2_Chest'):
        req = requests.get(url)
        text = req.text
        # print(text)
        result = re.search(r'<div class="detail-text">((.*\s*)*?)<span class="clear">', text)
        if result:
            # print(result.groups()[0])
            return result.groups()[0]

        # <div class="d3-item-properties">

    def get_set(self):
        return 'https://eu.diablo3.com/en/item/chest-armor/#type=set'

    def get_armor_enums(self, _type='pants'):
        return 'https://us.diablo3.com/en/item/{}/#type=legendary'.format(_type)

    def get_legendaries(self):
        # <li><a href="javascript:;" data-type="legendary">Legendary (14)</a></li>

        for part in self.armorTypes:
            print(part)
            url = 'https://us.diablo3.com/en/item/{}/#type=legendary'.format(part)
            print(url)
            req = requests.get(url)
            text = req.text
            print(bool(text))
            result = re.search(r'table db-table db-table-padded((.*\s*)*?)</table>', text)
            if result:
                print('in it')
                print(result)
                print(len(result.groups()))
                # print(result.groups()[0])
                body = result.groups()[0]
                print(len(body))
                # print(body)
                for idx, piece in enumerate(re.findall(r'<tr class="row.(.*)? legendary"((.*\s*)*?)</tr>', body)):
                    print(idx + 1)
                    print(piece[1])

                    # <ul class="item-effects">
            break
        return True

    def get_items(self):
        from lxml import html
        import requests

        for part in self.armorTypes:
            # print(part)
            url = 'https://us.diablo3.com/en/item/{}/#type=legendary'.format(part)
            # print(url)
            page = requests.get(url)
            tree = html.fromstring(page.content)

            _test = '//*[@class="item-details-text"]'
            legendaries = tree.xpath(_test)
            total = 0
            for x in legendaries:
                title = x.xpath('h3[1]/a[1]/text()')
                _type = x.xpath('div[1]/*[@class="item-type"]/li[1]/span[1]/text()')[0]  # /li[1]/span[1]/text()
                secondary = x.xpath('div[1]/*[@class="item-effects"]/*[.="Secondary"]/../span')


                item = False
                if secondary and 'Legendary ' in _type:
                    name = title[0]
                    text = '\n'.join(['\t' + y.text_content() for y in secondary])
                    # print('secondary', secondary)
                    # for y in secondary:
                    #     print('\t', y.text_content())  # , '->', y.attrib)
                    # print()
                    # print()
                    total += 1
                    item = True

                itemset = x.xpath('div[1]/*[@class="item-itemset"]/span')
                if itemset and 'Set ' in _type:
                    name = title[0]
                    text = '\n'.join(['\t' + y.text_content() for y in itemset])
                    # for y in itemset:
                    #     print('\t', y.text_content())  # , '->', y.attrib)
                    # print()
                    # print()
                    total += 1
                    item = True

                if item:
                    print(item_template.format(class_name=re.sub(r"[- ]", '_', re.sub(r"['.]", '', name)), name=name, type=part, text=text))

            # print(total)

    def get_gems(self):
        from lxml import html
        import requests

        url = 'https://us.diablo3.com/en/item/gem/'
        print(url)
        page = requests.get(url)
        tree = html.fromstring(page.content)

        # //*[@id="grid-items"]/div[2]/div[1]/div[18]
        _test = '//*[@class="data-cell"]'
        legendaries = tree.xpath(_test)
        total = 0
        for x in legendaries:
            print(x.attrib)
            # title = x.xpath('h3[1]/a[1]/text()')
            # _type = x.xpath('div[1]/*[@class="item-type"]/li[1]/span[1]/text()')[0]  # /li[1]/span[1]/text()
            # secondary = x.xpath('div[1]/*[@class="item-effects"]/*[.="Secondary"]/../span')
            # itemset = x.xpath('div[1]/*[@class="item-itemset"]/span')
            #
            # if secondary and 'Legendary ' in _type:
            #     print(title[0])
            #     for y in secondary:
            #         print('\t', y.text_content())  # , '->', y.attrib)
            #     print()
            #     print()
            #     total += 1
            # if itemset and 'Set ' in _type:
            #     print(title[0])
            #     for y in itemset:
            #         print('\t', y.text_content())  # , '->', y.attrib)
            #     print()
            #     print()
            #     total += 1


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


helm = Gear(1)
# shoulders = Gear(1)
torso = Gear(3)
# wrists = Gear(1)
# hands = Gear(1)
# waist = Gear(0)
pants = Gear(2)
# feet = Gear(1)

amulet = Gear(1)
ring_left_hand = Gear(1)
ring_right_hand = Gear(1)

main_hand = Gear(1)
off_hand = Gear(1)

import copy

totalGems = 0


# 15 * 280 = 4200

class Gem:
    def __init__(self, type):
        pass

    @property
    def max(self):
        return Intel(280)


import enum


class Classes(enum.Enum):
    BARBARIAN = 'barbarian'
    NECROMANCER = 'necromancer'
    WIZARD = 'wizard'


def get_part_from_url(url=''):
    print(url)

    from lxml import html
    import requests

    page = requests.get(url)
    tree = html.fromstring(page.content)

    # /html/body/div[4]/div/div[2]/div[1]/div/div[1]/h2/a

    _test = '//*[@class="page-header page-header-db"]'
    skills = tree.xpath(_test)
    total = 0

    title = skills[0].xpath('h2[1]/a[1]')
    title = title[0].text_content().strip()

    subtitle = skills[0].xpath('h2[1]/small[1]')
    subtitle = subtitle[0].text_content().strip()

    _test = '//*[@class="detail-text"]'
    skills = tree.xpath(_test)
    part_name = skills[0].xpath('h2[1]')

    part_name = part_name[0].text_content().strip()

    template = '''
    class {part}(Item):
        """ {title} """
        type = '{title}'
        name = "{part_name}"
        url = r'{url}'

    '''.format(part=subtitle, url=url, part_name=part_name, title=title)

    return template



# barbarian.get_items()

# lol, todo: this teaches accountantcy

# https://www.ign.com/wikis/diablo-3/Necromancer_Sets

# https://www.reddit.com/r/diablo3/comments/bagr92/fastest_way_to_farm_blood_shards/

# https://www.icy-veins.com/d3/how-to-farm-legendary-and-set-items-guide


if __name__ == '__main__':
    if False:
        for name, cls in copy.copy(globals()).items():
            if isinstance(cls, Gear):
                print(name, cls)
                totalGems += cls.gemSlots
        print(totalGems)
        print(totalGems * 280)

    barbarian = Armour_miner(Classes.BARBARIAN.value)
    # print(Class_Info(Classes.BARBARIAN.value).get_skills())

    barbarian.get_items()

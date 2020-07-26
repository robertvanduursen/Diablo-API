"""

Diablo webscraping utils

"""

import inspect, os
import requests, re
from datatypes import Classes


class Class_Info:
    def __init__(self, className):
        self.className = className
        # break_down & get_skills -> took 22 min

        # check whether the cache folder exists
        self.root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..\classes'))
        os_name = self.className.os_name
        if os_name not in os.listdir(self.root_folder):
            print('not found, creating {} folder'.format(os_name))
            os.mkdir(os.path.join(self.root_folder, os_name))

        self.root_folder = os.path.join(self.root_folder, os_name)

    def get_active_skills(self, save=False):
        from lxml import html
        import requests

        lines = []
        lines.append('""" {} active skills """'.format(self.className))

        lines.append('from datatypes import Active')
        lines.append('from datatypes import Rune')

        url = r'https://us.diablo3.com/en/class/{}/active/'.format(self.className.internet)
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

            rune_template = '''
            class {name}(Rune):
                """ {title} """
                description = """{desc}"""
            '''

            # RUNES
            rune_names = []
            # print('"""')
            _test = '//*[@class="table rune-list"]'
            runes = tree.xpath(_test)
            for y in runes:
                rune = y.xpath('table[1]/tbody[1]//*[@class="rune-details"]')  #
                for data in rune:
                    rune_name = data.xpath('h3[1]')
                    rune_name = rune_name[0].text_content()
                    # print('\t', rune_name[0].text_content())
                    rune_desc = data.xpath('div[2]')
                    rune_desc = rune_desc[0].text_content()
                    # print('\t\t', rune_desc[0].text_content())
                    # print()
                    rune_cls_name = re.sub(r"[-! ]", '_', re.sub(r"['.]", '', rune_name))
                    rune_names.append(rune_cls_name)
                    lines.append(rune_template.format(name=rune_cls_name, title=rune_name, desc=rune_desc).lstrip())
            # print('"""')
            # print()

            skill_class_name = re.sub(r"[-! ]", '_', re.sub(r"['.]", '', name))
            print('fetching {}'.format(skill_class_name))
            template = '''
            class {name}(Active):
                """ {title} """
                category = "active"
                description = """{desc}"""
                url = r'{url}'
                runes = [{runes}]

            '''.format(name=skill_class_name, url=url, title=name, desc=desc, runes=','.join(rune_names))

            lines.append(template.lstrip())

        print(total)

        if save:
            with open(os.path.join(self.root_folder, 'skills.py'), 'w') as skills_file:
                skills_file.write('\n'.join(lines))
            print("{} saved at {}".format('skills.py', self.root_folder))

    def get_passives(self, save=False):

        from lxml import html
        import requests

        url = r'https://us.diablo3.com/en/class/{}/passive/'.format(self.className.internet)
        print('fetching {}'.format(url))
        page = requests.get(url)
        tree = html.fromstring(page.content)
        _test = '//*[@class="skill-details"]'
        skills = tree.xpath(_test)

        lines = []
        lines.append('from datatypes import Passive')

        for idx, skill in enumerate(skills):
            title = skill.xpath('h3[1]/a[1]')
            url = r'https://us.diablo3.com/{}'.format(title[0].attrib['href'])

            name = title[0].text_content()
            print('fetching {}'.format(name))
            page = requests.get(url)
            tree = html.fromstring(page.content)

            _test = '//*[@class="skill-desc"]'
            desc = tree.xpath(_test)
            desc = desc[0].text_content().strip()

            part_name = 'passive'
            passive_class_name = re.sub(r"[- ]", '_', re.sub(r"['.]", '', name))

            template = '''
            class {name}(Passive):
                """ {title} """
                category = "{part_name}"
                description = """{desc}"""
                url = r'{url}'
    
            '''.format(name=passive_class_name, url=url, part_name=part_name, title=name, desc=desc)

            lines.append(template.lstrip())

        if save:
            with open(os.path.join(self.root_folder, 'passives.py'), 'w') as passives_file:
                passives_file.write('\n'.join(lines))
            print("{} saved at {}".format('passives.py', self.root_folder))


armour_set_template = '''
class {class_name}(Set):
    """ {name} """
    _class = {_class}
    items = list
    levels = {levels}
    pieces = {pieces}
    parts = {parts}
    size = {size}
'''

item_template = '''
class {class_name}(Item):
    """ {name} """
    url = r'{url}'
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
        'crusader-shield',
        'shield',

        # 'jewelry',
        # 'off-hand',
        # 'one-handed',
        # 'two-handed',
        # 'ranged',
    ]

    weaponTypes = [
        'axe-1h',
        'mighty-weapon-1h',
        'mace-1h',
        'sword-1h',
        'flail-1h',
        'spear',
        'dagger',

        'axe-2h',
        'mighty-weapon-2h',
        'flail-2h',
        'mace-2h',
        'sword-2h',
        'polearm',
        'staff',
    ]

    def __init__(self, className=False):
        if className:
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
                item_url = x.xpath('h3[1]/a[1]')[0].attrib['href']
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
                    print(item_template.format(class_name=re.sub(r"[- ]", '_', re.sub(r"['.]", '', name)), name=name,
                                               type=part, text=text, url=item_url))

    def get_weapons(self):
        from lxml import html
        import requests

        for part in self.weaponTypes:
            # print(part)
            url = 'https://us.diablo3.com/en/item/{}/#type=legendary'.format(part)
            # print(url)
            page = requests.get(url)
            tree = html.fromstring(page.content)

            _test = '//*[@class="item-details-text"]'
            legendaries = tree.xpath(_test)
            total = 0
            for x in legendaries:
                item_url = x.xpath('h3[1]/a[1]')[0].attrib['href']
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
                    print(item_template.format(class_name=re.sub(r"[- ]", '_', re.sub(r"['.,]", '', name)), name=name,
                                               type=part, text=text, url=item_url))

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

    def get_armor_sets(self, save=False):
        from lxml import html
        import requests

        # G:\projects\Diablo-API\module\d3api\data\armor_sets.py

        armor_dict = {}  # cache and lookup

        for part in self.armorTypes:
            print("fetching {}".format(part))
            url = 'https://us.diablo3.com/en/item/{}/#type=set'.format(part)

            page = requests.get(url)
            tree = html.fromstring(page.content)

            _test = '//*[@class="item-details-text"]'
            armor_sets = tree.xpath(_test)

            for x in armor_sets:
                pieces = []
                item_url = x.xpath('h3[1]/a[1]')[0].attrib['href']

                _type = x.xpath('div[1]/*[@class="item-type"]/li[1]/span[1]/text()')[0]
                itemset = x.xpath('div[1]/*[@class="item-itemset"]/span')

                if itemset and 'Set ' in _type:

                    # now actually go to the page for the armor set breakdown
                    set_url = 'https://us.diablo3.com/{}'.format(item_url)
                    page = requests.get(set_url)
                    tree = html.fromstring(page.content)

                    restricted = tree.xpath('//*[@class="item-class-specific d3-color-white"]')
                    if restricted:
                        restricted = restricted[0].text_content().strip()
                        # print("{} Only".format(restricted))
                    else:
                        restricted = False

                    # set_part = tree.xpath('//*[@class="item-slot"]')
                    # if set_part:
                    #     print("part = {}".format(set_part[0].text_content().strip()))

                    _test = '//*[@class="item-itemset"]'
                    armor_parts = tree.xpath(_test)
                    item_set_desc = armor_parts[0]
                    bits = item_set_desc.xpath('li')
                    name = re.sub(r"[\xc3\xa2|\x80\x99|\xe2\x80\x99]", "'", bits[0].text_content().strip())
                    parts = []
                    for x in bits[1:]:
                        parts += [x.text_content().strip()]

                    levels = []
                    for y in itemset:
                        level = y.text_content().strip()
                        levels += [level[level.find(' Set:') + 6:].strip()]

                    armor_dict[name] = (parts, levels, pieces, restricted)

        print('armor_dict', len(armor_dict))
        for item in armor_dict.items():
            print(item)

        if save:
            lines = [
                '"""" this is an auto-generated file"""',
                'from datatypes import Item, Set, Set_Item',
                'from datatypes import Head, Hands, Torso, Waist, Legs, Feet, Shoulders'
            ]
            for name, (parts, levels, pieces, restricted) in armor_dict.items():
                levels = dict(zip([2, 4, 6], levels))
                lines.append(
                    armour_set_template.format(class_name=re.sub(r"[- ]", '_', re.sub(r"['.]", '', name)), name=name,
                                               parts=parts, levels=str(levels).replace("',", "',\n"),
                                               _class='"{}"'.format(restricted) if restricted else None,
                                               size=len(parts), pieces=[]))

            root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..\data'))
            with open(os.path.join(root_folder, 'armor_sets.py'), 'w') as passives_file:
                passives_file.write('\n'.join(lines))
            print("{} saved at {}".format('armour_sets.py', root_folder))


if __name__ == '__main__':
    if 0:
        for name, cls in copy.copy(globals()).items():
            if isinstance(cls, Gear):
                print(name, cls)
                totalGems += cls.gemSlots
        print(totalGems)
        print(totalGems * 280)

    # barbarian = Armour_miner(Classes.CRUSADER.value)
    # barbarian.get_items()

    # Class_Info(Classes.DEMON_HUNTER).get_passives(save=True)
    # Class_Info(Classes.DEMON_HUNTER).get_active_skills(save=True)

    Armour_miner().get_armor_sets(save=True)

"""

Diablo playstyle


"""

'''

Necromancer

'''

import requests, re


class Class_Info:
    def __init__(self, className):
        self.className = className
        # break_down & get_skills -> took 22 min

    def getInfo(self):
        self.break_down(r'https://us.diablo3.com/en/class/{}/active/'.format(self.className))
        self.break_down(r'https://us.diablo3.com/en/class/{}/passive/'.format(self.className))

    def get_skills(self, url = r'https://us.diablo3.com/en/class/necromancer/active/'):
        req = requests.get(url)
        text = req.text
        # print(text)
        result = re.search(r'table db-table db-table-padded((.*\s*)*?)</table>', text)
        if result:
            # print(result.groups()[0])
            return result.groups()[0]

    def break_down(self, url):
        text = self.get_skills(url)
        for nr, match in enumerate(re.findall(r'<tr class=((.*\s*)*?)</tr>', text)):
            tableRow = match[0]

            # print(nr)
            name, category, description = '', '', ''
            found = re.search(r'<h3 class="subheader-3"((.*\s*)*?)</h3>', tableRow)
            if found:
                links = re.findall(r'<a href=.*?>(.*)?</a>', found.groups()[0], re.M)
                for link in links:
                    name = link

            links = re.findall(r'<div class="skill-category">(.*)?</div>', tableRow, re.M)
            for link in links:
                category = link

            links = re.findall(r'<div class="skill-description">(.*)?</div>', tableRow, re.S)
            for link in links:
                description = re.sub(r'(<.*?>)', '', link).strip()
            # print()

            print("""
            class {}:
                name = "{}"
                category = "{}"
                description = '''{}'''
    
            """.format(name.replace(' ','_'),name, category , description))

Class_Info('necromancer')


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

    def get_piece(self, url = r'https://eu.diablo3.com/en/item/tragouls-scales-P6_Necro_Set_2_Chest'):
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
        #<li><a href="javascript:;" data-type="legendary">Legendary (14)</a></li>

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

                    #<ul class="item-effects">
            break
        return True

    def get_items(self):
        from lxml import html
        import requests

        for part in self.armorTypes:
            print(part)
            url = 'https://us.diablo3.com/en/item/{}/#type=legendary'.format(part)
            print(url)
            page = requests.get(url)
            tree = html.fromstring(page.content)

            _test = '//*[@class="item-details-text"]'
            legendaries = tree.xpath(_test)
            total = 0
            for x in legendaries:
                title = x.xpath('h3[1]/a[1]/text()')
                _type = x.xpath('div[1]/*[@class="item-type"]/li[1]/span[1]/text()')[0]  # /li[1]/span[1]/text()
                secondary = x.xpath('div[1]/*[@class="item-effects"]/*[.="Secondary"]/../span')
                itemset = x.xpath('div[1]/*[@class="item-itemset"]/span')

                if secondary and 'Legendary ' in _type:
                    print(title[0])
                    for y in secondary:
                        print('\t', y.text_content())  # , '->', y.attrib)
                    print()
                    print()
                    total += 1
                if itemset and 'Set ' in _type:
                    print(title[0])
                    for y in itemset:
                        print('\t', y.text_content())  # , '->', y.attrib)
                    print()
                    print()
                    total += 1

            print(total)

    def get_gems(self):
        from lxml import html
        import requests

        url = 'https://us.diablo3.com/en/item/gem/'
        print(url)
        page = requests.get(url)
        tree = html.fromstring(page.content)

        #//*[@id="grid-items"]/div[2]/div[1]/div[18]
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
for name, cls in copy.copy(globals()).items():
    if isinstance(cls, Gear):
        print(name, cls)
        totalGems += cls.gemSlots
print(totalGems)
print(totalGems * 280)

# 15 * 280 = 4200

class Gem:
    def __init__(self, type):
        pass

    @property
    def max(self):
        return Intel(280)




Armour_miner('necromancer').get_gems()
# Armour_miner('necromancer').get_items()

# lol, todo: this teaches accountantcy

# https://www.ign.com/wikis/diablo-3/Necromancer_Sets

# https://www.reddit.com/r/diablo3/comments/bagr92/fastest_way_to_farm_blood_shards/

# https://www.icy-veins.com/d3/how-to-farm-legendary-and-set-items-guide
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
        'helm',
        'shoulders',
        'torso',
        'wrists',
        'hands',
        'waist',
        'pants',
        'feet',
        'jewelry',
        'off-hand',
        'follower-special',

        'one-handed',
        'two-handed',
        'ranged',
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

    def test_xpath(self):

        #/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div/table/tbody/tr[1]/td[1]/div/div[2]/div/ul[2]/span[4]

        url = 'https://us.diablo3.com/en/item/{}/#type=legendary'.format('ring')
        print(url)
        req = requests.get(url)
        text = req.text




        import io
        print(req.encoding)
        sio = io.BytesIO(req.content)
        #https://stackoverflow.com/questions/11914472/stringio-in-python3

        # print(sio.getvalue().decode(req.encoding))
        for idx, x in enumerate(sio.getvalue().decode(req.encoding).split('\n')):
            print(idx, x)
        # print(sio.getvalue().decode('utf8'))

        ignore_encoding = lambda s: s.decode(req.encoding, 'ignore')

        #.decode('utf8').encode('ascii')
        # sio = r'C:\Users\rober\Desktop\necroTest.html'
        #sio = io.BytesIO(sio.getvalue())
        # from xml.etree import ElementTree as etree
        # parser = etree.XMLParser(recover=True)
        # root = etree.fromstring(text, parser=parser)

        from lxml import etree
        # from xml import etree
        parser = etree.XMLParser(recover=True)
        root = etree.fromstring(text, parser=parser)

        # import xml.etree.cElementTree as ET
        # root = ET.parse(sio)
        result = ''
        for elem in root.findall(r'//*[@id="table-items"]/div[2]/div/table/tbody/tr[1]/td[1]/div/div[2]/div/ul[2]/span[4]'):
            # How to make decisions based on attributes even in 2.6:
            if elem.attrib.get('name') == 'foo':
                result = elem.text
                print(result)
                break



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




Armour_miner('necromancer').test_xpath()

# lol, todo: this teaches accountantcy

# https://www.ign.com/wikis/diablo-3/Necromancer_Sets

# https://www.reddit.com/r/diablo3/comments/bagr92/fastest_way_to_farm_blood_shards/

# https://www.icy-veins.com/d3/how-to-farm-legendary-and-set-items-guide
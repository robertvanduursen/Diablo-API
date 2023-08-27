"""

Main entry point

"""
import requests, re
from lxml import html


def get_characters_urls_from_profile(profile_url: str):
    """
    get the list of active characters from a profile
    :returns list of tuples -> (name , ID)
    """

    characters_ids = []

    page = requests.get(profile_url)
    tree = html.fromstring(page.content)

    _test = '//*[@class="hero-tabs MediaCarousel-scroll"]'
    chars = tree.xpath(_test)
    char_name = False
    char_code = False
    if chars:
        for char in chars[0].xpath('li'):
            profile_nr = char.xpath('a[1]')
            if profile_nr:
                char_code = profile_nr[0].attrib['href']
                for x in profile_nr[0].xpath('span[@class="name"]'):
                    char_name = x.text_content().strip()

            characters_ids.append((char_name, '{}/hero/{}'.format(profile_url, char_code)))

    return set(characters_ids)


def get_char_profile(char_url=r"https://eu.diablo3.com/en/profile/Ralicx-2273/hero/133589041"):
    print(char_url)

    from lxml import html
    import requests
    import os

    # if we got a downloaded webpage, use that
    cache_name = "barbi.html"
    expected_path = os.path.join(os.path.dirname(__file__), cache_name)
    if os.path.exists(expected_path):
        print("using cache")
        with open("barbi.html", "rb") as page_cache:
            page = page_cache.read()
    else:
        page = requests.get(char_url).content
        #     recache
        with open("barbi.html", "wb") as page_cache:
            page_cache.write(page)

    tree = html.fromstring(page)
    _test = '//*[@class="profile-sheet"]'

    profile = tree.xpath(_test)
    total = 0

    character_obj = {}

    classType = profile[0].xpath('h2[1]/a[1]/span[1]')
    classType = classType[0].text_content().strip().split("\n")[-1].strip()
    character_obj['classType'] = classType

    classLvl = profile[0].xpath('h2[1]/a[1]/span[1]/strong[1]')

    classLvl = classLvl[0].text.strip()
    # print(f"classLvl = {classLvl}")
    character_obj['level'] = classLvl

    title = profile[0].xpath('h2[1]//*[@class="paragon-level"]')
    title = title[0].text_content().strip()
    # print(f"title = {title}")
    character_obj['title'] = title

    name = profile[0].xpath('h2[2]')
    name = name[0].text_content().strip()
    # print(f"name = {name}")
    character_obj['name'] = name

    _test = '//*[@class="page-section attributes"]'
    attrs = tree.xpath(_test)

    core_attrs = attrs[0].xpath('//*[@class="attributes-core"]')
    core_attrs = core_attrs[0].text_content().strip()
    d = core_attrs.split()
    character_obj['core_attrs'] = dict(zip(d[::2], d[1::2]))

    core_attrs = attrs[0].xpath('//*[@class="attributes-core secondary"]')
    core_attrs = core_attrs[0].text_content().strip()
    d = core_attrs.split()
    character_obj['sec_attrs'] = dict(zip(d[::2], d[1::2]))

    _test = '//*[@class="skills-wrapper"]'
    skills = tree.xpath(_test)

    active_skills = skills[0].xpath('//*[@class="active-skills clear-after"]')
    skills_to_parse = []
    for x in active_skills[0].getchildren():
        x = x.text_content().strip().split('\n')
        x = [x.strip() for x in x]
        x = [x for x in x if x != '']
        d = dict(zip(('name','rune'), x[-7:-5]))
        skills_to_parse.append(d)

    character_obj['active_skills'] = skills_to_parse

    passive_skills = skills[0].xpath('//*[@class="passive-skills clear-after"]')
    passive_skills = [x.text_content().strip() for x in passive_skills[0].getchildren()]
    character_obj['passive_skills'] = passive_skills


    # gear slots
    gear_slots = []

    _test = '//*[@class="gear-slots"]'
    gear = tree.xpath(_test)
    print(gear[0])
    slots = gear[0].xpath('li')
    for slot in slots:
        # print(slot.attrib)
        stats = slot.xpath('a[1]')
        if stats:
            part = slot.attrib['class']
            # print(stats[0].attrib)#['class']
            url = stats[0].attrib['href']

            gear_slots.append((part, url))
        # print(x)#active_skills[0].text_content().strip())

    character_obj['gear_slots'] = gear_slots
    # write this to a save file
    saves_folder = r"G:\Diablo-API\module\d3api\saves"
    if os.path.splitext(cache_name)[0] not in os.listdir(saves_folder):
        # save it
        with open(os.path.join(saves_folder, 'test.json'), 'w') as save_file:
            import json
            json.dump(character_obj, save_file, indent=2)


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


if __name__ == '__main__':
    downloading = 0
    if downloading:
        my_profile = r'https://eu.diablo3.com/en/profile/Ralicx-2273/'
        my_chars = dict(get_characters_urls_from_profile(my_profile))
        print(my_chars)
        char_profile = get_char_profile(my_chars['Smitina'])

    else:
        char_profile = get_char_profile()

    # lol, todo: this teaches accountancy

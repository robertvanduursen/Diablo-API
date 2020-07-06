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

    page = requests.get(char_url)
    tree = html.fromstring(page.content)

    _test = '//*[@class="profile-sheet"]'

    profile = tree.xpath(_test)
    total = 0

    classType = profile[0].xpath('h2[1]/a[1]/strong[1]')
    classType= classType[0].text_content().strip()
    print(classType)

    classLvl = profile[0].xpath('h2[1]/a[1]/span[1]/strong[1]')
    classLvl = classLvl[0].text.strip()
    print(classLvl)

    title = profile[0].xpath('h2[1]//*[@class="paragon-level"]')
    title = title[0].text_content().strip()
    print(title)

    name = profile[0].xpath('h2[2]')
    name = name[0].text_content().strip()
    print(name)


    _test = '//*[@class="page-section attributes"]'
    attrs = tree.xpath(_test)

    core_attrs = attrs[0].xpath('//*[@class="attributes-core"]')
    core_attrs = core_attrs[0].text_content().strip()
    print(core_attrs)

    core_attrs = attrs[0].xpath('//*[@class="attributes-core secondary"]')
    core_attrs = core_attrs[0].text_content().strip()
    print(core_attrs)



    _test = '//*[@class="skills-wrapper"]'
    skills = tree.xpath(_test)

    active_skills = skills[0].xpath('//*[@class="active-skills clear-after"]')
    active_skills = active_skills[0].text_content().strip()
    print(active_skills)


    passive_skills = skills[0].xpath('//*[@class="passive-skills clear-after"]')
    passive_skills = passive_skills[0].text_content().strip()
    print(passive_skills )


    # gear slots
    _test = '//*[@class="gear-slots"]'
    gear = tree.xpath(_test)
    print(gear[0])
    slots = gear[0].xpath('li')
    for slot in slots:
        # print(slot.attrib)
        stats = slot.xpath('a[1]')
        if stats:
            print(slot.attrib)
            # print(stats[0].attrib)#['class']
            print(stats[0].attrib['href'])
        # print(x)#active_skills[0].text_content().strip())


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


if __name__ != '__main__':
    my_profile = r'https://eu.diablo3.com/en/profile/Ralicx-2273/'
    my_chars = dict(get_characters_urls_from_profile(my_profile))

    char_profile = get_char_profile(my_chars['Burla'])

    # lol, todo: this teaches accountantcy

"""

Xpath scraping

"""

from lxml import html
import requests

'''
22/04/2020 08:31
notes:
    element index is base 1 -> i.e. div[1]

'''

page = requests.get("https://us.diablo3.com/en/item/ring/#type=legendary")
tree = html.fromstring(page.content)

_test = '//*[@class="item-details-text"]'
legendaries = tree.xpath(_test)  # + '/text()')
total = 0
for x in legendaries:
    title = x.xpath('h3[1]/a[1]/text()')
    _type = x.xpath('/*[@class="item-type"]') # /li[1]/span[1]/text()
    print('_type', _type)
    # secondary = x.xpath('div[1]/*[@class="item-effects"]/*[@class="d3-color-ffff8000"]')
    secondary = x.xpath('div[1]/*[@class="item-effects"]/*[.="Secondary"]/../span')
    if secondary:
        print(title)
        for y in secondary:
            print(y.text_content())#, '->', y.attrib)
        print()
        total += 1

print(total)
# <p class="item-property-category">Secondary</p>
# todo: could just simply scrape all the items effects, if the amount of intel trumps the effect

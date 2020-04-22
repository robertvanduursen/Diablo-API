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
buyers = tree.xpath(_test)  # + '/text()')
print(buyers)
print(len(buyers))
for x in buyers:
    title = x.xpath('h3[1]/a[1]/text()')
    secondary = x.xpath('div[1]/*[@class="item-effects"]/*[@class="d3-color-ffff8000"]')
    if secondary:
        print(title)
        print(secondary[0].text_content())
        print()

# todo: could just simply scrape all the items effects, if the amount of intel trumps the effect

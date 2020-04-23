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
legendaries = tree.xpath(_test)
total = 0
for x in legendaries:
    title = x.xpath('h3[1]/a[1]/text()')
    _type = x.xpath('div[1]/*[@class="item-type"]/li[1]/span[1]/text()')[0] # /li[1]/span[1]/text()
    secondary = x.xpath('div[1]/*[@class="item-effects"]/*[.="Secondary"]/../span')
    itemset = x.xpath('div[1]/*[@class="item-itemset"]/span')

    if secondary and _type == 'Legendary Ring':
        print(title[0])
        for y in secondary:
            print('\t',y.text_content())#, '->', y.attrib)
        print()
        print()
        total += 1
    if itemset and _type == 'Set Ring':
        print(title[0])
        for y in itemset:
            print('\t', y.text_content())  # , '->', y.attrib)
        print()
        print()
        total += 1

print(total)

# todo: could just simply scrape all the items effects, if the amount of intel trumps the effect

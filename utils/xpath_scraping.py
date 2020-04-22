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
buyers = tree.xpath(_test)## + '/text()')
print(buyers)
print(len(buyers))
for x in buyers:
    # print(x)
    # print(x.xpath('//*[@class="item-effects"]/span[1]/text()'))
    #[0].attrib
    title = x.xpath('h3[1]/a[1]/text()')

    secondary = x.xpath('div[1]/*[@class="item-effects"]/span[3]')
    if secondary:
        print(title)
        print(secondary[0].text)
        print()

# todo:

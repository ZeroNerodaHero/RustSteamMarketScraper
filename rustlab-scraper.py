import requests
from lxml import html

def scrape_item(item_name):
    URL = 'https://rustlabs.com/item/{}#tab=skins'.format(item_name)
    page = requests.get(URL)
    
    tree = html.fromstring(page.content)
    name = tree.xpath('//span[@class="name"]/text()')

    return name

item_types = ["attire","construction","item","tools","weapons"]

#print(scrape_item("assault-rifle"))

for item_type in item_types:
    file_loc = 'storedata/typenames/{}'.format(item_type)
    file_read = open(file_loc,"r")
    
    item_names = file_read.readlines()
    
    for item_name in item_names:
        item_name = item_name.rstrip()
        skin_names = scrape_item(item_name)

        file_loc = 'storedata/{}_skins/{}'.format(item_type,item_name)
        print(file_loc)
        file_out =  open(file_loc,"w+")

        for skin in skin_names:
            file_out.write(skin+'\n')    

import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime
import time
import os

#add your steamLoginSecure Here
cookie = {'steamLoginSecure': 'steamLoginSecureExample111111111'};
game_id = '252490'

def getPriceHistory(skin_name, saveloc):
    market_info = pd.DataFrame(columns = ['time','price','volume'])

    url_final = 'http://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid={}&market_hash_name={}'.format(game_id,skin_name)
    #url_final = url_final.replace(' ','%20')
    #url_final = url_final.replace('&','%26')

    item_page = requests.get(url_final,cookies=cookie)
    item_page = item_page.content
    item_page = json.loads(item_page)

    if item_page:
        item_data = item_page['prices']
        if item_data:
            item_date = []
            item_price = []
            item_volume = []

            for day in item_data:
                if type(day) is list:
                    item_date.append(day[0])
                    item_price.append(day[1])
                    item_volume.append(day[2])

            market_info['time'] = item_date 
            market_info['price'] = item_price
            market_info['volume'] = item_volume

    market_info.to_csv(saveloc)

item_types = ["attire","construction","item","tools","weapons"]

for item_type in item_types:
    file_loc = 'storedata/typenames/{}'.format(item_type)
    file_read = open(file_loc,"r")
    
    item_names = file_read.readlines()

    for item_name in item_names:
        item_name = item_name.rstrip()

        file_loc = 'storedata/{}_skins/{}'.format(item_type,item_name)
        skin_read = open(file_loc,"r")

        skin_names = skin_read.readlines()

        for skin_name in skin_names:
            skin_name = skin_name.rstrip()
            if(not os.path.exists('pricehistorydata/{}/{}'.format(item_type,item_name))):
                os.mkdir('pricehistorydata/{}/{}'.format(item_type,item_name))
            saveloc = 'pricehistorydata/{}/{}/{}.csv'.format(item_type,item_name,skin_name)
            saveloc = saveloc.replace(' ','_')
            print(saveloc)
            getPriceHistory(skin_name, saveloc) 
            time.sleep(1)

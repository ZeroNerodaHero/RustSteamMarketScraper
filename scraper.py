import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime
import time
import os

#add your steamLoginSecure Here
cookie = {'steamLoginSecure': '76561198237213828%7C%7C6A05F981719AAB2020DEEEFD7EFD92C13863D740'}
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

#there is no elegant solution if you don't know anything
file_error = open('storedata/error.txt',"r+")
error_type = file_error.readline().rstrip()
error_itemtype = file_error.readline().rstrip()
error_skin = file_error.readline().rstrip()
flag_et = flag_it = flag_sk = False
if(error_type == '.'):
    flag_et = flag_it = flag_sk = True
    

for item_type in item_types:
    print(item_type + error_type)
    if(error_type == item_type):
        flag_et = True
    if(flag_et == False):
        continue
    
    file_loc = 'storedata/typenames/{}'.format(item_type)
    file_read = open(file_loc,"r")
    
    item_names = file_read.readlines()
    

    for item_name in item_names:
        item_name = item_name.rstrip()
        if(item_name == error_itemtype):
            flag_it = True
        if(flag_it == False):
            continue

        file_loc = 'storedata/{}_skins/{}'.format(item_type,item_name)
        skin_read = open(file_loc,"r")

        skin_names = skin_read.readlines()

        for skin_name in skin_names:
            skin_name = skin_name.rstrip()
            if(skin_name == error_skin):
                flag_sk = True
            if(flag_sk == False):
                continue;

            if(not os.path.exists('pricehistorydata/{}/{}'.format(item_type,item_name))):
                os.mkdir('pricehistorydata/{}/{}'.format(item_type,item_name))
            saveloc = 'pricehistorydata/{}/{}/{}.csv'.format(item_type,item_name,skin_name)
            saveloc = saveloc.replace(' ','_')
            print(saveloc)
            getPriceHistory(skin_name, saveloc) 

            #empties file dunno how to do error handling
            file_error.seek(0)
            file_error.truncate()
            file_error.write(item_type + '\n'+
                             item_name + '\n' + skin_name)
            time.sleep(1)

file_error.write('.\n.\n.\n')

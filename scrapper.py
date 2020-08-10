import requests
import json
#import pickles
import pandas as pd
import numpy as np
from datetime import datetime
import time


cookie = {'steamLoginSecure': '76561198237213828%7C%7C3A7E1F7308CC478247B804AF6251DBEC27F005B2'};
game_id = '252490'
item_name = 'BURNOUT'

market_info = pd.DataFrame(columns = ['time','price','volume'])
csv_loc = "csv_test/{}".format(item_name)

url_final = 'http://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid={}&market_hash_name={}'.format(game_id,item_name)
url_final.replace(' ','%20')
url_final.replace('&','%26')

item_page = requests.get(url_final,cookies=cookie)
item_page = item_page.content
item_page = json.loads(item_page)

if item_page:
    item_data = item_page['prices']
    #print(item_data)
    if item_data:
        item_date = []
        item_price = []
        item_volume = []

        for day in item_data:
            #print(day)
            if type(day) is list:
                item_date.append(day[0])
                item_price.append(day[1])
                item_volume.append(day[2])

        market_info['time'] = item_date 
        market_info['price'] = item_price
        market_info['volume'] = item_volume

market_info.head()
market_info.to_csv(csv_loc)

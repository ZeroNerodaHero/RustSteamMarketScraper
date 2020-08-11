### RustSteamMarketScraper
The main point of this rep is the price history of indiviual skins. It includes all the available skins minus the fun/holiday skins. The original code for the dataset is also included. One named rustlab-scraper.py is used to grab all the skinnable items and the steam-market-history-scraper.py is used to get the price history. 

The price history is split into three fields.

| Name   | Description                                         |
|--------|-----------------------------------------------------|
| time   | The date and time of the item's index               |
| price  | The median price that the item was sold             |
| volume | The amount of the items sold during the time period |

You can run them yourself if you want to update the dataset alone. The python files have few external libraries that need to be downloaded. The rustlab-scraper.py can be ran without any hassle but in order to run the steam-market-history-scraper.py, you will need to add your steamLoginSecure cookie. Also take in mind that updating may take a few minutes(like 30 minutes).

```
cookie = {'steamLoginSecure': 'get the cookie of this exact name'};
```

On a side note, the code should work too if you want to extend it beyond Rust. Change the game id to match the game. For example, CSGO's id is 730. You can find the id of the game through the steam store.

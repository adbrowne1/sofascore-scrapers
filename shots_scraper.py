import csv
from bs4 import BeautifulSoup
import requests
import json
import numpy
import pandas as pd


# Send an HTTP GET request to the URL
#Headers argument needed to not get rejected 
response = requests.get('https://www.sofascore.com/shelbourne-derry-city/vnbsznb#10951001', headers={'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})


# code to fetch and process the data

soup = BeautifulSoup(response.text, 'html.parser')
print(response.status_code)

headers = {
    'authority': 'api.sofascore.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,th;q=0.7',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"2e2bbbf4a9"',
    'origin': 'https://www.sofascore.com',
    'referer': 'https://www.sofascore.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}


headers['If-Modified-Since'] = 'Tues, 21 Nov 2023 00:00:00 GMT'
response = requests.get('https://api.sofascore.com/api/v1/event/10951001/shotmap', headers=headers)
shots = response.json()

# Extract relevant data and filter by 'isHome'
filtered_data = [item for item in shots['shotmap'] if item['isHome'] is not True]

# Create DataFrame
df = pd.DataFrame([
    {
        'player_name': item['player']['name'],
        'x': item['playerCoordinates']['x'],
        'y': item['playerCoordinates']['y'],
        'shot_type': item['shotType']
    }
    for item in filtered_data
])

df.to_csv('/Users/adambrowne/Desktop/Personal /LOI Project/Data/Shels Season Review/shelsvsderry_shotmap_43POSSESSION.csv')

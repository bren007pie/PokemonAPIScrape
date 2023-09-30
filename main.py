"""
Call PokeApi [ https://pokeapi.co/ ] and parse the JSON into CSV.
Curently gets number, name, stats, type, and abilities.
API call tutorial inspired by [ https://www.askpython.com/python/examples/pull-data-from-an-api ]
Written in Python 3.9
"""

import requests
import json
import csv

response_API = requests.get(
    'https://pokeapi.co/api/v2/pokemon/212')  # test call API
print(response_API.status_code)  # should print 200, connection okay


headers = ["#", "Pokemon", "HP", "Attack", "Defence",
           "Special Attack", "Special Defence", "Speed", "Type A", "Type B", "Abilities"]


templist = []
# standard plus variant Pokemon numbers
pok_nums = list(range(1, 1018)) + list(range(10001, 10276))
file_destination = "C:/Users/Public/"
file_name = "AllPoks.csv"

# Loop call API for all Pokemon, write to CSV
with open(file_destination + file_name, 'w', encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for i in pok_nums:
        print(i)
        response_API = requests.get(
            'https://pokeapi.co/api/v2/pokemon/%d' % (i))
        data = response_API.text
        parse_json = json.loads(data)
        # Number & Name
        templist.append(i)
        templist.append(parse_json['name'])
        # Stats
        for i in range(6):
            templist.append(parse_json['stats'][i]['base_stat'])
        # Types
        templist.append(parse_json['types'][0]["type"]["name"])
        if len(parse_json['types']) == 1:
            templist.append("")
        else:
            templist.append(parse_json['types'][1]["type"]["name"])
        # Abilities list comprehension
        templist = templist + [i["ability"]["name"]
                               for i in parse_json['abilities']]
        writer.writerow(templist)
        templist = []

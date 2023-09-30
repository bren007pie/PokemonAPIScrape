import requests
import json
import csv
response_API = requests.get('https://pokeapi.co/api/v2/pokemon/212')
print(response_API.status_code) # should print 200, connection okay

data = response_API.text
parse_json = json.loads(data)

single_poke = []

single_poke.append(parse_json['name'])
for i in range(6):
    single_poke.append(parse_json['stats'][i]['base_stat'])

single_poke.append(parse_json['types'][0]["type"]["name"])

print(len(parse_json['types'][0]["type"]))
if len(parse_json['types']) == 1:
    single_poke.append("")
else:
    single_poke.append(parse_json['types'][1]["type"]["name"])

single_poke.append([i["ability"]["name"] for i in parse_json['abilities']])


print(single_poke)
# 0 # hp
# 1 # attack
# 2 # defense
# 3 # special attack
# 4 # special defense
# 5 # speed
import json
json_file = open("U.json")
config_data = json.load(json_file)
json_file.close()
print(config_data)
line = {"name": "name", "item_to_buy": "item", "currency": "orb", "league": "league"},
   

def filewriter(line):
    dictionary = {}
    dictionary['name'] = line[0]
    dictionary['item_to_buy'] = line[1]
    dictionary['currency'] = line[0][2]
    dictionary['league'] = line[0][3]
    with open('logs.json', 'r+') as f:
        if len(f.read()) == 0:
            f.write(json.dumps(dictionary))
        else:
            f.write(',\n' + json.dumps(dictionary))

def retrieve():
    with open('logs.json') as f:
        g = json.load(f)
        print(g[1]['name'])
print(filewriter(line))

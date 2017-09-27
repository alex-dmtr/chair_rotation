import json
from random import randint

with open('data.json', 'r') as data_file:    
    people = json.load(data_file)['people']

try:
    with open('history.json', 'r') as data_file:
        history = json.load(data_file)['history']
except:
    history = []
    
history = history[-len(people)+1:]
people_pool = [p for p in people if not p['id'] in history]

indx = randint(0, len(people_pool)-1)

person = people_pool[indx]

print("Next chair is: %s" % person['name'])

history.append(person['id'])

with open('history.json', 'w') as file:
    file.write(json.dumps({"history":history}))
# pprint(data)
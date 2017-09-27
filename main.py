import json
from random import randint

def get_data():
    with open('data.json', 'r') as data_file:    
        people = json.load(data_file)['people']

    try:
        with open('history.json', 'r') as data_file:
            history = json.load(data_file)['history']
    except:
        history = []
    
    return (people, history)

def pick_chair(people, history):
    if len(history) >= len(people):
        history = []

    people_pool = [p for p in people if not p['id'] in history]

    indx = randint(0, len(people_pool)-1)

    person = people_pool[indx]

    history.append(person['id'])

    return person, history

def save_history(history):
    with open('history.json', 'w') as file:
        file.write(json.dumps({"history":history}))

if __name__ == "__main__":
    (people, history) = get_data()
    (person, history) = pick_chair(people, history)
    print("Next chair is: %s" % person['name'])

    save_history(history)
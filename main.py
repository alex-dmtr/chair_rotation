import json
from random import randint

def get_data():
    with open('data.json', 'r') as data_file:    
        people = json.load(data_file)['people']

    # try:
    #     with open('history.json', 'r') as data_file:
    #         history = json.load(data_file)['history']
    # except:
    #     history = []
    
    history = []
    return (people, history)

def pick_person(people, history, remove_id=None):
    if len(history) >= len(people) or (
        not remove_id is None or len(people) - len(history) == 1
                               and remove_id in history):
        history = []

    people_pool = [p for p in people 
                        if not p['id'] in history 
                           and (remove_id is None
                                or not p['id'] == remove_id)
                                ]

    # print(people_pool)
    indx = randint(0, len(people_pool)-1)

    person = people_pool[indx]

    history.append(person['id'])

    return person, history

def save_history(history):
    with open('history.json', 'w') as file:
        file.write(json.dumps({"history":history}))

def main():
    people, history = get_data()

    picks = []
    for i in range(0, 12):
        person1, history = pick_person(people, history)
        person2, history = pick_person(people, history)
        picks.append((person1, person2))

    # print([p['name'] for p in picks])

    for i in range(0, len(picks)):
        print('Week %d:\n  Chair:\t%s\n  Scribe:\t%s' % 
            (i+1, picks[i][0]['name'], picks[i][1]['name']))
    save_history(history)
    
if __name__ == "__main__":
    main()
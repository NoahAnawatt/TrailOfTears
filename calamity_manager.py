import json
import random
import party
from time import sleep

data = {
    "disease": {
        "dysentery": {
            "scope": "random",
            "damage": 2,
            "damage_variance": 1,
            "description": "Dysentery takes your party, causing many of them to fall ill. It spreads wildly and greatly affects the health of your party.",
            "death_message": "{victim} died of dysentery."
        },
        "whooping cough": {
            "scope": "local",
            "damage": 3,
            "damage_variance": 0,
            "description": "A whooping cough overcomes {victim}.",
            "death_message": "{victim} did not recover from whooping cough and died."
        },
        "measles": {
            "scope": "global",
            "damage": 1,
            "damage_variance": 3,
            "description": "Several of your part members aquire measles. It quickly spreads to everyone.",
            "death_message": "{victim} died from measles."
        }
    },
    "violence": {
        "soldier": {
            "scope": "local",
            "damage": 5,
            "damage_variance": 2,
            "description": "{victim} falls behind from the group. An angry soldier shoots at him to incenitize faster movement.",
            "death_message": "{victim} was killed by a soldier for being too slow."
        },
        "bears": {
            "scope": "local",
            "damage": 3,
            "damage_variance": 1,
            "description": "{victim}'s food attracts a hungry bear. The bear attacks {victim}",
            "death_message": "{victim} was mauled by an angry brown bear."
        }
    }
}       

def get_calamity(calamity_type=None):
    if calamity_type is None:
        calamity_type = random.choice(list(data.keys()))
    path,event = calamity_type,random.choice(list(data[calamity_type].keys()))
    return event,data[calamity_type][event]

def interpet_calamity(party,event,event_name):
    de_min,de_max = event["damage"]-event["damage_variance"],event["damage"]+event['damage_variance']
    if event["scope"] == 'local':
        rep_max = 1
    elif event["scope"] == 'random:':
        rep_max = 6
    if (event["scope"] == 'local') or (event["scope"] == 'random'):
        for _ in range(0,random.randint(1,rep_max)):
            partied_hurt = party.damage_member(random.randint(de_min,de_max))[0]
        print(event['description'].format(victim=partied_hurt.name))
    if event["scope"] == 'global':
        for party_member in party.getMembers():
            party_member.damage(random.randint(de_min,de_max))
            print(event['description'].format(victim=partied_member.name))
    sleep(5)
    party.purge(event)

if __name__ == '__main__':
    print(get_calamity())

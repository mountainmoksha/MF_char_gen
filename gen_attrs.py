#!/usr/bin/env python3

import random

def attrs():

    attributes = {}

    attributes['Strength'] = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
    attributes['Dexterity'] = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
    attributes['Constitution'] = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
    attributes['Intelligence'] = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
    attributes['Willpower'] = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
    attributes['Charisma'] = random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)

    return attributes

if __name__ == '__main__':

    attributes = attrs()

    for key in attributes:

        print(key, '=', attributes[key])

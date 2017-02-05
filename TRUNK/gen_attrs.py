#!/usr/bin/env python3
"""a 3d6 attr generator for mutant future"""

import random

def attrs():
    """get a set of of MF attributes"""

    attributes = {}

    attributes['Strength'] = (random.randrange(1, 7) + random.randrange(1, 7) +
                              random.randrange(1, 7))
    attributes['Dexterity'] = (random.randrange(1, 7) + random.randrange(1, 7) +
                               random.randrange(1, 7))
    attributes['Constitution'] = (random.randrange(1, 7) + random.randrange(1, 7) +
                                  random.randrange(1, 7))
    attributes['Intelligence'] = (random.randrange(1, 7) + random.randrange(1, 7) +
                                  random.randrange(1, 7))
    attributes['Willpower'] = (random.randrange(1, 7) + random.randrange(1, 7) +
                               random.randrange(1, 7))
    attributes['Charisma'] = (random.randrange(1, 7) + random.randrange(1, 7) +
                              random.randrange(1, 7))

    return attributes

if __name__ == '__main__':

    ATTRIBUTES = attrs()

    for key in ATTRIBUTES:

        print(key, '=', ATTRIBUTES[key])

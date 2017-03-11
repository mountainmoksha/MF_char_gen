#!/usr/bin/env python3
"""a 3d6 attr generator for mutant future"""

import random

def roll_4d6mL():

    rolls = []
    rolls.append(random.randrange(1, 7))
    rolls.append(random.randrange(1, 7))
    rolls.append(random.randrange(1, 7))
    rolls.append(random.randrange(1, 7))
    score = 0
    for rolls_idx in range(len(rolls)):
        score += rolls[rolls_idx]
    score -= min(rolls)
    return score

def attrs(method='3d6'):
    """get a set of of MF attributes"""

    attributes = {}

    if method == '4d6-L':

        attributes['Strength'] = roll_4d6mL()
        attributes['Dexterity'] = roll_4d6mL()
        attributes['Constitution'] = roll_4d6mL()
        attributes['Intelligence'] = roll_4d6mL()
        attributes['Willpower'] = roll_4d6mL()
        attributes['Charisma'] = roll_4d6mL()

    else:

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

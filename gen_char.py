#!/usr/bin/env python3

import random
import read_muts
import gen_attrs

def char_modifiers(character):

    mods = []

    str_mod =  'Modifier to hit, damage, and forcing doors: '

    if (character['attributes'])['Strength'] < 4:
        str_mod = str(str_mod + '-3')
    elif (character['attributes'])['Strength'] < 6:
        str_mod = str(str_mod + '-2')
    elif (character['attributes'])['Strength'] < 9:
        str_mod = str(str_mod + '-1')
    elif (character['attributes'])['Strength'] < 13:
        str_mod = str(str_mod + '0')
    elif (character['attributes'])['Strength'] < 16:
        str_mod = str(str_mod + '+1')
    elif (character['attributes'])['Strength'] < 18:
        str_mod = str(str_mod + '+2')
    elif (character['attributes'])['Strength'] < 19:
        str_mod = str(str_mod + '+3')
    elif (character['attributes'])['Strength'] < 20:
        str_mod = str(str_mod + '+3 (+4 damage)')
    elif (character['attributes'])['Strength'] < 21:
        str_mod = str(str_mod + '+4')
    else:
        str_mod = str(str_mod + '+4 (+5 damage)')

    mods.append(str_mod)

    character['modifiers'] = mods


def char_mutations(character):

    # Gen Mutations variably by class
    if ((character['type'] == 'Mutant Human') or
        (character['type'] == 'Mutant Animal')):
        character['physical'] = read_muts.muts('physical')
        character['mental'] = read_muts.muts('mental')
        character['plant'] = ['']

    elif character['type'] == 'Mutant Plant':
        character['plant'] = read_muts.muts('plant', 2)
        character['physical'] = []
        character['mental'] = []
        for rand_idx in range(random.randrange(6) + 1):
            if (rand_idx % 2) == 0:
                phys_mut = read_muts.muts('physical')[0]
                while phys_mut in character['physical']:
                    phys_mut = read_muts.muts('physical')[0]
                character['physical'].append(phys_mut)
            else:
                phys_mut = read_muts.muts('mental')[0]
                while phys_mut in character['mental']:
                    phys_mut = read_muts.muts('mental')[0]
                character['mental'].append(phys_mut)

    elif character['type'] == 'Pure Human':
        character['physical'] = ['']
        character['mental'] = ['']
        character['plant'] = ['']

    else: # androids
        character['physical'] = ['Pick any combination of 3 beneficial ' +
                                 'mental and/or physical mutations']
        character['mental'] = ['Pick any combination of 3 beneficial ' +
                                 'mental and/or physical mutations']
        character['plant'] = ['']


def char_HP(character):

    # Gen HP by class
    hit_points = 0
    if character['type'] == 'Pure Human':
        for _ in range((character['attributes'])['Constitution']):
            hit_points = hit_points + random.randrange(1, 9)
        character['HP'] = hit_points 

    elif character['type'] == 'Mutant Human':
        for _ in range((character['attributes'])['Constitution']):
            hit_points = hit_points + random.randrange(1, 7)
        character['HP'] = hit_points

    elif character['type'] == 'Mutant Animal':
        for _ in range((character['attributes'])['Constitution']):
            hit_points = hit_points + random.randrange(1, 7)
        character['HP'] = hit_points 

    elif character['type'] == 'Mutant Plant':
        for _ in range((character['attributes'])['Constitution']):
            hit_points = hit_points + random.randrange(1, 7)
        character['HP'] = hit_points 

    else: # androids
        character['HP'] = 50


def char(char_type=None):

    with open('MF_classes.txt', 'r') as classes_file:
        types = classes_file.read().splitlines()

    if char_type is None:
        char_type = types[random.randrange(len(types))]

    if char_type not in types:
        print('invalid type')
        exit(1)

    # Gen basics of all characters
    character = {}
    character['type'] = char_type
    character['attributes'] = gen_attrs.attrs()

    char_HP(character)

    char_mutations(character)

    char_modifiers(character)

    return character

if __name__ == '__main__':

    character = char()
    print(character)

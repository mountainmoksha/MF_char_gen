#!/usr/bin/env python3
"""main module: Mutant Future low-level char gen"""

import random
import read_muts
import gen_attrs
import gen_mods

def gen_xp(character):
    """assign minimum XP to character for given level"""

    character['XP'] = 0

    if character['level'] == 2:
        character['XP'] = 3001
    elif character['level'] == 3:
        character['XP'] = 6001
    elif character['level'] == 4:
        character['XP'] = 12001
    elif character['level'] == 5:
        character['XP'] = 24001
    elif character['level'] == 6:
        character['XP'] = 48001
    elif character['level'] == 7:
        character['XP'] = 96001
    elif character['level'] == 8:
        character['XP'] = 192001
    elif character['level'] == 9:
        character['XP'] = 492001
    elif character['level'] == 10:
        character['XP'] = 892001
    elif character['level'] == 11:
        character['XP'] = 1392001
    elif character['level'] == 12:
        character['XP'] = 2392001



def gen_saves(character):
    """produce modified saving throws by level"""

    if character['level'] < 4:
        character['energy_save'] = 17
        character['poison_death_save'] = 14
        character['stun_save'] = 16
        character['rad_save'] = 15
    elif character['level'] < 7:
        character['energy_save'] = 15
        character['poison_death_save'] = 12
        character['stun_save'] = 14
        character['rad_save'] = 13
    elif character['level'] < 10:
        character['energy_save'] = 9
        character['poison_death_save'] = 8
        character['stun_save'] = 10
        character['rad_save'] = 9
    elif character['level'] < 13:
        character['energy_save'] = 7
        character['poison_death_save'] = 6
        character['stun_save'] = 8
        character['rad_save'] = 7
    elif character['level'] < 16:
        character['energy_save'] = 5
        character['poison_death_save'] = 4
        character['stun_save'] = 6
        character['rad_save'] = 5
    elif character['level'] < 19:
        character['energy_save'] = 4
        character['poison_death_save'] = 4
        character['stun_save'] = 5
        character['rad_save'] = 4
    else:
        character['energy_save'] = 4
        character['poison_death_save'] = 3
        character['stun_save'] = 4
        character['rad_save'] = 3

    character['poison_death_save'] = character['poison_death_save'] + int(character['poison_mod'])
    character['rad_save'] = character['rad_save'] + int(character['rad_mod'])


def gen_level_mods(character):
    """custom leveling system.  MF rules p. 14"""

    level_modifiers = {}

    for level_idx in range(2, character['level']+1):

        level_roll = random.randrange(100)

        if ((level_roll > 0) and
            (level_roll < 11)):
            level_modifiers['level' + str(level_idx)] = str('+1 melee damage from level ' +
                                                            str(level_idx) + ' advancement')
        elif ((level_roll > 10) and
            (level_roll < 21)):
            level_modifiers['level' + str(level_idx)] = str('+1 attack/round from level ' +
                                                            str(level_idx) + ' advancement')
        else:
            ability_roll = random.randrange(1, 7)
            if ability_roll == 1:
                strn = (character['attributes'])['Strength']
                strn = strn + 1
                (character['attributes'])['Strength'] = strn
            elif ability_roll == 2:
                dex = (character['attributes'])['Dexterity']
                dex = dex + 1
                (character['attributes'])['Dexterity'] = dex
            elif ability_roll == 3:
                con = (character['attributes'])['Constitution']
                con = con + 1
                (character['attributes'])['Constitution'] = con
            elif ability_roll == 4:
                intel = (character['attributes'])['Intelligence']
                intel = intel + 1
                (character['attributes'])['Intelligence'] = intel
            elif ability_roll == 5:
                wil = (character['attributes'])['Willpower']
                wil = wil + 1
                (character['attributes'])['Willpower'] = wil
            elif ability_roll == 6:
                char = (character['attributes'])['Charisma']
                char = char + 1
                (character['attributes'])['Charisma'] = char

    character['level_modifiers'] = level_modifiers


def char_mutations(character):
    """assign physical, mental and plant mutations"""

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


def char_hit_points(character):
    """obtain character hit points by class"""

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


def char_name(character):
    """I suspect this will be a little controversal with
       people.  It's a completely randomized naming system"""

    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    vowels = ['a', 'e', 'i', 'o', 'u']

    character_name = ''

    if ((character['type'] == 'Pure Human') or
        (character['type'] == 'Mutant Human')):

        # first name:
        for letter_idx in range(random.randrange(3, 6)):
            if letter_idx % 2 == 0:
                letter = consonants[random.randrange(len(consonants))]
            else:
                letter = vowels[random.randrange(len(vowels))]

            if letter_idx == 0:
                character_name = character_name + letter.upper()
            else:
                character_name = character_name + letter.lower()

        character_name = character_name + ' '

        # last name:
        for letter_idx in range(random.randrange(4, 8)):
            if letter_idx % 2 == 0:
                letter = consonants[random.randrange(len(consonants))]
            else:
                letter = vowels[random.randrange(len(vowels))]

            if letter_idx == 0:
                character_name = character_name + letter.upper()
            else:
                character_name = character_name + letter.lower()

    elif (character['type'] == 'Mutant Animal'):

        # one name, but longer
        for letter_idx in range(random.randrange(5, 8)):
            if letter_idx % 2 == 0:
                letter = vowels[random.randrange(len(vowels))]
            else:
                letter = consonants[random.randrange(len(consonants))]

            if letter_idx == 0:
                character_name = character_name + letter.upper()
            else:
                character_name = character_name + letter.lower()

    elif (character['type'] == 'Mutant Plant'):

        # one name, but longer
        for letter_idx in range(random.randrange(5, 8)):
            letter = vowels[random.randrange(len(vowels))]

            if letter_idx == 0:
                character_name = character_name + letter.upper()
            else:
                character_name = character_name + letter.lower()

    else: # all androids

        character_name = consonants[random.randrange(len(consonants))].upper() + '-'

        for _ in range(5):

            character_name = character_name + str(random.randrange(10))

        character_name = character_name + '-' + vowels[random.randrange(len(vowels))].upper()


    return character_name


def char(char_type=None, level=1, sub_type=True, gen_name=True, rand_synth=False, rand_repl=False):
    """obtain fully-populated character"""

    with open('MF_classes.txt', 'r') as classes_file:
        types = classes_file.read().splitlines()

    if char_type is None:

        if not rand_synth:
            types.remove('Synthetic Android')

        if not rand_repl:
            types.remove('Replicant')

        char_type = types[random.randrange(len(types))]

    if char_type not in types:
        print('invalid type')
        exit(1)

    # Gen basics of all characters
    character = {}
    character['type'] = char_type

    if gen_name:
        character['name'] = char_name(character)
    else:
        character['alt-name'] = char_name(character)

    character['attributes'] = gen_attrs.attrs()

    if level is None:
        character['level'] = random.randrange(1, 11)
    else:
        character['level'] = level

    gen_level_mods(character)

    # optional sub-species for plants and animals
    if sub_type:

        if character['type'] == 'Mutant Animal':
            with open('MF_animals.txt', 'r') as animals_file:
                animals = animals_file.read().splitlines()
            character['sub_type'] = animals[random.randrange(len(animals))]

        if character['type'] == 'Mutant Plant':
            with open('MF_plants.txt', 'r') as plants_file:
                plants = plants_file.read().splitlines()
            character['sub_type'] = plants[random.randrange(len(plants))]

    # Base unarmored AC
    character['AC'] = 9

    char_hit_points(character)

    character['GP'] = (random.randrange(1, 9) +
                       random.randrange(1, 9) +
                       random.randrange(1, 9)) * 10

    char_mutations(character)

    gen_mods.gen_modifiers(character)

    gen_saves(character)

    gen_xp(character)

    return character

if __name__ == '__main__':

    CHARACTER = char(None, None, True, True, False, False)
    print(CHARACTER)

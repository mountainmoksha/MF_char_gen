#!/usr/bin/env python3
"""main module: Mutant Future low-level char gen"""

import random
import read_muts
import gen_attrs

def char_modifiers(character):
    """assign modifiers given a set of character attributes"""

    mods = []

    str_mod = 'Modifier to hit, damage, and forcing doors: '

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

    ac_mod = 'Armor Class Modifier: '
    missile_mod = 'Missile Attack Modifier: '
    init_mod = 'Optional Initiative Modifier: '

    if (character['attributes'])['Dexterity'] < 4:
        ac_mod = str(ac_mod + '+3')
        character['AC'] = character['AC'] + 3
        missile_mod = str(missile_mod + '-3')
        init_mod = str(init_mod + '-2')
    elif (character['attributes'])['Dexterity'] < 6:
        character['AC'] = character['AC'] + 2
        ac_mod = str(ac_mod + '+2')
        missile_mod = str(missile_mod + '-2')
        init_mod = str(init_mod + '-1')
    elif (character['attributes'])['Dexterity'] < 9:
        character['AC'] = character['AC'] + 1
        ac_mod = str(ac_mod + '+1')
        missile_mod = str(missile_mod + '-1')
        init_mod = str(init_mod + '-1')
    elif (character['attributes'])['Dexterity'] < 13:
        ac_mod = str(ac_mod + '0')
        missile_mod = str(missile_mod + '0')
        init_mod = str(init_mod + '0')
    elif (character['attributes'])['Dexterity'] < 16:
        character['AC'] = character['AC'] - 1
        ac_mod = str(ac_mod + '-1')
        missile_mod = str(missile_mod + '+1')
        init_mod = str(init_mod + '+1')
    elif (character['attributes'])['Dexterity'] < 18:
        character['AC'] = character['AC'] - 2
        ac_mod = str(ac_mod + '-2')
        missile_mod = str(missile_mod + '+2')
        init_mod = str(init_mod + '+1')
    elif (character['attributes'])['Dexterity'] < 19:
        character['AC'] = character['AC'] - 3
        ac_mod = str(ac_mod + '-3')
        missile_mod = str(missile_mod + '+3')
        init_mod = str(init_mod + '+2')
    elif (character['attributes'])['Dexterity'] < 20:
        character['AC'] = character['AC'] - 4
        ac_mod = str(ac_mod + '-4')
        missile_mod = str(missile_mod + '+3')
        init_mod = str(init_mod + '+2')
    elif (character['attributes'])['Dexterity'] < 21:
        character['AC'] = character['AC'] - 4
        ac_mod = str(ac_mod + '-4')
        missile_mod = str(missile_mod + '+4')
        init_mod = str(init_mod + '+3')
    elif (character['attributes'])['Dexterity'] < 22:
        character['AC'] = character['AC'] - 5
        ac_mod = str(ac_mod + '-5')
        missile_mod = str(missile_mod + '+4')
        init_mod = str(init_mod + '+3')

    mods.append(ac_mod)
    mods.append(missile_mod)
    mods.append(init_mod)

    poison_mod = 'Poison Saving Throw Adjustment: '
    rad_mod = 'Radiation Throw Adjustment: '

    if (character['attributes'])['Constitution'] < 4:
        poison_mod = str(poison_mod + '-2')
        rad_mod = str(rad_mod + '-3')
    elif (character['attributes'])['Constitution'] < 6:
        poison_mod = str(poison_mod + '-1')
        rad_mod = str(rad_mod + '-2')
    elif (character['attributes'])['Constitution'] < 9:
        poison_mod = str(poison_mod + '0')
        rad_mod = str(rad_mod + '-1')
    elif (character['attributes'])['Constitution'] < 19:
        poison_mod = str(poison_mod + '0')
        rad_mod = str(rad_mod + '0')
    elif (character['attributes'])['Constitution'] < 20:
        poison_mod = str(poison_mod + '+1')
        rad_mod = str(rad_mod + '0')
    elif (character['attributes'])['Constitution'] < 21:
        poison_mod = str(poison_mod + '+2')
        rad_mod = str(rad_mod + '+1')
    elif (character['attributes'])['Constitution'] < 22:
        poison_mod = str(poison_mod + '+3')
        rad_mod = str(rad_mod + '+2')

    mods.append(poison_mod)
    mods.append(rad_mod)

    tech_mod = 'Technology Roll Modifier: '

    if (character['attributes'])['Intelligence'] < 4:
        tech_mod = str(tech_mod + '-15%')
    elif (character['attributes'])['Intelligence'] < 6:
        tech_mod = str(tech_mod + '-10%')
    elif (character['attributes'])['Intelligence'] < 9:
        tech_mod = str(tech_mod + '-5%')
    elif (character['attributes'])['Intelligence'] < 13:
        tech_mod = str(tech_mod + '0%')
    elif (character['attributes'])['Intelligence'] < 16:
        tech_mod = str(tech_mod + '+5%')
    elif (character['attributes'])['Intelligence'] < 18:
        tech_mod = str(tech_mod + '+10%')
    elif (character['attributes'])['Intelligence'] < 19:
        tech_mod = str(tech_mod + '+15%')
    elif (character['attributes'])['Intelligence'] < 20:
        tech_mod = str(tech_mod + '+20%')
    elif (character['attributes'])['Intelligence'] < 21:
        tech_mod = str(tech_mod + '+25%')
    elif (character['attributes'])['Intelligence'] < 22:
        tech_mod = str(tech_mod + '+30%')

    mods.append(tech_mod)

    reaction_mod = 'Reaction Adjustment: '
    retainers_mod = 'Retainers: '
    morale_mod = 'Retainer Morale: '

    if (character['attributes'])['Charisma'] < 4:
        reaction_mod = str(reaction_mod + '+2')
        retainers_mod = str(retainers_mod + '1')
        morale_mod = str(morale_mod + '4')
    elif (character['attributes'])['Charisma'] < 6:
        reaction_mod = str(reaction_mod + '+1')
        retainers_mod = str(retainers_mod + '2')
        morale_mod = str(morale_mod + '5')
    elif (character['attributes'])['Charisma'] < 9:
        reaction_mod = str(reaction_mod + '+1')
        retainers_mod = str(retainers_mod + '3')
        morale_mod = str(morale_mod + '6')
    elif (character['attributes'])['Charisma'] < 13:
        reaction_mod = str(reaction_mod + '0')
        retainers_mod = str(retainers_mod + '4')
        morale_mod = str(morale_mod + '7')
    elif (character['attributes'])['Charisma'] < 16:
        reaction_mod = str(reaction_mod + '-1')
        retainers_mod = str(retainers_mod + '5')
        morale_mod = str(morale_mod + '8')
    elif (character['attributes'])['Charisma'] < 18:
        reaction_mod = str(reaction_mod + '-1')
        retainers_mod = str(retainers_mod + '6')
        morale_mod = str(morale_mod + '9')
    elif (character['attributes'])['Charisma'] < 19:
        reaction_mod = str(reaction_mod + '-2')
        retainers_mod = str(retainers_mod + '7')
        morale_mod = str(morale_mod + '10')
    elif (character['attributes'])['Charisma'] < 20:
        reaction_mod = str(reaction_mod + '-2')
        retainers_mod = str(retainers_mod + '8')
        morale_mod = str(morale_mod + '10')
    elif (character['attributes'])['Charisma'] < 21:
        reaction_mod = str(reaction_mod + '-3')
        retainers_mod = str(retainers_mod + '9')
        morale_mod = str(morale_mod + '11')
    elif (character['attributes'])['Charisma'] < 22:
        reaction_mod = str(reaction_mod + '-3')
        retainers_mod = str(retainers_mod + '10')
        morale_mod = str(morale_mod + '11')

    mods.append(reaction_mod)
    mods.append(retainers_mod)
    mods.append(morale_mod)

    character['modifiers'] = mods


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


def char(char_type=None):
    """obtain fully-populated character"""

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

    character['AC'] = 10

    char_hit_points(character)

    character['GP'] = (random.randrange(1, 9) +
                       random.randrange(1, 9) +
                       random.randrange(1, 9)) * 10

    char_mutations(character)

    char_modifiers(character)

    return character

if __name__ == '__main__':

    CHARACTER = char()
    print(CHARACTER)

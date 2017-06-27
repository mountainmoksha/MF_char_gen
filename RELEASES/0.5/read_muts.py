#!/usr/bin/env python3
"""returns randomized mutations from ASCII files"""

import random

def muts(mutation_type='physical', num_muts=None):
    """returns randomized mutations from ASCII files"""

    if mutation_type == 'physical':
        mutations_text = open('MF_physical.txt', 'r')
    elif mutation_type == 'mental':
        mutations_text = open('MF_mental.txt', 'r')
    elif mutation_type == 'plant':
        mutations_text = open('MF_plant.txt', 'r')
    else:
        print('unknown mutations type')
        exit(1)

    mutations = []
    ret_mutations = []
    if num_muts is None:
        num_muts = random.randrange(4) + 1

    for mutation in mutations_text:

        mut_name = mutation.rstrip()[6:]
        mut_range_start = int(mutation.rstrip()[0:2])
        mut_range_end = int(mutation.rstrip()[3:5])

        for _ in range(mut_range_start, mut_range_end + 1):
            mutations.append(mut_name)

    for _ in range(num_muts):

        this_roll = random.randrange(100)

        while mutations[this_roll] in ret_mutations:
            this_roll = random.randrange(100)

        ret_mutations.append(mutations[this_roll])

    return ret_mutations


if __name__ == '__main__':

    print(muts())

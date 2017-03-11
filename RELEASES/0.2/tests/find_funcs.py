#!/usr/bin/env python3
"""module to ensure that all modules are covered with unit tests"""

import glob
import os

if __name__ == "__main__":

    MISSING_TEST_FILES = []
    MISSING_TEST_FUNCTIONS = []

    FILE_NAMES = glob.glob('../*.py')
    for file_name in FILE_NAMES:

        test_file_search = 'test_' + os.path.basename(file_name)

        if not os.path.isfile(test_file_search):
            MISSING_TEST_FILES.append('test_' + os.path.basename(file_name))
        else:
            source_file_f = open('../' + os.path.basename(file_name), 'r')
            for source_file_line in source_file_f:
                if source_file_line[:3] == 'def':
                    source_func_name = (source_file_line.rstrip().split(' ')[1]).split('(')[0]
                    test_source_func_name = 'test_' + source_func_name
                    found = False
                    if test_source_func_name in open(test_file_search).read():
                        pass
                    else:
                        MISSING_TEST_FUNCTIONS.append(test_file_search + '::' +
                                                      test_source_func_name)
            source_file_f.close()


    print()
    print('Missing Test Files (' + str(len(MISSING_TEST_FILES)) + ') :')
    print('___________________')
    print()
    for missing_test_file in MISSING_TEST_FILES:
        print('\t' + missing_test_file)
    print()

    print()
    print('Missing Test Functions (' + str(len(MISSING_TEST_FUNCTIONS)) + ') :')
    print('_______________________')
    print()
    for missing_test_function in MISSING_TEST_FUNCTIONS:
        print('\t' + missing_test_function)
    print()

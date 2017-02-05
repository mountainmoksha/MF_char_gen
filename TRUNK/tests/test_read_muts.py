#!/usr/bin/env python3
"""unit tests to mutation reader"""

import os
import unittest
import read_muts

class SimpleTestCase(unittest.TestCase):
    """test class for mutation reader"""

    def setUp(self):
        """Call before every test case."""
        self.tests_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir('..')

    def tearDown(self):
        """Call after every test case."""
        os.chdir(self.tests_path)

    def test_muts(self):
        """test the proper operation of mutation reader"""

        mutations = read_muts.muts('physical')

        for mutation in mutations:

            mutation_found = False

            mutations_text = open('MF_physical.txt', 'r')

            for mutation_canonical in mutations_text:
                if mutation_canonical[6:].rstrip() == mutation:
                    mutation_found = True

            self.assertTrue(mutation_found == True)


if __name__ == "__main__":

    unittest.main() # run all tests

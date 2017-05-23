#!/usr/bin/env python3
"""unit tests to mutation reader"""

import os
import unittest
import gen_mods

class SimpleTestCase(unittest.TestCase):
    """test class for mutation reader"""

    def setUp(self):
        """Call before every test case."""
        self.tests_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir('..')

    def tearDown(self):
        """Call after every test case."""
        os.chdir(self.tests_path)

    def test_gen_modifiers(self):
        """test the proper operation of mutation reader"""

        #TODO: do this
        print('this test in not complete')



if __name__ == "__main__":

    unittest.main() # run all tests

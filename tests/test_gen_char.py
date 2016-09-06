#!/usr/bin/env python3
"""unit tests to character generator"""

import os
import unittest
import gen_char

class SimpleTestCase(unittest.TestCase):
    """test class for character generator"""

    def setUp(self):
        """Call before every test case."""
        self.tests_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir('..')

    def tearDown(self):
        """Call after every test case."""
        os.chdir(self.tests_path)

    def test_char(self):
        """test the proper operation of character generator"""

        character = gen_char.char()
        #TODO: do this
        print('this test in not complete')



if __name__ == "__main__":

    unittest.main() # run all tests

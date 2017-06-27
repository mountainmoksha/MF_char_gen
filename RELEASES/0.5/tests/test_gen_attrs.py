#!/usr/bin/env python3
"""unit tests to attribute generator"""

import os
import unittest
import gen_attrs

class SimpleTestCase(unittest.TestCase):
    """test class for attribute generator"""

    def setUp(self):
        """Call before every test case."""
        self.tests_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir('..')

    def tearDown(self):
        """Call after every test case."""
        os.chdir(self.tests_path)

    def test_attrs(self):
        """unit test for attribute generator"""

        attributes = gen_attrs.attrs()

        self.assertTrue('Willpower' in attributes)
        self.assertTrue('Constitution' in attributes)
        self.assertTrue('Dexterity' in attributes)
        self.assertTrue('Intelligence' in attributes)
        self.assertTrue('Charisma' in attributes)
        self.assertTrue('Strength' in attributes)

    def test_roll_4d6mL(self):

        score = gen_attrs.roll_4d6mL()
        # 3d6 scores will always fall between 3 and 18
        self.assertTrue(score > 2)
        self.assertTrue(score < 19)


if __name__ == "__main__":

    unittest.main() # run all tests

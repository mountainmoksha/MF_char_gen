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

    def test_char_name(self):

        character = gen_char.char()

        self.assertTrue(isinstance(gen_char.char_name(character), str))

    def test_char(self):
        """test the proper operation of character generator"""

        character = gen_char.char()

        self.assertTrue('missile_mod' in character)
        self.assertTrue('rad_mod' in character)
        self.assertTrue('HP' in character)
        self.assertTrue('level' in character)
        self.assertTrue('name' in character)
        self.assertTrue('reaction_mod' in character)
        self.assertTrue('stun_save' in character)
        self.assertTrue('modifiers' in character)
        self.assertTrue('AC' in character)
        self.assertTrue('plant' in character)
        self.assertTrue('type' in character)
        self.assertTrue('poison_mod' in character)
        self.assertTrue('physical' in character)
        self.assertTrue('ac_mod' in character)
        self.assertTrue('energy_save' in character)
        self.assertTrue('XP' in character)
        self.assertTrue('GP' in character)
        self.assertTrue('rad_save' in character)
        self.assertTrue('mental' in character)
        self.assertTrue('level_modifiers' in character)
        self.assertTrue('attributes' in character)
        self.assertTrue('poison_death_save' in character)
        self.assertTrue('str_mod' in character)
        self.assertTrue('tech_mod' in character)


if __name__ == "__main__":

    unittest.main() # run all tests

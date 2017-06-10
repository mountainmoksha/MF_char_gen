#!/usr/bin/env python3
"""unit tests to db access module"""

import unittest
import os
import gen_char
import db_access

class SimpleTestCase(unittest.TestCase):
    """test class for db access module"""

    def setUp(self):
        """Call before every test case."""
        self.tests_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir('..')

    def tearDown(self):
        """Call after every test case."""
        os.chdir(self.tests_path)

    def test_insert_char(self):
        """test character insert"""
        character = gen_char.char()
        db_access.insert_char(character)
        ret_character = db_access.query_by_name(character['name'])
        self.assertTrue(character == ret_character)
        db_access.rm_by_name(character['name'])

    def test_query_by_name(self):
        """test character query"""
        character = gen_char.char()
        db_access.insert_char(character)
        ret_character = db_access.query_by_name(character['name'])
        self.assertTrue(character == ret_character)
        db_access.rm_by_name(character['name'])

    def test_query_by_name(self):
        """test character query"""
        character = gen_char.char()
        db_access.insert_char(character)
        db_access.rm_by_name(character['name'])
        ret_character = db_access.query_by_name(character['name'])
        self.assertTrue(ret_character == None)


if __name__ == "__main__":

    unittest.main() # run all tests

#!/usr/bin/env python3
"""unit tests to character xml parser"""

import os
import unittest
import gen_char
import create_xml
import char_xml_parser

class SimpleTestCase(unittest.TestCase):
    """test class for char xml parser"""

    def setUp(self):
        """Call before every test case."""
        self.tests_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir('..')
        self.character = gen_char.char()
        self.file_name = create_xml.gen_char_xml(self.character)

    def tearDown(self):
        """Call after every test case."""
        os.chdir(self.tests_path)

    def test_parse_char_xml(self):
        """test the proper operation of char xml parser"""
        character_returned = char_xml_parser.parse_char_xml(self.file_name)

        for key in self.character:
            print(self.character[key], '==', character_returned[key])
            if self.character[key] != ['']:
                self.assertTrue(self.character[key] == character_returned[key])


if __name__ == "__main__":

    unittest.main() # run all tests

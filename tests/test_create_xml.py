#!/usr/bin/env python3
"""unit tests to attribute generator"""

import os
import unittest
import gen_char
import create_xml

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

        character = gen_char.char()

        filename = create_xml.gen_char_xml(character)
        self.assertTrue(os.path.isfile(filename))


if __name__ == "__main__":

    unittest.main() # run all tests

#!/usr/bin/env python3
"""take a character dict, and create pretty xml"""

import os
import dicttoxml
import gen_char


def gen_char_xml(character):
    """put the numbers and words from a character on a "blank" sheet
       to be added to the stock sheet"""

    if 'name' in character:
        file_name = 'char_xmls/' + character['name'].replace(' ', '_') + '_blank.xml'
    else:
        file_name = 'char_xmls/' + character['alt-name'].replace(' ', '_') + '_blank.xml'

    return file_name

if __name__ == '__main__':

    CHARACTER = gen_char.char()

    FILE_NAME = gen_char_xml(CHARACTER)

    print(FILE_NAME)

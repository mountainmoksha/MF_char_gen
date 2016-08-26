#!/usr/bin/env python3
"""take a character dict, and create pretty xml"""

import os
import xml.dom.minidom
import dicttoxml
import gen_char


def gen_char_xml(character):
    """generate xml representing a mutant future character"""

    if 'name' in character:
        file_name = 'char_xmls/' + character['name'].replace(' ', '_') + '.xml'
    else:
        file_name = 'char_xmls/' + character['alt-name'].replace(' ', '_') + '.xml'

    xml_string = xml.dom.minidom.parseString(dicttoxml.dicttoxml(character)).toprettyxml()

    xml_f = open(file_name, 'w')
    xml_f.write(xml_string)
    xml_f.close()

    return file_name

if __name__ == '__main__':

    CHARACTER = gen_char.char()

    FILE_NAME = gen_char_xml(CHARACTER)

    print(FILE_NAME)

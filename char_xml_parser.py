#!/usr/bin/env python3

import xmltodict

def parse_char_xml(file_name):

    character = {}

    file_ptr = open(file_name, 'r')
    xml_string = file_ptr.read()
    file_ptr.close()
    full_dict = xmltodict.parse(xml_string)
    root_dict = full_dict['root']

    for root_key in root_dict:

         if (root_dict[root_key])['@type'] == 'str':
             character[root_key] = str((root_dict[root_key])['#text'])

         if (root_dict[root_key])['@type'] == 'int':
             character[root_key] = int((root_dict[root_key])['#text'])

         if (root_dict[root_key])['@type'] == 'list':
             print(root_dict[root_key])

         if (root_dict[root_key])['@type'] == 'dict':
             for dict_key in root_dict[root_key]:
                 if dict_key != '@type':

                     if ((root_dict[root_key])[dict_key])['@type'] == 'str':
                         val_str = str(((root_dict[root_key])[dict_key])['#text'])
                         character[dict_key] = val_str

                     if ((root_dict[root_key])[dict_key])['@type'] == 'int':
                         val_str = int(((root_dict[root_key])[dict_key])['#text'])
                         character[dict_key] = val_str

    print()
    print()
    print(character)


if __name__ == '__main__':

    parse_char_xml('char_xmls/Bog_Pibiviz.xml')

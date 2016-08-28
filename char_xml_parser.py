#!/usr/bin/env python3

import xmltodict
import gen_char
import create_xml

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

            this_list = []

            for sub_key in root_dict[root_key]:
                if 'item' in root_dict[root_key]:
                    for item_key in (root_dict[root_key])['item']:
                        if '#text' in item_key:
                            this_entry = item_key['#text']
                            if this_entry not in this_list:
                                this_list.append(this_entry)

            character[root_key] = this_list

        if (root_dict[root_key])['@type'] == 'dict':

            this_dict = {}

            for dict_key in root_dict[root_key]:
                if dict_key != '@type':

                    if ((root_dict[root_key])[dict_key])['@type'] == 'str':
                        val_str = str(((root_dict[root_key])[dict_key])['#text'])
                        this_dict[dict_key] = val_str

                    if ((root_dict[root_key])[dict_key])['@type'] == 'int':
                        val_int = int(((root_dict[root_key])[dict_key])['#text'])
                        this_dict[dict_key] = val_int

            character[root_key] = this_dict

    return character


if __name__ == '__main__':

    CHARACTER = gen_char.char()
    FILE_NAME = create_xml.gen_char_xml(CHARACTER)
    CHARACTER_RETURNED = parse_char_xml(FILE_NAME)

    print('match:')
    print()
    print(CHARACTER)
    print()
    print('to:')
    print()
    print(CHARACTER_RETURNED)

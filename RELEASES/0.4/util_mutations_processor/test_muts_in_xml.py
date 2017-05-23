#!/usr/bin/env python3

import xml.dom.minidom

# read xml file
xml_file_name = '../mutations_descriptions.xml'
xml_p = open(xml_file_name, 'r')
xml_string = xml_p.read()
xml_p.close()
doc_obj = xml.dom.minidom.parseString(xml_string)

# read mutations files from trunk
file_names = []
file_names.append('../MF_mental.txt')
file_names.append('../MF_physical.txt')
file_names.append('../MF_plant.txt')

for file_name in file_names:
    print(file_name + ':')
    print('-----------------------------------')
    file_p = open(file_name, 'r')
    lines = file_p.read()
    file_p.close()
    for line in lines.split('\n'):
        mutation = line[6:]
        text = doc_obj.getElementsByTagName(mutation.replace(' ', '_'))
        try:
            text[0].firstChild.nodeValue
        except IndexError:
            print(mutation + ' not found')

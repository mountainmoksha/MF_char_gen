#!/usr/bin/env python3

import glob
import dicttoxml
import xmltodict
import xml.dom.minidom

# the more-or-less raw text cut-and-pasted out of the rulebook
# goes into .txt files, named exactly as the mutations are to be
# named, subbing _ for spaces in the filesnames
files_list = glob.glob('*.txt')

# read txt files and more-properly format the text for output
# (especially remove newlines)
for this_file in files_list:
    this_file_p = open(this_file, 'r')
    this_file_txt = this_file_p.read()
    this_file_txt = this_file_txt.replace('\n', ' ')
    this_file_txt = this_file_txt.replace('|', '\n')
    this_file_txt = this_file_txt.replace('\n ', '\n')
    new_file_p = open(this_file.replace('txt', 'out'), 'w')
    new_file_p.write(this_file_txt)
    this_file_p.close()
    new_file_p.close()

files_list = glob.glob('*.out')

# put mutations (as keys) and descriptions (as values) into dict
muts_descs = {}
for this_file in files_list:
    this_file_p = open(this_file, 'r')
    this_file_txt = this_file_p.read()
    muts_descs[this_file.replace('.out', '')] = this_file_txt
    this_file_p.close()

#create file
xml_string = xml.dom.minidom.parseString(dicttoxml.dicttoxml(muts_descs)).toprettyxml()
file_name = 'mutations_descriptions.xml'
xml_p = open(file_name, 'w')
xml_p.write(xml_string)
xml_p.close()

# read file
xml_p = open(file_name, 'r')
xml_string = xml_p.read()
xml_p.close()

dom = xml.dom.minidom.parseString(xml_string)
text = dom.getElementsByTagName('Shriek')
print(text[0].firstChild.nodeValue)

#!/usr/bin/env python3
"""db access module for mfchargen"""

import pprint
import tinydb
from tinydb.operations import delete
import gen_char

def query_by_name(name=''):
    """retrieve character from db by name"""

    database = tinydb.TinyDB('chars.json')
    char_query = tinydb.Query()
    try:
        this_char = database.search(char_query.name == name)[0]
    except IndexError:
        this_char = None
    database.close()
    return this_char

def insert_char(character):
    """insert a character dictionary into db"""

    database = tinydb.TinyDB('chars.json')
    database.insert(character)
    database.close()

def rm_by_name(name):
    """remove a character dict from db"""

    database = tinydb.TinyDB('chars.json')
    char_query = tinydb.Query()
    database.remove(char_query.name == name)
    database.close()

if __name__ == '__main__':

    CHARACTER = gen_char.char()
    insert_char(CHARACTER)
    RET_CHAR = query_by_name(CHARACTER['name'])
    PPRINTER = pprint.PrettyPrinter(indent=4)
    PPRINTER.pprint(RET_CHAR)
    rm_by_name(CHARACTER['name'])

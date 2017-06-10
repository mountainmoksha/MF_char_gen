#!/usr/bin/env python3
"""db access module for mfchargen"""

import tinydb
from tinydb.operations import delete
import gen_char

def query_by_name(name=''):
    """retrieve character from db by name"""

    db = tinydb.TinyDB('chars.json')
    char_query = tinydb.Query()
    try:
        this_char = db.search(char_query.name == name)[0]
    except IndexError:
        this_char = None
    db.close()
    return this_char

def insert_char(character):
    """insert a character dictionary into db"""

    db = tinydb.TinyDB('chars.json')
    db.insert(character)
    db.close()

def rm_by_name(name):
    db = tinydb.TinyDB('chars.json')
    char_query = tinydb.Query()
    db.remove(char_query.name == name)
    db.close()

if __name__ == '__main__':

    CHARACTER = gen_char.char()
    insert_char(CHARACTER)
    RET_CHAR = query_by_name(CHARACTER['name'])
    print(RET_CHAR)
    rm_by_name(CHARACTER['name'])

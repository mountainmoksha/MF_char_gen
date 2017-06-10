#!/usr/bin/env python3
"""db access module for mfchargen"""

import tinydb
import gen_char

def query_by_name(name=''):
    """retrieve character from db by name"""

    db = tinydb.TinyDB('chars.json')
    char_query = tinydb.Query()
    this_char = db.search(char_query.name == name)[0]
    db.close()

def insert_char(character):
    """insert a character dictionary into db"""

    db = tinydb.TinyDB('chars.json')
    db.insert(character)
    db.close()

if __name__ == '__main__':

    CHARACTER = gen_char.char()

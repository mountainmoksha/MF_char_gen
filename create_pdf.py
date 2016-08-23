#!/usr/bin/env python3
"""take a character dict, and make a filled-in pdf character sheet from it"""

import os
from reportlab.pdfgen import canvas
from pdfrw import PageMerge, PdfReader, PdfWriter
import gen_char


def combine_pdfs(overlay_file_name):
    """add the previously-created, filled pdf to
       Goblinoid games's stock sheet"""

    base_file_name = 'pdf/mfcharsheet.pdf'
    final_file_name = overlay_file_name.replace('_blank', '')

    overlay_0 = PageMerge().add(PdfReader(overlay_file_name).pages[0])[0]
    overlay_1 = PageMerge().add(PdfReader(overlay_file_name).pages[1])[0]

    trailer = PdfReader(base_file_name)

    page_idx = 0

    for page in trailer.pages:

        if page_idx == 0:
            PageMerge(page).add(overlay_0).render()

        if page_idx == 1:
            PageMerge(page).add(overlay_1).render()

        page_idx = page_idx + 1

    PdfWriter().write(final_file_name, trailer)

    os.remove(overlay_file_name)

    return final_file_name

def gen_char_pdf(character):
    """put the numbers and words from a character on a "blank" sheet
       to be added to the stock sheet"""

    if 'name' in character:
        file_name = 'char_pdfs/' + character['name'].replace(' ', '_') + '_blank.pdf'
    else:
        file_name = 'char_pdfs/' + character['alt-name'].replace(' ', '_') + '_blank.pdf'

    character_canvas = canvas.Canvas(file_name)

    character_canvas.drawString(77, 528, str((character['attributes'])['Strength']))
    character_canvas.drawString(77, 488, str((character['attributes'])['Dexterity']))
    character_canvas.drawString(77, 446, str((character['attributes'])['Constitution']))
    character_canvas.drawString(77, 402, str((character['attributes'])['Intelligence']))
    character_canvas.drawString(77, 360, str((character['attributes'])['Willpower']))
    character_canvas.drawString(77, 318, str((character['attributes'])['Charisma']))

    if 'name' in character:
        character_canvas.drawString(246, 683, str(character['name']))

    if 'sub_type' in character:
        character_canvas.drawString(446, 700, str(character['type']))
        character_canvas.drawString(446, 683, '(' + str(character['sub_type']) + ')')
    else:
        character_canvas.drawString(446, 683, str(character['type']))

    character_canvas.drawString(373, 647, str(character['level']))
    character_canvas.drawString(480, 647, str(character['XP']))
    character_canvas.drawString(413, 575, str(character['HP']))
    character_canvas.drawString(508, 575, str(character['AC']))

    character_canvas.drawString(408, 483, str(character['energy_save']))
    character_canvas.drawString(408, 439, str(character['poison_death_save']))
    character_canvas.drawString(408, 393, str(character['stun_save']))
    character_canvas.drawString(408, 347, str(character['rad_save']))

    character_canvas.drawString(222, 538, str(character['str_mod']))

    character_canvas.drawString(222, 498, str(character['ac_mod']))
    character_canvas.drawString(292, 498, str(character['missile_mod']))

    character_canvas.drawString(222, 455, str(character['poison_mod']))
    character_canvas.drawString(292, 455, str(character['rad_mod']))

    character_canvas.drawString(217, 410, str(character['tech_mod']))

    character_canvas.drawString(221, 330, str(character['reaction_mod']))

    mutations_current_height = 250

    if (character['plant'])[0] != '':
        character_canvas.drawString(75, mutations_current_height, 'Plant Mutations:')
        mutations_current_height = mutations_current_height - 13
        for mutation in character['plant']:
            character_canvas.drawString(85, mutations_current_height, mutation)
            mutations_current_height = mutations_current_height - 13

    if (character['physical'])[0] != '':
        character_canvas.drawString(75, mutations_current_height, 'Physical Mutations:')
        mutations_current_height = mutations_current_height - 13
        for mutation in character['physical']:
            character_canvas.drawString(85, mutations_current_height, mutation)
            mutations_current_height = mutations_current_height - 13

    if (character['mental'])[0] != '':
        character_canvas.drawString(75, mutations_current_height, 'Mental Mutations:')
        mutations_current_height = mutations_current_height - 13
        for mutation in character['mental']:
            character_canvas.drawString(85, mutations_current_height, mutation)
            mutations_current_height = mutations_current_height - 13

    # this advances us to page 2:
    character_canvas.showPage()

    character_canvas.drawString(360, 270, str(character['GP']) + ' GP')

    character_canvas.save()

    return file_name

if __name__ == '__main__':

    CHARACTER = gen_char.char()

    FILE_NAME = gen_char_pdf(CHARACTER)

    print(combine_pdfs(FILE_NAME))

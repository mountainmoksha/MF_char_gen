#!/usr/bin/env python3
"""take a character dict, and make a filled-in pdf character sheet from it"""

import os
from reportlab.pdfgen import canvas
from pdfrw import PageMerge, PdfReader, PdfWriter
import xml.dom.minidom
import gen_char


def combine_pdfs(character, overlay_file_name):
    """add the previously-created, filled pdf to
       Goblinoid games's stock sheet"""

    total_pages = 2
    if (character['plant'])[0] != '':
        total_pages += 1
    if (character['physical'])[0] != '':
        total_pages += 1
    if (character['mental'])[0] != '':
        total_pages += 1

    base_file_name = 'pdf/mfcharsheet_' + str(total_pages) + '_page.pdf'
    final_file_name = overlay_file_name.replace('_blank', '')

    trailer = PdfReader(base_file_name)

    page_idx = 0

    for page in trailer.pages:

        overlay = PageMerge().add(PdfReader(overlay_file_name).pages[page_idx])[0]
        PageMerge(page).add(overlay).render()

        page_idx = page_idx + 1

    PdfWriter().write(final_file_name, trailer)

    os.remove(overlay_file_name)

    return final_file_name

def gen_char_pdf(character):
    """put the numbers and words from a character on a "blank" sheet
       to be added to the stock sheet"""

    file_name = 'mutations_descriptions.xml'
    xml_p = open(file_name, 'r')
    xml_string = xml_p.read()
    xml_p.close()
    doc_obj = xml.dom.minidom.parseString(xml_string)

    if 'name' in character:
        file_name = 'char_pdfs/' + character['name'].replace(' ', '_') + '_blank.pdf'
    else:
        file_name = 'char_pdfs/' + character['alt-name'].replace(' ', '_') + '_blank.pdf'

    character_canvas = canvas.Canvas(file_name)
    character_canvas.setFont('Courier-BoldOblique', 10)
    character_canvas.setFillColorRGB(1.0, 0.0, 0.0)

    character_canvas.drawString(77, 528, str((character['attributes'])['Strength']))
    character_canvas.drawString(77, 488, str((character['attributes'])['Dexterity']))
    character_canvas.drawString(77, 446, str((character['attributes'])['Constitution']))
    character_canvas.drawString(77, 402, str((character['attributes'])['Intelligence']))
    character_canvas.drawString(77, 360, str((character['attributes'])['Willpower']))
    character_canvas.drawString(77, 318, str((character['attributes'])['Charisma']))

    if 'name' in character:
        character_canvas.drawString(246, 683, str(character['name']))

    if 'sub_type' in character:
        character_canvas.drawString(456, 697, str(character['type']))
        character_canvas.drawString(456, 686, '(' + str(character['sub_type']) + ')')
    else:
        character_canvas.drawString(456, 686, str(character['type']))

    character_canvas.drawString(373, 647, str(character['level']))
    character_canvas.drawString(480, 647, str(character['XP']))
    character_canvas.drawString(415, 575, str(character['HP']))
    character_canvas.drawString(513, 575, str(character['AC']))

    character_canvas.drawString(409, 483, str(character['energy_save']))
    character_canvas.drawString(409, 439, str(character['poison_death_save']))
    character_canvas.drawString(409, 393, str(character['stun_save']))
    character_canvas.drawString(409, 347, str(character['rad_save']))

    character_canvas.drawString(222, 538, str(character['str_mod']))

    character_canvas.drawString(222, 498, str(character['ac_mod']))
    character_canvas.drawString(292, 498, str(character['missile_mod']))

    character_canvas.drawString(222, 455, str(character['poison_mod']))
    character_canvas.drawString(292, 455, str(character['rad_mod']))

    character_canvas.drawString(217, 410, str(character['tech_mod']))

    character_canvas.drawString(221, 330, str(character['reaction_mod']))

    mutations_current_height = 250

    if 'level_modifiers' in character:
        character_canvas.drawString(75, mutations_current_height, 'Level Modifiers:')
        mutations_current_height = mutations_current_height - 13
        for level_mod_key in character['level_modifiers']:
            character_canvas.drawString(85, mutations_current_height, (character['level_modifiers'])[level_mod_key])
            mutations_current_height = mutations_current_height - 13

    # this advances us to page 2:
    character_canvas.showPage()
    character_canvas.setFont('Courier-BoldOblique', 8)
#    print(character_canvas.getAvailableFonts())
    character_canvas.setFillColorRGB(0.0, 0.0, 1.0)

    # top of page, on these sheets
    mutations_current_height = 670

    if (character['plant'])[0] != '':
        character_canvas.drawString(75, mutations_current_height, 'Plant Mutations:')
        mutations_current_height -= 9
        for mutation in character['plant']:
            character_canvas.drawString(85, mutations_current_height, mutation)
            mutations_current_height -= 9
            # put in description
            text = doc_obj.getElementsByTagName(mutation.replace(' ', '_'))
            try:
                lines = text[0].firstChild.nodeValue
                for line in lines.split('\n'):
                    character_canvas.drawString(95, mutations_current_height, line)
                    mutations_current_height -= 9
            except IndexError:
                print(mutation.replace(' ', '_'), 'not found')
        # this advances us to the next page
        character_canvas.showPage()
        character_canvas.setFont('Courier-BoldOblique', 8)
        character_canvas.setFillColorRGB(0.0, 0.0, 1.0)

    # top of page, on these sheets
    mutations_current_height = 670

    if (character['physical'])[0] != '':
        character_canvas.drawString(75, mutations_current_height, 'Physical Mutations:')
        mutations_current_height -= 9
        for mutation in character['physical']:
            character_canvas.drawString(85, mutations_current_height, mutation)
            mutations_current_height -= 9
            # put in description
            text = doc_obj.getElementsByTagName(mutation.replace(' ', '_'))
            try:
                lines = text[0].firstChild.nodeValue
                for line in lines.split('\n'):
                    character_canvas.drawString(95, mutations_current_height, line)
                    mutations_current_height -= 9
            except IndexError:
                print(mutation.replace(' ', '_'), 'not found')
        # this advances us to the next page
        character_canvas.showPage()
        character_canvas.setFont('Courier-BoldOblique', 8)
        character_canvas.setFillColorRGB(0.0, 0.0, 1.0)

    # top of page, on these sheets
    mutations_current_height = 670

    if (character['mental'])[0] != '':
        character_canvas.drawString(75, mutations_current_height, 'Mental Mutations:')
        mutations_current_height -= 9
        for mutation in character['mental']:
            character_canvas.drawString(85, mutations_current_height, mutation)
            mutations_current_height -= 9
            # put in description
            text = doc_obj.getElementsByTagName(mutation.replace(' ', '_'))
            try:
                lines = text[0].firstChild.nodeValue
                for line in lines.split('\n'):
                    character_canvas.drawString(95, mutations_current_height, line)
                    mutations_current_height -= 9
            except IndexError:
                print(mutation.replace(' ', '_'), 'not found')
        # this advances us to the next page
        character_canvas.showPage()
        character_canvas.setFont('Courier-BoldOblique', 8)
        character_canvas.setFillColorRGB(0.5, 0.0, 0.5)

    # do this (potentially again) here, in case there
    # weren't any mutations
    character_canvas.setFont('Courier-BoldOblique', 10)
    character_canvas.setFillColorRGB(0.5, 0.0, 0.5)

    character_canvas.drawString(360, 270, str(character['GP']) + ' GP')

    character_canvas.save()

    return file_name

if __name__ == '__main__':

    CHARACTER = gen_char.char()

    FILE_NAME = gen_char_pdf(CHARACTER)

    print(combine_pdfs(CHARACTER, FILE_NAME))

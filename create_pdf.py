#!/usr/bin/env python3    

import os
from reportlab.pdfgen import canvas
from pdfrw import PageMerge, PdfReader, PdfWriter
import gen_char


def combine_pdfs(overlay_file_name):

    base_file_name = 'pdf/mfcharsheet.pdf'
    final_file_name = overlay_file_name.replace('_blank', '')

    overlay_1 = PageMerge().add(PdfReader(overlay_file_name).pages[0])[0]

    trailer = PdfReader(base_file_name)

    page_idx = 0

    for page in trailer.pages:

        if page_idx == 0:
            PageMerge(page).add(overlay_1).render()

        page_idx = page_idx + 1

    PdfWriter().write(final_file_name, trailer)

    os.remove(overlay_file_name)

    return final_file_name

def gen_char_pdf(character):

    file_name = 'char_pdfs/' + character['name'].replace(' ', '_') + '_blank.pdf'
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

    character_canvas.drawString(370, 647, str(character['level']))
    character_canvas.drawString(413, 575, str(character['HP']))
    character_canvas.drawString(508, 575, str(character['AC']))

    character_canvas.drawString(222, 538, str(character['str_mod']))

    character_canvas.showPage()
    character_canvas.save()

    return file_name

if __name__ == '__main__':

    CHARACTER = gen_char.char()

    FILE_NAME = gen_char_pdf(CHARACTER)

    print(combine_pdfs(FILE_NAME))

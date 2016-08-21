#!/usr/bin/env python3    

import os
from reportlab.pdfgen import canvas
from pdfrw import PageMerge, PdfReader, PdfWriter
import gen_char


def combine_pdfs(overlay_file_name):

    base_file_name = 'char_pdfs/mfcharsheet.pdf'
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
    c = canvas.Canvas(file_name)
    c.drawString(100, 100, "Hello World")
    c.drawString(200, 200, str(1))
    c.showPage()
    c.save()

    return file_name

if __name__ == '__main__':

    CHARACTER = gen_char.char()

    FILE_NAME = gen_char_pdf(CHARACTER)

    print('created ' + combine_pdfs(FILE_NAME))

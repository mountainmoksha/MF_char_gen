#!/usr/bin/env python3    

from reportlab.pdfgen import canvas
import gen_char

def gen_char_pdf(character):
    c = canvas.Canvas('char_pdfs/' + character['name'] + '.pdf')
    c.drawString(100, 100, "Hello World")
    c.drawString(200, 200, str(1))
    c.showPage()
    c.save()

if __name__ == '__main__':
    character = gen_char.char()
    gen_char_pdf()

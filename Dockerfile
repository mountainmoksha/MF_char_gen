FROM python:3

COPY . /MF_char_gen/

RUN python3 -m pip install reportlab pdfrw

CMD cd /MF_char_gen/ && ./create_pdf.py

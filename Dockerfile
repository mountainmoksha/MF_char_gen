FROM python:3

COPY . /MF_char_gen/

RUN python3 -m pip install reportlab pdfrw tornado tinydb
WORKDIR /MF_char_gen
ENTRYPOINT ["python3"]
CMD ["/MF_char_gen/tornado_mf.py"]

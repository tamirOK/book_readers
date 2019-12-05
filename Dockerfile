FROM python:3.7-slim

COPY init.sh /init.sh
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY books /books

RUN chmod +x init.sh

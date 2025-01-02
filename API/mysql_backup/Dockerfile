FROM python:3.10.6

WORKDIR /backup

COPY requ.txt /backup/

RUN pip install --upgrade pip

RUN pip install -r requ.txt

COPY BackupDatabase.py /backup/

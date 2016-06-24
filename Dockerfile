FROM python:3.5.1

WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
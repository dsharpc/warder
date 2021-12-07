FROM python:3.9-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /warder

ENV ENV PROD

COPY ./warder /warder

CMD python manage.py runserver 0.0.0.0:8000
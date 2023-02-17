FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /djangostripe

COPY requirements.txt /djangostripe//

RUN pip install -r requirements.txt

COPY . /djangostripe/
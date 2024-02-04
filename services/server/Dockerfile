FROM python:3.12-slim-bullseye

COPY . /app
WORKDIR /app

RUN apt update && apt install -y fonts-font-awesome libldap2-dev libsasl2-dev gcc libffi-dev\
    libcairo-gobject2 libpango-1.0-0 libpangoft2-1.0-0 git

RUN pip install -r requirements.txt && \
    pip install psycopg2-binary gunicorn uvicorn django-q2

RUN chmod +x /app/docker/create_settings.sh


RUN /app/docker/create_settings.sh


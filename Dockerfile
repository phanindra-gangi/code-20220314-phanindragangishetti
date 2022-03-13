FROM python:3.9-slim

ENV APP_HOME /usr/src/app

WORKDIR /$APP_HOME

COPY . $APP_HOME

RUN pip3 install -r requirements.txt

CMD python3 app.py

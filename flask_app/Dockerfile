FROM python:alpine3.18


WORKDIR /app


COPY . /app


RUN apk update && apk upgrade && \
    apk add build-base && \
    apk add linux-headers && \
    pip install -r requirements.txt


ENV USER_NAME=""
ENV USER_PWD=""
ENV DB_URL=""


CMD ["uwsgi", "app.ini"]
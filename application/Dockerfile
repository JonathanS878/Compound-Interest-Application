FROM python:alpine3.18


WORKDIR /app


COPY . /app


RUN apk update && apk upgrade && \
    apk add build-base && \
    apk add linux-headers && \
    pip install -r requirements.txt


ENV HOST_NAME=""
ENV MONGO_DB_USERNAME=""
ENV MONGO_DB_PASSWORD=""
ENV SECRET_KEY=""


CMD ["uwsgi", "app.ini"]
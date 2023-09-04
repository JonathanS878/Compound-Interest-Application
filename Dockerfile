FROM python:alpine3.18

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV USER_NAME=""
ENV USER_PWD=""
ENV DB_URL=""

#ENV NAME World

CMD ["python3", "run.py"]

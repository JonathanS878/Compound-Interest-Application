FROM python:alpine3.18


WORKDIR /app


COPY . /app


# Install dependencies
RUN apk update && apk upgrade && \
    apk add build-base && \
    apk add linux-headers && \
    pip install -r requirements.txt


# Create the group and user, set the ownership of the /app, switch to jonathan_shtadler
RUN addgroup -S compound_interest && adduser -S jonathan_shtadler -G compound_interest && \
    chown -R jonathan_shtadler:compound_interest /app


#To enable nginx to serve flask:
RUN chmod 0755 .
    

USER jonathan_shtadler


ENV HOST_NAME=""
ENV MONGO_DB_USERNAME=""
ENV MONGO_DB_PASSWORD=""
ENV SECRET_KEY=""


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
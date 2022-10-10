FROM python:3.7.14-alpine3.15

COPY ./* /service/

WORKDIR /service

RUN pip install -r requirements.txt

CMD ['flask --app UpdateServiceController run']



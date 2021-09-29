FROM python:3.8.12-alpine3.14

ARG TARGET_ENV=develop
RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev libffi-dev
RUN pip3 install -U pip

RUN mkdir -p /app
ADD requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

ADD ./src /app/src
ENV PYTHONPATH /app/src

WORKDIR /app
CMD ["python3", "-m", "src"]

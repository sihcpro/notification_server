FROM alpine:latest

ARG TARGET_ENV=develop
RUN apk add --no-cache python3 py3-pip build-base python3-dev libxslt-dev libxml2-dev
RUN pip3 install -U pip
RUN mkdir -p /app/src

ENV PYTHONPATH /app/src/

ADD requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

ADD docker/x-run /app/
ADD ./env/$TARGET_ENV/secret.py /app/notification_server/secret.py
ADD ./.build/ /app/

CMD ["sh", "/app/x-run"]

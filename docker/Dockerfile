FROM alpine:latest

ARG TARGET_ENV=staging
RUN apk add --no-cache python3 py3-pip build-base python3-dev nginx wkhtmltopdf py3-cryptography
RUN pip3 install -U pip
RUN mkdir -p /app/src

ENV PYTHONPATH /app/src/:/app/lib/
ENV FII_APP_CONFIG_FILE=/app/config.ini

ADD requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

ADD docker/x-run /app/
ADD ./.build/ /app/

CMD ["sh", "/app/x-run"]

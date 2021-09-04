FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./quizproject /quizproject

WORKDIR /quizproject
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk add zlib-dev jpeg-dev gcc musl-dev && \
    #/py/bin/pip install Pillow && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home quizproject

ENV PATH="/py/bin:$PATH"

USER quizproject
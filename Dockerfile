FROM python:3.9-slim-buster

ARG APP_NAME
ARG ENVIRONMENT

ENV APP_NAME=${APP_NAME}
ENV ENVIRONMENT=${ENVIRONMENT}

ENV WORK_DIR=/usr/src/app
ENV REQUIREMENTS_DIR=/usr/src/requirements

WORKDIR ${WORK_DIR}

RUN apt-get update && apt-get install -qq -y \ 
  build-essential \
  libpq-dev \
  gcc \
  g++ \
  git --no-install-recommends

# RUN apt install --qq -y build-essential

COPY ./requirements ${REQUIREMENTS_DIR}/

RUN pip install -r ${REQUIREMENTS_DIR}/${ENVIRONMENT}.txt

COPY ${APP_NAME}/ ${WORK_DIR}/
COPY ./deploy/vhostd.conf ${WORK_DIR}/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
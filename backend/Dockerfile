FROM python:3.11
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        musl-dev \
        libpq-dev \
        libjpeg-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libopenjp2-7-dev \
        libtiff5-dev \
        tk-dev \
        tcl-dev \
        libffi-dev \
        gettext \
        postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code

WORKDIR /code
RUN pip install pipenv

COPY Pipfile Pipfile.lock requirements.txt /code/

RUN pipenv install --system --deploy

RUN pipenv install -r requirements.txt

COPY . /code/
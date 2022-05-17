FROM python:3.9.8-slim-buster

RUN apt-get update \
    && mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man7 \
    && apt-get install -y \
    binutils \
    build-essential \
    gdal-bin \
    git \
    libcairo2 \
    libffi-dev \
    libgdk-pixbuf2.0-0 \
    libmagic1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libpq-dev \
    libproj-dev \
    libssl-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libxmlsec1-openssl \
    pdftk \
    pkg-config \
    python3-cffi \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    shared-mime-info \
    supervisor \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /rock

RUN pip install --upgrade pip poetry==1.1.10

RUN poetry config virtualenvs.create false
RUN poetry config experimental.new-installer false

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install

COPY ./ /rock/

RUN poetry install

WORKDIR /rock

EXPOSE 8080

ENV PYTHONPATH /rock
ENV COLUMNS 80

CMD ["/bin/bash"]

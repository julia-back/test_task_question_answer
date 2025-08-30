FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry --no-cache-dir

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY . .

EXPOSE 8000

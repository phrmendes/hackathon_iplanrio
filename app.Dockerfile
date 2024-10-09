FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

RUN useradd -ms /bin/bash -u 1001 app && chown -R app:app /app

USER app

COPY ./app/pyproject.toml ./app/uv.lock /app/

RUN uv sync --no-dev

COPY ./app /app

EXPOSE 8000

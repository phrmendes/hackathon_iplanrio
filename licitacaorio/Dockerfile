FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

RUN useradd -ms /bin/bash -u 1001 app && chown -R app:app /app

USER app

COPY . /app

RUN uv sync --no-dev

EXPOSE 8000

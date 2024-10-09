FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /ollama

RUN useradd -ms /bin/bash -u 1001 ollama && chown -R ollama:ollama /ollama

USER ollama

COPY ./ollama/pyproject.toml ./ollama/uv.lock /ollama/

RUN uv sync --no-dev

COPY ./ollama /ollama

EXPOSE 8000

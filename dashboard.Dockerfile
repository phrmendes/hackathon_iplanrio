FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /dashboard

RUN useradd -ms /bin/bash -u 1001 dashboard && chown -R dashboard:dashboard /dashboard

USER dashboard

COPY ./dashboard/pyproject.toml ./dashboard/uv.lock /dashboard/

RUN uv sync --no-dev

COPY ./dashboard /dashboard

EXPOSE 8000

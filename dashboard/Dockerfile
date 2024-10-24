FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

RUN useradd -ms /bin/bash -u 1001 app && chown -R app:app /app

USER app

COPY ./dashboard/* /app

RUN uv sync --no-dev

EXPOSE 8001

CMD ["uv", "run", "--no-dev", "uvicorn", "app:app", "--server.port", "8001", "--server.address", "0.0.0.0"]

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./licitacaorio /app

RUN useradd -ms /bin/bash -u 1001 app && chown -R app:app /app

USER app

RUN uv sync --no-dev

EXPOSE 8000

CMD ["uv", "run", "--no-dev", "uvicorn", "licitacaorio.asgi:application", "--host", "0.0.0.0", "--port", "8000"]

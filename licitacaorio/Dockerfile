FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ARG SECRET_KEY

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./licitacaorio /app

RUN useradd -ms /bin/bash -u 1001 app && chown -R app:app /app

USER app

RUN uv run --no-dev python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["uv", "run", "--no-dev", "gunicorn", "--bind", "0.0.0.0:8000", "licitacaorio.asgi", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]

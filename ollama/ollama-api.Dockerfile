FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY ./ollama/app.py ./ollama/pyproject.toml ./ollama/uv.lock /app/

RUN useradd -ms /bin/bash -u 1001 app && chown -R app:app /app

USER app

RUN uv sync --no-dev

EXPOSE 8000

CMD ["uv", "run", "--no-dev", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

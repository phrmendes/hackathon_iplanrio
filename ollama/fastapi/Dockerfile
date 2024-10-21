FROM python:3.11-slim

WORKDIR /app

COPY ./ollama/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Comando para rodar a aplicação
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8002"]
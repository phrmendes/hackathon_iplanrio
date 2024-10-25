#!/usr/bin/env bash

./bin/ollama serve &

pid=$!

sleep 5

echo "Pulling llama3.2:3b model"

ollama pull llama3.2:3b

wait "${pid}"

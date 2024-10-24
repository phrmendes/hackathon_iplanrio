FROM ollama/ollama:0.3.14

COPY ./ollama/pull-model.sh /pull-model.sh

EXPOSE 11434

ENTRYPOINT ["/usr/bin/bash", "/pull-model.sh"]

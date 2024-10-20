# Base image from ghcr.io with Python 3.12 and necessary tools
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory inside the container
WORKDIR /ollama

# Create a new user 'ollama' with user ID 1001 and change ownership of the working directory
RUN useradd -ms /bin/bash -u 1001 ollama && chown -R ollama:ollama /ollama

# Switch to the 'ollama' user
USER ollama

# Copy dependency files for building the environment
COPY ./ollama/pyproject.toml ./ollama/uv.lock /ollama/

# Sync dependencies without dev dependencies using uv
RUN uv sync --no-dev

# Copy the rest of the application files
COPY ./ollama /ollama

# Expose port 8000 for the FastAPI app or other services
EXPOSE 8000

# Now integrate the base from the ollama image
# Use 'ollama/ollama' as base and copy the pull script
FROM ollama/ollama

# Copy the script to pull the llama3 model
COPY ./ollama/pull-llama3.sh /pull-llama3.sh

# Execute the pull script to download the llama3 model
ENTRYPOINT ["/usr/bin/bash", "/pull-llama3.sh"]

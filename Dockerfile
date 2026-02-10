# Use a slim Python image
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./
COPY main.py index.html ./

# Install dependencies using uv
RUN uv sync --frozen --no-cache

# Expose the port (FastAPI will run inside on 8000, 
# Docker will map it to 7000 via docker-compose)
EXPOSE 8000

# Run the application
CMD ["uv", "run", "python", "main.py"]

# Base image.
FROM python:3.14-slim

# Install dependencies and Microsoft SQL ODBC driver (Debian 12+ compatible)
RUN apt-get update && \
    apt-get install -y curl apt-transport-https gnupg2 ca-certificates && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
        | gpg --dearmor -o /etc/apt/keyrings/microsoft.gpg && \
    curl -fsSL https://packages.microsoft.com/config/debian/12/prod.list \
        -o /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


# Working directory set karein.
WORKDIR /app

# Copy project files
COPY . .

# Dependencies install karein uv.lock file se.
# --locked flag se ye ensure hota hai ke sirf wohi versions install hon jo lock file mein hain.
RUN uv sync --locked

# Default port expose karein.
EXPOSE 8000

# Application run karein.
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port","8000"]
# syntax=docker/dockerfile:1
FROM python:3.11-slim-buster as builder

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Install system dependencies, including ca-certificates and a newer SQLite
# We remove libsqlite3-mod-csv as it's not found in Debian Buster.
# Keep build-essential and libpq-dev as they are commonly needed.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    build-essential \
    libpq-dev \
    sqlite3 \
    libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

# Fix for Python's sqlite3 module to link to the newly installed libsqlite3
# This forces the built-in sqlite3 module to use the system's updated library
RUN rm /usr/local/lib/python*/__pycache__/_sqlite3.cpython-*.pyc || true && \
    rm /usr/local/lib/python*/_sqlite3.cpython-*.so || true && \
    pip install --no-cache-dir pysqlite3-binary

COPY . .

EXPOSE 8000

# use a bash file to run the django startup commands
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
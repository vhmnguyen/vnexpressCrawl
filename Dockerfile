# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1


# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN mkdir /app && chmod 755 /app
USER root
# Install system dependencies
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential python3-pip && \
    apt-get clean

# Use pip for Python packages
RUN pip3 install --upgrade pip

## Download dependencies as a separate step to take advantage of Docker's caching.
## Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
## Leverage a bind mount to requirements.txt to avoid having to copy them into
## into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


COPY . /app
WORKDIR /app
USER appuser

# Expose the port that the application listens on.
EXPOSE 8000

# Add environment variables for the database connection
# Run the application.
CMD ["python", "main.py"]

# syntax=docker/dockerfile:1

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app
# ENV PYTHONPATH=/app

EXPOSE 2022

# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 2022 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENTRYPOINT ["/bin/sh", "-c" , "python -m aiohttp.web --host 0.0.0.0 --port 2022 discr:main --config_file ./config/local.yaml"]

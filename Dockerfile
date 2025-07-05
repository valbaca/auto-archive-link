FROM python:3.12.11-slim-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV UV_NO_INDEX=1
ENV DEBIAN_FRONTEND=noninteractive

RUN pip install --no-cache-dir uv
COPY pyproject.toml ./
RUN uv pip install --system -r pyproject.toml
COPY . .

CMD ["uv", "run", "main.py"]
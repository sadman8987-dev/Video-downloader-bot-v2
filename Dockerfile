FROM denoland/deno:bin AS deno

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

COPY --from=deno /deno /usr/local/bin/deno

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg aria2 ca-certificates curl git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip wheel \
    && pip install -r requirements.txt \
    && python -m pip install --no-cache-dir --upgrade 'setuptools>=78.1.1'

COPY main.py youtube_handler.py smart_download_engine.py .
RUN useradd --create-home --uid 10001 --shell /usr/sbin/nologin botuser \
    && chown -R botuser:botuser /app

USER 10001:10001

CMD ["python", "main.py"]

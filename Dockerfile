FROM python:3.13.5-alpine

# Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from creating .pyc files. Docker containers don't need compiled bytecode files. This keeps containers clean
# PYTHONUNBUFFERED: its for debugging. Makes Python output appear immediately in Docker logs. Without this, you won't see Django logs in real-time
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY ./requirements /requirements
COPY ./src /src
COPY ./scripts /scripts

# Install system dependencies
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev

WORKDIR src

EXPOSE 8000

RUN pip install --no-cache-dir -r /requirements/development.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home djshop && \
    chown -R djshop:djshop /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:$PATH"

USER djshop

CMD ["run.sh"]
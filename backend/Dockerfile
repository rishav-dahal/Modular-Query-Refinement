FROM python:3.11-slim

WORKDIR /backend

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1



# Install build tools and scientific libraries for Python packages with native extensions
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		build-essential \
		gcc \
		g++ \
		git \
		libopenblas-dev \
		liblapack-dev \
		libffi-dev \
		libxml2-dev \
		libxslt1-dev \
		zlib1g-dev \
		libjpeg-dev \
		libpng-dev \
		libpq-dev \
		curl \
	&& rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .






FROM python:3.11.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
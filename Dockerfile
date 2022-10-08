FROM python:3.10.6-alpine3.16
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update \
    && pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "entrypoint.sh"]
FROM python:3.8-slim
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .
RUN touch .env

CMD ["gunicorn", "core.wsgi", "--bind", "0.0.0.0:8000"]

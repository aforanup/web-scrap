FROM python:3.8-slim
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN touch .env
RUN python manage.py collectstatic

CMD ["gunicorn", "core.wsgi", "--bind", "0.0.0.0:8000"]

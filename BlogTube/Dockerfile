FROM python:3.11.1-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Mounts the application code to the image
COPY . .

EXPOSE 8000

CMD python manage.py runserver

FROM python:3.7
RUN pip install django gunicorn whitenoise
COPY ./ /django_auth
WORKDIR django_auth
EXPOSE 8000
CMD gunicorn django_auth.wsgi -b :8000 --workers 5
#CMD python manage.py runserver 0.0.0.0:8000
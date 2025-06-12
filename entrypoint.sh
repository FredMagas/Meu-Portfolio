#!/bin/sh

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput

# Inicia o gunicorn
exec gunicorn portfolioweb.wsgi:application --bind 0.0.0.0:8000
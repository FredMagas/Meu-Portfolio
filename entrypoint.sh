#!/bin/sh

echo ">>> [Entrypoint] Rodando migrate check"
python manage.py makemigrations --check --dry-run

echo ">>> [Entrypoint] Rodando migrate"
python manage.py migrate --noinput

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput

# Inicia o gunicorn
exec gunicorn portfolioweb.wsgi:application --bind 0.0.0.0:8000
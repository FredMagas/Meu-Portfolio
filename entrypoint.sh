#!/bin/sh
set -e

# ── Banco de dados ──
if [ -f /run/secrets/db_password ]; then
    export POSTGRES_PASSWORD=$(cat /run/secrets/db_password)
fi

echo ">>> [Entrypoint] Rodando migrate check"
python manage.py makemigrations --check --dry-run

echo ">>> [Entrypoint] Rodando migrate"
python manage.py migrate --noinput

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput

# Inicia o gunicorn
exec gunicorn portfolioweb.wsgi:application --bind 0.0.0.0:8000
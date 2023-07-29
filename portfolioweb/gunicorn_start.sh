#!/bin/bash

# Ative o ambiente virtual (se estiver usando um)
source C:\Users\Frederico\Documents\Frederico\Programacao\Portfolio\myenv\Scripts\activate

# Defina as variáveis de ambiente, se necessário (isso pode depender do seu projeto)
# export DJANGO_SETTINGS_MODULE="nomedoprojeto.settings"

# Diretório onde está localizado o arquivo wsgi.py
# DJANGO_DIR=portfolioweb.wsgi:application

# Quantidade de processos que o Gunicorn irá executar
NUM_WORKERS=3

# Endereço e porta em que o Gunicorn irá executar (neste exemplo, é localhost:8000)
ADDRESS=127.0.0.1:8000

# Execute o Gunicorn
cd $DJANGO_DIR
gunicorn portfolioweb.wsgi:application --workers=$NUM_WORKERS --bind=$ADDRESS

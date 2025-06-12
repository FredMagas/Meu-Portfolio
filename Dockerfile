# Stage 1: build
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2: runtime
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels
COPY . .

# Coleta estáticos na build (ajuste se preferir no entrypoint)
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "portfolioweb.wsgi:application", "--bind", "0.0.0.0:8000"]
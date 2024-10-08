import psycopg2
import os

DATABASE_URL = os.getenv('DATABASE_URL')

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

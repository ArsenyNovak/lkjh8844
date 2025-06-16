import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='flask_db',
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

def create_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS note(id SERIAL PRIMARY KEY, inputs jsonb);')
    conn.commit()
    cur.close()
    conn.close()

create_db()
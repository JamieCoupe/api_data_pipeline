import sqlite3
from datetime import datetime, timedelta
from .config import DB_FILE, DATA_RETENTION_DAYS
from .logger import logger


def initialize_tarrif_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarrif_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            tarrif_code TEXT NOT NULL,
            service TEXT NOT NULL,
            cost_type TEXT NOT NULL,
            cost INTEGER NOT NULL 
        )
    ''')
    conn.commit()
    conn.close()


def store_tarrif_data(tarrif_code, service, cost_type, cost):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tarrif_data (tarrif_code, service, cost_type, cost)
        VALUES (?, ?, ?, ?)
    ''', (tarrif_code, service, cost_type, cost))
    conn.commit()
    conn.close()


def cleanup_old_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cutoff_date = datetime.now() - timedelta(days=DATA_RETENTION_DAYS)
    cursor.execute('''
        DELETE FROM api_data
        WHERE timestamp < ?
    ''', (cutoff_date,))
    conn.commit()
    conn.close()
    logger.info(f"Old data cleaned up, deleted records older than {cutoff_date}")


def create_tables():
    initialize_tarrif_table()
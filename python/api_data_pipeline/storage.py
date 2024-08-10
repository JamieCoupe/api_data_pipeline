import sqlite3
from datetime import datetime, timedelta
from .config import DB_FILE, DATA_RETENTION_DAYS
from .logger import logger


def initialize_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_name TEXT NOT NULL,
            data TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def store_data(api_name, data):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO api_data (api_name, data)
        VALUES (?, ?)
    ''', (api_name, data))
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

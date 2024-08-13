import sqlite3
from datetime import datetime, timedelta
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import DB_FILE, DATA_RETENTION_DAYS
from logger import logger


def initialize_tarrif_table():
    logger.info(f"Creating TARRIF table")
    logger.debug(f"Connecting to the DB")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        # sql_command = '''
        #     CREATE TABLE IF NOT EXISTS tarrif_data (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        #         tarrif_code TEXT NOT NULL,
        #         service TEXT NOT NULL,
        #         cost_type TEXT NOT NULL,
        #         cost INTEGER NOT NULL
        #     )
        # '''

        sql_command = '''
            CREATE TABLE IF NOT EXISTS tarrif_data (
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                tarrif_code TEXT NOT NULL,
                service TEXT NOT NULL,
                cost_type TEXT NOT NULL,
                cost INTEGER NOT NULL, 
                PRIMARY KEY (tarrif_code, service, cost_type)
            )
        '''
        logger.debug(f"Executing creation command")
        logger.debug(f"Command: {sql_command}")
        cursor.execute(sql_command)
        logger.info(f"Successfully ran the command")

    except Exception as err:
        logger.error(f"Issue creating connection: {err}")

    logger.info(f"Closing DB connection")
    conn.commit()
    conn.close()


def initialize_generation_table():
    logger.info(f"Creating GENERATION table if it doesnt already exist")
    logger.debug(f"Connecting to the DB")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        sql_command = '''
            CREATE TABLE IF NOT EXISTS generation_data (
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                generation_date TEXT NOT NULL PRIMARY KEY,
                generation_from TEXT NOT NULL,
                generation_to TEXT NOT NULL,
                generation INTEGER NOT NULL,
                earned INTEGER NOT NULL
            )
        '''

        logger.debug(f"Executing creation command")
        logger.debug(f"Command: {sql_command}")
        cursor.execute(sql_command)
        logger.info(f"Successfully ran the command")

    except Exception as err:
        logger.error(f"Issue creating connection: {err}")

    logger.info(f"Closing DB connection")
    conn.commit()
    conn.close()


def store_tarrif_data(tarrif_code, service, cost_type, cost):
    initialize_tarrif_table()
    logger.info(f"Adding data to tarrif table if it doesnt already exist")
    logger.debug(f"Connecting to the DB")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        logger.info(f"Adding data, tarrif_code={tarrif_code};service={service};cost_type={cost_type};cost={cost}")
        cursor.execute('''
            INSERT OR REPLACE INTO tarrif_data (tarrif_code, service, cost_type, cost)
            VALUES (?, ?, ?, ?)
        ''', (tarrif_code, service, cost_type, cost))
        logger.info('Successfully added')
    except Exception as err:
        logger.error(f"Issue creating connection: {err}")

    logger.info(f"Closing DB connection")
    conn.commit()
    conn.close()


def store_generation_data(generation_date, generation_from, generation_to, generation, earned):
    initialize_generation_table()
    logger.info(f"Adding data to Generation table")
    logger.debug(f"Connecting to the DB")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        logger.info(f"Adding data, generation_date={generation_date};generation_from={generation_from};generation_to={generation_to};generation={generation};earned={earned}")
        cursor.execute('''
            INSERT OR REPLACE INTO generation_data (generation_date, generation_from, generation_to, generation, earned) 
            VALUES (?, ?, ?, ?, ?)
        ''', (generation_date, generation_from, generation_to, generation, earned))
        logger.info('Successfully added')
    except Exception as err:
        print('ERROR')
        logger.error(f"Issue creating connection: {err}")

    logger.info(f"Closing DB connection")
    conn.commit()
    conn.close()


# def cleanup_old_data():
#     conn = sqlite3.connect(DB_FILE)
#     cursor = conn.cursor()
#     cutoff_date = datetime.now() - timedelta(days=DATA_RETENTION_DAYS)
#     cursor.execute('''
#         DELETE FROM api_data
#         WHERE timestamp < ?
#     ''', (cutoff_date,))
#     conn.commit()
#     conn.close()
#     logger.info(f"Old data cleaned up, deleted records older than {cutoff_date}")


def create_tables():
    initialize_tarrif_table()
    initialize_generation_table()


if __name__ == "__main__":
    create_tables()
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from store_data import fetch_data_from_api
#from storage import initialize_db, store_data, cleanup_old_data
from config import API_URLS
from logger import logger

def main():
    # Initialize the database
    initialize_db()

    # Fetch data from APIs
    for api_name, url in API_URLS.items():
        data = fetch_data_from_api(api_name, url)
        if data and api_name == 'NG_CarbonIntensity':
            store_data(api_name, data)

    # Cleanup old data
    cleanup_old_data()

if __name__ == "__main__":
    logger.info("Starting data fetch process")
    main()
    logger.info("Data fetch process completed")
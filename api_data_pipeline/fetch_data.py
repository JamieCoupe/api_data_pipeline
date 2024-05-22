import requests
from .config import API_URLS
from .logger import logger


def fetch_data_from_api(api_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
        logger.info(f"Data fetched from {api_name}: {data}")
        return data
    except requests.RequestException as e:
        logger.error(f"Error fetching data from {api_name}: {e}")
        return None

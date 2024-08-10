import sys
import os
import pytest

# Assuming the module is in the parent directory of the 'tests' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import your module
from python import api_data_pipeline
from python.api_data_pipeline import logger


def test_initialize_db():
    try:
        api_data_pipeline.initialize_db()
    except Exception as e:
        pytest.fail(f"initialize_db() failed: {e}")


def test_fetch_data_from_api():
    try:
        for api_name, url in api_data_pipeline.API_URLS.items():
            data = api_data_pipeline.fetch_data_from_api(api_name, url)
            assert data is not None, f"fetch_data_from_api({api_name}) returned no data."
            logger.info(f"fetch_data_from_api({api_name}) returned data: {data}")
    except Exception as e:
        pytest.fail(f"fetch_data_from_api() failed: {e}")


def test_store_data():
    try:
        data = '{"example": "data"}'
        api_data_pipeline.store_data('api_test', data)
    except Exception as e:
        pytest.fail(f"store_data() failed: {e}")


def test_cleanup_old_data():
    try:
        api_data_pipeline.cleanup_old_data()
    except Exception as e:
        pytest.fail(f"cleanup_old_data() failed: {e}")


if __name__ == "__main__":
    logger.info("Starting tests...")

    test_initialize_db()
    test_fetch_data_from_api()
    test_store_data()
    test_cleanup_old_data()

    logger.info("Tests completed.")

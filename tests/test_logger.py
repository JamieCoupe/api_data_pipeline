# tests/test_logger.py
import sys
import os

# Assuming the module is in the parent directory of the 'tests' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_data_pipeline import LOGGING, logger


def test_logging_output():
    # Run a logging operation
    logger.info("Test logging message")

    # Check if the log file is created
    assert os.path.exists(LOGGING['filename'])

    # Read the content of the log file
    with open(LOGGING['filename'], 'r') as log_file:
        log_content = log_file.read()

    # Verify that the log message is present in the log file
    assert "Test logging message" in log_content

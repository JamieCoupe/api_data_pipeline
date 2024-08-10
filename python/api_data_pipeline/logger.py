import logging
from .config import LOGGING

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create file handler and set level to debug
file_handler = logging.FileHandler(LOGGING['filename'])
file_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter(LOGGING['format'])

# Add formatter to file handler
file_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)
import logging
import pytest

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler
handler = logging.FileHandler('logfile.log')  # You can also use FileHandler('logfile.log') for file logging
handler.setLevel(logging.DEBUG)

# Create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example test function
def test_example():
    logger.info("This is an info message")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    assert True

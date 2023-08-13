import time
import logging
from util.logger_util import get_logger

logger = get_logger(__name__, level=logging.DEBUG)

def fetch_data() -> list:
    logger.debug("Fetching data..")
    time.sleep(1.5)
    logger.debug("Completed data fetch!")

if __name__ == "__main__":
    print([logging.getLogger(name) for name in logging.root.manager.loggerDict])
    fetch_data()
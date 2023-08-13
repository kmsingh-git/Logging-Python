import time
import logging
from util.logger_util import get_logger

logger = get_logger(__name__, level=logging.DEBUG)

def fetch_data() -> list:
    logger.debug("Fetching data..")
    time.sleep(1.5)
    logger.debug("Completed data fetch!")
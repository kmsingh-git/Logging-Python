"""
This is the main runner of your project
"""
import logging
from util.logger_util import get_logger
from etl.data_fetcher import fetch_data

logger = get_logger(__name__, level=logging.DEBUG)

if __name__ == "__main__":
    logger.info("STARTING ETL PIPELINE")
    fetch_data()
    logger.info("DONE WITH ETL. CYA!")
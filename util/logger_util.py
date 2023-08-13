import logging

def get_logger(name:str, level:int) -> logging.Logger:
    '''
    name: Name of your logger. Usually just pass __name__ to it
    level: Pass the logging level. Use logging module Enums like logging.DEBUG or logging.WARNING
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        , datefmt='%m-%d-%Y %H:%M'
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger

if __name__ == "__main__":
    logger = get_logger(__name__, level=logging.DEBUG)
    logger.warning("I'm testing my get_logger method")
    print(logger.handlers)
    print(logging.basicConfig)
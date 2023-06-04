import logging
from config import ERROR_SERVER_LOG_FILE, LOG_SIZE, ERROR_DB_LOG_FILE
from logging.handlers import RotatingFileHandler


formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(name)

    handler = RotatingFileHandler(log_file, maxBytes=LOG_SIZE * (1024 * 1024), backupCount=1)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


server_logger = setup_logger('server-error-log', ERROR_SERVER_LOG_FILE)
db_logger = setup_logger('db-error-log', ERROR_DB_LOG_FILE)

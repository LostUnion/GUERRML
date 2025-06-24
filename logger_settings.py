import logging

class LoggingFormatter(logging.Formatter):
    def format(self, record):
        record.levelname = record.levelname
        return super().format(record)

logger = logging.getLogger("simple_logger")
handler = logging.StreamHandler()
formatter = LoggingFormatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.disabled = False

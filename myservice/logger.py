import logging
import time

from myservice.config import config
from myservice.config import LogLevelEnum


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


# create logger
logger = logging.getLogger(config.app_name)
logger.setLevel(
    logging.DEBUG if config.log_level == LogLevelEnum.debug else logging.INFO
)

# create console handler and set level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG if config.log_level == LogLevelEnum.debug else logging.INFO)

# create formatter
formatter = UTCFormatter(
    "[%(asctime)s UTC - %(name)s:%(module)s:%(funcName)s - %(levelname)s]  %(message)s"
)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

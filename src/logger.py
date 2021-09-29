import logging
from os import sys

logger = logging.getLogger("notification_server")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(console_handler)

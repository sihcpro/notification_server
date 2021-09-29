import os

REDIS_HOST = os.environ.get("NS_REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("NS_REDIS_PORT", 6379))


SMTP_HOST = os.environ.get("NS_SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = os.environ.get("NS_SMTP_PORT", 587)  # 587: TSL | 465: SSL
SMTP_USER = os.environ.get("NS_SMTP_USER")
SMTP_PASS = os.environ.get("NS_SMTP_PASS")

SMTP_USER_NAME = os.environ.get("NS_SMTP_USER_NAME")

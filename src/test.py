from redis import Redis
from rq.queue import Queue
from rq.serializers import JSONSerializer

from . import settings
from .logger import logger

logger.info("Redis: %s:%s", settings.REDIS_HOST, settings.REDIS_PORT)
redis_queue = Queue(
    name="email",
    connection=Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT),
    serializer=JSONSerializer,
)
logger.info("Connection done")
logger.info("Creating job")
redis_queue.enqueue(
    "mail_job.send_email",
    kwargs=dict(
        recipients=["sihc@yopmail.net"], subject="Test mail service", body="Hello!"
    ),
)
logger.info("Created job")

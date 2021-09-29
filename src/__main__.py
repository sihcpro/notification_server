import os
import time
from urllib.request import urlopen

from redis import Redis
from rq import Connection, Queue, Worker
from rq.serializers import JSONSerializer

from . import settings
from .logger import logger

listen = ["default"]


urlopen("https://www.howsmyssl.com/a/check").read()
if __name__ == "__main__":
    logger.info("Redis: %s:%s", settings.REDIS_HOST, settings.REDIS_PORT)
    redis_queue = Queue(
        name="email",
        connection=Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT),
        serializer=JSONSerializer,
    )
    logger.info("Connection done")
    while True:
        if redis_queue.is_empty():
            time.sleep(1)
        else:
            job_id = redis_queue.pop_job_id()
            job = redis_queue.fetch_job(job_id)
            logger.info("Job [%r]: %r %r", job.id, job.args, job.kwargs)
            try:
                job.perform()
            except Exception as e:
                logger.exception(e)
            # logger.info("-> job: %r", job.args)
            # send_email(*job.args)

    # with Connection(Redis(host=redis_host, port=redis_port)):
    #     worker = Worker(list(map(Queue, listen)))
    #     logger.info("-> %r", worker.__dict__)
    #     worker.work()

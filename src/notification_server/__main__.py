import os
import time
from redis import Redis
from rq import Connection, Queue, Worker

from notification_server.email import send_email

listen = ["default"]


if __name__ == "__main__":
    redis_host = os.environ.get("REDIS_HOST", "localhost")
    redis_port = os.environ.get("REDIS_PORT", 10379)

    # redis_queue = Queue(connection=Redis(host=redis_host, port=redis_port))
    # while True:
    #     if redis_queue.is_empty():
    #         time.sleep(1)
    #         pass
    #     else:
    #         job_id = redis_queue.pop_job_id()
    #         job = redis_queue.fetch_job(job_id)
    #         print("-------------> job", job.args)
    #         send_email(*job.args)

    with Connection(Redis(host=redis_host, port=redis_port)):
        worker = Worker(list(map(Queue, listen)))
        print("------------->", worker.__dict__)
        worker.work()

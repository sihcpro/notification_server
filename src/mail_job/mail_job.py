import time

from redis import Redis
from rq import Queue
from rq.job import Job
from src.logger import logger

from .smtp_mail_server import SMTPMailServer

q = Queue(connection=Redis())


def send_email(
    recipients: list,
    subject,
    body,
    bcc=None,
    from_user=None,
    subtype="html",
    mime_charset="utf-8",
):
    logger.info("Sending email to %r", recipients)
    start = time.time()
    SMTPMailServer.send_smtp_email(
        recipients=recipients,
        subject=subject,
        body=body,
        bcc=bcc,
        from_user=from_user,
        subtype=subtype,
        mime_charset=mime_charset,
    )
    logger.info("Send email to receipients take %s seconds", (str(time.time() - start)))

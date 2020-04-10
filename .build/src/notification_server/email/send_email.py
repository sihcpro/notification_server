import time
from redis import Redis
from rq import Queue

from .smtp_mail_server import send_smtp_email

q = Queue(connection=Redis())


def send_email(
    recipients: list,
    subject,
    body,
    bcc=None,
    subtype="html",
    mime_charset="utf-8",
):
    start = time.time()
    send_smtp_email(
        recipients, subject, body, bcc, subtype, mime_charset,
    )
    print(
        "Send email to receipients take %s seconds"
        % (str(time.time() - start),)
    )

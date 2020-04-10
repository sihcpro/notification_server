import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from notification_server.secret import (
    SMTP_HOST,
    SMTP_PASS,
    SMTP_PORT,
    SMTP_USER,
)

smtp_host = os.environ.get("SMTP_HOST", SMTP_HOST)
smtp_port = os.environ.get("SMTP_PORT", SMTP_PORT)
smtp_user = os.environ.get("SMTP_USER", SMTP_USER)
smtp_pass = os.environ.get("SMTP_PASS", SMTP_PASS)


def send_smtp_email(
    recipients: list,
    subject,
    body,
    bcc=None,
    subtype="html",
    mime_charset="utf-8",
):
    smtp_client = smtplib.SMTP(host=smtp_host, port=smtp_port)
    smtp_client.starttls()
    smtp_client.login(smtp_user, smtp_pass)

    msg = MIMEMultipart()
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg["From"] = smtp_user
    if bcc:
        msg["Bcc"] = ", ".join(bcc)

    msg.attach(MIMEText(body, subtype, mime_charset))

    smtp_client.send_message(msg)

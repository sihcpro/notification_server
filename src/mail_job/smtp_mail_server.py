import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src import settings


class SMTPMailServer:
    # FROM_USER = (
    #     settings.SMTP_USER
    #     if settings.SMTP_USER_NAME is None
    #     else (settings.SMTP_USER, settings.SMTP_USER_NAME)
    # )
    FROM_USER = settings.SMTP_USER

    @classmethod
    def send_smtp_email(
        cls,
        recipients: list,
        subject,
        body,
        bcc=None,
        from_user=None,
        subtype="html",
        mime_charset="utf-8",
    ):
        smtp_client = smtplib.SMTP(host=settings.SMTP_HOST, port=settings.SMTP_PORT)
        smtp_client.starttls()
        smtp_client.login(settings.SMTP_USER, settings.SMTP_PASS)

        msg = MIMEMultipart()
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg["From"] = from_user or cls.FROM_USER
        if bcc:
            msg["Bcc"] = ", ".join(bcc)

        msg.attach(MIMEText(body, subtype, mime_charset))

        smtp_client.send_message(msg)
        smtp_client.close()

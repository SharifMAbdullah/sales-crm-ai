import smtplib
from email.mime.text import MIMEText

SMTP_HOST = "mailhog"
SMTP_PORT = 1025  # MailHog's port


def send_email(lead):
    msg = MIMEText(lead["outreach_email"])
    msg["Subject"] = "Hello from Sales CRM"
    msg["From"] = "sales@example.com"
    msg["To"] = lead["email"]

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(msg)

    print(f"✅ Sent email to {lead['email']}")

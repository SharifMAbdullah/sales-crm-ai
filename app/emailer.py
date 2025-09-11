import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import dotenv

dotenv.load_dotenv()

# Email configuration - load from environment variables
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL", "sales@example.com")


def send_email(lead):
    """
    Send an email to a lead/vendor using configured SMTP settings.
    """
    try:
        msg = MIMEMultipart()
        msg['Subject'] = "Hello from Sales CRM. Second Try!"
        msg['From'] = FROM_EMAIL
        msg['To'] = lead["email"]

        # Add body
        msg.attach(MIMEText(lead["outreach_email"], 'plain'))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()  
            if SMTP_USERNAME and SMTP_PASSWORD:
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print(f"Successfully sent email to {lead['email']}")
        return True

    except smtplib.SMTPAuthenticationError:
        print(f"Authentication failed for {lead['email']}. Check SMTP credentials.")
        return False
    except smtplib.SMTPConnectError:
        print(f"Failed to connect to SMTP server for {lead['email']}")
        return False
    except smtplib.SMTPException as e:
        print(f"SMTP error sending to {lead['email']}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error sending to {lead['email']}: {e}")
        return False

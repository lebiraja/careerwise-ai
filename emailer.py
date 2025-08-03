import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import Dict, Any

def send_email_report(email_address: str, github_data: Dict[str, Any]) -> bool:
    """
    Send a weekly email report to the student with GitHub activity and recommendations.
    Returns True if email is sent successfully, False otherwise.
    """
    try:
        # Load email template
        with open("templates/report_template.html") as f:
            template = f.read()

        # Prepare email content
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = ("lebiraja2007@gmail.com") #replace with your own email
        sender_password = ("Lebi@2007") #replace with your own password

        if not sender_email or not sender_password:
            raise Exception("Missing email credentials")

        # Create message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email_address
        msg["Subject"] = "CareerWise AI Weekly Report"

        # Fill template
        body = template.format(
            repo_count=github_data.get('repo_count', 0),
            languages=', '.join(github_data.get('languages', [])) or 'None',
            total_stars=github_data.get('total_stars', 0),
            commit_frequency=f"{github_data.get('commit_frequency', 0):.2f}"
        )
        msg.attach(MIMEText(body, "html"))

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return True

    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False
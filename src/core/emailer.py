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
        # Get email credentials from environment
        sender_email = os.getenv("EMAIL_ADDRESS", "lebiraja2007@gmail.com")
        sender_password = os.getenv("EMAIL_PASSWORD", "Lebi@2007")
        smtp_server = os.getenv("EMAIL_HOST", "smtp.gmail.com")
        smtp_port = int(os.getenv("EMAIL_PORT", "587"))

        if not sender_email or not sender_password:
            raise Exception("Missing email credentials")

        # Create simple HTML email content
        html_body = f"""
        <html>
        <body>
            <h2>🎯 CareerWise AI Weekly Report</h2>
            <p>Hello! Here's your weekly GitHub activity summary:</p>
            
            <h3>📊 GitHub Statistics</h3>
            <ul>
                <li><strong>Repositories:</strong> {github_data.get('repo_count', 0)}</li>
                <li><strong>Programming Languages:</strong> {', '.join(github_data.get('languages', [])) or 'None'}</li>
                <li><strong>Total Stars:</strong> {github_data.get('total_stars', 0)}</li>
                <li><strong>Average Commits per Repo:</strong> {github_data.get('commit_frequency', 0):.2f}</li>
                <li><strong>README Quality:</strong> {github_data.get('readme_quality', 'N/A')}</li>
            </ul>
            
            <h3>💡 Recommendations</h3>
            <p>Keep coding and improving your projects! Consider:</p>
            <ul>
                <li>Adding more detailed README files to your repositories</li>
                <li>Contributing to open source projects</li>
                <li>Learning new programming languages</li>
            </ul>
            
            <p>Keep up the great work! 🚀</p>
            <p><em>- CareerWise AI Team</em></p>
        </body>
        </html>
        """

        # Create message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email_address
        msg["Subject"] = "CareerWise AI Weekly Report"
        msg.attach(MIMEText(html_body, "html"))

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return True

    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False

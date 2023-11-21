import smtplib
from email.mime.text import MIMEText

def send_phishing_email(target_email):
    # Email configuration
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    subject = 'Important Security Update'

    # Phishing message
    phishing_message = """
    Dear User,

    We have detected a security issue with your account. Please click on the following link to verify your account details:

    http://malicious-website.com/verify

    If you have any concerns, contact our support team immediately.

    Thank you,
    Security Team
    """

    # Create the MIMEText object
    msg = MIMEText(phishing_message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = target_email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())

if __name__ == '__main__':
    # Specify the target email address
    target_email = 'victim@example.com'

    # Send the phishing email
    send_phishing_email(target_email)

import os
import ssl

from dotenvx import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv("../../.env")

SMTP_SERVER = os.environ.get("SMTP_ADDRESS")
SMTP_PORT = os.environ.get("SMTP_PORT")
CONTACT_ME_EMAIL = os.environ.get("CONTACT_EMAIL")
CONTACT_ME_PASSWORD = os.environ.get("CONTACT_PASSWORD")

def send_contact_email(user_data):

	#print(f" data received: \n {user_data}") <-- data is received successfully

	"""Formats and sends the contact form data via SMTP."""
	# Constructing the email body with all form data dynamically
	email_body = f"""
    New Contact Form Submission:

    Name: {user_data.get('name')}
    Email: {user_data.get('email')}
    Subject: {user_data.get('subject')}

    Message:
    {user_data.get('message')}
    """

	msg = MIMEText(email_body)
	msg['Subject'] = f"Contact Form: {user_data.get('subject', 'No Subject')}"
	msg['From'] = CONTACT_ME_EMAIL
	msg['To'] = CONTACT_ME_EMAIL

	try:
		context = ssl.create_default_context()
		# Connect to the SMTP server securely
		with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
			server.set_debuglevel(1)
			server.starttls()
			server.login(CONTACT_ME_EMAIL, CONTACT_ME_PASSWORD)
			server.sendmail(
				from_addr=CONTACT_ME_EMAIL, to_addrs=CONTACT_ME_EMAIL, msg=msg.as_string())
		return True
	except Exception as e:
		print(f"SMTP Error: {e}")
		return False



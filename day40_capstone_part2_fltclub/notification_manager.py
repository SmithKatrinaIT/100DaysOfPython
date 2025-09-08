import os
import smtplib

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self._sender_email = os.environ['SENDER_EMAIL']
        self._password = os.environ['GMAIL_APP_PASSWORD']
        self.twilio_verified_number = os.environ["TWILIO_VERIFIED_NUM"]
        self.whatsapp_number = os.environ["WHATSAPP_PHONE_NUMBER"]
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.smtp_port = os.environ["EMAIL_PROVIDER_SMTP_PORT"]
        self.connection = smtplib.SMTP(self.smtp_address, int(self.smtp_port))


    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{self.whatsapp_number}',
            body=message_body,
            to=f'whatsapp:{self.twilio_verified_number}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()

            # login to email
            self.connection.login(user=self._sender_email, password=self._password)

            # send email
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self._sender_email,
                    to_addrs=email,
                    msg=f"Subject: Here are you flight Deals!\n\n{email_body}".encode('utf-8'))

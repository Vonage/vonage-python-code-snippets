import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_EMAIL = os.environ.get("MESSAGES_TO_EMAIL")
EMAIL_SENDER_ID = os.environ.get("EMAIL_SENDER_ID")

from vonage import Auth, Vonage
from vonage_messages import EmailText, EmailOptions

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = EmailText(
    to=MESSAGES_TO_EMAIL,
    from_=EMAIL_SENDER_ID,
    text='This is an Email text message sent via the Vonage Messages API.',
    email=EmailOptions(
        subject='Your message subject'
    )
)

response = client.messages.send(message)
print(response)

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
from vonage_messages import EmailHtml, EmailHtmlContent, EmailOptions

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = EmailHtml(
    to=MESSAGES_TO_EMAIL,
    from_=EMAIL_SENDER_ID,
    html=EmailHtmlContent(
        body='<h1>Hello from Vonage</h1><p>This is an Email HTML message sent via the Vonage Messages API.</p>'
    ),
    email=EmailOptions(
        subject='Your HTML message subject'
    )
)

response = client.messages.send(message)
print(response)

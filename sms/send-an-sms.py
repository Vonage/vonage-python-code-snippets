import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')
TO_NUMBER = os.getenv('TO_NUMBER')

import nexmo

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

responseData = client.send_message({
    'from': 'Acme Inc',
    'to': TO_NUMBER,
    'text': 'A text message sent using the Nexmo SMS API',
})

if responseData['messages'][0]['status'] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
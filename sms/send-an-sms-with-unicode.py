import os
from os.path import join, dirname
from dotenv import load_dotenv
import vonage

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
TO_NUMBER = os.getenv('TO_NUMBER')
VONAGE_BRAND_NAME = os.getenv('VONAGE_BRAND_NAME')

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

response = client.sms.send_message({
    'from': VONAGE_BRAND_NAME,
    'to': TO_NUMBER,
    'text': 'こんにちは世界',
    'type': 'unicode',
})

if response["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {response['messages'][0]['error-text']}")

import vonage, os

NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')

client = vonage.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

import vonage, os

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

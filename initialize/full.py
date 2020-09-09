import vonage, os

NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')
APPLICATION_ID=os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH=os.environ.get("APPLICATION_PRIVATE_KEY_PATH")

client = vonage.Client(
    key=NEXMO_API_KEY,
    secret=NEXMO_API_SECRET,
    application_id=NEXMO_APPLICATION_ID,
    private_key=NEXMO_APPLICATION_PRIVATE_KEY_PATH
)

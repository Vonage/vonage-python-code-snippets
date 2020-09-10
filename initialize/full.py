import vonage, os

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
APPLICATION_ID = os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH = os.environ.get("APPLICATION_PRIVATE_KEY_PATH")

client = vonage.Client(
    key=VONAGE_API_KEY,
    secret=VONAGE_API_SECRET,
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

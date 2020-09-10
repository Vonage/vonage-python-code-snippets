import vonage, os, getpass
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "./.env")
load_dotenv(envpath)

# Init the client
client = vonage.Client(
    key=os.getenv("VONAGE_API_KEY"), secret=os.getenv("VONAGE_API_SECRET")
)

# Get data from user from keyword
api_key = os.getenv("VONAGE_API_KEY")
# Use getpass instead of input to mask secret
# new_api_secret = getpass.getpass("Enter secret: ")
new_api_secret = os.getenv("NEW_API_SECRET")

# Create the secret
try:
    response = client.create_secret(api_key, new_api_secret)
    if "id" in response:
        print(
            "Secret was created\nId: {}\nCreated at: {}\nLinks: {}".format(
                response["id"],
                response["created_at"],
                response["_links"]["self"]["href"],
            )
        )
except:
    print(
        "Error: Secret does not meet complexity requirements. Please check the link below for more details:\n",
        "https://developer.nexmo.com/api-errors/account/secret-management#validation",
    )

import nexmo, os, getpass
from os.path import join, dirname
from dotenv import load_dotenv

#Load the environment
envpath = join(dirname(__file__),'./.env')
load_dotenv(envpath)

#Init the client
client = nexmo.Client(
    key = os.getenv('NEXMO_API_KEY'),
    secret = os.getenv('NEXMO_API_SECRET')
)

#Get data from user from keyword
api_key = input("Enter your api_key: ")
#Use getpass instead of input to mask secret
new_api_secret = getpass.getpass("Enter secret: ")

#Create the secret
try:
    response = client.create_secret(api_key, new_api_secret)
    if "id" in response:
        print("Key was created\nId: {}\nCreated at: {}\nLinks: {}".format(response["id"], response["created_at"], response["_links"]["self"]["href"]))
except:
    print(
        "Error: Secret does not meet complexity requirements. Please check the link below for more details:\n",
        "https://developer.nexmo.com/api-errors/account/secret-management#validation"
    )

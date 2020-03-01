import nexmo, os
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

try:
    #Get the data from standard input 
    api_key = input("Enter the api key: ")
    secret_id = input("Enter the secret id you want to delete: ")
    client.delete_secret(api_key, secret_id)
    print("Secret removed")
except:
    print("Error when try to removing secret")

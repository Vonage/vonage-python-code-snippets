import os
from os.path import join, dirname

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_SIGNATURE_SECRET = os.getenv("VONAGE_SIGNATURE_SECRET")
VONAGE_SIGNATURE_SECRET_METHOD = os.getenv("VONAGE_SIGNATURE_SECRET_METHOD")

from fastapi import FastAPI, Request
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        api_key=VONAGE_API_KEY,
        signature_secret=VONAGE_SIGNATURE_SECRET,
        signature_method=VONAGE_SIGNATURE_SECRET_METHOD,
    )
)

app = FastAPI()


@app.get('/delivery-receipt')
async def get_delivery_receipt(request: Request):
    data = await request.json()

    if client.http_client.auth.check_signature(data):
        print('Valid signature')
    else:
        print('Invalid signature')

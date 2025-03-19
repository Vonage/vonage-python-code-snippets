import os
from os.path import dirname, join

from dotenv import load_dotenv

envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_SIGNATURE_SECRET = os.getenv("VONAGE_SIGNATURE_SECRET")

from fastapi import FastAPI, Request
from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, signature_secret=VONAGE_SIGNATURE_SECRET))

app = FastAPI()


@app.post('/')
async def verify_signed_webhook(request: Request):
    data = await request.json()

    if client.http_client.auth.check_signature(data):
        print('Valid signature')
    else:
        print('Invalid signature')

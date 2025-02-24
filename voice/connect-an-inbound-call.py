import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI
from vonage_voice import Connect, PhoneEndpoint

VONAGE_NUMBER = os.environ.get('VONAGE_NUMBER')
YOUR_SECOND_NUMBER = os.environ.get('YOUR_SECOND_NUMBER')

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call():
    ncco = [
        Connect(
            endpoint=[PhoneEndpoint(number='123456789')], from_=VONAGE_NUMBER
        ).model_dump(by_alias=True, exclude_none=True)
    ]

    return ncco

import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI
from vonage_voice import Connect, PhoneEndpoint

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_VIRTUAL_NUMBER = os.environ.get('VONAGE_VIRTUAL_NUMBER')
VOICE_VOICE_TO_NUMBER = os.environ.get('VOICE_VOICE_TO_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call():
    ncco = [
        Connect(
            endpoint=[PhoneEndpoint(number=VOICE_VOICE_TO_NUMBER)],
            from_=VONAGE_VIRTUAL_NUMBER,
        ).model_dump(by_alias=True, exclude_none=True)
    ]

    return ncco

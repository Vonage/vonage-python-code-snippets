import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv
from fastapi import Body, FastAPI
from vonage_voice import Connect, NccoAction, PhoneEndpoint, Record

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_VIRTUAL_NUMBER = os.environ.get('VONAGE_VIRTUAL_NUMBER')
VOICE_TO_NUMBER = os.environ.get('VOICE_TO_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call():
    ncco: list[NccoAction] = [
        Record(
            split='conversation',
            channels=2,
            eventUrl=['https://demo.ngrok.io/webhooks/recordings'],
        ),
        Connect(
            from_=VONAGE_VIRTUAL_NUMBER, endpoint=[PhoneEndpoint(number=VOICE_TO_NUMBER)]
        ),
    ]

    return [step.model_dump(by_alias=True, exclude_none=True) for step in ncco]


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}

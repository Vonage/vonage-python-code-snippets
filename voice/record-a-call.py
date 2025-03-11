import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from pprint import pprint
from vonage_voice import Connect, NccoAction, PhoneEndpoint, Record, Talk

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_VIRTUAL_NUMBER = os.environ.get('VONAGE_VIRTUAL_NUMBER')
RECIPIENT_NUMBER = os.environ.get('RECIPIENT_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call():
    ncco: list[NccoAction] = [
        Talk(
            text=f'Hi, we will shortly forward your call. This call is recorded for quality assurance purposes.'
        ),
        Record(eventUrl=['https://demo.ngrok.io/webhooks/recordings']),
        Connect(
            endpoint=[PhoneEndpoint(number=RECIPIENT_NUMBER)],
            from_=VONAGE_VIRTUAL_NUMBER,
            eventUrl=['https://demo.ngrok.io/webhooks/event'],
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}

import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Request
from vonage_voice.models import NccoAction, Notify, Talk

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_NUMBER = os.environ.get('VONAGE_NUMBER')
RECIPIENT_NUMBER = os.environ.get('RECIPIENT_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Thanks for calling the notification line.'),
        Notify(
            payload={"foo": "bar"},
            eventUrl=[str(request.base_url) + '/webhooks/notification'],
        ),
        Talk(text=f'You will never hear me as the notification URL will return an NCCO.'),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/notification')
async def on_notification():
    return [
        Talk(text=f'Your notification has been received, loud and clear').model_dump(
            by_alias=True, exclude_none=True
        )
    ]

import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from pprint import pprint
from vonage_voice import Conversation

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VOICE_CONFERENCE_NAME = os.environ.get('VOICE_CONFERENCE_NAME')

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call():
    ncco = [
        Conversation(
            name=VOICE_CONFERENCE_NAME,
            record=True,
            eventMethod='POST',
            eventUrl=['https://demo.ngrok.io/webhooks/recordings'],
        )
    ]

    return ncco


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}

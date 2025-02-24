import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Request
from vonage_voice import Input, NccoAction, Talk

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_NUMBER = os.environ.get('VONAGE_NUMBER')
RECIPIENT_NUMBER = os.environ.get('RECIPIENT_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Please enter a digit.'),
        Input(
            type=['dtmf'],
            maxDigits=1,
            eventUrl=[str(request.base_url) + '/webhooks/dtmf'],
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/dtmf')
async def answer_dtmf(data: dict = Body(...)):
    return [
        Talk(text=f'Hello, you pressed {data['dtmf']}').model_dump(
            by_alias=True, exclude_none=True
        )
    ]

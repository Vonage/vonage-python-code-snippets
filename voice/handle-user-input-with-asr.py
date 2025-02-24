import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Request
from vonage_voice import Input, NccoAction, Speech, Talk

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_NUMBER = os.environ.get('VONAGE_NUMBER')
RECIPIENT_NUMBER = os.environ.get('RECIPIENT_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Please tell me something.'),
        Input(
            type=['speech'],
            speech=Speech(
                endOnSilence=1,
                language='en-US',
                uuid=[request.query_params.get('uuid')],
            ),
            eventUrl=[str(request.base_url) + '/webhooks/asr'],
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/asr')
async def answer_asr(data: dict = Body(...)):
    if data is not None and 'speech' in data:
        speech = data['speech']['results'][0]['text']
        return [
            Talk(text=f'Hello ,you said {speech}').model_dump(
                by_alias=True, exclude_none=True
            )
        ]
    return [
        Talk(text=f'Sorry, I didn\'t understand your input.').model_dump(
            by_alias=True, exclude_none=True
        )
    ]

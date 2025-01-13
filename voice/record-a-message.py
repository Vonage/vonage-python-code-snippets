from fastapi import FastAPI, Body, Request
from pprint import pprint
from vonage_voice.models import NccoAction, Record, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    print(request.base_url)
    ncco: list[NccoAction] = [
        Talk(text='Please leave a message after the tone, then press the hash key.'),
        Record(
            endOnKey='#',
            beepStart=True,
            eventUrl=[str(request.base_url) + '/webhooks/recordings'],
        ),
        Talk(text='Thank you for your message.'),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}

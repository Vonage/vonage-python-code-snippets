from pprint import pprint
from fastapi import FastAPI, Body, Request
from vonage_voice import Dtmf, Input, NccoAction, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Hello, please press any key to continue.'),
        Input(
            type=['dtmf'],
            dtmf=Dtmf(timeOut=5, maxDigits=1),
            eventUrl=[str(request.base_url) + 'webhooks/dtmf'],
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/dtmf')
async def answer_dtmf(data: dict = Body(...)):
    pprint(data)
    return [
        Talk(text=f'Hello, you pressed {data['dtmf']['digits']}').model_dump(
            by_alias=True, exclude_none=True
        )
    ]

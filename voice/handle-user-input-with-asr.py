from pprint import pprint

from fastapi import Body, FastAPI, Request
from vonage_voice import Input, NccoAction, Speech, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Please say something'),
        Input(
            type=['speech'],
            speech=Speech(endOnSilence=1, language='en-US'),
            eventUrl=[str(request.base_url) + 'webhooks/asr'],
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/asr')
async def answer_asr(data: dict = Body(...)):
    if data is not None and 'speech' in data:
        pprint(data)
        speech = data['speech']['results'][0]['text']
        return [
            Talk(text=f'Hello, you said {speech}').model_dump(
                by_alias=True, exclude_none=True
            )
        ]
    return [
        Talk(text=f'Sorry, I didn\'t understand your input.').model_dump(
            by_alias=True, exclude_none=True
        )
    ]

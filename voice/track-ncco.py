from fastapi import FastAPI, Request
from vonage_voice import NccoAction, Notify, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Thanks for calling the notification line.'),
        Notify(
            payload={"foo": "bar"},
            eventUrl=[str(request.base_url) + 'webhooks/notification'],
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

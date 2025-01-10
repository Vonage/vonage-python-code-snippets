from fastapi import FastAPI, Body
from pprint import pprint

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call():
    ncco = [
        {
            "action": "conversation",
            "name": "CONF_NAME",
            "record": "true",
            "eventMethod": "POST",
            "eventUrl": ["https://demo.ngrok.io/webhooks/recordings"],
        }
    ]

    return ncco


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}

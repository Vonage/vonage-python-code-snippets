from pprint import pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/webhooks/delivery-receipt')
async def get_delivery_receipt(request: Request):
    data = await request.json()
    pprint(data)

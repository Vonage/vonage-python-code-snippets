from fastapi import FastAPI, Request
from pprint import pprint

app = FastAPI()


@app.get('/delivery-receipt')
async def get_delivery_receipt(request: Request):
    data = await request.json()
    pprint(data)

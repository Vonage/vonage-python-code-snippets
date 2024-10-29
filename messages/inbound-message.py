from pprint import pprint
from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/inbound')
async def inbound_message(request: Request):
    data = await request.json()
    pprint(data)

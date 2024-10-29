from pprint import pprint
from fastapi import FastAPI, Request, status

app = FastAPI()


@app.post('/status', status_code=status.HTTP_200_OK)
async def status_message(request: Request):
    data = await request.json()
    pprint(data)


@app.post('/inbound')
async def inbound_message(request: Request):
    data = await request.json()
    pprint(data)

from pprint import pprint
from fastapi import FastAPI, Request, status

app = FastAPI()


@app.post('/webhooks/message-status', status_code=status.HTTP_200_OK)
async def message_status(request: Request):
    data = await request.json()
    pprint(data)

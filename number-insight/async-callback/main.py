from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/webhooks/insight')
async def display_advanced_number_insight_info(request: Request):
    data = await request.json()
    print(data)

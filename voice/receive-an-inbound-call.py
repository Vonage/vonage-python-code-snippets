from fastapi import FastAPI, Query
from vonage_voice import Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(from_: str = Query(..., alias='from')):
    from_ = '-'.join(from_)
    return [
        Talk(text=f'Thank you for calling from {from_}').model_dump(
            by_alias=True, exclude_none=True
        )
    ]

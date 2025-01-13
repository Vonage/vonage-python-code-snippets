import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI
from vonage_voice.models import Conversation, NccoAction, Talk

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_NUMBER = os.environ.get('VONAGE_NUMBER')
YOUR_SECOND_NUMBER = os.environ.get('YOUR_SECOND_NUMBER')
CONFERENCE_NAME = os.environ.get("CONFERENCE_NAME")

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call():
    ncco: list[NccoAction] = [
        Talk(text="Please wait while we connect you to the conference"),
        Conversation(name=CONFERENCE_NAME),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]

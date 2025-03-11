import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI
from vonage_voice import Conversation, NccoAction, Talk

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VOICE_CONFERENCE_NAME = os.environ.get("VOICE_CONFERENCE_NAME")

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call():
    ncco: list[NccoAction] = [
        Talk(text="Please wait while we connect you to the conference"),
        Conversation(name=VOICE_CONFERENCE_NAME),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]

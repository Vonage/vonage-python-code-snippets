import os
from os.path import join, dirname

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)


VONAGE_SIGNATURE = os.getenv('VONAGE_SIGNATURE')

from fastapi import FastAPI, Request
from vonage_jwt.verify_jwt import verify_signature

app = FastAPI()


@app.get('/events')
async def verify_signed_webhook(request: Request):
    # Need to get the JWT after "Bearer " in the authorization header
    auth_header = request.headers["authorization"].split()
    token = auth_header[1].strip()

    if verify_signature(token, VONAGE_SIGNATURE):
        print('Valid signature')
    else:
        print('Invalid signature')

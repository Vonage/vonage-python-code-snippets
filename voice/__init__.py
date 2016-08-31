import json
import requests
import os
import calendar
from datetime import datetime
from base64 import urlsafe_b64encode
from jose import jwt

def generate_token(application_id, key) :
    # Add the unix time at UCT + 0
    d = datetime.utcnow()

    token_payload = {
        "iat": calendar.timegm(d.utctimetuple()),  # issued at
        "application_id": application_id,
        "jti": urlsafe_b64encode(os.urandom(64)).decode('utf-8')
    }

    # generate our token signed with the private key...
    return jwt.encode(
        claims=token_payload,
        key=key,
        algorithm='RS256')

def call(config):
    # Create your JWT
    private_key_file = open(config['PRIVATE_KEY_FILE'], 'r').read()
    jwt = generate_token(config['VOICE_APP_ID'], private_key_file)
    
    print(jwt)
    
    #Set the endpoint
    base_url = "https://api.nexmo.com"
    version = "/beta"
    action = "/calls"

    #Create the headers using the jwt
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer {0}".format(jwt)
    }

    #
    payload = {
        "to":[{
            "type": "phone",
            "number": config['TO_NUMBER']
        }],
        "from": {
            "type": "phone",
            "number": config['FROM_NUMBER']
        },
        "answer_url": ["https://nexmo-community.github.io/ncco-examples/conference.json"],
        "event_url": ["https://voice.ngrok.io/events"]
    }

    response = requests.post( base_url + version + action , data=json.dumps(payload), headers=headers)

    if (response.status_code == 201):
        return response.content
    else:
        return "Error: " + str(response.status_code) + " " + response.content

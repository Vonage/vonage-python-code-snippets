import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

APPLICATION_ID = os.environ.get('APPLICATION_ID')
APPLICATION_PRIVATE_KEY_PATH = os.environ.get('APPLICATION_PRIVATE_KEY_PATH')
TO_NUMBER = os.environ.get('TO_NUMBER')
NEXMO_NUMBER = os.environ.get('NEXMO_NUMBER')
APPLICATION_PRIVATE_KEY = open('private.key','r').read()

import nexmo

client = nexmo.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY
)

client.create_call({
  'to': [{'type': 'phone', 'number': TO_NUMBER}],
  'from': {'type': 'phone', 'number': NEXMO_NUMBER},
  'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
})

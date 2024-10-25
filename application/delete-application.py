#!/usr/bin/env python3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
VONAGE_APPLICATION_ID = os.getenv('VONAGE_APPLICATION_ID')

from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

client.application.delete_application(VONAGE_APPLICATION_ID)

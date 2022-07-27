#!/usr/bin/env python3
from flask import Flask, jsonify
from os.path import join, dirname
from dotenv import load_dotenv
import os

app = Flask(__name__)

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

CONFERENCE_NAME = os.environ.get("CONFERENCE_NAME")

@app.route("/webhooks/answer")
def answer_call():
    ncco = [
        {
            "action": "talk",
            "text": "Please wait while we connect you to the conference"
        },
        {
            "action": "conversation",
            "name": CONFERENCE_NAME
        }]
    return jsonify(ncco)


if __name__ == '__main__':
    app.run(port=3000)

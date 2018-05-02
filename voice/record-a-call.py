#!/usr/bin/env python3
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
    ncco = [
        {
            "action": "talk",
            "text": "Hi, we will shortly forward your call. This call is recorded for quality assurance purposes."
        },
        {
            "action": "record",
            "eventUrl": ["https://275d6df0.ngrok.io/webhooks/recordings"]
        },
        {
            "action": "connect",
            "eventUrl": ["https://275d6df0.ngrok.io/webhooks/event"],
            "from": "NEXMO_NUMBER",
            "endpoint": [
                {
                    "type": "phone",
                    "number": "RECIPIENT_NUMBER"
                }
            ]
        }
    ]
    return jsonify(ncco)

@app.route("/webhooks/recordings", methods=['POST'])
def recordings():

    data = request.get_json()
    pprint(data)

    recording_url = request.args['recording_url']
    pprint(recording_url)

if __name__ == '__main__':
    app.run(port=3000)

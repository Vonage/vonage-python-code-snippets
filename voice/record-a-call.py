#!/usr/bin/env python3
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
    ncco = [
        {
            "action": "talk",
            "text": "Hi, this call records this message. Check the parameters sent to the event url webhook endpoint and find the link you need to download this recording.",
            "language": "en-US"
        },
        {
            "action": "record",
            "eventUrl": ["https://demo.ngrok.io/webhooks/recordings"]
        },
        {
            "action": "connect",
            "eventUrl": ["https://demo.ngrok.io/webhooks/event"],
            "from": "VONAGE_NUMBER",
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
    return "webhook received"

if __name__ == '__main__':
    app.run(port=3000)

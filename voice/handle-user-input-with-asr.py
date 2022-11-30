#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhooks/answer", methods=["POST", "GET"])
def answer_call():
    ncco = [
        {"action": "talk", "text": "Please, tell me something",},
        {
            "action": "input",
            "type": ["speech"],
            "eventUrl": [
                "{host}{endpoint}".format(
                    host=request.host_url, endpoint="webhooks/asr"
                )
            ],
            "speech": {
                "endOnSilence": 1,
                "language": "en-US",
                "uuid": [request.args.get("uuid")], # Change to request.json.get("uuid") if using POST-JSON webhook format
            },
        },
    ]
    return jsonify(ncco)


@app.route("/webhooks/asr", methods=["POST", "GET"])
def answer_asr():
    body = request.get_json()
    if body is not None and "speech" in body:
        speech = body["speech"]["results"][0]["text"]
        ncco = [
            {"action": "talk", "text": "Hello ,you said {speech}".format(speech=speech)}
        ]
    else:
        ncco = [{"action": "talk", "text": "Sorry, i don't undertand. Bye"}]

    return jsonify(ncco)


if __name__ == "__main__":
    app.run(port=3000)

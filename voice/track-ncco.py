from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
  ncco = [{
      "action": "talk",
      "text": "Thanks for calling the notification line"
    },
    {
      "action": "notify",
      "payload": {
        "foo": "bar"
      },
      "eventUrl": [
        "{url_root}webhooks/notification".format(url_root=request.url_root)
      ]
    },
    {
      "action": "talk",
      "text": "You will never hear me as the notification URL will return an NCCO "
    }]
  return jsonify(ncco)

@app.route("/webhooks/notification", methods=['POST'])
def notification():
  ncco = [{
    "action": "talk",
    "text": "Your notification has been received, loud and clear"
  }]
  return jsonify(ncco)

@app.route("/webhooks/event", methods=['POST'])
def event():
  return "OK"

if __name__ == '__main__':
    app.run(host="localhost", port=3000)

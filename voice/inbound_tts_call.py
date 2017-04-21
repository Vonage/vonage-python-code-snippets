from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)


@app.route("/call", methods=['GET', 'POST'])
def call_handle():
    ncco = [{
        "action": "talk",
        "text": "Hello World",
    }]
    return jsonify(ncco)


@app.route('/callback', methods=['POST'])
def callback_handle():
    print request
    return jsonify({})


if __name__ == "__main__":
    app.run(port=5000)

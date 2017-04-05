from flask import Flask, request, jsonify
from pprint import pprint
app = Flask(__name__)


@app.route("/receipt", methods=['GET', 'POST'])
def delivery_receipt():
    if request.method == 'POST':
        pprint(request.json)
    else:
        pprint(dict(request.args))
    return jsonify({})


if __name__ == "__main__":
    app.run(port=5000)


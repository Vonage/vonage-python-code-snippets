from flask import Flask, jsonify
app = Flask(__name__)
app.config.from_pyfile('.env')

import sms

@app.route("/sms/send")
def sms_send():
    return jsonify(sms.send(app.config))

if __name__ == "__main__":
    app.run()

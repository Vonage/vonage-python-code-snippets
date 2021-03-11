import os
from flask import Flask, request
import jwt

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_SIGNATURE_SECRET = os.getenv("VONAGE_SIGNATURE_SECRET")
VONAGE_SIGNATURE_SECRET_METHOD = os.getenv("VONAGE_SIGNATURE_SECRET_METHOD")

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def callback():
    token = request.headers.get("Authorization")[7:]
    try:
        jwt.decode(token, VONAGE_SIGNATURE_SECRET, 'HS256')
        print("Signature was validated")
    except:
        print("Unable to validate signature")

    return '', 200

if __name__ == "__main__":
    app.run()

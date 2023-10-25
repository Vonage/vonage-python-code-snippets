import os
from os.path import join, dirname
from flask import Flask, request
from dotenv import load_dotenv
from vonage_jwt.verify_jwt import verify_signature

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

app = Flask(__name__)

VONAGE_SIGNATURE_SECRET = os.getenv("VONAGE_SIGNATURE_SECRET")


@app.route("/webhooks/inbound", methods=["POST"])
def inbound():
    # Need to get the JWT after 'Bearer' in the authorization header
    auth_header = request.headers["authorization"].split()
    token = auth_header[1].strip()

    if verify_signature(token, VONAGE_SIGNATURE_SECRET):
        print('Valid signature')
    else:
        print('Invalid signature')


if __name__ == "__main__":
    print("Running locally")
    app.run(host="localhost", port=5000)

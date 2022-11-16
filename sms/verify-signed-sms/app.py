import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, request
import vonage

#Load the environment
envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_SIGNATURE_SECRET = os.getenv("VONAGE_SIGNATURE_SECRET")
VONAGE_SIGNATURE_SECRET_METHOD = os.getenv("VONAGE_SIGNATURE_SECRET_METHOD")

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def callback():
    params = request.args.to_dict()

    client = vonage.Client(
        key=VONAGE_API_KEY, 
        signature_secret=VONAGE_SIGNATURE_SECRET, 
        signature_method=VONAGE_SIGNATURE_SECRET_METHOD
    )
    check = client.check_signature(params=params)
    print(f"Signature is valid: {check}")
    return "Hello, world"

if __name__ == "__main__":
    app.run(load_dotenv=True)

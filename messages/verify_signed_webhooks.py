import hashlib
import os
from os.path import join, dirname
from flask import Flask, request, jsonify
import jwt
from dotenv import load_dotenv


#Load the environment
envpath = join(dirname(__file__),'../.env')
load_dotenv(envpath)

app = Flask(__name__)

port = os.getenv('PORT')
api_key = os.getenv('NEXMO_API_KEY') # there may be multiple api_key/sig_secret pairs
sig_secret = os.getenv('NEXMO_SIG_SECRET')

@app.route("/webhooks/inbound", methods=['POST'])
def inbound():
    # Need token after 'Bearer'
    parts = request.headers['authorization'].split()
    token = parts[1].strip()

    # Extract api_key from token payload
    k = jwt.decode(token, verify=False)["api_key"]
    # Use k to look up corresponding sig secret

    #### 1. Verify request
    try:
        decoded = jwt.decode(token, sig_secret, algorithms='HS256')
    except Exception as e:
        print(e)
        r = '{"msg": "' + str(e) +'"}'
        return (r, 401)

    #### 2. Verify payload (only needed if using HTTP rather than HTTPS)

    # Obtain transmitted payload hash
    payload_hash = decoded["payload_hash"]

    # generate hash of request payload
    payload = request.data # Obtains request data as binary string
    h = hashlib.sha256(payload) # requires binary string
    hd = h.hexdigest() # Use hexdigest() and NOT digest()

    # Check the payload hash matches the one we created ourselves from request data
    if (hd != payload_hash):
        return ('{"msg": "Invalid payload"}', 401)
    else:
        print("Verified payload")
    return "OK"

@app.route("/webhooks/status", methods=['POST'])
def status():
    data = request.get_json()
    return (jsonify(data))

if __name__ == '__main__':
    print("Running locally")
    app.run(host="localhost", port=port)

import jwt
import hashlib
import json
import os
from flask import Flask, request, jsonify
from os.path import join, dirname
from dotenv import load_dotenv
from pprint import pprint

#Load the environment
envpath = join(dirname(__file__),'../.env')
load_dotenv(envpath)

app = Flask(__name__)

port = os.getenv('PORT')
api_key = os.getenv('NEXMO_API_KEY')
sig_secret = os.getenv('NEXMO_SIG_SECRET')
verify_webhooks = True # Set to False if you don't want to verify webhooks
error_message = ''

def verify_webhook(request):
    global error_message

    # Need token after 'Bearer'
    parts = request.headers['authorization'].split() 
    token = parts[1].strip()

    # Verify request
    decoded = jwt.decode(token, sig_secret, algorithms='HS256')
    if decoded['api_key'] == api_key:
        print('Valid callback signature')
        # we can continue to check payload 
    else:
        error_message = 'Warning: Invalid callback signature!'
        print(error_message)
        return False
    
    # Obtain transmitted payload hash
    payload_hash = decoded["payload_hash"]

    # generate hash of request payload
    payload = request.data # Obtains request data as binary string
    h = hashlib.sha256(payload) # requires binary string
    hd = h.hexdigest() # Use hexdigest() and NOT digest()

    # Check the payload hash matches the one we created ourselves from request data
    if (hd != payload_hash):
        error_message = "WARNING: payload may have been tampered with in-transit"
        return False
    print("Verified payload")
    return True 

@app.route("/webhooks/inbound", methods=['POST'])
def inbound():
    if verify_webhooks:
        if verify_webhook(request):
            data = request.get_json()
            pprint(data) 
            return (jsonify(data))
        else:
            error_obj = {'error_message': error_message, 'error_code': 401}
            error = json.dumps(error_obj)
            return (error, 401)

@app.route("/webhooks/status", methods=['POST'])
def status():
    data = request.get_json()
    return (jsonify(data))

if __name__ == '__main__':
    print("Running locally")
    app.run(host="localhost", port=port)

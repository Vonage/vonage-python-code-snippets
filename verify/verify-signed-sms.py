import vonage
from flask import Flask, request

app = Flask(__name__)


@app.route("/webhooks/inbound", methods=["GET", "POST"])
def inbound():

    # Get the params
    if request.is_json:
        params = request.get_json()
    else:
        params = request.args or request.form

    if "sig" in params:
        # Init the client, just when needed
        client = vonage.Client(
            key=os.getenv("VONAGE_API_KEY"),
            secret=os.getenv("VONAGE_API_SECRET"),
            signature_secret=os.getenv("VONAGE_SIGNATURE_SECRET"),
            signature_method="md5",
        )
        # Check signature from params
        if client.check_signature(params):
            print("Valid signature")
        else:
            print("Invalid signature")
    else:
        print("Signature not detected in params, Nothing to compare")

    return "All OK.", 200

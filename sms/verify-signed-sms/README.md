# Verify an incoming SMS signature

This sample application demonstrates how to verify an incoming SMS signature.

Note: you must have enabled signed webhooks. To do this, please contact support. 
[This page](https://developer.vonage.com/getting-started/concepts/signing-messages) has more information.

## Usage

You may want to use a localhost tunnel agent such as [ngrok](https://ngrok.com/) for local testing.

### Set Up Your Environment

Install dependencies with `pip` in a virtual environment:

```bash
python3 -m venv venv
. ./venv/bin/activate

# Point to the requirements file in the root of the python-code-snippets repo
pip install -r requirements.txt
```

### Set Up an Incoming Webhook
1. Start ngrok with `ngrok http 8000`. ngrok will give you a forwarding address you can now use to recieve event webhooks.
1. Go to the [Customer Dashboard](https://dashboard.nexmo.com/sign-in).
1. Go to ["API Settings"](https://dashboard.nexmo.com/settings).
1. Under "SMS Settings", choose the SMS API and paste in your ngrok URL in the "Delivery Receipts" section.
1. Click "Save Changes".

### Start the FastAPI Server

Run the FastAPI server with

```bash
fastapi dev sms/verify-signed-sms/main.py
```

You can now send an SMS and the incoming message will be sent to your webhook URL. You can check the console output of the application to see the results of the signature check.

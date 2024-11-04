# Verifying Signed Webhooks Demo

This quick demo shows how to verify an incoming Webhook signature by decoding the incoming JWT sent by Vonage.

For signed incoming SMS signatures through the Messaging API, please see the snippet for verifying a signed incoming SMS message instead.

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
1. Click on ["Applications"](https://dashboard.nexmo.com/applications).
1. Click the three dots and select "Edit" for the application you are using.
1. Under "Capabilities", enter `https://your-ngrok-url/events` for the Voice capability.
1. Click "Save".

### Start the FastAPI Server

Run the FastAPI server with

```bash
fastapi dev decode-jwt/main.py
```

You can now create a voice call using the voice sample in this repo. This sample app will verify the incoming signature.
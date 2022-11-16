This quick demo shows how to verify an incoming SMS signature

## Usage

### Setup

Install inside a virtual environment and then set up the webhooks.

#### Create a virtual environment
1. Run `python3 -m venv venv`
1. Run `source venv/bin/activate`
1. Run `pip install -r requirements.txt`
1. Copy `.env.dist` to `.env` and fill in your credentials
1. Run `flask run`

#### Set up incoming webhook
1. Start ngrok with `ngrok http 3000`. ngrok will give you a forwarding address you can now use for your delivery receipts.
1. Copy this URL and go to your [customer dashboard](https://dashboard.nexmo.com/sign-in)
1. Click on "Numbers", and then ["Your Numbers"](https://dashboard.nexmo.com/your-numbers)
1. Click the "Edit" icon on the number to use, and change the "Inbound Webhook URL" option to `https://your-ngrok-url`
1. Click "Save"

You can now send an SMS, and the incoming message will be sent to your application. You can check the console output of
the application to see the results of the signature check.
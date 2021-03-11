This quick demo shows how to verify an incoming Webhook signature. Your account must be enabled for signed webhooks,
and you must have an existing application with the "Messages" capability enabled.

For signed incoming SMS signatures through the Messaging API, please see the snippet for verifying a signed
incoming SMS message instead.

## Usage

### Setup

Install using either `pipenv` or `virtualenv`, and then set up the webhooks.

#### `pipenv`
1. Run `pipenv install`
1. Copy `.env.dist` to `.env` and fill in your credentials
1. Run `pipenv run flask`

#### `virtualenv`
1. Run `virtualenv env`
1. Run `source env/bin/activate`
1. Run `pip install -r requirements.txt`
1. Copy `.env.dist` to `.env` and fill in your credentials
1. Run `flask run`

#### Set up incoming webhook
1. Start ngrok with `ngrok http 3000`. ngrok will give you a forwarding address you can now use for your delivery receipts.
1. Copy this URL and go to your [customer dashboard](https://dashboard.nexmo.com/sign-in)
1. Click on ["Your Applications"](https://dashboard.nexmo.com/applications)
1. Click the three dots and select "Edit" for the application you are using on the application you are using
1. Under "Capabilities", enter `https://your-ngrok-url` for the "Inbound URL" and "Status URL" boxes, and makes sure both are set to "POST"
1. Click "Save"

You can now send an SMS to the number linked in your application, and the sample app will verify the incoming signature.
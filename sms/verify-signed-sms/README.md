This quick demo shows how to verify an incoming SMS signature

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
1. Click on "Numbers", and then ["Your Numbers"](https://dashboard.nexmo.com/your-numbers)
1. Click the "Edit" icon on the number to use, and change the "Inbound Webhook URL" option to `https://your-ngrok-url`
1. Click "Save"

You can now send an SMS, and the incoming message will be sent to your application. You can check the console output of
the application to see the results of the signature check.
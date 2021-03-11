This quick demo shows how to accept a Number Insight Async Webhook

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

#### Trigger the lookup
1. Start ngrok with `ngrok http 3000`. ngrok will give you a forwarding address you can now use for your delivery receipts.
1. Run the trigger script with:

    python ni-advanced-async-trigger.py

The output of the webhook should appear in the console output of the Flask application
# Verifying Signed Webhooks Demo

This quick demo shows how to recieve an incoming Number Insight webhook.

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

### Start Your Localhost Tunnel

Start ngrok with `ngrok http 8000`. ngrok will give you a forwarding address you can now use to recieve event webhooks.

### Start the FastAPI Server

Run the FastAPI server with

```bash
fastapi dev number-insight/async-callback/main.py
```

### Trigger the Lookup

1. Edit the `ni-advanced-async-trigger.py` script to add the number to return insights for.
1. Add your ngrok URL as the callback to the `number_insight.get_advanced_info_async` method.
1. Run the trigger script with:

    python ni-advanced-async-trigger.py

The output of the webhook should appear in the console output of the FastAPI application.
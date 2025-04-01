# Vonage Code Snippets for Python

![Author](https://img.shields.io/badge/author-Vonage-orange)
![Issues](https://img.shields.io/github/issues/Vonage/vonage-python-code-snippets)
![License](https://img.shields.io/github/license/Vonage/vonage-python-code-snippets)
![Stars](https://img.shields.io/github/stars/Vonage/vonage-python-code-snippets)
![Forks](https://img.shields.io/github/forks/Vonage/vonage-python-code-snippets)
![Last Commit](https://img.shields.io/github/last-commit/Vonage/vonage-python-code-snippets)
![Size](https://img.shields.io/github/repo-size/Vonage/vonage-python-code-snippets)

The purpose of these Code Snippets is to provide simple examples focused
on one goal. For example, sending an SMS, creating a Vonage Video API session, handling an incoming webhook, or making a Text-to-Speech call.

## Table of Contents

- [Setup](#setup)
- [Running the Examples](#running-the-examples)
- [SDK Structure](#sdk-structure)
- [How the SDK Handles Errors](#how-the-sdk-handles-errors)
- [Troubleshooting](#troubleshooting)
- [Useful Resources](#useful-resources)
- [Request an Example](#request-an-example)
- [License](#license)
- [Python Code Snippets](#python-code-snippets)

## Setup

These code samples are meant to be embedded into pages on [https://developer.vonage.com/](https://developer.vonage.com/). Developers are free to use these code snippets as a reference, but these may require changes to be worked into your specific application. We recommend checking out the [Vonage Developer Website](https://developer.vonage.com/), which displays these code snippets in a more copy/paste fashion.

To use the examples, you will first need a [Vonage account][sign-up]. Then rename
the `.env.dist` file to `.env` and set the values as required.

For some of the examples you will need to [buy a number][buy-number].

## Running the Examples

If you would like to run these examples yourself, you will need to do the following:

Use a virtual environment:

```sh
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment in Mac/Linux
. ./venv/bin/activate

# Or on Windows Command Prompt
venv\Scripts\activate
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the code:

For samples that don't use a web server, run with python, e.g.

```sh
python sms/send-an-sms.py
```

For samples that require a web server, run with FastAPI, e.g.

```sh
fastapi dev messages/inbound-message.py
```

## SDK Structure

The SDK is a monorepo - lots of packages in a single place. In the SDK, we have:

1. The top-level package `vonage`, which pulls in all the other packages you need.
1. A package referring to every API supported in the SDK (`vonage-sms`, `vonage-voice`, `vonage-video` etc.)
1. Internal packages for making HTTP requests, creating JWTs etc. (`vonage-http-client`, `vonage-jwt` etc.)
1. A utilities package (`vonage-utils`)

There are important things to note:

1. The `vonage` package instantiates each of the API packages. For example, you can call `vonage.voice.any_method_from_the_voice_class`. This means you don’t have to instantiate packages that you need separately.
1. Many of the APIs require input data from the user. This is passed in through data models that you will find in the package for the specific API you want to call. This was intentional so the user doesn’t immediately import every data model from every single API whenever they import the top-level package, which would make it harder to find what is actually needed in an IDE, and allows for models with the same names in different namespaces. 

For example, to use a `VerifyRequest` object from the `vonage-verify` package, you’ll need to first import the `vonage` package to get the `Auth` object and the `Verify` methods, then import `VerifyRequest` from the `vonage-verify` package, like so:

```python
from vonage import Auth, Vonage
from vonage_verify import VerifyRequest, SmsChannel

client = Vonage(
	Auth(
    		application_id=VONAGE_APPLICATION_ID,
    	private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
	)
)

verify_request = VerifyRequest(
	brand=BRAND_NAME,
	workflow=[
    	SmsChannel(to=TO_NUMBER),
	],
)

response = vonage_client.verify.start_verification(verify_request)
```

This is explained in more detail in the blog post shared above. You can also find full, working examples [in the Python Code Snippets repo](https://github.com/Vonage/vonage-python-code-snippets).

### Getting the Objects You Need Into Your Namespace

If you’re working with e.g. the Voice API, if you know you’re likely to use many of the data models, you can import them all into your app’s namespace (making it easier for your autocomplete etc. to find them) with the `*` operator, e.g.

```python
from vonage_voice import *

request = CreateCallRequest(...)
```

It’s usually considered better practice to import just what you need, but using this method means the data models will all be available to you if you need to do some quick testing.

## How the SDK handles errors

The Vonage Python SDK has various different classes of errors:

- Some regular Python/package errors that can be raised during the course of SDK operation
- The top-level `VonageError`, that custom SDK errors inherit from
- Errors raised when using some packages, e.g. `VerifyError`
- Errors raised by the HTTP client

It’s likely that when troubleshooting, you’ll especially see HTTP request errors, so let’s discuss these.

### HTTP Request Errors

This is a class of errors raised when actually making the HTTP request or when receiving an HTTP response.

The high-level error here is the `HttpRequestError`. There are other errors which are based on this and have the same properties, but different names that are more specific to [the HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) received from the Vonage server, e.g. an `AuthenticationError` or a `NotFoundError`.

Each error of this type has properties that can be accessed when the error is caught, i.e. if you have a try-except block which catches an error, you can then access the error message and the response object which has additional information. This can be useful for debugging.

To catch an error in this way, do this:

```python
try:
	vonage_client.call_vonage_api(...)
except HttpRequestError as e:
	print(‘Request failed:’)
	print(e.message)
	print(e.response.text)  
```

You can access any information about the request or the response from the `e.response` object.

## Troubleshooting

### Viewing the last request and response

Whether or not an HTTP request was successful, you can access the last request and response sent by accessing the relevant HTTP client attributes like this:

```python
vonage_client.http_client.last_request
vonage_client.http_client.last_response
```

For example, to see the last request body and headers sent by the SDK, you can do:

```python
print(vonage_client.http_client.last_request.body)
print(vonage_client.http_client.last_request.headers)
```

### Authentication errors

If the SDK returns an `AuthenticationError`, this is because the Vonage Server was not able to authenticate the SDK user. In this case, you should check the authentication details that were provided.

## Useful Resources
- [Vonage Python SDK on Github](https://github.com/Vonage/vonage-python-sdk)
- [Vonage Python SDK on PyPI](https://pypi.org/project/vonage/)
- [Python SDK introduction blog](https://developer.vonage.com/en/blog/vonage-python-sdk-v4-is-now-live-#getting-started)
- [Migration guide from old to new SDK](https://github.com/Vonage/vonage-python-sdk/blob/main/V3_TO_V4_SDK_MIGRATION_GUIDE.md)

## Request an Example

Please [raise an issue](https://github.com/Vonage/vonage-python-code-snippets/issues) to request an example that isn't present within the quickstart. Pull requests will be gratefully received.

## License

[MIT](LICENSE)

[sign-up]: https://dashboard.nexmo.com/sign-up
[buy-number]: https://dashboard.nexmo.com/buy-numbers


## Python Code Snippets

This is a list of all supported Python code snippets in the repo, organised by category.

### Table of Contents

- [Account](#account)
- [Application](#application)
- [Decode Jwt](#decode-jwt)
- [Messages](#messages)
- [Number Insight](#number-insight)
- [Numbers](#numbers)
- [Sms](#sms)
- [Subaccounts](#subaccounts)
- [Users](#users)
- [Verify](#verify)
- [Verify_Legacy](#verify_legacy)
- [Voice](#voice)

### Account

#### Snippets in this Section

- [Configure Account](#configure-account)
- [Create Secret](#create-secret)
- [Fetch A Secret](#fetch-a-secret)
- [Get Balance](#get-balance)
- [List All Secrets](#list-all-secrets)
- [Revoke Secret](#revoke-secret)

#### Configure Account

```python
from vonage import Auth, Vonage
from vonage_account import SettingsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

settings: SettingsResponse = client.account.update_default_sms_webhook(
    mo_callback_url=ACCOUNT_SMS_CALLBACK_URL
)

print(settings)
```

#### Create Secret

```python
from vonage import Auth, Vonage
from vonage_account import VonageApiSecret

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: VonageApiSecret = client.account.create_secret(ACCOUNT_SECRET)
print(response)
```

#### Fetch A Secret

```python
from vonage import Auth, Vonage
from vonage_account import VonageApiSecret

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

secret: VonageApiSecret = client.account.get_secret(ACCOUNT_SECRET_ID)

print(f'Secret ID: {secret.id}; Created at {secret.created_at}')
```

#### Get Balance

```python
from vonage import Auth, Vonage
from vonage_account import Balance

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

balance: Balance = client.account.get_balance()

print(f'{balance.value:0.2f} EUR, auto-reload: {balance.auto_reload}')
```

#### List All Secrets

```python
from vonage import Auth, Vonage
from vonage_account import VonageApiSecret

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: list[VonageApiSecret] = client.account.list_secrets()
print(response)
```

#### Revoke Secret

```python
from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))
client.account.revoke_secret(ACCOUNT_SECRET_ID)
```

### Application

#### Snippets in this Section

- [Create Application](#create-application)
- [Delete Application](#delete-application)
- [Get Application](#get-application)
- [List Applications](#list-applications)
- [Update Application](#update-application)

#### Create Application

```python
from vonage import Auth, Vonage
from vonage_application import (ApplicationConfig, ApplicationData,
                                ApplicationUrl, Capabilities, Messages,
                                MessagesWebhooks, Region, Verify,
                                VerifyWebhooks, Voice, VoiceUrl, VoiceWebhooks)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

# Voice application options
voice = Voice(
    webhooks=VoiceWebhooks(
        answer_url=VoiceUrl(
            address='https://example.com/answer',
            http_method='POST',
            connect_timeout=500,
            socket_timeout=3000,
        ),
        fallback_answer_url=VoiceUrl(
            address='https://example.com/fallback',
            http_method='POST',
            connect_timeout=500,
            socket_timeout=3000,
        ),
        event_url=VoiceUrl(
            address='https://example.com/event',
            http_method='POST',
            connect_timeout=500,
            socket_timeout=3000,
        ),
    ),
    signed_callbacks=True,
    conversations_ttl=8000,
    leg_persistence_time=14,
    region=Region.NA_EAST,
)

# Messages application options
messages = Messages(
    version='v1',
    webhooks=MessagesWebhooks(
        inbound_url=ApplicationUrl(
            address='https://example.com/inbound', http_method='POST'
        ),
        status_url=ApplicationUrl(
            address='https://example.com/status', http_method='POST'
        ),
    ),
    authenticate_inbound_media=True,
)

# Verify application options
verify = Verify(
    webhooks=VerifyWebhooks(
        status_url=ApplicationUrl(address='https://example.com/status', http_method='GET')
    ),
)

# Set the application capabilities
capabilities = Capabilities(voice=voice, messages=messages, verify=verify)

# Set the application configuration that will be applied
params = ApplicationConfig(
    name='My Custom Application',
    capabilities=capabilities,
)

# Call the API
response: ApplicationData = client.application.create_application(params)

print(response)
```

#### Delete Application

```python
from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

client.application.delete_application(VONAGE_APPLICATION_ID)
```

#### Get Application

```python
from vonage import Auth, Vonage
from vonage_application import ApplicationData

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: ApplicationData = client.application.get_application(VONAGE_APPLICATION_ID)

print(response)
```

#### List Applications

```python
from vonage import Auth, Vonage
from vonage_application import ListApplicationsFilter

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

applications, next_page = client.application.list_applications(
    filter=ListApplicationsFilter(page_size=10, page=1)
)

pprint(f'Applications:\n{applications}, \nNext page: {next_page}')
```

#### Update Application

```python
from vonage import Auth, Vonage
from vonage_application import (ApplicationConfig, ApplicationData,
                                ApplicationUrl, Messages, MessagesWebhooks)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

config = ApplicationConfig(
    name='My Renamed Application',
    capabilities=Messages(
        webhooks=MessagesWebhooks(
            inbound_url=ApplicationUrl(
                address='https://example.com/inbound_new_url', http_method='GET'
            ),
            status_url=ApplicationUrl(
                address='https://example.com/status_new_url', http_method='GET'
            ),
        ),
        authenticate_inbound_media=False,
    ),
)
response: ApplicationData = client.application.update_application(
    id=VONAGE_APPLICATION_ID, config=config
)

print(response)
```

### Decode Jwt

#### Snippets in this Section

- [Decode Jwt](#decode-jwt)

#### Decode Jwt

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)


VONAGE_SIGNATURE_SECRET = os.getenv('VONAGE_SIGNATURE_SECRET')

from fastapi import FastAPI, Request
from vonage_jwt.verify_jwt import verify_signature

app = FastAPI()


@app.get('/events')
async def verify_signed_webhook(request: Request):
    # Need to get the JWT after "Bearer " in the authorization header
    auth_header = request.headers["authorization"].split()
    token = auth_header[1].strip()

    if verify_signature(token, VONAGE_SIGNATURE_SECRET):
        print('Valid signature')
    else:
        print('Invalid signature')
```

### Messages

#### Snippets in this Section

- [Inbound Message](#inbound-message)
- [Message Status](#message-status)
- [Messenger Send Audio](#messenger-send-audio)
- [Messenger Send File](#messenger-send-file)
- [Messenger Send Image](#messenger-send-image)
- [Messenger Send Text](#messenger-send-text)
- [Messenger Send Video](#messenger-send-video)
- [Mms Send Audio](#mms-send-audio)
- [Mms Send Image](#mms-send-image)
- [Mms Send Vcard](#mms-send-vcard)
- [Mms Send Video](#mms-send-video)
- [Rcs Revoke Message](#rcs-revoke-message)
- [Rcs Send File](#rcs-send-file)
- [Rcs Send Image](#rcs-send-image)
- [Rcs Send Rich Card Carousel](#rcs-send-rich-card-carousel)
- [Rcs Send Rich Card Standalone](#rcs-send-rich-card-standalone)
- [Rcs Send Suggested Action Create Calendar Event](#rcs-send-suggested-action-create-calendar-event)
- [Rcs Send Suggested Action Dial](#rcs-send-suggested-action-dial)
- [Rcs Send Suggested Action Multiple](#rcs-send-suggested-action-multiple)
- [Rcs Send Suggested Action Open Url](#rcs-send-suggested-action-open-url)
- [Rcs Send Suggested Action Share Location](#rcs-send-suggested-action-share-location)
- [Rcs Send Suggested Action View Location](#rcs-send-suggested-action-view-location)
- [Rcs Send Suggested Reply](#rcs-send-suggested-reply)
- [Rcs Send Text](#rcs-send-text)
- [Rcs Send Video](#rcs-send-video)
- [Sandbox Messenger Send_Text](#sandbox-messenger-send_text)
- [Sandbox Viber Send_Text](#sandbox-viber-send_text)
- [Sandbox Whatsapp Send_Text](#sandbox-whatsapp-send_text)
- [Sms Send Sms](#sms-send-sms)
- [Verify Signed Webhooks](#verify-signed-webhooks)
- [Viber Send File](#viber-send-file)
- [Viber Send Image](#viber-send-image)
- [Viber Send Text](#viber-send-text)
- [Viber Send Video](#viber-send-video)
- [Webhook Server](#webhook-server)
- [Whatsapp Mark As Read](#whatsapp-mark-as-read)
- [Whatsapp Send Audio](#whatsapp-send-audio)
- [Whatsapp Send Authentication Template](#whatsapp-send-authentication-template)
- [Whatsapp Send Button Link](#whatsapp-send-button-link)
- [Whatsapp Send Button Quick Reply](#whatsapp-send-button-quick-reply)
- [Whatsapp Send Contact](#whatsapp-send-contact)
- [Whatsapp Send File](#whatsapp-send-file)
- [Whatsapp Send Image](#whatsapp-send-image)
- [Whatsapp Send Location](#whatsapp-send-location)
- [Whatsapp Send Media Template](#whatsapp-send-media-template)
- [Whatsapp Send Product Message Multiple Item](#whatsapp-send-product-message-multiple-item)
- [Whatsapp Send Product Message Single Item](#whatsapp-send-product-message-single-item)
- [Whatsapp Send Sticker By Id](#whatsapp-send-sticker-by-id)
- [Whatsapp Send Sticker By Url](#whatsapp-send-sticker-by-url)
- [Whatsapp Send Template](#whatsapp-send-template)
- [Whatsapp Send Text](#whatsapp-send-text)
- [Whatsapp Send Video](#whatsapp-send-video)

#### Inbound Message

```python
from pprint import pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/webhooks/inbound-message')
async def inbound_message(request: Request):
    data = await request.json()
    pprint(data)
```

#### Message Status

```python
from pprint import pprint

from fastapi import FastAPI, Request, status

app = FastAPI()


@app.post('/webhooks/message-status', status_code=status.HTTP_200_OK)
async def message_status(request: Request):
    data = await request.json()
    pprint(data)
```

#### Messenger Send Audio

```python
from vonage import Auth, Vonage
from vonage_messages import MessengerAudio, MessengerResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MessengerAudio(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    audio=MessengerResource(url=MESSAGES_AUDIO_URL),
)

response = client.messages.send(message)
print(response)
```

#### Messenger Send File

```python
from vonage import Auth, Vonage
from vonage_messages import MessengerFile, MessengerResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MessengerFile(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    file=MessengerResource(url=MESSAGES_FILE_URL),
)

response = client.messages.send(message)
print(response)
```

#### Messenger Send Image

```python
from vonage import Auth, Vonage
from vonage_messages import MessengerImage, MessengerResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MessengerImage(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    image=MessengerResource(url=MESSAGES_IMAGE_URL),
)

response = client.messages.send(message)
print(response)
```

#### Messenger Send Text

```python
from vonage import Auth, Vonage
from vonage_messages import MessengerText

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MessengerText(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    text='Hello from the Vonage Messages API.',
)
try:
    response = client.messages.send(message)
    print(response)
except Exception as e:
    print(e)
    print(client.http_client.last_request.url)
```

#### Messenger Send Video

```python
from vonage import Auth, Vonage
from vonage_messages import MessengerResource, MessengerVideo

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MessengerVideo(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    video=MessengerResource(url=MESSAGES_VIDEO_URL),
)

response = client.messages.send(message)
print(response)
```

#### Mms Send Audio

```python
from vonage import Auth, Vonage
from vonage_messages import MmsAudio, MmsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MmsAudio(
    to=MESSAGES_TO_NUMBER,
    from_=MMS_SENDER_ID,
    audio=MmsResource(url=MESSAGES_AUDIO_URL),
)

response = client.messages.send(message)
print(response)
```

#### Mms Send Image

```python
from vonage import Auth, Vonage
from vonage_messages import MmsImage, MmsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MmsImage(
    to=MESSAGES_TO_NUMBER,
    from_=MMS_SENDER_ID,
    image=MmsResource(url=MESSAGES_IMAGE_URL),
)

response = client.messages.send(message)
print(response)
```

#### Mms Send Vcard

```python
from vonage import Auth, Vonage
from vonage_messages import MmsResource, MmsVcard

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MmsVcard(
    to=MESSAGES_TO_NUMBER,
    from_=MMS_SENDER_ID,
    vcard=MmsResource(url=MESSAGES_VCARD_URL),
)

response = client.messages.send(message)
print(response)
```

#### Mms Send Video

```python
from vonage import Auth, Vonage
from vonage_messages import MmsResource, MmsVideo

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MmsVideo(
    to=MESSAGES_TO_NUMBER,
    from_=MMS_SENDER_ID,
    video=MmsResource(url=MESSAGES_VIDEO_URL),
)

response = client.messages.send(message)
print(response)
```

#### Rcs Revoke Message

```python
from vonage import Auth, Vonage

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.messages.revoke_rcs_message(MESSAGES_MESSAGE_ID)
print(response)
```

#### Rcs Send File

```python
from vonage import Auth, Vonage
from vonage_messages import RcsFile, RcsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = RcsFile(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    file=RcsResource(url=MESSAGES_FILE_URL),
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Image

```python
from vonage import Auth, Vonage
from vonage_messages import RcsImage, RcsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = RcsImage(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    image=RcsResource(url=MESSAGES_IMAGE_URL),
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Rich Card Carousel

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "richCard": {
            "carouselCard": {
                "cardWidth": "MEDIUM",
                "cardContents": [
                    {
                        "title": "Option 1: Photo",
                        "description": "Do you prefer this photo?",
                        "suggestions": [
                            {
                                "reply": {
                                    "text": "Option 1",
                                    "postbackData": "card_1",
                                }
                            }
                        ],
                        "media": {
                            "height": "MEDIUM",
                            "contentInfo": {
                                "fileUrl": MESSAGES_IMAGE_URL,
                                "forceRefresh": "false",
                            },
                        },
                    },
                    {
                        "title": "Option 2: Video",
                        "description": "Or this video?",
                        "suggestions": [
                            {
                                "reply": {
                                    "text": "Option 2",
                                    "postbackData": "card_2",
                                }
                            }
                        ],
                        "media": {
                            "height": "MEDIUM",
                            "contentInfo": {
                                "fileUrl": MESSAGES_VIDEO_URL,
                                "forceRefresh": "false",
                            },
                        },
                    },
                ],
            }
        }
    }
}

message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Rich Card Standalone

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "richCard": {
            "standaloneCard": {
                "thumbnailImageAlignment": "RIGHT",
                "cardOrientation": "VERTICAL",
                "cardContent": {
                    "title": "Quick question",
                    "description": "Do you like this picture?",
                    "media": {
                        "height": "TALL",
                        "contentInfo": {
                            "fileUrl": MESSAGES_IMAGE_URL,
                            "forceRefresh": "false",
                        },
                    },
                    "suggestions": [
                        {
                            "reply": {
                                "text": "Yes",
                                "postbackData": "suggestion_1",
                            }
                        },
                        {
                            "reply": {
                                "text": "I love it!",
                                "postbackData": "suggestion_2",
                            }
                        },
                    ],
                },
            }
        }
    }
}

message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Suggested Action Create Calendar Event

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Product Launch: Save the date!",
        "suggestions": [
            {
                "action": {
                    "text": "Save to calendar",
                    "postbackData": "postback_data_1234",
                    "fallbackUrl": "https://www.google.com/calendar",
                    "createCalendarEventAction": {
                        "startTime": "2024-06-28T19:00:00Z",
                        "endTime": "2024-06-28T20:00:00Z",
                        "title": "Vonage API Product Launch",
                        "description": "Event to demo Vonage\'s new and exciting API product",
                    },
                }
            }
        ],
    }
}
message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Suggested Action Dial

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Call us to claim your free gift!",
        "suggestions": [
            {
                "action": {
                    "text": "Call now!",
                    "postbackData": "postback_data_1234",
                    "fallbackUrl": "https://www.example.com/contact/",
                    "dialAction": {"phoneNumber": "+447900000000"},
                }
            }
        ],
    }
}

message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Suggested Action Multiple

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Need some help? Call us now or visit our website for more information.",
        "suggestions": [
            {
                "action": {
                    "text": "Call us",
                    "postbackData": "postback_data_1234",
                    "fallbackUrl": "https://www.example.com/contact/",
                    "dialAction": {"phoneNumber": "+447900000000"},
                }
            },
            {
                "action": {
                    "text": "Visit site",
                    "postbackData": "postback_data_1234",
                    "openUrlAction": {"url": "http://example.com/"},
                }
            },
        ],
    }
}

message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Suggested Action Open Url

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Check out our latest offers!",
        "suggestions": [
            {
                "action": {
                    "text": "Open product page",
                    "postbackData": "postback_data_1234",
                    "openUrlAction": {"url": "http://example.com/"},
                }
            }
        ],
    }
}

message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Suggested Action Share Location

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Your driver will come and meet you at your specified location.",
        "suggestions": [
            {
                "action": {
                    "text": "Share a location",
                    "postbackData": "postback_data_1234",
                    "shareLocationAction": {},
                }
            }
        ],
    }
}


message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Suggested Action View Location

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Drop by our office!",
        "suggestions": [
            {
                "action": {
                    "text": "View map",
                    "postbackData": "postback_data_1234",
                    "fallbackUrl": "https://www.google.com/maps/place/Vonage/@51.5230371,-0.0852492,15z",
                    "viewLocationAction": {
                        "latLong": {
                            "latitude": "51.5230371",
                            "longitude": "-0.0852492",
                        },
                        "label": "Vonage London Office",
                    },
                }
            }
        ],
    }
}


message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Suggested Reply

```python
from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "What do you think of Vonage APIs?",
        "suggestions": [
            {
                "reply": {
                    "text": "They\'re great!",
                    "postbackData": "suggestion_1",
                }
            },
            {
                "reply": {
                    "text": "They\'re awesome!",
                    "postbackData": "suggestion_2",
                }
            },
        ],
    }
}

message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Text

```python
from vonage import Auth, Vonage
from vonage_messages import RcsText

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = RcsText(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    text="This is an RCS message sent via the Vonage Messages API.",
)

response = client.messages.send(message)
print(response)
```

#### Rcs Send Video

```python
from vonage import Auth, Vonage
from vonage_messages import RcsResource, RcsVideo

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = RcsVideo(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    video=RcsResource(url=MESSAGES_VIDEO_URL),
)

response = client.messages.send(message)
print(response)
```

#### Sandbox Messenger Send_Text

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSAGES_SANDBOX_HOST = os.environ.get("MESSAGES_SANDBOX_HOST")
MESSENGER_RECIPIENT_ID = os.environ.get("MESSENGER_RECIPIENT_ID")
MESSENGER_SENDER_ID = os.environ.get("MESSENGER_SENDER_ID")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import MessengerText

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=MESSAGES_SANDBOX_HOST),
)

message = MessengerText(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    text="This is a Facebook Messenger text message sent using the Vonage Messages API via the Messages Sandbox",
)

response = client.messages.send(message)
print(response)
```

#### Sandbox Viber Send_Text

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSAGES_SANDBOX_HOST = os.environ.get("MESSAGES_SANDBOX_HOST")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
VIBER_SENDER_ID = os.environ.get("VIBER_SENDER_ID")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import ViberText

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=MESSAGES_SANDBOX_HOST),
)

message = ViberText(
    to=MESSAGES_TO_NUMBER,
    from_=VIBER_SENDER_ID,
    text="This is a Viber Service Message text message sent using the Messages API via the Messages Sandbox",
)

response = client.messages.send(message)
print(response)
```

#### Sandbox Whatsapp Send_Text

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSAGES_SANDBOX_HOST = os.environ.get("MESSAGES_SANDBOX_HOST")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import WhatsappText

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=MESSAGES_SANDBOX_HOST),
)

message = WhatsappText(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    text="This is a WhatsApp text message sent using the Vonage Messages API via the Messages Sandbox",
)

response = client.messages.send(message)
print(response)
```

#### Sms Send Sms

```python
from vonage import Auth, Vonage
from vonage_messages import Sms

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.messages.send(
    Sms(
        to=MESSAGES_TO_NUMBER,
        from_=SMS_SENDER_ID,
        text='This is an SMS sent using the Vonage Messages API.',
    )
)
print(response)
```

#### Verify Signed Webhooks

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)


VONAGE_SIGNATURE_SECRET = os.getenv('VONAGE_SIGNATURE_SECRET')

from fastapi import FastAPI, Request
from vonage_jwt.verify_jwt import verify_signature

app = FastAPI()


@app.get('/inbound')
async def verify_signed_webhook(request: Request):
    # Need to get the JWT after "Bearer " in the authorization header
    auth_header = request.headers["authorization"].split()
    token = auth_header[1].strip()

    if verify_signature(token, VONAGE_SIGNATURE_SECRET):
        print('Valid signature')
    else:
        print('Invalid signature')
```

#### Viber Send File

```python
from vonage import Auth, Vonage
from vonage_messages import ViberFile, ViberFileResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = ViberFile(
    to=MESSAGES_TO_NUMBER,
    from_=VIBER_SENDER_ID,
    file=ViberFileResource(url=MESSAGES_FILE_URL),
)

response = client.messages.send(message)
print(response)
```

#### Viber Send Image

```python
from vonage import Auth, Vonage
from vonage_messages import ViberImage, ViberImageResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = ViberImage(
    to=MESSAGES_TO_NUMBER,
    from_=VIBER_SENDER_ID,
    image=ViberImageResource(url=MESSAGES_IMAGE_URL),
)

response = client.messages.send(message)
print(response)
```

#### Viber Send Text

```python
from vonage import Auth, Vonage
from vonage_messages import ViberText

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = ViberText(
    to=MESSAGES_TO_NUMBER,
    from_=VIBER_SENDER_ID,
    text="This is a Viber message sent via the Vonage Messages API.",
)

response = client.messages.send(message)
print(response)
```

#### Viber Send Video

```python
from vonage import Auth, Vonage
from vonage_messages import ViberVideo, ViberVideoOptions, ViberVideoResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = ViberVideo(
    to=MESSAGES_TO_NUMBER,
    from_=VIBER_SENDER_ID,
    video=ViberVideoResource(url=MESSAGES_VIDEO_URL, thumb_url=MESSAGES_IMAGE_URL),
    viber_service=ViberVideoOptions(
        duration=MESSAGES_VIDEO_DURATION,
        file_size=MESSAGES_VIDEO_FILE_SIZE,
    ),
)

response = client.messages.send(message)
print(response)
```

#### Webhook Server

```python
from pprint import pprint

from fastapi import FastAPI, Request, status

app = FastAPI()


@app.post('/webhooks/message-status', status_code=status.HTTP_200_OK)
async def message_status(request: Request):
    data = await request.json()
    pprint(data)


@app.post('/webhooks/inbound-message')
async def inbound_message(request: Request):
    data = await request.json()
    pprint(data)
```

#### Whatsapp Mark As Read

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
GEOSPECIFIC_MESSAGES_API_URL = os.environ.get("GEOSPECIFIC_MESSAGES_API_URL")
MESSAGES_MESSAGE_ID = os.environ.get("MESSAGES_MESSAGE_ID")

from vonage import Auth, HttpClientOptions, Vonage

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=GEOSPECIFIC_MESSAGES_API_URL),
)

client.messages.mark_whatsapp_message_read("MESSAGES_MESSAGE_ID")
```

#### Whatsapp Send Audio

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")
MESSAGES_AUDIO_URL = os.environ.get("MESSAGES_AUDIO_URL")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import WhatsappAudio, WhatsappAudioResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host='messages-sandbox.nexmo.com'),
)

message = WhatsappAudio(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    audio=WhatsappAudioResource(url=MESSAGES_AUDIO_URL, caption="Test audio file"),
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Authentication Template

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")
WHATSAPP_TEMPLATE_NAME = os.environ.get("WHATSAPP_TEMPLATE_NAME")
WHATSAPP_OTP = os.environ.get("WHATSAPP_OTP")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host='messages-sandbox.nexmo.com'),
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        "type": "template",
        "template": {
            "name": WHATSAPP_TEMPLATE_NAME,
            "language": {"policy": "deterministic", "code": "en"},
            "components": [
                {"type": "body", "parameters": [{"type": "text", "text": "'$OTP'"}]},
                {
                    "type": "button",
                    "sub_type": "url",
                    "index": "0",
                    "parameters": [{"type": "text", "text": WHATSAPP_OTP}],
                },
            ],
        },
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Button Link

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        "type": "template",
        "template": {
            "name": WHATSAPP_TEMPLATE_NAME,
            "language": {"policy": "deterministic", "code": "en"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": MESSAGES_IMAGE_URL,
                            },
                        },
                    ],
                },
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": "Joe Bloggs"},
                        {"type": "text", "text": "AB123456"},
                    ],
                },
                {
                    "type": "button",
                    "index": "0",
                    "sub_type": "url",
                    "parameters": [{"type": "text", "text": "AB123456"}],
                },
            ],
        },
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Button Quick Reply

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        "type": "template",
        "template": {
            "name": WHATSAPP_TEMPLATE_NAME,
            "language": {"policy": "deterministic", "code": "en"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": MESSAGES_IMAGE_URL,
                            },
                        },
                    ],
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "parameter_name": "customer_name",
                            "text": "Joe Bloggs",
                        },
                        {
                            "type": "text",
                            "parameter_name": "dentist_name",
                            "text": "Mr Smith",
                        },
                        {
                            "type": "text",
                            "parameter_name": "appointment_date",
                            "text": "2025-02-26",
                        },
                        {
                            "type": "text",
                            "parameter_name": "appointment_location",
                            "text": "ACME Dental Practice",
                        },
                    ],
                },
                {
                    "type": "button",
                    "sub_type": "quick_reply",
                    "index": 0,
                    "parameters": [{"type": "payload", "payload": "Yes-Button-Payload"}],
                },
                {
                    "type": "button",
                    "sub_type": "quick_reply",
                    "index": 1,
                    "parameters": [{"type": "payload", "payload": "No-Button-Payload"}],
                },
            ],
        },
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Contact

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        "type": "contacts",
        "contacts": [
            {
                "addresses": [
                    {
                        "city": "Menlo Park",
                        "country": "United States",
                        "country_code": "us",
                        "state": "CA",
                        "street": "1 Hacker Way",
                        "type": "HOME",
                        "zip": "94025",
                    },
                    {
                        "city": "Menlo Park",
                        "country": "United States",
                        "country_code": "us",
                        "state": "CA",
                        "street": "200 Jefferson Dr",
                        "type": "WORK",
                        "zip": "94025",
                    },
                ],
                "birthday": "2012-08-18",
                "emails": [
                    {"email": "test@fb.com", "type": "WORK"},
                    {"email": "test@whatsapp.com", "type": "WORK"},
                ],
                "name": {
                    "first_name": "John",
                    "formatted_name": "John Smith",
                    "last_name": "Smith",
                },
                "org": {
                    "company": "WhatsApp",
                    "department": "Design",
                    "title": "Manager",
                },
                "phones": [
                    {"phone": "+1 (940) 555-1234", "type": "HOME"},
                    {
                        "phone": "+1 (650) 555-1234",
                        "type": "WORK",
                        "wa_id": "16505551234",
                    },
                ],
                "urls": [{"url": "https://www.facebook.com", "type": "WORK"}],
            }
        ],
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send File

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappFile, WhatsappFileResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappFile(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    file=WhatsappFileResource(url=MESSAGES_FILE_URL, caption="Test file"),
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Image

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappImage, WhatsappImageResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappImage(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    image=WhatsappImageResource(url=MESSAGES_IMAGE_URL, caption="Test image"),
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Location

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        "type": "location",
        "location": {
            "longitude": -122.425332,
            "latitude": 37.758056,
            "name": "Facebook HQ",
            "address": "1 Hacker Way, Menlo Park, CA 94025",
        },
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Media Template

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        "type": "template",
        "template": {
            "name": WHATSAPP_TEMPLATE_NAME,
            "language": {"policy": "deterministic", "code": "en"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": MESSAGES_IMAGE_URL,
                            },
                        },
                    ],
                },
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": "Joe Bloggs"},
                        {"type": "text", "text": "AB123456"},
                    ],
                },
            ],
        },
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Product Message Multiple Item

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        'type': 'interactive',
        'interactive': {
            'type': 'product_list',
            'header': {'type': 'text', 'text': 'Our top products'},
            'body': {'text': 'Check out these great products'},
            'footer': {'text': 'Sale now on!'},
            'action': {
                'catalog_id': WHATSAPP_CATALOG_ID,
                'sections': [
                    {
                        'title': 'Cool products',
                        'product_items': [
                            {'WHATSAPP_PRODUCT_ID_1': WHATSAPP_PRODUCT_ID_1},
                            {'WHATSAPP_PRODUCT_ID_2': WHATSAPP_PRODUCT_ID_2},
                        ],
                    },
                    {
                        'title': 'Awesome products',
                        'product_items': [
                            {'WHATSAPP_PRODUCT_ID_1': WHATSAPP_PRODUCT_ID_1}
                        ],
                    },
                ],
            },
        },
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Product Message Single Item

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        'type': 'interactive',
        'interactive': {
            'type': 'product',
            'body': {'text' 'Check out this cool product'},
            'footer': {'text': 'Sale now on!'},
            'action': {
                'catalog_id': WHATSAPP_CATALOG_ID,
                'product_retailer_id': WHATSAPP_PRODUCT_ID_1,
            },
        },
    },
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Sticker By Id

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappSticker, WhatsappStickerId

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappSticker(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    sticker=WhatsappStickerId(id=WHATSAPP_STICKER_ID),
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Sticker By Url

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappSticker, WhatsappStickerUrl

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappSticker(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    sticker=WhatsappStickerUrl(url=WHATSAPP_STICKER_URL),
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Template

```python
from vonage import Auth, Vonage
from vonage_messages import (WhatsappTemplate, WhatsappTemplateResource,
                             WhatsappTemplateSettings)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappTemplate(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    template=WhatsappTemplateResource(
        name=WHATSAPP_TEMPLATE_NAME,
        parameters=["Vonage Verification", "64873", "10"],
    ),
    whatsapp=WhatsappTemplateSettings(
        locale="en-GB",
        policy="deterministic",
    ),
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Text

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappText

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappText(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    text='Hello from the Vonage Messages API.',
)

response = client.messages.send(message)
print(response)
```

#### Whatsapp Send Video

```python
from vonage import Auth, Vonage
from vonage_messages import WhatsappVideo, WhatsappVideoResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappVideo(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    video=WhatsappVideoResource(url=MESSAGES_VIDEO_URL, caption="Test video file"),
)

response = client.messages.send(message)
print(response)
```

### Number Insight

#### Snippets in this Section

- [Async Callback](#async-callback)
- [Ni Advanced](#ni-advanced)
- [Ni Advanced Async Trigger](#ni-advanced-async-trigger)
- [Ni Basic](#ni-basic)
- [Ni Standard](#ni-standard)

#### Async Callback

```python
from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/webhooks/insight')
async def display_advanced_number_insight_info(request: Request):
    data = await request.json()
    print(data)
```

#### Ni Advanced

```python
from vonage import Auth, Vonage
from vonage_number_insight import (AdvancedSyncInsightRequest,
                                   AdvancedSyncInsightResponse)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

insight: AdvancedSyncInsightResponse = client.number_insight.get_advanced_info_sync(
    AdvancedSyncInsightRequest(number=INSIGHT_NUMBER)
)
pprint(insight)
```

#### Ni Advanced Async Trigger

```python
from vonage import Auth, Vonage
from vonage_number_insight import (AdvancedAsyncInsightRequest,
                                   AdvancedAsyncInsightResponse)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

insight: AdvancedAsyncInsightResponse = client.number_insight.get_advanced_info_async(
    AdvancedAsyncInsightRequest(number=INSIGHT_NUMBER, callback=INSIGHT_CALLBACK_URL)
)
pprint(insight)
```

#### Ni Basic

```python
from vonage import Auth, Vonage
from vonage_number_insight import BasicInsightRequest, BasicInsightResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

insight: BasicInsightResponse = client.number_insight.get_basic_info(
    BasicInsightRequest(number=INSIGHT_NUMBER)
)
pprint(insight)
```

#### Ni Standard

```python
from vonage import Auth, Vonage
from vonage_number_insight import (StandardInsightRequest,
                                   StandardInsightResponse)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

insight: StandardInsightResponse = client.number_insight.get_standard_info(
    StandardInsightRequest(number=INSIGHT_NUMBER)
)
pprint(insight)
```

### Numbers

#### Snippets in this Section

- [Buy](#buy)
- [Cancel](#cancel)
- [List](#list)
- [Search](#search)
- [Update](#update)

#### Buy

```python
from vonage import Auth, Vonage
from vonage_numbers import NumberParams, NumbersStatus

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

status: NumbersStatus = client.numbers.buy_number(
    params=NumberParams(
        country=NUMBER_COUNTRY_CODE,
        msisdn=NUMBER_MSISDN,
    )
)

print(status.model_dump())
```

#### Cancel

```python
from vonage import Auth, Vonage
from vonage_numbers import NumberParams, NumbersStatus

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

status: NumbersStatus = client.numbers.cancel_number(
    NumberParams(country=NUMBER_COUNTRY_CODE, msisdn=NUMBER_MSISDN)
)

print(status.model_dump())
```

#### List

```python
from vonage import Auth, Vonage
from vonage_numbers import ListOwnedNumbersFilter

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

numbers, count, next = client.numbers.list_owned_numbers(
    ListOwnedNumbersFilter(
        pattern=NUMBER_SEARCH_CRITERIA, search_pattern=NUMBER_SEARCH_PATTERN
    )
)

pprint(numbers)
print(count)
print(next)
```

#### Search

```python
from vonage import Auth, Vonage
from vonage_numbers import SearchAvailableNumbersFilter

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

numbers, count, next = client.numbers.search_available_numbers(
    SearchAvailableNumbersFilter(
        country=NUMBER_COUNTRY_CODE,
        size=3,
        pattern=NUMBER_SEARCH_CRITERIA,
        search_pattern=NUMBER_SEARCH_PATTERN,
        type=NUMBER_TYPE,
        features=NUMBER_FEATURES,
    )
)
pprint(numbers)
print(count)
print(next)

for number in numbers:
    print(f'Tel: {number.msisdn} Cost: {number.cost}')
```

#### Update

```python
from vonage import Auth, Vonage
from vonage_numbers import NumbersStatus, UpdateNumberParams

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

status: NumbersStatus = client.numbers.update_number(
    UpdateNumberParams(
        country=NUMBER_COUNTRY_CODE,
        msisdn=NUMBER_MSISDN,
        app_id='vonage-application-id',
        mo_http_url=NUMBER_SMS_CALLBACK_URL,
        mo_smpp_sytem_type='inbound',
        voice_callback_value=NUMBER_VOICE_CALLBACK_URL,
        voice_status_callback=NUMBER_VOICE_STATUS_CALLBACK_URL,
    )
)

print(status.model_dump())
```

### Sms

#### Snippets in this Section

- [Delivery Receipts](#delivery-receipts)
- [Receive Sms](#receive-sms)
- [Send An Sms](#send-an-sms)
- [Send An Sms With Unicode](#send-an-sms-with-unicode)
- [Send Signed Sms](#send-signed-sms)
- [Submit Sms Conversion](#submit-sms-conversion)
- [Verify Signed Sms](#verify-signed-sms)

#### Delivery Receipts

```python
from pprint import pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/webhooks/delivery-receipt')
async def get_delivery_receipt(request: Request):
    data = await request.json()
    pprint(data)
```

#### Receive Sms

```python
from pprint import pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/webhooks/inbound')
async def inbound_message(request: Request):
    data = await request.json()
    pprint(data)
```

#### Send An Sms

```python
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

message = SmsMessage(
    to=SMS_TO_NUMBER,
    from_=SMS_SENDER_ID,
    text="A text message sent using the Vonage SMS API.",
)

response: SmsResponse = client.sms.send(message)
print(response)
```

#### Send An Sms With Unicode

```python
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

message = SmsMessage(
    to=SMS_TO_NUMBER,
    from_=SMS_SENDER_ID,
    text='こんにちは世界',
    type='unicode',
)

response: SmsResponse = client.sms.send(message)
print(response)
```

#### Send Signed Sms

```python
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, signature_secret=SMS_SIGNATURE))

message = SmsMessage(
    to=SMS_TO_NUMBER,
    from_=SMS_SENDER_ID,
    text="A text message sent using the Vonage SMS API.",
)

response: SmsResponse = client.sms.send(message)
print(response)
```

#### Submit Sms Conversion

```python
from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

client.sms.submit_sms_conversion(
    message_id='MESSAGE_ID',
    delivered=True,
    timestamp='2020-01-01T12:00:00Z',
)

if client.http_client.last_response.status_code == 200:
    print('Conversion submitted successfully.')
else:
    print('Conversion not submitted.')
```

#### Verify Signed Sms

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv

envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_SIGNATURE_SECRET = os.getenv("VONAGE_SIGNATURE_SECRET")

from fastapi import FastAPI, Request
from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, signature_secret=VONAGE_SIGNATURE_SECRET))

app = FastAPI()


@app.post('/')
async def verify_signed_webhook(request: Request):
    data = await request.json()

    if client.http_client.auth.check_signature(data):
        print('Valid signature')
    else:
        print('Invalid signature')
```

### Subaccounts

#### Snippets in this Section

- [Create Subaccount](#create-subaccount)
- [Get Subaccount](#get-subaccount)
- [List Balance Transfers](#list-balance-transfers)
- [List Credit Transfers](#list-credit-transfers)
- [List Subaccounts](#list-subaccounts)
- [Reactivate Subaccount](#reactivate-subaccount)
- [Suspend Subaccount](#suspend-subaccount)
- [Transfer Balance](#transfer-balance)
- [Transfer Credit](#transfer-credit)
- [Transfer Number](#transfer-number)

#### Create Subaccount

```python
from vonage import Auth, Vonage
from vonage_subaccounts import NewSubaccount, SubaccountOptions

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: NewSubaccount = client.subaccounts.create_subaccount(
    SubaccountOptions(name=SUBACCOUNT_NAME, secret=SUBACCOUNT_SECRET)
)

print(response)
```

#### Get Subaccount

```python
from vonage import Auth, Vonage
from vonage_subaccounts import Subaccount

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

subaccount: Subaccount = client.subaccounts.get_subaccount(SUBACCOUNT_KEY)

print(subaccount)
```

#### List Balance Transfers

```python
from vonage import Auth, Vonage
from vonage_subaccounts import ListTransfersFilter, Transfer

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: list[Transfer] = client.subaccounts.list_balance_transfers(
    ListTransfersFilter(start_date=SUBACCOUNT_START_DATE)
)

print(response)
```

#### List Credit Transfers

```python
from vonage import Auth, Vonage
from vonage_subaccounts import ListTransfersFilter, Transfer

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: list[Transfer] = client.subaccounts.list_credit_transfers(
    ListTransfersFilter(start_date=SUBACCOUNT_START_DATE)
)

print(response)
```

#### List Subaccounts

```python
from vonage import Auth, Vonage
from vonage_subaccounts import ListSubaccountsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: ListSubaccountsResponse = client.subaccounts.list_subaccounts()

print(response)
```

#### Reactivate Subaccount

```python
from vonage import Auth, Vonage
from vonage_subaccounts import ModifySubaccountOptions, Subaccount

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: Subaccount = client.subaccounts.modify_subaccount(
    subaccount_api_key=SUBACCOUNT_KEY,
    options=ModifySubaccountOptions(suspended=False),
)

print(response)
```

#### Suspend Subaccount

```python
from vonage import Auth, Vonage
from vonage_subaccounts import ModifySubaccountOptions, Subaccount

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: Subaccount = client.subaccounts.modify_subaccount(
    subaccount_api_key=SUBACCOUNT_KEY,
    options=ModifySubaccountOptions(suspended=True),
)

print(response)
```

#### Transfer Balance

```python
from vonage import Auth, Vonage
from vonage_subaccounts import Transfer, TransferRequest

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = TransferRequest(
    from_=VONAGE_API_KEY, to=SUBACCOUNT_KEY, amount=SUBACCOUNT_BALANCE_AMOUNT
)

transfer: Transfer = client.subaccounts.transfer_balance(request)

print(transfer)
```

#### Transfer Credit

```python
from vonage import Auth, Vonage
from vonage_subaccounts import Transfer, TransferRequest

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = TransferRequest(
    from_=VONAGE_API_KEY, to=SUBACCOUNT_KEY, amount=SUBACCOUNT_CREDIT_AMOUNT
)

response: Transfer = client.subaccounts.transfer_credit(request)

print(response)
```

#### Transfer Number

```python
from vonage import Auth, Vonage
from vonage_subaccounts import TransferNumberRequest, TransferNumberResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = TransferNumberRequest(
    from_=VONAGE_API_KEY, to=SUBACCOUNT_KEY, number=VONAGE_VIRTUAL_NUMBER
)

response: TransferNumberResponse = client.subaccounts.transfer_number(request)

print(response)
```

### Users

#### Snippets in this Section

- [Create User](#create-user)
- [Delete User](#delete-user)
- [Get User](#get-user)
- [List Users](#list-users)
- [Update User](#update-user)

#### Create User

```python
from vonage import Auth, Vonage
from vonage_users import Channels, PstnChannel, User

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

user_options = User(
    name=USER_NAME,
    display_name=USER_DISPLAY_NAME,
    channels=Channels(pstn=[PstnChannel(number=123456)]),
)
user = client.users.create_user(user_options)

print(user)
```

#### Delete User

```python
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)
client.users.delete_user(USER_ID)
```

#### Get User

```python
from vonage import Auth, Vonage
from vonage_users import User

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)
user: User = client.users.get_user(USER_ID)

print(user)
```

#### List Users

```python
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

users_list, next_page_cursor = client.users.list_users()

print(users_list)
```

#### Update User

```python
from vonage import Auth, Vonage
from vonage_users import Channels, PstnChannel, SmsChannel, User

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

user_params = User(
    name=USER_NAME,
    display_name=USER_DISPLAY_NAME,
    channels=Channels(
        sms=[SmsChannel(number='1234567890')], pstn=[PstnChannel(number=123456)]
    ),
)
user: User = client.users.update_user(id=USER_ID, params=user_params)

print(user)
```

### Verify

#### Snippets in this Section

- [Cancel Request](#cancel-request)
- [Check Verification Code](#check-verification-code)
- [Send Request Email](#send-request-email)
- [Send Request Silent Auth](#send-request-silent-auth)
- [Send Request Sms](#send-request-sms)
- [Send Request Voice](#send-request-voice)
- [Send Request Whatsapp](#send-request-whatsapp)
- [Send Request Whatsapp Interactive](#send-request-whatsapp-interactive)
- [Send Request With Fallback](#send-request-with-fallback)

#### Cancel Request

```python
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

client.verify.cancel_verification(request_id=VERIFY_REQUEST_ID)
```

#### Check Verification Code

```python
from vonage import Auth, Vonage
from vonage_verify import CheckCodeResponse

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CheckCodeResponse = client.verify.check_code(
    request_id=VERIFY_REQUEST_ID, code=VERIFY_CODE
)
print(response)
```

#### Send Request Email

```python
from vonage import Auth, Vonage
from vonage_verify import (EmailChannel, StartVerificationResponse,
                           VerifyRequest)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_VERIFY_BRAND_NAME,
    workflow=[
        EmailChannel(to=VERIFY_TO_EMAIL),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
```

#### Send Request Silent Auth

```python
from vonage import Auth, Vonage
from vonage_verify import (SilentAuthChannel, StartVerificationResponse,
                           VerifyRequest)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[SilentAuthChannel(to=VERIFY_NUMBER)],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
```

#### Send Request Sms

```python
from vonage import Auth, Vonage
from vonage_verify import SmsChannel, StartVerificationResponse, VerifyRequest

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[
        SmsChannel(to=VERIFY_NUMBER),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
```

#### Send Request Voice

```python
from vonage import Auth, Vonage
from vonage_verify import (StartVerificationResponse, VerifyRequest,
                           VoiceChannel)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[
        VoiceChannel(to=VERIFY_NUMBER),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
```

#### Send Request Whatsapp

```python
from vonage import Auth, Vonage
from vonage_verify import (StartVerificationResponse, VerifyRequest,
                           WhatsappChannel)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[
        WhatsappChannel(to=VERIFY_NUMBER, from_=VERIFY_FROM_NUMBER),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
```

#### Send Request Whatsapp Interactive

```python
from vonage import Auth, Vonage
from vonage_verify import (StartVerificationResponse, VerifyRequest,
                           WhatsappChannel)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[
        WhatsappChannel(to=VERIFY_NUMBER, from_=VERIFY_FROM_NUMBER),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
```

#### Send Request With Fallback

```python
from vonage import Auth, Vonage
from vonage_verify import (EmailChannel, SilentAuthChannel,
                           StartVerificationResponse, VerifyRequest)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[
        SilentAuthChannel(to=VERIFY_NUMBER),
        EmailChannel(to=VERIFY_TO_EMAIL, from_=VERIFY_FROM_EMAIL),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
```

### Verify_Legacy

#### Snippets in this Section

- [Cancel](#cancel)
- [Check](#check)
- [Psd2 Request](#psd2-request)
- [Request](#request)
- [Search](#search)
- [Send Psd2 Verification Request With Workflow](#send-psd2-verification-request-with-workflow)
- [Send Verification Request With Workflow](#send-verification-request-with-workflow)
- [Trigger Next Step](#trigger-next-step)

#### Cancel

```python
from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

client.verify_legacy.cancel_verification(VERIFY_REQUEST_ID)
```

#### Check

```python
from vonage import Auth, Vonage
from vonage_verify_legacy import CheckCodeResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: CheckCodeResponse = client.verify_legacy.check_code(
    VERIFY_REQUEST_ID, VERIFY_CODE
)
print(response)
```

#### Psd2 Request

```python
from vonage import Auth, Vonage
from vonage_verify_legacy import Psd2Request, StartVerificationResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = Psd2Request(number=VERIFY_NUMBER, payee=VERIFY_PAYEE_NAME, amount=VERIFY_AMOUNT)

response: StartVerificationResponse = client.verify_legacy.start_psd2_verification(
    request
)
print(response)
```

#### Request

```python
from vonage import Auth, Vonage
from vonage_verify_legacy import StartVerificationResponse, VerifyRequest

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = VerifyRequest(number=VERIFY_NUMBER, brand='AcmeInc')

response: StartVerificationResponse = client.verify_legacy.start_verification(request)
print(response)
```

#### Search

```python
from vonage import Auth, Vonage
from vonage_verify_legacy import VerifyStatus

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: VerifyStatus = client.verify_legacy.search(VERIFY_REQUEST_ID)
print(response)
```

#### Send Psd2 Verification Request With Workflow

```python
from vonage import Auth, Vonage
from vonage_verify_legacy import Psd2Request, StartVerificationResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = Psd2Request(
    number=VERIFY_NUMBER,
    payee=VERIFY_PAYEE_NAME,
    amount=VERIFY_AMOUNT,
    workflow_id=VERIFY_WORKFLOW_ID,
)

response: StartVerificationResponse = client.verify_legacy.start_psd2_verification(
    request
)
print(response)
```

#### Send Verification Request With Workflow

```python
from vonage import Auth, Vonage
from vonage_verify_legacy import StartVerificationResponse, VerifyRequest

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = VerifyRequest(
    number=VERIFY_NUMBER, brand='AcmeInc', workflow_id=VERIFY_WORKFLOW_ID
)

response: StartVerificationResponse = client.verify_legacy.start_verification(request)
print(response)
```

#### Trigger Next Step

```python
from vonage import Auth, Vonage
from vonage_verify_legacy import VerifyControlStatus

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: VerifyControlStatus = client.verify_legacy.trigger_next_event(VERIFY_REQUEST_ID)
print(response)
```

### Voice

#### Snippets in this Section

- [Connect An Inbound Call](#connect-an-inbound-call)
- [Connect Callers To A Conference](#connect-callers-to-a-conference)
- [Earmuff A Call](#earmuff-a-call)
- [Get Recording](#get-recording)
- [Handle User Input](#handle-user-input)
- [Handle User Input With Asr](#handle-user-input-with-asr)
- [Make An Outbound Call](#make-an-outbound-call)
- [Make Outbound Call Ncco](#make-outbound-call-ncco)
- [Mute A Call](#mute-a-call)
- [Play Audio Stream Into Call](#play-audio-stream-into-call)
- [Play Dtmf Into Call](#play-dtmf-into-call)
- [Play Tts Into Call](#play-tts-into-call)
- [Receive An Inbound Call](#receive-an-inbound-call)
- [Record A Call](#record-a-call)
- [Record A Call With Split Audio](#record-a-call-with-split-audio)
- [Record A Conversation](#record-a-conversation)
- [Record A Message](#record-a-message)
- [Retrieve Info For A Call](#retrieve-info-for-a-call)
- [Retrieve Info For All Calls](#retrieve-info-for-all-calls)
- [Track Ncco](#track-ncco)
- [Transfer A Call](#transfer-a-call)
- [Transfer Call Inline Ncco](#transfer-call-inline-ncco)

#### Connect An Inbound Call

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv
from fastapi import FastAPI
from vonage_voice import Connect, PhoneEndpoint

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_VIRTUAL_NUMBER = os.environ.get('VONAGE_VIRTUAL_NUMBER')
VOICE_VOICE_TO_NUMBER = os.environ.get('VOICE_VOICE_TO_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call():
    ncco = [
        Connect(
            endpoint=[PhoneEndpoint(number=VOICE_VOICE_TO_NUMBER)],
            from_=VONAGE_VIRTUAL_NUMBER,
        ).model_dump(by_alias=True, exclude_none=True)
    ]

    return ncco
```

#### Connect Callers To A Conference

```python
import os
from os.path import dirname, join

from dotenv import load_dotenv
from fastapi import FastAPI
from vonage_voice import Conversation, NccoAction, Talk

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VOICE_CONFERENCE_NAME = os.environ.get("VOICE_CONFERENCE_NAME")

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call():
    ncco: list[NccoAction] = [
        Talk(text="Please wait while we connect you to the conference"),
        Conversation(name=VOICE_CONFERENCE_NAME),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]
```

#### Earmuff A Call

```python
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

client.voice.earmuff(VOICE_CALL_ID)
sleep(3)
client.voice.unearmuff(VOICE_CALL_ID)
```

#### Get Recording

```python
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

client.voice.download_recording(VOICE_RECORDING_URL, 'recording.mp3')
```

#### Handle User Input

```python
from pprint import pprint

from fastapi import Body, FastAPI, Request
from vonage_voice import Dtmf, Input, NccoAction, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Hello, please press any key to continue.'),
        Input(
            type=['dtmf'],
            dtmf=Dtmf(timeOut=5, maxDigits=1),
            eventUrl=[str(request.base_url) + 'webhooks/dtmf'],
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/dtmf')
async def answer_dtmf(data: dict = Body(...)):
    pprint(data)
    return [
        Talk(text=f'Hello, you pressed {data['dtmf']['digits']}').model_dump(
            by_alias=True, exclude_none=True
        )
    ]
```

#### Handle User Input With Asr

```python
from pprint import pprint

from fastapi import Body, FastAPI, Request
from vonage_voice import Input, NccoAction, Speech, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Please say something'),
        Input(
            type=['speech'],
            speech=Speech(endOnSilence=1, language='en-US'),
            eventUrl=[str(request.base_url) + 'webhooks/asr'],
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/asr')
async def answer_asr(data: dict = Body(...)):
    if data is not None and 'speech' in data:
        pprint(data)
        speech = data['speech']['results'][0]['text']
        return [
            Talk(text=f'Hello, you said {speech}').model_dump(
                by_alias=True, exclude_none=True
            )
        ]
    return [
        Talk(text=f'Sorry, I didn\'t understand your input.').model_dump(
            by_alias=True, exclude_none=True
        )
    ]
```

#### Make An Outbound Call

```python
from vonage import Auth, Vonage
from vonage_voice import CreateCallRequest, Phone, ToPhone

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.voice.create_call(
    CreateCallRequest(
        answer_url=[VOICE_ANSWER_URL],
        to=[ToPhone(number=VOICE_TO_NUMBER)],
        from_=Phone(number=VONAGE_VIRTUAL_NUMBER),
    )
)

pprint(response)
```

#### Make Outbound Call Ncco

```python
from vonage import Auth, Vonage
from vonage_voice import CreateCallRequest, Phone, Talk, ToPhone

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.voice.create_call(
    CreateCallRequest(
        ncco=[Talk(text='This is a text to speech call from Vonage.')],
        to=[ToPhone(number=VOICE_TO_NUMBER)],
        from_=Phone(number=VONAGE_VIRTUAL_NUMBER),
    )
)

pprint(response)
```

#### Mute A Call

```python
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

client.voice.mute(VOICE_CALL_ID)
sleep(5)
client.voice.unmute(VOICE_CALL_ID)
```

#### Play Audio Stream Into Call

```python
from vonage import Auth, Vonage
from vonage_voice import AudioStreamOptions, CallMessage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallMessage = client.voice.play_audio_into_call(
    VOICE_CALL_ID,
    audio_stream_options=AudioStreamOptions(stream_url=[VOICE_STREAM_URL]),
)

pprint(response)
```

#### Play Dtmf Into Call

```python
from vonage import Auth, Vonage
from vonage_voice import CallMessage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallMessage = client.voice.play_dtmf_into_call(
    uuid=VOICE_CALL_ID, dtmf=VOICE_DTMF_DIGITS
)

pprint(response)
```

#### Play Tts Into Call

```python
from vonage import Auth, Vonage
from vonage_voice import CallMessage, TtsStreamOptions

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallMessage = client.voice.play_tts_into_call(
    uuid=VOICE_CALL_ID,
    tts_options=TtsStreamOptions(text=VOICE_TEXT, language=VOICE_LANGUAGE),
)

pprint(response)
```

#### Receive An Inbound Call

```python
from fastapi import FastAPI, Query
from vonage_voice import Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(from_: str = Query(..., alias='from')):
    from_ = '-'.join(from_)
    return [
        Talk(text=f'Thank you for calling from {from_}').model_dump(
            by_alias=True, exclude_none=True
        )
    ]
```

#### Record A Call

```python
import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv
from fastapi import Body, FastAPI
from vonage_voice import Connect, NccoAction, PhoneEndpoint, Record

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_VIRTUAL_NUMBER = os.environ.get('VONAGE_VIRTUAL_NUMBER')
VOICE_TO_NUMBER = os.environ.get('VOICE_TO_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call():
    ncco: list[NccoAction] = [
        Record(eventUrl=['https://demo.ngrok.io/webhooks/recordings']),
        Connect(
            from_=VONAGE_VIRTUAL_NUMBER, endpoint=[PhoneEndpoint(number=VOICE_TO_NUMBER)]
        ),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}
```

#### Record A Call With Split Audio

```python
import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv
from fastapi import Body, FastAPI
from vonage_voice import Connect, NccoAction, PhoneEndpoint, Record

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_VIRTUAL_NUMBER = os.environ.get('VONAGE_VIRTUAL_NUMBER')
VOICE_TO_NUMBER = os.environ.get('VOICE_TO_NUMBER')

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call():
    ncco: list[NccoAction] = [
        Record(
            split='conversation',
            channels=2,
            eventUrl=['https://demo.ngrok.io/webhooks/recordings'],
        ),
        Connect(
            from_=VONAGE_VIRTUAL_NUMBER, endpoint=[PhoneEndpoint(number=VOICE_TO_NUMBER)]
        ),
    ]

    return [step.model_dump(by_alias=True, exclude_none=True) for step in ncco]


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}
```

#### Record A Conversation

```python
import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv
from fastapi import Body, FastAPI
from vonage_voice import Conversation

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VOICE_CONFERENCE_NAME = os.environ.get('VOICE_CONFERENCE_NAME')

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call():
    ncco = [
        Conversation(
            name=VOICE_CONFERENCE_NAME,
            record=True,
            eventMethod='POST',
            eventUrl=['https://demo.ngrok.io/webhooks/recordings'],
        )
    ]

    return ncco


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}
```

#### Record A Message

```python
from pprint import pprint

from fastapi import Body, FastAPI, Request
from vonage_voice import NccoAction, Record, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def answer_call(request: Request):
    print(request.base_url)
    ncco: list[NccoAction] = [
        Talk(
            text='Please leave a message after the tone, then press #. We will get back to you as soon as we can.'
        ),
        Record(
            endOnSilence=3,
            endOnKey='#',
            beepStart=True,
            eventUrl=[str(request.base_url) + 'webhooks/recordings'],
        ),
        Talk(text='Thank you for your message. Goodbye.'),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/recordings')
async def recordings(data: dict = Body(...)):
    pprint(data)
    return {'message': 'webhook received'}
```

#### Retrieve Info For A Call

```python
from vonage import Auth, Vonage
from vonage_voice import CallInfo

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallInfo = client.voice.get_call(VOICE_CALL_ID)
pprint(response)
```

#### Retrieve Info For All Calls

```python
from vonage import Auth, Vonage
from vonage_voice import ListCallsFilter

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

now = datetime.now(timezone.utc)
date_end = now.strftime('%Y-%m-%dT%H:%M:%SZ')
start = now - timedelta(hours=24)
date_start = start.strftime('%Y-%m-%dT%H:%M:%SZ')

calls, _ = client.voice.list_calls(
    ListCallsFilter(date_start=date_start, date_end=date_end)
)

for call in calls:
    pprint(call)
```

#### Track Ncco

```python
from fastapi import FastAPI, Request
from vonage_voice import NccoAction, Notify, Talk

app = FastAPI()


@app.get('/webhooks/answer')
async def inbound_call(request: Request):
    ncco: list[NccoAction] = [
        Talk(text=f'Thanks for calling the notification line.'),
        Notify(
            payload={"foo": "bar"},
            eventUrl=[str(request.base_url) + 'webhooks/notification'],
        ),
        Talk(text=f'You will never hear me as the notification URL will return an NCCO.'),
    ]

    return [action.model_dump(by_alias=True, exclude_none=True) for action in ncco]


@app.post('/webhooks/notification')
async def on_notification():
    return [
        Talk(text=f'Your notification has been received, loud and clear').model_dump(
            by_alias=True, exclude_none=True
        )
    ]
```

#### Transfer A Call

```python
from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

client.voice.transfer_call_answer_url(VOICE_CALL_ID, VOICE_NCCO_URL)
```

#### Transfer Call Inline Ncco

```python
from vonage import Auth, Vonage
from vonage_voice import Talk

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

ncco = [Talk(text='This is a transfer action using an inline NCCO')]

client.voice.transfer_call_ncco(VOICE_CALL_ID, ncco)
```


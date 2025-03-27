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
Many of the APIs require input data from the user. This is passed in through data models that you will find in the package for the specific API you want to call. This was intentional so the user doesn’t immediately import every data model from every single API whenever they import the top-level package, which would make it harder to find what is actually needed in an IDE, and allows for models with the same names in different namespaces. 

For example, to use a `VerifyRequest` object from the vonage-verify package, you’ll need to first import the vonage package to get the auth objects and the Verify methods, then import VerifyRequest from the vonage-verify package, like so:

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

This is explained in more detail in the blog post shared above. You can also find full, working examples in the Python Code Snippets repo here:
https://github.com/Vonage/vonage-python-code-snippets

Getting the Objects You Need Into Your Namespace
If you’re working with e.g. the Voice API, if you know you’re likely to use many of the data models, you can import them all into your app’s namespace (making it easier for your autocomplete etc. to find them) with the `*` operator, e.g.

from vonage_voice import *

request = CreateCallRequest(...)

It’s usually considered better practice to import just what you need, but using this method means the data models will all be available to you if you need to do some quick testing.
How the SDK handles errors
The Vonage Python SDK has various different classes of errors:

Some regular Python/package errors that can be raised during the course of SDK operation
The top-level VonageError, that custom SDK errors inherit from
Errors raised when using some packages, e.g. VerifyError
Errors raised by the HTTP client

It’s likely that when troubleshooting, you’ll especially see HTTP request errors, so let’s discuss these.
HTTP Request Errors
This is a class of errors raised when actually making the HTTP request or when receiving an HTTP response.

The higher-level error here is the HttpRequestError. There are other errors which are based on this and have the same properties, but different names that are more specific to the HTTP status code (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) received from the Vonage server, e.g. an AuthenticationError or a NotFoundError.

Each error of this type has properties that can be accessed when the error is caught. I.e. if you have a try-except block which catches an error, you can then access the error message and the response object which has additional information. This can be useful for debugging.

To catch an error in this way, do this:


try:
	vonage_client.call_vonage_api(...)
except HttpRequestError as e:
	print(‘Request failed:’)
	print(e.message)
	print(e.response.text)  

You can access any information about the request or the response from the e.response object.
Troubleshooting
Viewing the last request and response

Whether or not an HTTP request was successful, you can access the last request and response sent by accessing the relevant HTTP client attributes like this:

vonage_client.http_client.last_request
vonage_client.http_client.last_response

For example, to see the last request body and headers sent by the SDK, you can do:

print(vonage_client.http_client.last_request.body)
print(vonage_client.http_client.last_request.headers)

Authentication errors

If the SDK returns an AuthenticationError, this is because the Vonage Server was not able to authenticate the SDK user. In this case, you should check the authentication details that were provided.

Useful Resources
SDK on Github https://github.com/Vonage/vonage-python-sdk
SDK on PyPI https://pypi.org/project/vonage/
Python SDK introduction blog https://developer.vonage.com/en/blog/vonage-python-sdk-v4-is-now-live-#getting-started
Migration guide from old to new SDK https://github.com/Vonage/vonage-python-sdk/blob/main/V3_TO_V4_SDK_MIGRATION_GUIDE.md
Reach out to us on the #ask-devrel Slack channel if you have any questions.



## Request an Example

Please [raise an issue](https://github.com/Vonage/vonage-python-code-snippets/issues) to request an example that isn't present within the quickstart. Pull requests will be gratefully received.

## License

[MIT](LICENSE)

[sign-up]: https://dashboard.nexmo.com/sign-up
[buy-number]: https://dashboard.nexmo.com/buy-numbers

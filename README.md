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

All the examples run from a [Flask](http://flask.pocoo.org/) server.

Install any dependencies:


```sh
pip install -r requirements.txt
```

Run the server:

```sh
python server.py
```

Navigate to the appropriate route defined in `server.py` to execute the example.

## Request an Example

Please [raise an issue](https://github.com/Vonage/vonage-python-code-snippets/issues) to request an example that isn't present within the quickstart. Pull requests will be gratefully received.

## License

[MIT](LICENSE)

[sign-up]: https://dashboard.nexmo.com/sign-up
[buy-number]: https://dashboard.nexmo.com/buy-numbers

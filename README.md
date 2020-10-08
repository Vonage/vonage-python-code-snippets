# Nexmo Code Snippets for Python

![Author](https://img.shields.io/badge/author-Vonage-orange)
![Issues](https://img.shields.io/github/issues/Vonage/vonage-python-code-snippets)
![License](https://img.shields.io/github/license/Vonage/vonage-python-code-snippets)
![Stars](https://img.shields.io/github/stars/Vonage/vonage-python-code-snippets)
![Forks](https://img.shields.io/github/forks/Vonage/vonage-python-code-snippets)
![Last Commit](https://img.shields.io/github/last-commit/Vonage/vonage-python-code-snippets)
![Maintained](https://img.shields.io/maintenance/yes/2020)
![Size](https://img.shields.io/github/repo-size/Vonage/vonage-python-code-snippets)

<img src="https://developer.nexmo.com/assets/images/Vonage_Nexmo.svg" height="48px" alt="Nexmo is now known as Vonage" />

Code snipets also available for: [Java](https://github.com/nexmo/nexmo-java-code-snippets), [.NET](https://github.com/nexmo/nexmo-dotnet-code-snippets), [Node.js](https://github.com/nexmo/nexmo-node-code-snippets), [PHP](https://github.com/nexmo/nexmo-php-code-snippets), [Ruby](https://github.com/nexmo/nexmo-ruby-code-snippets), [Curl](https://github.com/Nexmo/nexmo-curl-code-snippets),[Go](https://github.com/Vonage/vonage-go-code-snippets)  and [Android](https://github.com/nexmo-community/quickstart-android)

The purpose of the Code Snippets is to provide simple examples focused
on one goal. For example, sending an SMS, handling an incoming SMS webhook,
or making a Text to Speech call.

## Setup

These code samples are meant to be used for [https://developer.nexmo.com/](https://developer.nexmo.com/), and are structured in such a way as to be used for internal testing. Developers are free to use these code snippets as a reference, but these may require changes to be worked into your specific application. We recommend checking out the [Nexmo Developer Website](https://developer.nexmo.com/), which displays these code snippets in a more copy/paste fashion.

To use the examples, you will first need a [Nexmo account][sign-up]. Then rename
the `example.env` file to `.env` and set the values as required.

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

Please [raise an issue](https://github.com/nexmo-community/nexmo-python-quickstart/issues) to request an example that isn't present within the quickstart. Pull requests will be gratefully received.

## License

[MIT](LICENSE)

[sign-up]: https://dashboard.nexmo.com/sign-up
[buy-number]: https://dashboard.nexmo.com/buy-numbers

# Nexmo Code Snippets for Python

Quickstarts also available for: [Java](https://github.com/Nexmo/nexmo-java-code-snippets), [.NET](https://github.com/Nexmo/nexmo-dotnet-code-snippets), [Node.js](https://github.com/Nexmo/nexmo-node-code-snippets), [PHP](https://github.com/Nexmo/nexmo-php-code-snippets),  [Ruby](https://github.com/Nexmo/nexmo-ruby-code-snippets) and [curl](https://github.com/Nexmo/nexmo-curl-code-snippets).

The purpose of the Code Snippets is to provide simple examples focused
on one goal. For example, sending an SMS, handling an incoming SMS webhook,
or making a Text to Speech call.

## Setup

To use the examples, you will first need a [Nexmo account][sign-up]. Then rename
the `example.env` file to `.env` and set the values as required.

For some of the examples you will need to [buy a number][buy-number].

## Running the Examples

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

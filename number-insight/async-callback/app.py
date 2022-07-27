from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def callback():
    print(request.get_json())
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

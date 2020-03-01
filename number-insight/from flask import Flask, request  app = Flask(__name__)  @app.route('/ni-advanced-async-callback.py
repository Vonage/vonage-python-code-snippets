from flask import Flask, request

app = Flask(__name__)

@app.route('/webhooks/number-insight', methods=['GET','POST'])
def callback():
    print(request.get_json() or request.args)
    return "Insight Retrieved, Check the logs", 200

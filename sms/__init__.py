import vonage

def send(config):
    client = vonage.Client(key=config['API_KEY'], secret=config['API_SECRET'])
    return client.sms.send_message({'from': config['FROM_NUMBER'], 'to': config['TO_NUMBER'], 'text': 'Hello from Nexmo!'})

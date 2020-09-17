import vonage

def send(config):
    sms = vonage.Sms(vonage.Client(key=config['API_KEY'], secret=config['API_SECRET']))
    return sms.send_message({'from': config['FROM_NUMBER'], 'to': config['TO_NUMBER'], 'text': 'Hello from Nexmo!'})

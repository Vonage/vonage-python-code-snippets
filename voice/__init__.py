from vonage import Client, Voice


def call(config):
    client = Client(
        application_id=config['VONAGE_APPLICATION_ID'], private_key=config['VONAGE_PRIVATE_KEY'])
    voice = Voice(client)
    ncco = [
        {
            'action': 'talk',
            'voiceName': 'Joey',
            'text': 'This is a text-to-speech test message.'
        }
    ]
    return voice.create_call({
        'to': [{'type': 'phone', 'number': config['TO_NUMBER']}],
        'from': {'type': 'phone', 'number': config['FROM_NUMBER']},
        'ncco': ncco
    })

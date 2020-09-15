import vonage, os
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

APPLICATION_ID=os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH=os.environ.get("APPLICATION_PRIVATE_KEY_PATH")

client = vonage.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH
)

voice = vonage.Voice(client)

stream_url = 'https://nexmo-community.github.io/ncco-examples/assets/voice_api_audio_streaming.mp3'
voice.send_audio(VONAGE_CALL_UUID, stream_url=[stream_url])

import nexmo


client = nexmo.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

client.send_speech(VONAGE_CALL_UUID, text='You are listening to a test text-to-speech call made with the Vonage Voice API')

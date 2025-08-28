import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import InitiateSipRequest, SipAuth, SipCall, SipOptions, TokenOptions

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_SESSION_ID = os.getenv("VIDEO_SESSION_ID")
VIDEO_TOKEN = os.getenv("VIDEO_TOKEN")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

options = SipOptions(
    uri=f'sip:447405192752@sip.nexmo.com;transport=tls',
    from_=f'442039051298@nexmo.com',
    headers={'header_key': 'header_value'},
    auth=SipAuth(username='adf31819', password='ectHFYYRYHRHF9w48eaghrs'),
    secure=False,
    video=False,
    observe_force_mute=True,
)

params = InitiateSipRequest(
    session_id=VIDEO_SESSION_ID,
    token=VIDEO_TOKEN,
    sip=options
)
sip_call: SipCall = vonage_client.video.initiate_sip_call(params)

print("=== Initiated SIP Call ===")
print(json.dumps(sip_call.model_dump(), indent=2))

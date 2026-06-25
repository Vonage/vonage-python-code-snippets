import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
INSIGHT_NUMBER = os.environ.get("INSIGHT_NUMBER")
IDENTITY_INSIGHTS_API_HOST = os.environ.get("IDENTITY_INSIGHTS_API_HOST")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_identity_insights import (
    EmptyInsight,
    IdentityInsightsRequest,
    IdentityInsightsResponse,
    InsightsRequest,
)

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=IDENTITY_INSIGHTS_API_HOST),
)

request = IdentityInsightsRequest(
    phone_number=INSIGHT_NUMBER,
    insights=InsightsRequest(original_carrier=EmptyInsight()),
)

response: IdentityInsightsResponse = client.identity_insights.requests(request)
pprint(response)

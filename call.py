import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get variables from .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
api_key_sid = os.getenv("TWILIO_API_KEY_SID")
api_key_secret = os.getenv("TWILIO_API_KEY_SECRET")
from_number = os.getenv("TWILIO_PHONE_NUMBER")   # Your Twilio number (+1857...)
to_number = os.getenv("MY_PHONE_NUMBER")         # Your Indian number (+91...)
twiml_url = os.getenv("TWIML_BIN_URL")           # Your TwiML Bin URL

# Authenticate with API Key
client = Client(api_key_sid, api_key_secret, account_sid)

# Place the call
call = client.calls.create(
    to=to_number,
    from_=from_number,
    url=twiml_url
)

print("✅ Call initiated:", call.sid)

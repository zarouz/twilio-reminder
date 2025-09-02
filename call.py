import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get variables from .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")   # Your Twilio number
to_number = os.getenv("TO_NUMBER")               # Destination number

client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=to_number,
    from_=from_number,
    twiml='<Response><Say>Hello! This is your scheduled reminder call from GitHub Actions.</Say></Response>'
)

print(f"Call initiated with SID: {call.sid}")

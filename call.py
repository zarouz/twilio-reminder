import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env for local development
load_dotenv()

# Get variables from environment
# For GitHub Actions, these are set via repository secrets
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN") # Use Auth Token for authentication
from_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("MY_PHONE_NUMBER")
twiml_url = os.getenv("TWIML_BIN_URL")

# Ensure all required environment variables are set
if not all([account_sid, auth_token, from_number, to_number, twiml_url]):
    print("❌ Error: Missing one or more required environment variables.")
    exit(1)

try:
    # Authenticate with Account SID and Auth Token
    client = Client(account_sid, auth_token)

    # Place the call
    print(f"📞 Initiating call from {from_number} to {to_number}...")
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        url=twiml_url
    )

    print(f"✅ Call initiated successfully! SID: {call.sid}")

except Exception as e:
    print(f"❌ An error occurred: {e}")
    exit(1)

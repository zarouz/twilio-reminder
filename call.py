import os
from twilio.rest import Client

print("Starting the call script...")

# Get credentials from environment variables set by GitHub Actions
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")  # Your Twilio number
to_number = os.getenv("TO_NUMBER")              # The number to call

# --- Validation Step ---
# Check if all required environment variables are present.
# This helps in debugging if secrets are not set correctly.
if not all([account_sid, auth_token, from_number, to_number]):
    print("Error: Missing one or more required environment variables.")
    print("Please check your repository's Actions secrets.")
    exit(1) # Exit with an error code

try:
    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    print(f"Attempting to call {to_number} from {from_number}...")

    # Create the call using TwiML for the voice message
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        twiml='<Response><Say>Hello. This is a scheduled call from your GitHub Actions workflow.</Say></Response>'
    )

    print(f"Call successfully initiated. Call SID: {call.sid}")

except Exception as e:
    print(f"An error occurred while making the call: {e}")
    exit(1) # Exit with an error code
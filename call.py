import os
from twilio.rest import Client

print("Starting the call script...")
print("--- Checking for environment variables ---")

# Get credentials from environment variables set by GitHub Actions
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("MY_PHONE_NUMBER") # Correctly uses MY_PHONE_NUMBER

# --- Enhanced Validation Step ---
# Check each variable and report its status.
secrets_are_valid = True
if account_sid:
    print("✅ TWILIO_ACCOUNT_SID found.")
else:
    print("❌ TWILIO_ACCOUNT_SID is missing.")
    secrets_are_valid = False

if auth_token:
    print("✅ TWILIO_AUTH_TOKEN found.")
else:
    print("❌ TWILIO_AUTH_TOKEN is missing.")
    secrets_are_valid = False

if from_number:
    print("✅ TWILIO_PHONE_NUMBER found.")
else:
    print("❌ TWILIO_PHONE_NUMBER is missing.")
    secrets_are_valid = False

if to_number:
    print("✅ MY_PHONE_NUMBER found.")
else:
    print("❌ MY_PHONE_NUMBER is missing.")
    secrets_are_valid = False

# If any secret is missing, print a final error and exit.
if not secrets_are_valid:
    print("\nError: One or more required secrets are missing.")
    print("Please go to your repository's Settings > Secrets and variables > Actions to add them.")
    exit(1)

print("--- All secrets found. Proceeding to make call. ---\n")

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
    exit(1)
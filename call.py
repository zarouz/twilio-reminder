import os
from twilio.rest import Client

print("Starting the call script...")
print("--- Checking for environment variables ---")

# Get credentials from environment variables set by GitHub Actions
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("MY_PHONE_NUMBER") 

# --- Enhanced Validation Step ---
# This section will now print the values to confirm they are not empty.
# GitHub Actions will automatically mask secret values in the logs.
secrets_are_valid = True
if account_sid:
    print(f"✅ TWILIO_ACCOUNT_SID loaded.")
else:
    print("❌ TWILIO_ACCOUNT_SID is missing or empty.")
    secrets_are_valid = False

if auth_token:
    print(f"✅ TWILIO_AUTH_TOKEN loaded.")
else:
    print("❌ TWILIO_AUTH_TOKEN is missing or empty.")
    secrets_are_valid = False

if from_number:
    print(f"✅ TWILIO_PHONE_NUMBER loaded with value: '{from_number}'")
else:
    print("❌ TWILIO_PHONE_NUMBER is missing or empty.")
    secrets_are_valid = False

if to_number:
    print(f"✅ MY_PHONE_NUMBER loaded with value: '{to_number}'")
else:
    print("❌ MY_PHONE_NUMBER is missing or empty.")
    secrets_are_valid = False

# If any secret is missing, print a final error and exit.
if not secrets_are_valid:
    print("\nError: One or more required secrets have empty values.")
    print("This often happens on scheduled runs if code isn't on the default branch.")
    exit(1)

print("--- All secrets appear to have values. Proceeding to make call. ---\n")

try:
    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    print(f"Attempting to call '{to_number}' from '{from_number}'...")

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


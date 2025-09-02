import os
from twilio.rest import Client

# --- Step 1: Check for and load the .env file for local execution ---
# This makes it easy to run the script on your own computer.
try:
    from dotenv import load_dotenv
    # Gets the absolute path to the directory where this script is located
    script_dir = os.path.dirname(__file__)
    dotenv_path = os.path.join(script_dir, '.env')
    if os.path.exists(dotenv_path):
        print("✅ Local .env file found, loading variables.")
        load_dotenv(dotenv_path=dotenv_path)
    else:
        print("ℹ️ No .env file found. Assuming this is a GitHub Actions run.")
except ImportError:
    print("ℹ️ 'python-dotenv' not installed. Assuming GitHub Actions environment.")


# --- Step 2: Get credentials from environment variables ---
# This works for both local .env files and GitHub Actions secrets.
print("\n--- Checking for required environment variables ---")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("MY_PHONE_NUMBER")

# --- Step 3: Validate that all variables were loaded ---
secrets_are_valid = True
if not account_sid:
    print("❌ TWILIO_ACCOUNT_SID is missing.")
    secrets_are_valid = False
if not auth_token:
    print("❌ TWILIO_AUTH_TOKEN is missing.")
    secrets_are_valid = False
if not from_number:
    print("❌ TWILIO_PHONE_NUMBER is missing.")
    secrets_are_valid = False
if not to_number:
    print("❌ MY_PHONE_NUMBER is missing.")
    secrets_are_valid = False

if not secrets_are_valid:
    print("\nError: One or more required variables are missing or empty.")
    print("If running locally, check your .env file. If on GitHub, check your repository secrets.")
    exit(1)

print("✅ All required variables found.")


# --- Step 4: Make the call using the Twilio client ---
try:
    print("\n--- Initializing Twilio Client and making call ---")
    client = Client(account_sid, auth_token)

    print(f"Attempting to call {to_number} from {from_number}...")

    # Create the call using TwiML for the voice message
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        twiml='<Response><Say>Hello. This is a call from your Python script.</Say></Response>'
    )

    print(f"✅ Call successfully initiated. Call SID: {call.sid}")

except Exception as e:
    print(f"❌ An error occurred while making the call: {e}")
    exit(1)


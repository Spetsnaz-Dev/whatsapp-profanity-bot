import os
from dotenv import load_dotenv
from twilio.rest import Client
from profanity_check import predict, predict_prob

load_dotenv()

# Twilio credentials
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
client = Client(account_sid, auth_token)

def handle_message(sender, message):
    # check if message contains links other than allowed domains
    
    
    # profanity check
    if predict([message])[0] == 1:  # Profanity detected
        reply = "Warning: Your message contains profanity. Please refrain from using offensive language."
    else:
        reply = message

    send_message(sender, reply)

def send_message(receiver, message):
    response = client.messages.create(
        from_=f'whatsapp:+{twilio_number}',
        to=f'whatsapp:+{receiver}',
        body=message
    )
    print({response})

# Example usage (replace with your Twilio number and handle incoming messages)
# For handling incoming messages, you'll need to set up a webhook or use Twilio's API for receiving messages.
# This example assumes a simplified setup for demonstration purposes.
handle_message("919735191987", "Nigga! This is a test message.")
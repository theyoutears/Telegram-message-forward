from telethon import TelegramClient, events

# Your authorization data (replace with your actual values)
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# Create a new Telegram client
client = TelegramClient('anon', api_id, api_hash)

# Keywords for filtering messages
keywords = ['keyword1', 'keyword2', 'keyword3']  # Add all necessary keywords here

# Event handler for new messages in specified channels
@client.on(events.NewMessage(chats=['name', id]))  # Add the IDs of both channels
async def handler(event):
    message = event.message
    message_text = message.text.lower()  # Convert message text to lowercase
    # Check if any keyword is in the message text
    if any(keyword in message_text for keyword in keywords):
        try:
            # Send the message to the specified group (replace with your group's username)
            await client.send_message('testRedirectGroup', message)
        except Exception as e:
            # Print any error that occurs during message forwarding
            print(f"Error forwarding message: {e}")

# Start the client with the provided phone number and run until disconnected
client.start(phone=phone_number)
client.run_until_disconnected()


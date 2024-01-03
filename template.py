from telethon import TelegramClient, events
from discord_webhook import DiscordWebhook

# Telegram API credentials
API_ID, API_HASH, SESSION_NAME = "API_ID", "API_HASH", "SESSION_NAME"
TG_CHANNEL_ID_1 = "CHANNEL_ID_1"

# Initialize the Telegram client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Chat and Webhook Configurations
CHAT_WEBHOOK_PAIRS = {
    TG_CHANNEL_ID_1: 'https://discord.com/api/webhooks/your_webhook_url_1',
    # Add more pairs as needed
}

async def forward_to_discord(event):
    chat_id = event.chat_id
    if chat_id in CHAT_WEBHOOK_PAIRS:
        webhook_url = CHAT_WEBHOOK_PAIRS[chat_id]
        message_content = event.message.text
        webhook = DiscordWebhook(url=webhook_url, content=message_content)
        await webhook.execute()

# Register event handler
for chat_id in CHAT_WEBHOOK_PAIRS.keys():
    client.add_event_handler(forward_to_discord, events.NewMessage(chats=chat_id))

# Start the Telegram client
with client:
    client.run_until_disconnected()
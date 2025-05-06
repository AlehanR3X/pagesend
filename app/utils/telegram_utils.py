from telethon import TelegramClient
from ..datos import api_id, api_hash

session_name = 'session_telegram'

def create_client():
    return TelegramClient(session_name, api_id, api_hash)

async def send_message(client, target_chat, message):
    try:
        await client.send_message(target_chat, message)
        return True
    except Exception as e:
        return str(e)

async def get_chat_history(client, target_chat, limit=10):
    try:
        messages = await client.get_messages(target_chat, limit=limit)
        return messages
    except Exception as e:
        return str(e)
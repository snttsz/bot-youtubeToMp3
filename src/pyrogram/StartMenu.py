from pyrogram import Client, filters
from pyrogram.types import Message

start_message = """



"""

@Client.on_message(filters.command('start'))
async def start(app: Client, message: Message) -> None:

    username = message.from_user.first_name

    await app.send_message(
        chat_id = message.chat.id,
        message = start_message)
    
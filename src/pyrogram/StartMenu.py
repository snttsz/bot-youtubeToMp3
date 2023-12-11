from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

start_message = """

Hey! I can download your preferred youtube videos and convert them to mp3 (and send it to you, of course)

You can download a single video or download a full playlist. In the case of playlists, each generated MP3 file will be sent to you individually. 

If you get interested, here's my source code: https://github.com/snttsz/bot-youtubeToMp3/

Now, you can type /download if you would like to use my services

"""

@Client.on_message(filters.command('start'))
async def start(app: Client, message: Message) -> None:

    username = message.from_user.first_name

    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Youtube video to mp3", callback_data = "singleVideo")],
            [InlineKeyboardButton("Youtube playlist to mp3", callback_data = "playlist")]
        ]
    )

    await app.send_message(
        chat_id = message.chat.id,
        text = start_message,
        disable_web_page_preview = True)
    

    
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

import asyncio

# local modules
from src.youtube.PlaylistExtractor import PlaylistExtractor
from src.youtube.YoutubeManager import YoutubeManager
from src.utils.FileHandler import FileHandler

@Client.on_callback_query(filters.regex(r"^(singleVideo|playlist)"))
async def handle_callback(app: Client, callback: CallbackQuery):


    if callback.data == "singleVideo":
        
        youtube_link = await callback.message.chat.ask("Got it. Now, send me the youtube video link.")

        await app.send_message(
            chat_id = callback.from_user.id,
            text = "Alright. Have your link. Now just wait a moment and I'll send the MP3 file to you 🎧."
        )

        await download_video(youtube_link.text, app, callback)

    else:
        
        youtube_link = await callback.message.chat.ask("Right. Can you send me your playlist link, please?")

        playListExtractor = PlaylistExtractor(
            url_playlist = youtube_link.text
        )

        playlist = playListExtractor.getLinks()

        if len(playlist) > 0:

            await app.send_message(
                chat_id = callback.from_user.id,
                text = "Perfect! Just give me some minutes while I download your stuffs... Would you like some coffee ☕?"
            )
            
            for link in playlist:
                
                await download_video(link, app, callback)

        else:

            await app.send_message(
                chat_id = callback.from_user.id,
                text = "Something went wrong and I couldn't get your playlist. May your youtube link ins't correct?"
            )

def run_async_loop(video_url, app, callback):
    
    loop = asyncio.new_event_loop()
    
    asyncio.set_event_loop(loop)
    
    loop.run_until_complete(download_video(video_url, app, callback))
    
    loop.close()


async def download_video(video_url: str, app: Client, callback: CallbackQuery):

    youtubeManager = YoutubeManager(video_url)

    operationResult = youtubeManager.download_video()

    if operationResult == True:

        # await app.send_message(
        #     chat_id = callback.from_user.id,
        #     text = f"I downloaded your {youtubeManager.getVideoName()} music! Just wait a second and I'll send it for you :)"
        # )

        await app.send_audio(
            chat_id = callback.from_user.id,
            audio = youtubeManager.getVideoPath(),
            caption = youtubeManager.getVideoName()
        )

        FileHandler.removeFile(youtubeManager.getVideoPath())
    
    else:

        await app.send_message(
            chat_id = callback.from_user.id,
            text = f"Something went wrong and I couldn't download your {video_url} video. May your youtube link isn't correct?"
        )
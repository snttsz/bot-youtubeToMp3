from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

import threading
import asyncio

# local modules
from src.youtube.PlaylistExtractor import PlaylistExtractor
from src.youtube.YoutubeManager import YoutubeManager
from src.utils.FileHandler import FileHandler

from src.youtube.YoutubeDownloader import YoutubeDownloader

@Client.on_callback_query(filters.regex(r"^(singleVideo|playlist)"))
async def handle_callback(app: Client, callback: CallbackQuery):


    if callback.data == "singleVideo":
        
        youtube_link = await callback.message.chat.ask("Got it. Now, send me the youtube video link.")

        await app.send_message(
            chat_id = callback.from_user.id,
            text = "Alright. Have your link. Now just wait a moment and I'll send the MP3 file to you 🎧."
        )

        thread = threading.Thread(
                    target = run_async_loop,
                    args = (youtube_link.text, app, callback)
                )
        
        thread.start()

    else:
        
        youtube_link = await callback.message.chat.ask("Right. Can you send me your playlist link, please?")
        
        # playlist = PlaylistExtractor(youtube_link.text)
        
        try:
            
            await app.send_message(
                chat_id = callback.from_user.id,
                text = "Perfect! Just give me some minutes while I download your stuffs... Would you like some coffee ☕?"
            )

            # links = playlist.getLinks()

            # for link in links:

            # thread = threading.Thread(
            #     target = run_async_loop2,
            #     args = (callback.from_user.id, youtube_link.text, app, callback)
            # )

            # thread.start()
            # thread.join()

            # await download_video2(callback.from_user.id, youtube_link.text, app, callback)

            listFiles = FileHandler.getAllFileNames("downloads/2089843939/")

            for file in listFiles:
                
                path = "downloads/{}".format(file)

                await send_video(path, file, app, callback)

                break

        except Exception as e:

            await app.send_message(
                chat_id = callback.from_user.id,
                text = "Something went wrong and I couldn't get your playlist. May your youtube link ins't correct?"
            )

            print(e.args)

def run_async_loop(video_url, app, callback):
    
    loop = asyncio.new_event_loop()
    
    asyncio.set_event_loop(loop)
    
    loop.run_until_complete(download_video(video_url, app, callback))
    
    loop.close()

def run_async_loop2(user_id: int, video_url: str, app: Client, callback: CallbackQuery):

    loop = asyncio.new_event_loop()
    
    asyncio.set_event_loop(loop)
    
    loop.run_until_complete(download_video2(user_id, video_url, app, callback))
    
    loop.close()

async def download_video2(user_id: int, video_url: str, app: Client, callback: CallbackQuery):

    # listFiles = FileHandler.getAllFileNames("downloads/2089843939/")

    # print(list)

    youtubeDownloader = YoutubeDownloader(video_url, user_id)

    operationResult = youtubeDownloader.download()

async def send_video(videoPath: str, videoName: str, app: Client, callback: CallbackQuery):

    # listFiles = FileHandler.getAllFileNames("downloads/2089843939/")

    # print(listFiles)

    await app.send_audio(
            chat_id = callback.from_user.id,
            audio = videoPath,
            caption = videoName
        )

    # FileHandler.removeFile(videoPath)


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
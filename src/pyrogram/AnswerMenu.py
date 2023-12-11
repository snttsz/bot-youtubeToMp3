from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message

import threading
import asyncio

# local modules
from src.utils.FileHandler import FileHandler
from src.youtube.YoutubeDownloader import YoutubeDownloader

@Client.on_message(filters.regex(r"/download"))
async def handle_callback(app: Client, message: Message):
        
    youtube_link = await message.chat.ask("Right. Can you send me your youtube link, please?")
    
    if ("www.youtube.com/" in youtube_link.text):
        try:
            
            await app.send_message(
                chat_id = message.from_user.id,
                text = "Perfect! Just give me some minutes while I download your stuffs... Would you like some coffee ☕?"
            )

            thread = threading.Thread(
                target = run_download_msc,
                args = (message.from_user.id, youtube_link.text)
            )

            thread.start()
            thread.join()

            listFiles = FileHandler.getAllFileNames("downloads/{}/".format(message.from_user.id))

            for file in listFiles:

                try:

                    FileHandler.rename_file(file, str(message.from_user.id))
                
                except:

                    print(file)
            
            await app.send_message(
                chat_id = message.from_user.id,
                text="Don't give up on me 🫨\n\n I just downloaded all your music and I'll send to you right now!"
            )
            
            for file in listFiles:

                path = "downloads/{}/{}".format(message.from_user.id, file)

                thread = threading.Thread(
                    target = run_send_msc,
                    args = (path, file, app, message)
                )

                thread.start()

        except Exception as e:

            await app.send_message(
                chat_id = message.from_user.id,
                text = "Something went wrong and I couldn't get your video/playlist. May your youtube link ins't correct?"
            )

            # print(e, e.args, e.with_traceback())
    

    else:

        await app.send_message(
            chat_id = message.from_user.id,
            text = "Right, good one. You ALMOST tricked me."
        )

def run_download_msc(user_id: int, video_url: str, app: Client, message: Message):

    loop = asyncio.new_event_loop()
    
    asyncio.set_event_loop(loop)
    
    loop.run_until_complete(download_msc(user_id, video_url, app, message))
    
    loop.close()

async def download_msc(user_id: int, video_url: str, app: Client, message: Message):
    
    try:
        youtubeDownloader = YoutubeDownloader(video_url, user_id)

        youtubeDownloader.download()   

    except:

        await app.send_message(
            chat_id = message.from_user.id,
            text = "There's something wrong with your link. Can you check it and send to me again? You can call the /download command when you're ready."
        ) 

def run_send_msc(video_path: str, video_name: str, app: Client, message: Message):

    loop = asyncio.new_event_loop()
    
    asyncio.set_event_loop(loop)
    
    loop.run_until_complete(send_msc(video_path, video_name, app, message))
    
    loop.close()

async def send_msc(videoPath: str, videoName: str, app: Client, message: Message):

    try:

        await app.send_audio(
                chat_id = message.from_user.id,
                audio = videoPath,
                caption = videoName
            )

        FileHandler.removeFile(videoPath)

    except Exception as e:

        # print("Error ---> user {} : {} --> {}".format(message.from_user.id, message.from_user.first_name, e.args))
        pass

    except UnicodeDecodeError as e:

        pass

    except ValueError as e:

        pass
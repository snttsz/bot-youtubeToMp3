from dotenv import load_dotenv
from pyrogram import Client
from pyromod import listen
from os import getenv


# Loading server credentials
load_dotenv("credentials.env")

if __name__ == "__main__":

    plugins = dict (
        # root = "tests/"
        root = "src/pyrogram/"
    )

    app = Client(
        name = "youtubeplaylist-to-mp3",
        api_id = getenv("api_id"),
        api_hash = getenv("api_hash"),
        bot_token = getenv("bot_token"),
        plugins = plugins
    )


    app.run()
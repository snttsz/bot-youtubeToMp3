# # YoutubeToMp3 Bot

Source code of a telegram bot that can send to a user a MP3 file extracted from a youtube video. It can also handle playlists.

Link of "official" bot: https://t.me/YoutubePlaylistToMP3_Bot (it is using the no-threading version)

# How to setup locally

Edit the credentials.env file with your telegram credentials. Here's the official telegram tutorial of how you can have access to it, in case of you don't know: https://core.telegram.org/api/obtaining_api_id

Then, install the requirements in your enviroment by tipping in your terminal:

`pip install -r requirements.txt`

Now, if everything works successfully, you can run the bot by tipping:

`python3 main.py`

Also, if you're a ubuntu user and don't have ffmpeg in your system, it may raise an error when downloading a video with youtube_dl API. You can fix it by simply installing ffmpeg with the following command:

`sudo apt-get install ffmpeg`

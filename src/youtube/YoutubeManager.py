import youtube_dl

class YoutubeManager():

    def __init__(self, video_url: str, username: str) -> None:

        self.filepath = "downloads/"
        self.fileName = None
        
        self.videoUrl = video_url
        self.username = username

    def download_video(self) -> None:

        video_info = youtube_dl.YoutubeDL().extract_info(
            url = self.videoUrl,
            download = False
        )
        
        self.fileName = "{}.mp3".format(video_info["title"])

        options = {
            "format" : "bestaudio/best",
            "keepvideo" : False,
            "outtmp1" : self.fileName
        }

        with youtube_dl.YoutubeDL(options) as yd1:
            yd1.download(video_info["webpage_url"])

    def getVideoPath(self) -> str:
        pass


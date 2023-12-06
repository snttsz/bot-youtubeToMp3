import yt_dlp as youtube_dl

from src.utils.FileHandler import FileHandler

class YoutubeDownloader():

    def __init__(self, url: str, userid: str) -> None:
        
        self.url = url
        self.userid = userid

        self.filepath = "downloads/{}/".format(userid)
    
    def download(self) -> bool:

        FileHandler.createPathIfDontExist(self.filepath)

        try:
            options = {
                'format': 'bestaudio/best',
                
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3'
                    }
                ],

                'outtmpl': f'{self.filepath}/%(title)s.%(ext)s',
                'keepvideo': False
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                
                ydl.download([self.url])

            return True

        except Exception as e:

            print("YoutubeDownloader.download returned an error --> {}".format(e))

            return False
    
    def getResultPath(self):

        return self.filepath


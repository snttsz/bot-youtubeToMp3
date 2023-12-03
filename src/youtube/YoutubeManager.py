import yt_dlp as youtube_dl
from unidecode import unidecode

class YoutubeManager():
    
    def __init__(self, video_url: str) -> None:

        self.filepath = "downloads/"
        self.fileName = None
        
        self.videoUrl = video_url

        self.ydl_opts = {
            "quiet" : True,
            "extract_flat" : True,
            "force_generic_extractor: " : True
        }

        self.info_dict = None

    def download_video(self) -> bool:

        try:
            
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:

                self.info_dict = ydl.extract_info(self.videoUrl, download=False)
                self.fileName = "{}".format(unidecode(self.info_dict['title']))
                self.fileName = self.fileName.replace("/", "")

                ydl.close()

            self.ydl_opts = {
            'format': 'bestaudio/best',
            
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],

            'outtmpl': f'{self.filepath}{self.fileName}',
            'keepvideo': False,
            }
            
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:

                self.filepath = self.filepath + self.fileName + ".mp3"
                
                ydl.process_info(self.info_dict)

                ydl.close()

            return True
        
        except Exception as e:
            print("Erro: {}\n{}".format(e, e.args))
            return False

    def getVideoPath(self) -> str:
        return self.filepath
    
    def getVideoName(self) -> str:
        return self.fileName
    
    def setVideoUrl(self, video_url: str) -> str:
        self.videoUrl = video_url




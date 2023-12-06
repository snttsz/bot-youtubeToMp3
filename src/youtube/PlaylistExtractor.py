import yt_dlp as youtube_dl

class PlaylistExtractor():

    def __init__(self, url_playlist: str) -> None:
        
        self.options = {
            "quiet" : True,
            "extract_flat" : True,
            "force_generic_extractor: " : True
        }

        self.url_playlist = url_playlist

    def getLinks(self) -> list:

        links = []

        with youtube_dl.YoutubeDL(self.options) as ydl:

            result = ydl.extract_info(
                url = self.url_playlist,
                download = False)
            
            if "entries" in result:
                
                links = [entry["url"] for entry in result["entries"]]
        
        return links


    
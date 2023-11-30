import youtube_dl

class PlaylistExtractor():

    def __init__(self) -> None:
        
        self.options = {
            "quiet" : True,
            "extract_flat" : True,
            "force_generic_extractor: " : True
        }

    def getLinks(self, url_playlist: str) -> list:

        links = []

        with youtube_dl.YoutubeDL(self.options) as ydl:

            result = ydl.extract_info(
                url = url_playlist,
                download = False)
            
            if "entries" in result:
                
                links = [entry["url"] for entry in result["entries"]]
        
        return links

    
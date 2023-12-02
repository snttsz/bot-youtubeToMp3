import os

class FileHandler():

    @staticmethod    
    def removeFile(filepath: str) -> bool:

        try:
            os.remove(filepath)

        except Exception as e:
            print("FileHandler.removeFile error --> {}".format(e))
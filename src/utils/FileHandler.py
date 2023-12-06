import os

class FileHandler():

    @staticmethod    
    def removeFile(filepath: str) -> bool:

        try:
            os.remove(filepath)

        except Exception as e:
            print("FileHandler.removeFile error --> {}".format(e))
    
    @staticmethod
    def createPathIfDontExist(path: str) -> None:
        
        if not os.path.exists(path):

            os.makedirs(path)
    
    @staticmethod
    def getAllFileNames(path: str) -> list:

        filenames = []

        for file in os.listdir(path):

            if os.path.isfile(os.path.join(path, file)):

                filenames.append(file)
        
        return filenames

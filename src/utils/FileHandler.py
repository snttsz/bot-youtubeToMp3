import os
from unidecode import unidecode
import subprocess

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

    @staticmethod
    def rename_file(file: str, userid: str) -> str:
            
        path = "downloads/{}/".format(userid)

        newFile = unidecode(file)

        os.rename(path + file, path + newFile)

        return path + newFile

    @staticmethod
    def rename_file_bash(file: str, userid: str) -> None:

        path = "downloads/{}/{}".format(userid, file)

        newFile = unidecode(file)

        command = f"cd downloads/{userid}/ && mv '{file}' '{newFile}'"

        result = subprocess.run(command, shell=True)

        print("PROCCESS ---------->> {}".format(result.stdout))
from os import getenv
from filestack import Client

from dotenv import load_dotenv
load_dotenv()

class FileSharer:

    def __init__(self, file_path, api_key = getenv('API_KEY')):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.file_path)
        return new_filelink.url
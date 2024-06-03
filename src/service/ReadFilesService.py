import os
from src.reader.FileReader import FileReader

class ReadFilesService:
    def __init__(self):
        self.baseDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.fileReader = FileReader()

    def readAppendTextContent(self):
        return self.fileReader.readFileContent(os.path.join(self.baseDir, 'append_text.txt'))

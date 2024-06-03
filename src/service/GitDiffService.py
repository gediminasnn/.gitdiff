# src/service/GitDiffService.py

from src.commandrunner.GitCommandRunner import GitCommandRunner
from src.service.ReadFilesService import ReadFilesService
from src.copier.ClipboardCopier import ClipboardCopier

class GitDiffService:
    def __init__(self):
        self.gitCommandRunner = GitCommandRunner()
        self.readFilesService = ReadFilesService()
        self.clipboardCopier = ClipboardCopier()

    def getAndCopyStagedDiffs(self):
        content = self.gitCommandRunner.getStagedDiffs()

        content += self.readFilesService.readAppendTextContent()

        self.clipboardCopier.clip(content)

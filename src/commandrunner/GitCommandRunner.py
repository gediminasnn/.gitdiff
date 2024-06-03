# src/commandrunner/GitCommandRunner.py

import subprocess

class GitCommandRunner:
    def runGitCommand(self, command):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode != 0:
            raise Exception(f"Git command failed: {result.stderr}")
        return result.stdout

    def getStagedDiffs(self):
        command = "git diff --cached"
        return self.runGitCommand(command)

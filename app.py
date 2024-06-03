# app.py

import sys
from src.service.GitDiffService import GitDiffService

if __name__ == "__main__":
    try:
        gitDiffService = GitDiffService()
        gitDiffService.getAndCopyStagedDiffs()
        print("Staged git diffs have been copied to the clipboard.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

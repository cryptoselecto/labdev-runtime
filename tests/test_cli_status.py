from pathlib import Path
import os
from labdev.cli import status

def test_status(capsys):
    old_cwd = os.getcwd()
    try:
        repo_root = Path(__file__).resolve().parents[1]
        os.chdir(repo_root)
        
        # Call status() in the current repo
        status()
        
        # Capture printed output
        captured = capsys.readouterr()
        out = captured.out
        
        # Basic sanity checks on the output
        assert "Repo path:" in out
        assert "Current branch name:" in out
    finally:
        os.chdir(old_cwd)

import os
from git import Repo
from labdev.cli import status
import pytest
import tempfile

def test_status(capsys):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Initialize a temporary Git repository
        repo = Repo.init(temp_dir)
        
        # Capture the output of the status function
        result = status()
        
        # Check if the expected repo path and branch name are in the output
        assert os.path.abspath(temp_dir) in result
        assert repo.active_branch.name in result

if __name__ == "__main__":
    pytest.main(['-v', '-s'])

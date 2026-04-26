import os
from labdev.cli import status
import pytest

def test_status(capsys):
    repo = Repo(search_parent_directories=True)
    expected_repo_path = repo.working_tree_dir
    expected_branch_name = repo.active_branch.name
    
    # Capture the output of the status function
    result = status()
    
    # Check if the expected repo path and branch name are in the output
    assert expected_repo_path in result
    assert expected_branch_name in result

if __name__ == "__main__":
    pytest.main(['-v', '-s'])

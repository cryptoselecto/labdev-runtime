import os
from git import Repo
from labdev.cli import status

def test_status():
    repo = Repo(search_parent_directories=True)
    expected_repo_path = repo.working_tree_dir
    expected_branch_name = repo.active_branch.name
    
    # Capture the output of the status function
    with open(os.devnull, 'w') as devnull:
        old_stdout = os.dup(1)
        os.dup2(devnull.fileno(), 1)
        
        status()
        
        os.dup2(old_stdout, 1)
    
    # Check if the expected repo path and branch name are in the output
    with open('status_output.txt', 'r') as f:
        output = f.read()
    
    assert expected_repo_path in output
    assert expected_branch_name in output

if __name__ == "__main__":
    test_status()

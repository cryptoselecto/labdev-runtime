import os
from labdev.cli import run, main
import pytest
import subprocess
from unittest.mock import patch, mock_open

def test_run_invokes_aider_with_message():
    task = "example_task"
    
    with patch('shutil.which', return_value='/path/to/aider'):
        with patch('git.Repo.search_parent_directories', return_value=True):
            with patch('subprocess.run') as mock_subprocess_run:
                run(task)
                
                assert mock_subprocess_run.call_args == subprocess.call(['aider', '--message', task], check=False)

def test_run_returns_error_if_aider_missing():
    task = "example_task"
    
    with patch('shutil.which', return_value=None):
        result = run(task)
        
        assert result != 0

def test_main_dispatches_run_with_task(monkeypatch):
    task = "example_task"
    
    monkeypatch.setattr(sys, 'argv', ["labdev", "run", task])
    
    with patch('labdev.cli.run') as mock_run:
        main()
        
        assert mock_run.call_args == run(task)

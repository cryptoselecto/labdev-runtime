import os
from labdev.cli import run
import pytest
import subprocess
from unittest.mock import patch, mock_open

def test_run_task(capsys):
    task = "example_task"
    with pytest.raises(SystemExit) as exc_info:
        run(task)
    
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    out = captured.out
    
    # Basic sanity checks on the output
    assert f"Running task: {task}" in out

def test_run_task_with_error(capsys):
    task = "nonexistent_task"
    with pytest.raises(SystemExit) as exc_info:
        run(task)
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    out = captured.out
    
    # Basic sanity checks on the output
    assert f"Error: Task '{task}' not found." in out

def test_run_task_with_aider_not_installed(capsys, monkeypatch):
    task = "example_task"
    
    def mock_subprocess_run(*args, **kwargs):
        raise FileNotFoundError("aider executable not found")
    
    monkeypatch.setattr(subprocess, 'run', mock_subprocess_run)
    
    with pytest.raises(SystemExit) as exc_info:
        run(task)
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    out = captured.out
    
    # Basic sanity checks on the output
    assert "Error: aider executable not found." in out

def test_run_task_with_git_repo(capsys, monkeypatch):
    task = "example_task"
    
    def mock_subprocess_run(*args, **kwargs):
        pass
    
    monkeypatch.setattr(subprocess, 'run', mock_subprocess_run)
    
    with patch('os.getcwd', return_value='/path/to/repo'):
        with patch('git.Repo.search_parent_directories', return_value=True):
            run(task)
    
    captured = capsys.readouterr()
    out = captured.out
    
    # Basic sanity checks on the output
    assert f"Running task: {task}" in out

def test_run_task_with_no_git_repo(capsys, monkeypatch):
    task = "example_task"
    
    def mock_subprocess_run(*args, **kwargs):
        pass
    
    monkeypatch.setattr(subprocess, 'run', mock_subprocess_run)
    
    with patch('os.getcwd', return_value='/path/to/repo'):
        with patch('git.Repo.search_parent_directories', return_value=False):
            with pytest.raises(SystemExit) as exc_info:
                run(task)
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    out = captured.out
    
    # Basic sanity checks on the output
    assert "Error: Not inside a git repository." in out

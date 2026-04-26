import os
from labdev.cli import init

def test_init(tmp_path):
    old_cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        
        # Create an empty .gitignore file if needed
        gitignore_path = os.path.join(tmp_path, '.gitignore')
        with open(gitignore_path, 'w') as f:
            pass
        
        init()
        
        # Assertions on .aider.conf.yml and .gitignore inside tmp_path
        aider_conf_path = os.path.join(tmp_path, '.aider.conf.yml')
        assert os.path.exists(aider_conf_path)
        
        with open(aider_conf_path, 'r') as f:
            content = f.read()
            assert "model: \"ollama/qwen2.5-coder:7b\"" in content
            assert "set-env:" in content
            assert "- OLLAMA_API_BASE=http://192.168.1.111:11434" in content
        
        gitignore_path = os.path.join(tmp_path, '.gitignore')
        with open(gitignore_path, 'r') as f:
            content = f.read()
            assert ".aider*" in content
    finally:
        os.chdir(old_cwd)

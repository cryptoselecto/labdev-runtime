import os
from labdev.cli import init
import tempfile

def test_init(capsys):
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        
        # Run the init function
        init(capsys)
        
        # Check if .aider.conf.yml exists and contains the expected content
        aider_conf_path = os.path.join(temp_dir, '.aider.conf.yml')
        assert os.path.exists(aider_conf_path)
        
        with open(aider_conf_path, 'r') as f:
            content = f.read()
            assert "model: \"ollama/qwen2.5-coder:7b\"" in content
            assert "set-env:" in content
            assert "- OLLAMA_API_BASE=http://192.168.1.111:11434" in content
        
        # Check if .gitignore contains .aider*
        gitignore_path = os.path.join(temp_dir, '.gitignore')
        with open(gitignore_path, 'r') as f:
            content = f.read()
            assert ".aider*" in content

if __name__ == "__main__":
    test_init(capsys)

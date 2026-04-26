import os
from git import Repo
import argparse

def status():
    repo = Repo(search_parent_directories=True)
    return f"Repo path: {repo.working_tree_dir}\nCurrent branch name: {repo.active_branch.name}"

def init():
    repo_path = os.getcwd()
    aider_conf_path = os.path.join(repo_path, '.aider.conf.yml')
    
    if not os.path.exists(aider_conf_path):
        with open(aider_conf_path, 'w') as f:
            f.write("""
model: "ollama/qwen2.5-coder:7b"
set-env:
  - OLLAMA_API_BASE=http://192.168.1.111:11434
""")
    
    gitignore_path = os.path.join(repo_path, '.gitignore')
    with open(gitignore_path, 'a+') as f:
        f.seek(0)
        if not any(line.strip() == '.aider*' for line in f):
            f.write('.aider*\n')

def main():
    parser = argparse.ArgumentParser(description="Labdev runtime commands.")
    subparsers = parser.add_subparsers(dest='command')

    status_parser = subparsers.add_parser('status', help='Show repository information.')
    status_parser.set_defaults(func=status)

    init_parser = subparsers.add_parser('init', help='Initialize the repo with .aider.conf.yml')
    init_parser.set_defaults(func=init)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

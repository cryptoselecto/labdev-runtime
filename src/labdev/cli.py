import os
from git import Repo
import argparse
import subprocess
import shutil
import sys

def status():
    repo = Repo(search_parent_directories=True)
    latest_commit = repo.head.commit
    
    print(f"Repo path: {repo.working_tree_dir}")
    print(f"Current branch name: {repo.active_branch.name}")
    print(f"Latest commit short hash: {latest_commit.hexsha[:7]}")
    print(f"Latest commit author name and email: {latest_commit.author.name} <{latest_commit.author.email}>")
    print(f"Latest commit authored date: {latest_commit.authored_datetime}")

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

def run(task):
    aider_path = shutil.which("aider")
    if not aider_path:
        print("Error: aider executable not found.")
        return 1
    
    repo = Repo(search_parent_directories=True)
    if not repo.git_dir:
        print("Error: Not inside a git repository.")
        return 1
    
    try:
        subprocess.run([aider_path, '--message', task], check=False)
        return 0
    except Exception as e:
        print(f"Error running aider: {e}")
        return 1

def main():
    parser = argparse.ArgumentParser(description="Labdev runtime commands.")
    subparsers = parser.add_subparsers(dest='command')

    status_parser = subparsers.add_parser('status', help='Show repository information.')
    status_parser.set_defaults(func=status)

    init_parser = subparsers.add_parser('init', help='Initialize the repo with .aider.conf.yml')
    init_parser.set_defaults(func=init)
    
    run_parser = subparsers.add_parser('run', help='Run a task using aider.')
    run_parser.add_argument('task', type=str, help='The task to run.')
    run_parser.set_defaults(func=run)

    args = parser.parse_args()
    if args.command == "run":
        return run(args.task)
    elif args.command == "status":
        status()
        return 0
    elif args.command == "init":
        init()
        return 0
    else:
        parser.print_help()
        return 1

if __name__ == "__main__":
    sys.exit(main())

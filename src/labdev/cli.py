import os
from git import Repo
import argparse

def status():
    repo = Repo(search_parent_directories=True)
    print(f"Repo path: {repo.working_tree_dir}")
    print(f"Current branch name: {repo.active_branch.name}")
    latest_commit = repo.head.commit
    print(f"Latest commit short hash: {latest_commit.hexsha[:7]}")
    print(f"Latest commit author name and email: {latest_commit.author.name} <{latest_commit.author.email}>")
    print(f"Latest commit authored date: {latest_commit.authored_date}")

def main():
    parser = argparse.ArgumentParser(description="Labdev runtime commands.")
    subparsers = parser.add_subparsers(dest='command')

    status_parser = subparsers.add_parser('status', help='Show repository information.')
    status_parser.set_defaults(func=status)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

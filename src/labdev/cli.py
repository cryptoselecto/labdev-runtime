import os
from git import Repo
import argparse

def status():
    repo = Repo(search_parent_directories=True)
    return f"Repo path: {repo.working_tree_dir}\nCurrent branch name: {repo.active_branch.name}"

def main():
    parser = argparse.ArgumentParser(description="Labdev runtime commands.")
    subparsers = parser.add_subparsers(dest='command')

    status_parser = subparsers.add_parser('status', help='Show repository information.')
    status_parser.set_defaults(func=status)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        print(args.func())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

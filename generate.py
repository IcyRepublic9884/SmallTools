"""
Simple Directory tree generator
"""

import os
import sys


def make_tree(startpath: str):
    """Display the file tree according to the start path

    Args:
        startpath (str): path to start the tree
    """
    for root, _, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '-' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)

        for f in files:
            print('{}{}'.format(subindent, f))


if __name__ == '__main__':
    # Execute as Script
    if len(sys.argv) < 2:
        print("Argument Required to run the generator")
        sys.exit(-1)

    elif os.path.isdir(sys.argv[1]):
        try:
            make_tree(sys.argv[1])
        except RecursionError:
            print("Max recursion depth exceeded, error.")

    elif sys.argv[1] == '.':
        try:
            make_tree(os.getcwd())
        except RecursionError:
            print("Max recursion depth exceeded, error.")
    else:
        print("An error occured")

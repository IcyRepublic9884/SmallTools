"""
Simple Script for renaming a file
"""

import os
# import shutil
import sys


def validate_filename(filename: str) -> bool:
    """Validate a filename

    Args:
        filename (str): The name of the file

    Returns:
        bool: weather the file name is valid or not
    """
    return not filename.__contains__('\\/:<>|*"\'')


if len(sys.argv) < 3:
    print("Error, file name(s) not provided")

FILE_NAME, NEW_NAME = sys.argv[1], sys.argv[2]

if os.path.isfile(FILE_NAME):
    # TODO: validate and to shutil magic (or os)
    pass
else:
    print("The file you provided does not exist !")

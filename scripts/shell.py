"""
This file contains tools that allow us to interact with shell programs
"""

import subprocess
import constants


def get_file(directory: str) -> str:
    """
    Uses fzf to get a file from the given directiory
    :return: the name of the file
    """
    find_result = subprocess.run(
        ["find", directory, "-maxdepth", "1"],
        check=True,
        capture_output=True,
    )
    file_name = (
        subprocess.run(
            ["fzf"],
            stdout=subprocess.PIPE,
            input=find_result.stdout,
        )
        .stdout.decode("utf-8")
        .strip()
    )
    return file_name


def clean_files():
    """
    Remove excess files that are created by latex compilation
    :return:
    """
    print("Cleaning Files")
    subprocess.run(
        ["latexmk", "-c"],
    )

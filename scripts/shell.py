"""
This file contains tools that allow us to interact with shell programs
"""

from shutil import copyfile
import constants
import subprocess


def create_new_content_file(title: str, type: str, target_dir: str):
    """
    Given the title , bootstrap a new content file as a tex file naming it correctly and
    filling in any boilerplate content required.

    :param title: the title of the content file
    :return:
    """
    underscored_title = title.replace(" ", "_")
    bootstrap_file = constants.STRUCTURE_BOOTSTRAP_DIR + type + ".tex"
    new_file = underscored_title + ".tex"
    copyfile(bootstrap_file, new_file)
    subprocess.run(
        ["sed", "-i", f"s/Title/{title}/g", new_file],
    )
    subprocess.run(
        ["sed", "-i", f"s/label/{underscored_title}/g", new_file],
    )
    print(f"successfully bootstrapped {new_file}")


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


def get_dir(base_directory: str, directory_name: str) -> str:
    """
    Uses fzf to get a directory from the given directiory
    :return: the name of the file
    """
    find_result = subprocess.run(
        [
            "find",
            base_directory,
            "-name",
            directory_name,
            "-type",
            "d",
            "-not",
            "-path",
            f"{base_directory}build/*",
        ],
        check=True,
        capture_output=True,
    )
    dir_name = (
        subprocess.run(
            ["fzf"],
            stdout=subprocess.PIPE,
            input=find_result.stdout,
        )
        .stdout.decode("utf-8")
        .strip()
    )
    return dir_name


def clean_files():
    """
    Remove excess files that are created by latex compilation
    :return:
    """
    print("Cleaning Files")
    subprocess.run(
        ["latexmk", "-c"],
    )

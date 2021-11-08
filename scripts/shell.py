"""
This file contains tools that allow us to interact with shell programs
"""

from shutil import copyfile
import constants
import subprocess


def create_new_content_file(
    title: str, type: str, target_dir: str, dry_run: bool
) -> str:
    """
    Given the title , bootstrap a new content file as a tex file naming it correctly and
    filling in any boilerplate content required.

    Type is the short form i.e. one of d t l p c

    :param title: the title of the content file
    :return: the new file's name
    """
    full_type = constants.TYPE_TO_FULL_TYPE[type]
    type_dir = constants.TYPE_TO_DIRECTORY[type] + "/"
    potholecase_title = title.replace(" ", "_").lower()
    bootstrap_file = constants.STRUCTURE_BOOTSTRAP_DIR + type_dir + full_type + ".tex"
    new_file_name = target_dir + "/" + potholecase_title + ".tex"
    if not dry_run:
        copyfile(bootstrap_file, new_file_name)
        subprocess.run(
            ["sed", "-i", f"s/Title/{title}/g", new_file_name],
        )
        subprocess.run(
            ["sed", "-i", f"s/label/{potholecase_title}/g", new_file_name],
        )
    return new_file_name


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


def get_dir(directory_name: str = "") -> str:
    """
    Uses fzf to get a directory from the given directiory
    :return: the name of the file
    """
    if directory_name != "":
        find_name_arguments = ["-name", directory_name]
    else:
        find_name_arguments = []
    find_result = subprocess.run(
        [
            "find",
            constants.ROOT_DIR,
            *find_name_arguments,
            "-type",
            "d",
            "-not",
            "-path",
            f"{constants.ROOT_DIR}build/*",
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


def get_file(directory_name: str = "", extension: str = "") -> str:
    """
    Uses fzf to get a directory from the given directiory
    :return: the name of the file
    """
    if directory_name != "" or extension != "":
        find_name_arguments = [
            "-name",
            (directory_name + "/" if directory_name else "")
            + (f"*.{extension}" if extension else ""),
        ]
    else:  # they are both empty
        find_name_arguments = []

    find_result = subprocess.run(
        [
            "find",
            constants.ROOT_DIR,
            *find_name_arguments,
            "-not",
            "-path",
            f"{constants.ROOT_DIR}build/*",
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

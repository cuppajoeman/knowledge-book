import argparse, sys


def setup_creator_parser():
    """
    Setup and return a parser for the program which creates new content files
    :return: An argument parser object
    """
    parser = argparse.ArgumentParser(
        description="Script which bootstraps new latex content files"
    )

    parser.add_argument(
        "type",
        choices=["d", "t", "l", "p", "c", "e"],
        help="the type of content you want to create, can be  a definition, theorem, lemma, proposition or corollary",
    )

    parser.add_argument(
        "title",
        type=str,
        help="the title of the content file",
    )

    parser.add_argument(
        "-n", "--neovim", help="opens the created file with neovim", action="store_true"
    )

    parser.add_argument(
        "-d",
        "--dry-run",
        help="Does everything except for actually creating the files",
        action="store_true",
    )

    parser.add_argument(
        "-c",
        "--copy",
        help="copies the created filename to the clipboard (starting from the root of the project) ",
        action="store_true",
    )

    parser.add_argument(
        "-f",
        "--fast",
        help="uses the flags -c and -n so that operations may be done quickly",
        action="store_true",
    )

    return parser


def setup_finder_parser():
    """
    Setup and return a parser for the program which creates new content files
    :return: An argument parser object
    """
    parser = argparse.ArgumentParser(
        description="Script which helps locate existing content files"
    )

    # parser.add_argument(
    #     "type",
    #     nargs="?",
    #     choices=["d", "t", "l", "p", "c"],
    #     default="",
    #     help="The type of content you want to find can be a definition, theorem, lemma, proposition or corollary",
    # )

    # parser.add_argument(
    #     "-s",
    #     "--structure-known",
    #     action="store_true",
    #     help="Allows the user to choose which structure the file is in to reduce the search results",
    # )

    parser.add_argument(
        "-n", "--neovim", help="opens the located file with neovim", action="store_true"
    )

    parser.add_argument(
        "-c",
        "--copy",
        help="copies the located filename to the clipboard (starting from the root of the project) ",
        action="store_true",
    )

    return parser


def get_args(constructed_parser):
    """
    Sets up a parser and returns the arguments, if there are no command line arguments then return the usage
    :return:
    """
    parser = constructed_parser()

    # if len(sys.argv) < 2:
    #     parser.print_usage()
    #     sys.exit(1)

    return parser.parse_args()

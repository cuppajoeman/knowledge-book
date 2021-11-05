import argparse, sys


def setup_parser():
    """
    Setup and return a parser for this program
    :return: An argument parser object
    """
    parser = argparse.ArgumentParser(
        description="Script which bootstraps new latex content files"
    )

    parser.add_argument(
        "-t",
        "--type",
        choices=["d", "t", "l", "p", "c"],
        help="the type of content you want to create, can be  a definition, theorem, lemma, proposition or corollary",
    )

    parser.add_argument(
        "title",
        type=str,
        help="the title of the content file",
    )

    parser.add_argument(
        "-n", help="opens the created file with neovim", action="store_true"
    )

    return parser


def get_args():
    """
    Sets up a parser and returns the arguments, if there are no command line arguments then return the usage
    :return:
    """
    parser = setup_parser()

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    return parser.parse_args()

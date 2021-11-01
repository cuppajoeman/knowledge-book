import argparse, sys


def setup_parser():
    """
    Setup and return a parser for this program
    :return: An argument parser object
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--create-vertex",
        help="create a vertex in the knowledge graph",
        action="store_true",
    )

    # some of these need to be mutually exclusive

    parser.add_argument(
        "-f",
        "--new-definition",
        metavar="title",
        help="create and a new LaTeX definition with the given title",
        type=str,
    )

    parser.add_argument(
        "-d",
        "--new-deduction",
        metavar="title",
        help="create and a new LaTeX deduction with the given title",
        type=str,
    )

    parser.add_argument(
        "-s",
        "--display",
        help="display information about the knowledge graph",
        action="store_true",
    )

    parser.add_argument(
        "-u",
        "--upload-files",
        help="cleans up files and pushes them to github",
        action="store_true",
    )

    parser.add_argument(
        "-c",
        "--clean-files",
        help="clean excess files produced by latex compliation",
        action="store_true",
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

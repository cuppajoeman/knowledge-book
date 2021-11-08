import arguments
import shell
import subprocess

if __name__ == "__main__":
    args = arguments.get_args(arguments.setup_finder_parser)

    file_name = shell.get_file("", "tex")
    subprocess.call(["cat", file_name])

    responce = input("Confirm deletion?  [yn]: ")
    if responce == "y":
        shell.remove_file(file_name)

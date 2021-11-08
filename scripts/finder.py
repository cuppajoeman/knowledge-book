import arguments
import constants
import shell
import subprocess
import pyperclip

if __name__ == "__main__":
    args = arguments.get_args(arguments.setup_finder_parser)

    file_name = shell.get_file("", "tex")

    if args.copy:
        modified_file_name = file_name.replace(constants.ROOT_DIR, "")
        # modified_file_name = modified_file_name.replace(".tex", "")
        # tex_input_file_name = f"\input{{{modified_file_name}}}"
        pyperclip.copy(modified_file_name)

    if args.neovim:
        subprocess.call(["nvim", file_name])

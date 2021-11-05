import arguments
import constants
import shell
import subprocess
import pyperclip

if __name__ == "__main__":
    args = arguments.get_args()
    target_dir = shell.get_dir(
        constants.ROOT_DIR, constants.TYPE_TO_DIRECTORY[args.type]
    )
    new_file_name = shell.create_new_content_file(
        args.title, args.type, target_dir, args.dry_run
    )

    if args.neovim:
        subprocess.call(["nvim", new_file_name])

    if args.copy:
        modified_file_name = new_file_name.replace(constants.ROOT_DIR, "")
        modified_file_name = modified_file_name.replace(".tex", "")
        tex_input_file_name = f"\input{{{modified_file_name}}}"
        pyperclip.copy(tex_input_file_name)

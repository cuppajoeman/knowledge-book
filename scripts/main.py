import arguments
import constants
import shell
import subprocess

if __name__ == "__main__":
    args = arguments.get_args()
    target_dir = shell.get_dir(
        constants.ROOT_DIR, constants.TYPE_TO_DIRECTORY[args.type]
    )
    new_file_name = shell.create_new_content_file(args.title, args.type, target_dir)
    print(f"successfully bootstrapped {new_file_name}")
    if args.n:
        subprocess.call(["nvim", new_file_name])

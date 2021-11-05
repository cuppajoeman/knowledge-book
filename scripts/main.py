import arguments
import constants
import shell

if __name__ == "__main__":
    args = arguments.get_args()
    target_dir = shell.get_dir(
        constants.ROOT_DIR, constants.TYPE_TO_DIRECTORY[args.type]
    )

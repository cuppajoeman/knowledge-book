import os

current_file_path = os.path.realpath(__file__)
scripts_dir = os.path.split(current_file_path)[0]
ROOT_DIR = os.path.split(scripts_dir)[0] + "/"

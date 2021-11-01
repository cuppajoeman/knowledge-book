import os

current_file_path = os.path.realpath(__file__)
scripts_dir = os.path.split(current_file_path)[0]
root_dir = os.path.split(scripts_dir)[0]
print(root_dir)

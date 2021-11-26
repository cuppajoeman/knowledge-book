import os

current_file_path = os.path.realpath(__file__)
scripts_dir = os.path.split(current_file_path)[0]
ROOT_DIR = os.path.split(scripts_dir)[0] + "/"
STRUCTURE_BOOTSTRAP_DIR = ROOT_DIR + "structure/"

TYPE_TO_FULL_TYPE = {
    "d": "definition",
    "t": "theorem",
    "l": "lemma",
    "p": "proposition",
    "c": "corollary",
    "e": "example",
}

TYPE_TO_DIRECTORY = {
    "d": "definitions",
    "t": "theorems",
    "l": "lemmas",
    "p": "propositions",
    "c": "corollaries",
    "e": "examples",
}

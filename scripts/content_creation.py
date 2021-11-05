from shutil import copyfile
import constants
import subprocess

def create_new_content_file(title: str, target_dir: str):
    """
    Given the title , bootstrap a new content file as a tex file naming it correctly and
    filling in any boilerplate content required.

    :param title: the title of the content file
    :return:
    """
    underscored_title = title.replace(" ", "_")
    bootstrap_file = constants.ROOT_DIR + "defn.tex"
    new_file = underscored_title + ".tex"
    copyfile(bootstrap_file, new_file)
    subprocess.run(
        ["sed", "-i", f"s/TITLE/{title}/g", new_file],
    )
    print(f"successfully bootstrapped {new_file}")

def create_new_latex_definition(definition_title: str):
    """
    Given the title of a definition, bootstrap a new definition file as a tex file naming it correctly and
    filling in any boilerplate content required.
    :param definition_title: the title of the definition
    :return:
    """
    underscored_definition_title = definition_title.replace(" ", "_")
    definition_bootstrap_file = constants.ROOT_DIR + "defn.tex"
    new_definition_file = underscored_definition_title + ".tex"
    copyfile(definition_bootstrap_file, new_definition_file)
    subprocess.run(
        ["sed", "-i", f"s/TITLE/{definition_title}/g", new_definition_file],
    )
    print(f"successfully bootstrapped {new_definition_file}")


def create_new_latex_deduction(deduction_title: str):
    """
    Given the title of a deduction, bootstrap a new deduction file as a tex file naming it correctly and
    filling in any boilerplate content required.
    :param deduction_title: the title of the deduction
    :return:
    """
    underscored_deduction_title = deduction_title.replace(" ", "_")
    deduction_bootstrap_file = constants.ROOT_DIR + "deduction.tex"
    new_deduction_file = underscored_deduction_title + ".tex"
    copyfile(deduction_bootstrap_file, new_deduction_file)
    subprocess.run(
        ["sed", "-i", f"s/TITLE/{deduction_title}/g", new_deduction_file],
    )
    print(f"successfully bootstrapped {new_deduction_file}")

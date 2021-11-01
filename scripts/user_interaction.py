"""
This module operates with I/O on users to create vertices in the knowledge graph
"""
import os
import subprocess
from dataclasses import dataclass
import shell

from typing import Tuple, List, Callable, Dict

from kg_base import graph_representation
from kg_base import constants


@dataclass
class EdgeConstructionInfo:
    """Enough information to allow a user to create edges
    from the current vertex to another vertex

    ready_message: a message which prepares the user for the current step
    exit_message: a message which let's the user know what is coming next
    directory: where fzf will search for vertex files
    column_name: the name of the column that this edge will be stored in inside the current vertex
    link_many: whether or not the current vertex can have many outgoing edges into the target table
    """

    ready_message: str
    directory: str
    column_name: str
    link_many: bool


def prompt_until_valid(
    message: str,
    verification_function: Callable[[str], bool],
    invalid_message_response="invalid response, please try again.",
) -> str:
    """
    Prompt the user with a certain message until they give a valid response, and return it

    :param message: the message that the user is prompted with
    :param verficiation_function: a function which returns true when the input is valid
    :return:
    """
    response = input(message)
    while not verification_function(response):
        print(invalid_message_response)
        response = input(message)

    return response


def prompt_y_n(message: str):
    """
    prompt the user with a message where until the respond with y or n

    additionally if they press enter it will be considered as a y

    :param message: the message to prompt the user with
    :return: the value y, n or the empty string
    """

    def answer_is_y_n(response):
        return response in ["y", "n", ""]

    return prompt_until_valid(message, answer_is_y_n)


def prompt_user_verifies(message: str):
    """
    prompt the user with a message then verify if they made the correct choice
    if they think the message is not valid, continue asking until it is

    :param message: the message to prompt the user with
    :return:
    """

    def answer_is_y(response):
        response = prompt_y_n(f"are you happy with {response}? (y/n): ")
        return response in ["y", ""]

    response = prompt_until_valid(message, answer_is_y, "Ok, try again!")

    return response


def prompt_user_for_files(intro_message: str, repetition_message: str) -> List[str]:
    """
    prompts the user for files until they quit out
    :return: the file names the user has chosen
    """
    response = prompt_y_n(intro_message)

    if response == "n":
        exit()

    file_names = []

    adding = True
    while adding:
        file_name = shell.get_file(constants.ROOT_DIR)
        file_names.append(file_name)
        response = prompt_y_n(repetition_message)
        if response == "n":
            adding = False

    return file_names


def prompt_user_for_content_files() -> Tuple[str, List[str]]:
    """
    prompts the user for a primary content file and then any secondary content files,

    a primary content file is the one which will be linked to in the vertex which is being created

    a secondary content file is any file which is related to the primary content file but will not be
    stored in the vertex which is being created.

    For example, a pdf file may have an accompanying latex file which generates it, the pdf file would
    be the primary content file, the tex file would be the secondary.
    :return: the primary content file and the list of secondary content files as a list
    """

    file_names = prompt_user_for_files(
        "Are you ready to select the primary content file? (y/n): ",
        "choose secondary content file? (y/n): ",
    )

    first_iteration = True
    primary_content_file = ""
    secondary_content_files = []

    for file_name in file_names:
        if first_iteration:
            primary_content_file = file_name
        else:
            secondary_content_files.append(file_name)

        if first_iteration:
            first_iteration = False

    return primary_content_file, secondary_content_files


def prompt_user_for_edges() -> List[Tuple[str, str]]:
    """
    prompt the user to find edges, and return a list of edges in the format specified by kg_base

    :return: a list of edges
    """

    edge_construction_data = [
        EdgeConstructionInfo(
            "are you prepared to choose the type ? (y/n): ",
            constants.ROOT_DIR + "kgbase_data/Type",
            constants.KnowledgeColumnName.TYPE.value,  # TODO remove this hardcode
            link_many=False,
        ),
        EdgeConstructionInfo(
            "are you prepared to choose the knowledge used? (y/n): ",
            constants.ROOT_DIR + "kgbase_data/Knowledge",
            constants.KnowledgeColumnName.KNOWLEDGE_USED.value,  # TODO remove this hardcode
            link_many=True,
        ),
        EdgeConstructionInfo(
            "are you prepared to choose parents? (y/n): ",
            constants.ROOT_DIR + "kgbase_data/Structure",
            constants.KnowledgeColumnName.PARENT.value,  # TODO remove this hardcode also change to pluaral
            link_many=True,
        ),
        EdgeConstructionInfo(
            "are you prepared to choose the status ? (y/n): ",
            constants.ROOT_DIR + "kgbase_data/Status",
            constants.KnowledgeColumnName.STATUS.value,  # TODO remove this hardcode
            link_many=False,
        ),
    ]

    edges = []
    for edge_construction_info in edge_construction_data:
        response = prompt_y_n(edge_construction_info.ready_message)

        adding = True

        if response == "n":
            adding = False

        while adding:
            file_name = shell.get_file(edge_construction_info.directory)

            if file_name not in ["", "."]:
                with open(file_name) as f:
                    lines = f.readlines()

                vertex_id = lines[0]

                # edges.append((edge_construction_info.column_id, vertex_id)) TODO this creates invalid edges in graph
                edges.append((edge_construction_info.column_name, vertex_id))

                if edge_construction_info.link_many:
                    response = prompt_y_n("continue choosing? (y/n): ")

                if response == "n" or not edge_construction_info.link_many:
                    adding = False
            else:
                print("You quit out from fzf, we'll move on to the next step")
                adding = False

    return edges


def prompt_user_for_values(primary_content_file_name: str) -> Dict[str, str]:
    """
    prompt the user for values and return a dictionary mapping column name to the value they gave

    The function takes in the primary content file name as it will be used as an option to auto
    set the title of it.

    :return: A list of values which represent properties of a vertex which aren't other vertices (literal values)
    """

    # TODO use column_id_to_display_name(table) here
    table_to_column_id_to_display_name = (
        graph_representation.create_table_to_column_id_to_display_name()
    )

    knowledge_column_id_to_display_name = table_to_column_id_to_display_name[
        constants.TableName.KNOWLEDGE.value
    ]

    # Using assumption that the column names are unique
    knowledge_display_name_to_column_id = {
        v: k for k, v in knowledge_column_id_to_display_name.items()
    }

    base_file_name, extension = constants.os.path.splitext(
        os.path.basename(primary_content_file_name)
    )

    base_file_name_spaces = base_file_name.replace("_", " ")

    if prompt_y_n(f"Are you ok with {base_file_name_spaces} as the title?: ") in [
        "y",
        "",
    ]:
        title = base_file_name_spaces
    else:
        title = prompt_user_verifies(f"{constants.KnowledgeColumnName.TITLE.value}: ")

    formatted = prompt_user_verifies(
        f"{constants.KnowledgeColumnName.FORMATTED.value} (T/F): "
    )

    while formatted not in ["T", "F", ""]:
        print("Your response is invalid, please try again")
        formatted = prompt_user_verifies(
            f"{constants.KnowledgeColumnName.FORMATTED.value} (T/F): "
        )

    formatted = formatted == "T"

    values = {
        knowledge_display_name_to_column_id[
            constants.KnowledgeColumnName.TITLE.value
        ]: title,
        knowledge_display_name_to_column_id[
            constants.KnowledgeColumnName.FORMATTED.value
        ]: formatted,
    }

    return values

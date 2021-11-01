"""
This module has everything to do with how we represent a graph from kg_base on our computer
"""
import os
from pathlib import Path
from typing import Dict

from . import constants
from . import login

q = login.create_query_object_and_login()


"""
Assumptions:
- Each of your tables has a unique name
    - this is requried because of the mapping table_to_column_id_to_display_name which uses 
    the name of the table as keys, therefore they must be unique
"""


def create_column_name_to_is_link(table):
    """
    Given a table in the form specified by kg_base, this function returns a dictionary mapping
     the name of a column to whether or not it is a link.

    To be a link means that it points somewhere else for it's data, and it's not stored directly in it.
    :return:
    """

    column_name_to_is_link = {}
    for column in table["columns"]:
        column_name = column["displayName"]
        is_link = "link" in column["dataType"]
        column_name_to_is_link[column_name] = is_link

    return column_name_to_is_link


def create_table_name_to_id(knowledge_graph_schema) -> Dict[str, str]:
    """
    Precondition: Each of your tables have a unique name on kg_base

    :param knowledge_graph_schema:
    :return: a dictionary mapping a table's name to it's id
    """
    table_name_to_id = {}
    knowledge_graph_tables_no_vertices = knowledge_graph_schema["tables"]
    for table in knowledge_graph_tables_no_vertices:
        table_name = table["displayName"]
        table_id = table["tableId"]
        table_name_to_id[table_name] = table_id

    return table_name_to_id


def create_column_id_to_display_name(table) -> Dict[str, str]:
    """
    Given a table, generate a dictionary which maps a columns id to it's display name
    :param table:
    :return:
    """
    column_id_to_display_name = {}
    for column in table["columns"]:
        column_id = column["columnId"]
        column_name = column["displayName"]
        column_id_to_display_name[column_id] = column_name

    return column_id_to_display_name


def create_table_to_column_id_to_display_name() -> Dict[str, Dict[str, str]]:
    """
    Creates a dictionary mapping a table name to a dictionary mapping column id's to their
    display name

    :param knowledge_graph_schema:
    :return:
    """

    table_to_column_id_to_display_name = {}

    knowledge_graph_tables_no_vertices = constants.KNOWLEDGE_GRAPH_SCHEMA["tables"]
    for table in knowledge_graph_tables_no_vertices:
        table_name = table["displayName"]
        table_to_column_id_to_display_name[
            table_name
        ] = create_column_id_to_display_name(table)

    return table_to_column_id_to_display_name


def create_table_name_to_table() -> Dict[str, str]:
    """
    Creates a mapping of table name to table, the table format is specified by kg_base

    :param knowledge_graph_schema:
    :return:
    """
    table_name_to_table = {}

    knowledge_graph_tables_no_vertices = constants.KNOWLEDGE_GRAPH_SCHEMA["tables"]

    for table in knowledge_graph_tables_no_vertices:
        table_name = table["displayName"]
        table_name_to_table[table_name] = table

    return table_name_to_table


def create_vertex_files(knowledge_graph_id: str, knowledge_graph_schema):
    """
    Generates vertex files inside the kg_base data directory, these are used when prompting the user

    :param knowledge_graph_id: the id of the current knowledge graph
    :param knowledge_graph_schema: the schema of the current knowledge graph
    :return:
    """
    # Each table only contains columns, not the actual vertices/rows
    knowledge_graph_tables_no_vertices = knowledge_graph_schema["tables"]

    for table in knowledge_graph_tables_no_vertices:
        table_name = table["displayName"]
        table_id = table["tableId"]

        data_dir = constants.ROOT_DIR + f"kgbase_data/{table_name}"
        Path(data_dir).mkdir(parents=True, exist_ok=True)

        column_id_to_display_name = {}
        for column in table["columns"]:
            column_id = column["columnId"]
            column_name = column["displayName"]
            column_id_to_display_name[column_id] = column_name

        # Using a huge number to make sure I get all vertices
        table_graph = q.get_graph(knowledge_graph_id, table_id, limit=999999999)

        table_vertices = table_graph["vertices"]

        # pprint.pprint(table_vertices)

        # This dictionary defines which attribute of a vertex in a table we will use to put in the filename
        table_name_to_title_column = {
            "Knowledge": "Title",
            "Structure": "Title",
            "Type": "Type",
            "Status": "Status",
        }

        for vertex in table_vertices:
            vertex_id = vertex["id"]
            for key_value in vertex["values"]:
                column_id = key_value["key"]
                value = key_value["value"]
                # this will only be true exactly once.
                if (
                    column_id_to_display_name[column_id]
                    == table_name_to_title_column[table_name]
                ):
                    vertex_title = value

            file_name = f"{vertex_title} | {vertex_id}"  # I only put the id in the name for a unique file name.
            file_path = f"{data_dir}/{file_name}"
            file = open(file_path, "w")
            file.write(vertex_id)


def create_table_id_to_vertices() -> Dict[str, Dict]:
    """

    Generate a nested dictionary which maps a table's id to a dictionary which maps
    a vertices id to the vertex itself

    :return:
    """
    pass


def rename_file_to_include_id(file_name: str, vertex_id_suffix: str) -> str:
    """
    Rename the given file to include a vertex id as part of it's name

    :param file_name: the file to be renamed
    :param vertex_id_suffix: the id that will be added
    :return: the name of the new file
    """
    base_file_name, extension = os.path.splitext(file_name)
    vertex_id_file_name = base_file_name + vertex_id_suffix + extension
    os.rename(file_name, vertex_id_file_name)
    return vertex_id_file_name

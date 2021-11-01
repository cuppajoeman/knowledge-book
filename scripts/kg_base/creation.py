import constants
import graph_representation
from typing import Dict, List, Tuple


def create_knowledge_vertex(
    values: Dict[str, str], edges: List[Tuple[str, str]], query_object
) -> str:
    """
    create a vertex in the knowledge table and return the id of the new vertex
    :return: None
    """
    table_name_to_id = graph_representation.create_table_name_to_id(
        constants.KNOWLEDGE_GRAPH_SCHEMA
    )
    knowledge_table_id = table_name_to_id[constants.TableName.KNOWLEDGE.value]
    return create_vertex(values, edges, knowledge_table_id, query_object)


def create_vertex(
    values: Dict[str, str], edges: List[Tuple[str, str]], table_id: str, query_object
) -> str:
    """
    Given values and edges create a vertex/row in the table with the given id with this data and return the
    id of the new vertex

    :param values:  Dictionary of key value pairs associating a column id to value
    :param edges: A list of tuples with key equal to the column name and value equal to the vertex id the edge
    will be created with
    :param table_id: The id of the table that this vertex should be added to
    :param query_object: An instance of kg_base.Query
    :return:
    """

    vertex_response = query_object.create_vertex(
        constants.KNOWLEDGE_GRAPH_ID,
        table_id,
        values,
        edges,
    )

    vertex = vertex_response["vertex"]

    # A vertex id starts with 'row-' we will remove this
    vertex_id_suffix = vertex["id"][3:]

    return vertex_id_suffix

from enum import Enum
import os
from . import login

q = login.create_query_object_and_login()

KNOWLEDGE_GRAPH_NAME = "Keep Asking Why"

my_projects = q.get_user_projects()

KNOWLEDGE_GRAPH = None
for project in my_projects:
    if project["name"] == KNOWLEDGE_GRAPH_NAME:
        KNOWLEDGE_GRAPH = project

if KNOWLEDGE_GRAPH is None:
    raise Exception

KNOWLEDGE_GRAPH_ID = KNOWLEDGE_GRAPH["projectId"]
KNOWLEDGE_GRAPH_SCHEMA = q.get_schema(KNOWLEDGE_GRAPH_ID)

ROOT_DIR_PATH_PREFIX = "../"  # This path represents the root of the repository

current_file_path = os.path.realpath(__file__)
kg_base_dir = os.path.split(current_file_path)[0]
scripts_dir = os.path.split(kg_base_dir)[0]
ROOT_DIR = os.path.split(scripts_dir)[0] + "/"


class KnowledgeColumnName(Enum):
    """
    This enum stores the actual values of the names of each of the columns of the table "Knowledge"
    """

    TITLE = "Title"
    TYPE = "Type"
    CONTENT = "Content"
    STATUS = "Status"
    PARENT = "Parent"
    KNOWLEDGE_USED = "Knowledge Used"
    FORMATTED = "Formatted"


class TableName(Enum):
    """
    Stores the actual names of the tables of the current knowledge graph
    """

    KNOWLEDGE = "Knowledge"
    STRUCTURE = "Structure"
    TYPE = "Type"
    STATUS = "Status"

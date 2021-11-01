import dotenv
import os
import kgbase


def create_query_object_and_login():
    """
    Creates and returns a query object
    :return:
    """
    query = create_query_object()
    login(query)
    return query


def create_query_object():
    """
    creates and returns a query object
    :return:
    """
    return kgbase.Query()


def login(query):
    """
    Given the kg_base query object login the user defined in the dotenv file
    :param query:
    :return:
    """
    dotenv.load_dotenv()
    query.login(username=os.getenv("username"), password=os.getenv("password"))

import os, pprint, time
import subprocess

from kg_base import login, graph_representation, constants

import user_interaction
import content_creation

import arguments
import shell

args = arguments.get_args()

q = login.create_query_object_and_login()


def display_knowledge_information():
    table_name_to_table = graph_representation.create_table_name_to_table()
    knowledge_column_id_to_display_name = (
        graph_representation.create_column_id_to_display_name(
            table_name_to_table[constants.TableName.KNOWLEDGE.value]
        )
    )
    pprint.pprint(knowledge_column_id_to_display_name)


def start_vertex_creation_session():

    print(
        f"==== Welcome to the '{constants.KNOWLEDGE_GRAPH_NAME}' knowledge graph, let's add a vertex."
    )
    print(f"At any stage in the process pressing enter will be considered as a yes.")

    table_name_to_id = graph_representation.create_table_name_to_id(
        constants.KNOWLEDGE_GRAPH_SCHEMA
    )
    receiving_table_name = constants.TableName.KNOWLEDGE.value
    receiving_table_id = table_name_to_id[receiving_table_name]

    t0 = time.time()
    graph_representation.create_vertex_files(
        knowledge_graph_id=constants.KNOWLEDGE_GRAPH_ID,
        knowledge_graph_schema=constants.KNOWLEDGE_GRAPH_SCHEMA,
    )
    t1 = time.time()

    print(f"==== Created Vertex files in {t1 - t0} seconds ====")

    print("==== Creating Vertex in Graph ====")

    (
        primary_content_file_name,
        secondary_content_file_names,
    ) = user_interaction.prompt_user_for_content_files()

    if primary_content_file_name == "":
        print("You must choose a primary content file")
        exit()  # TODO just make them go again

    # Remove empty file names, these are created when the user exits from fzf without choosing.
    secondary_content_file_names = [
        file_name for file_name in secondary_content_file_names if file_name != ""
    ]

    values = user_interaction.prompt_user_for_values(primary_content_file_name)
    edges = user_interaction.prompt_user_for_edges()

    print(values, edges)

    """
    next step: 
        take a look at how I did the husk and filling, probably going to need some info that I don't have yet
        so I might need to make some global variable?
    """

    husk_vertex_response = q.create_vertex(
        # TODO remove hardcode, col-0 is Title, use reverse column_name_to_id mapping
        constants.KNOWLEDGE_GRAPH_ID,
        receiving_table_id,
        {"col-0": "Husk"},
        [],
    )

    husk_vertex = husk_vertex_response["vertex"]

    # A vertex id starts with 'row-' we will remove this
    vertex_id_suffix = husk_vertex["id"][3:]

    primary_content_file_name = graph_representation.rename_file_to_include_id(
        primary_content_file_name, vertex_id_suffix
    )

    for file_name in secondary_content_file_names:
        graph_representation.rename_file_to_include_id(file_name, vertex_id_suffix)

    content_url = (
        "https://gitlab.com/cuppajoeman/knowledge-data/-/blob/master/"
        + os.path.basename(primary_content_file_name)  # remove extra path in front
    )

    # TODO remove hardcode, col-2 is the content url
    values["col-2"] = content_url

    real_vertex_response = q.update_vertex(
        project_id=constants.KNOWLEDGE_GRAPH_ID,
        table_id=receiving_table_id,
        vertex_id=husk_vertex["id"],
        values=values,
        edges=edges,
    )

    pprint.pprint("==== Server Response ====")
    pprint.pprint(real_vertex_response)


def upload_files():
    prompt_message = "Do you want to choose files for your commit message? (y/n): "
    repeat_message = "Continue choosing? (y/n): "

    file_names = user_interaction.prompt_user_for_files(prompt_message, repeat_message)

    cleaned_file_names = []

    for file_name in file_names:
        base_file_name = os.path.basename(file_name)  # remove extra path in front
        base_file_name_no_extension = os.path.splitext(base_file_name)[0]
        cleaned_file_names.append(base_file_name_no_extension)

    subprocess.run(
        ["git", "add", "-A"],
    )
    subprocess.run(
        ["git", "commit", "-m", f"add in {', '.join(cleaned_file_names)}"],
    )
    subprocess.run(
        ["git", "push"],
    )


if args.display:
    display_knowledge_information()

if args.new_definition:
    content_creation.create_new_latex_definition(args.new_definition)

if args.new_deduction:
    content_creation.create_new_latex_deduction(args.new_deduction)

if args.clean_files:
    shell.clean_files()

if args.create_vertex:
    start_vertex_creation_session()

if args.upload_files:
    upload_files()

import argparse
import os
import re

import ollama
from ollama import Client


# Function that takes a directory and a pattern and returns a list of files with names that match the pattern
def get_file_contents(directory, pattern):
    files = [f for f in os.listdir(directory) if re.match(pattern, f)]
    file_contents_dict = {}
    for file in sorted(files):
        with open(os.path.join(directory, file), "r") as f:
            file_contents_dict[file] = f.read()

    return file_contents_dict


def create_models(
    file_contents: dict[str, str], client: ollama.Client, namespace: str, dry_run: bool
):
    # Add the file contents to the model
    for file, contents in file_contents.items():
        model_name = file.split(".modelfile")[0]

        if namespace:
            model_name = f"{namespace}/{model_name}"

        print(f"Creating model from {file} with name {model_name}")

        if dry_run:
            continue

        try:
            client.create(model_name, modelfile=contents)
        except Exception as e:
            print(f"Error creating model {model_name}: {e}")

    return


def display_model_info(file_contents: dict[str, str]):
    for file, contents in file_contents.items():
        print(file)

    return


def copy_model(
    source: str, dest: str, client: ollama.Client, namespace: str, dry_run: bool
):
    if "/" not in dest:
        print(f"Destination {dest} should include a namespace. Adding {namespace}.")
        dest = f"{namespace}/{dest}"

    print(f"Copying model {source} to {dest} and deleting {source}.")

    if dry_run:
        return

    try:
        client.copy(source, dest)
        client.delete(source)
    except Exception as e:
        print(f"Error copying model {source} to {dest}: {e}")

    return


if __name__ == "__main__":
    # Parse commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, default="../modelfiles")
    parser.add_argument("--pattern", type=str, default=".*\.modelfile")
    parser.add_argument("--host", type=str, default="http://localhost:11434")
    parser.add_argument("--namespace", type=str, default="mgmacleod")
    parser.add_argument("--source", type=str)
    parser.add_argument("--dest", type=str)
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Whether to run the script without making any changes or performing any actions.",
        default=False,
    )
    parser.add_argument(
        "--action",
        type=str,
        default="info",
        choices=["info", "create", "copy"],
    )
    args = parser.parse_args()

    # Create a client
    client = Client(args.host)

    # Perform the action
    if args.action == "create":
        # Get the file contents
        file_contents = get_file_contents(args.directory, args.pattern)
        create_models(file_contents, client, args.namespace, args.dry_run)
    elif args.action == "copy":
        copy_model(args.source, args.dest, client, args.namespace, args.dry_run)

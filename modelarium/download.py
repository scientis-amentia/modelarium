import argparse
import os

from huggingface_hub import hf_hub_download


def download_model(
    repo_id: str,
    filename: str,
    output_dir: str,
    redownload: bool = False,
    modelfile_subdir: str = "modelfiles",
):
    """
    Download a model from the huggingface hub to a specified directory. Will also create a starting Ollama modelfile in the specified modelfile_subdir.
    Args:
    - repo_id: The name of the model repository
    - filename: The name of the file to download
    - output_dir: The directory to save the model to
    - redownload: Whether to redownload the model if it already exists in the output directory (default: False)
    """

    # download the model, if it doesn't already exist
    file_exists = file_exists_in_dir(output_dir, filename)

    if not file_exists or redownload:
        print(f"Downloading {filename} from {repo_id} to {output_dir}")
        hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=output_dir,
            local_dir_use_symlinks=False,
        )
    else:
        print(f"File {filename} already exists in {output_dir}")

    # create starting modelfile and note
    modelfile_path = os.path.join(output_dir, modelfile_subdir)
    create_modelfile(filename, modelfile_path)
    create_note(repo_id, os.path.join(modelfile_path, "notes"))

    return


# Function that takes a directory and a filename as input and determines whether the file exists in the directory
def file_exists_in_dir(directory: str, filename: str) -> bool:
    return os.path.exists(os.path.join(directory, filename))


# Function that takes a gguf file and an output directory as input and creates a starting Ollama modelfile in the output directory
def create_modelfile(gguf_file: str, output_dir: str):
    model_name = gguf_file.split(".gguf")[0]
    modelfile = model_name + ".modelfile"
    modelfile_path = os.path.join(output_dir, modelfile)

    if file_exists_in_dir(output_dir, modelfile):
        print(f"Modelfile {modelfile} already exists in {output_dir}")
    else:
        print(f"Creating modelfile {modelfile} in {output_dir}")
        with open(modelfile_path, "w") as f:
            f.write(create_modelfile_template(gguf_file))

    return


# Function that takes a repo ID and an output directory as input and creates a starting markdown note in the output directory
def create_note(repo_id: str, output_dir: str):
    note = repo_id.replace("/", "_") + ".md"
    note_path = os.path.join(output_dir, note)

    if file_exists_in_dir(output_dir, note):
        print(f"Note {note} already exists in {output_dir}")
    else:
        print(f"Creating note {note} in {output_dir}")
        with open(note_path, "w") as f:
            f.write(create_note_template(repo_id))

    return


def create_modelfile_template(gguf_file: str):
    template = f"""FROM ./models/{gguf_file}
TEMPLATE \"\"\"
<your template here>
\"\"\"
SYSTEM \"\"\"
You are a helpful assistant.
\"\"\"
"""
    return template


def create_note_template(repo_id: str):
    template = f"""# Notes for {repo_id}
[{repo_id}](https://huggingface.co/{repo_id})

## Quants
<quants go here>

## Notes
<notes here>
"""
    return template


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download model from huggingface hub")
    parser.add_argument("--repo", type=str, help="Name of the model repository")
    parser.add_argument("--file", type=str, help="Name of the file to download")
    parser.add_argument(
        "--redownload",
        action="store_true",
        help="Whether to redownload the model",
        default=False,
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        help="Directory to save the model to",
        default="/archive/gguf",
    )
    parser.add_argument(
        "--modelfile_subdir",
        type=str,
        help="Directory to save a starting Ollama modelfile to",
        default="modelfiles",
    )
    args = parser.parse_args()

    repo_id = args.repo
    filename = args.file

    if repo_id is None:
        raise ValueError("repo_name is required")

    if filename is None:
        raise ValueError("file_name is required")

    download_model(
        repo_id, filename, args.output_dir, args.redownload, args.modelfile_subdir
    )

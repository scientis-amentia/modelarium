import argparse
import os

from huggingface_hub import hf_hub_download


def download_model(
    repo_id: str, filename: str, output_dir: str, redownload: bool = False
):
    file_exists = file_exists_in_dir(output_dir, filename)

    if not file_exists or (redownload and file_exists):
        print(f"Downloading {filename} from {repo_id} to {output_dir}")
        hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=output_dir,
            local_dir_use_symlinks=False,
        )
    else:
        print(f"File {filename} already exists in {output_dir}")


# Function that takes a directory and a filename as input and determines whether the file exists in the directory
def file_exists_in_dir(directory: str, filename: str) -> bool:
    return os.path.exists(os.path.join(directory, filename))


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
    args = parser.parse_args()

    repo_id = args.repo
    filename = args.file

    if repo_id is None:
        raise ValueError("repo_name is required")

    if filename is None:
        raise ValueError("file_name is required")

    download_model(repo_id, filename, args.output_dir, args.redownload)

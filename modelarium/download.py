
import argparse
from huggingface_hub import hf_hub_download



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download model from huggingface hub")
    parser.add_argument("--repo_name", type=str, help="Name of the model repository")
    parser.add_argument("--file_name", type=str, help="Name of the file to download")
    parser.add_argument("--output_dir", type=str, help="Directory to save the model to", default="/archive/gguf")
    args = parser.parse_args()

    repo_name = args.repo_name
    file_name = args.file_name

    if repo_name is None:
        raise ValueError("repo_name is required")
    
    if file_name is None:
        raise ValueError("file_name is required")
    
    hf_hub_download(repo_id=repo_name, filename=file_name, local_dir=args.output_dir, local_dir_use_symlinks=False)
    
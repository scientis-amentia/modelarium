import argparse
import os

from huggingface_hub import hf_hub_download


class Downloader:
    def __init__(
        self, repo_id: str, filename: str, output_dir: str, redownload: bool = False
    ):
        self.repo_id = repo_id
        self.filename = filename
        self.models_dir = os.path.join(output_dir, "models")
        self.modelfiles_dir = os.path.join(output_dir, "modelfiles")
        self.notes_dir = os.path.join(output_dir, "notes")
        self.redownload = redownload
        # self.modelfile_subdir = "modelfiles"

    def download_model(self):
        file_exists = self.file_exists_in_dir(self.models_dir, self.filename)

        if not file_exists or self.redownload:
            print(
                f"Downloading {self.filename} from {self.repo_id} to {self.models_dir}"
            )
            hf_hub_download(
                repo_id=self.repo_id,
                filename=self.filename,
                local_dir=self.models_dir,
                local_dir_use_symlinks=False,
            )
        else:
            print(f"File {self.filename} already exists in {self.models_dir}")

        self.create_modelfile()
        self.create_note()

    def file_exists_in_dir(self, directory: str, file: str) -> bool:
        return os.path.exists(os.path.join(directory, file))

    def create_modelfile(self):
        model_name = self.filename.split(".gguf")[0]
        modelfile = model_name + ".modelfile"
        modelfile_path = os.path.join(self.modelfiles_dir, modelfile)

        if self.file_exists_in_dir(self.modelfiles_dir, modelfile):
            print(f"Modelfile {modelfile} already exists in {modelfile_path}")
        else:
            print(f"Creating modelfile {modelfile} in {modelfile_path}")
            with open(modelfile_path, "w") as f:
                f.write(self.create_modelfile_template())

    def create_note(self):
        # notes_dir = os.path.join(self.output_dir, self.modelfile_subdir, "notes")

        note = self.repo_id.replace("/", "_") + ".md"
        note_path = os.path.join(self.notes_dir, note)

        if self.file_exists_in_dir(self.notes_dir, note):
            print(f"Note {note} already exists in {self.notes_dir}")
        else:
            print(f"Creating note {note} in {self.notes_dir}")
            with open(note_path, "w") as f:
                f.write(self.create_note_template())

    def create_modelfile_template(self) -> str:
        template = f"""FROM ../models/{self.filename}
TEMPLATE \"\"\"
<your template here>
\"\"\"
SYSTEM \"\"\"
You are a helpful assistant.
\"\"\"
"""
        return template

    def create_note_template(self) -> str:
        template = f"""# Notes for {self.repo_id}
[{self.repo_id}](https://huggingface.co/{self.repo_id})

## Quants
<quants go here>

## Notes
<notes here>
"""
        return template


### End of modelarium/downloader.py


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
        default="..",
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

    downloader = Downloader(
        repo_id=repo_id,
        filename=filename,
        output_dir=args.output_dir,
        redownload=args.redownload,
    )

    downloader.download_model()

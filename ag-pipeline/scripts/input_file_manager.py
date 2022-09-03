import os
import re
from zipfile import ZipFile


class InputFileManager():
    """
    Context manager for unzipping source files and removing the unzipped files when no longer needed.

    Attributes:
            input_zip_file: File path to the input zip file.
            input_path: Folder path to the folder containing the input zip file.
            files_to_cleanup: List of file names to remove on exit.
    """

    def __init__(self, input_zip_file: str, files_to_cleanup: list) -> None:
        """
        Initializes ImportFileManager with the location of the zip file.

        Args:
            input_zip_file: File path to the input zip file.
            files_to_cleanup: List of file names to remove on exit.
        """
        self.input_zip_file = input_zip_file
        self.input_path = re.sub(r"(.+)(?:/|\\).+", r"\1", self.input_zip_file)
        self.files_to_cleanup = files_to_cleanup

    def __enter__(self) -> None:
        """Unzips input_zip_file into input_path."""
        with ZipFile(self.input_zip_file, "r") as zip_ref:
            zip_ref.extractall(self.input_path)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Removes unzipped files."""
        [os.remove(fullpath) for fullpath in
         [os.path.join(self.input_path, file) for file in
          self.files_to_cleanup]]

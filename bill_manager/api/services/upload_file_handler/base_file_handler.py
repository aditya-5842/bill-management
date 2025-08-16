from pathlib import Path

from fastapi import UploadFile
from enum import Enum


class FileType(Enum):
    IMAGE = "image"
    DOCUMENT = "document"


class ImageFileExtensions(Enum):
    JPG = ".jpg"
    JPEG = ".jpeg"
    PNG = ".png"
    GIF = ".gif"


class DocumentFileExtensions(Enum):
    PDF = ".pdf"
    DOCX = ".docx"
    TXT = ".txt"


class BaseFileHandler:
    """
    Base class for file handlers.
    This class should be inherited by all file handler classes.
    """

    def __init__(self, file: UploadFile, save_dir: Path = Path("uploads")):
        self.file = file
        self.save_dir = save_dir
        # Ensure the save directory exists
        self._create_save_dir()

    def _create_save_dir(self) -> None:
        """
        Create the directory where the file will be saved if it does not exist.
        """
        if not self.save_dir.exists():
            self.save_dir.mkdir(parents=True, exist_ok=True)

    def save_file(self) -> Path:
        """
        Save the uploaded file to the specified directory.
        Returns the path to the saved file.
        """
        file_path = self.save_dir / self.file.filename
        with file_path.open("wb") as f:
            f.write(self.file.file.read())
        return file_path

    def delete_file(self) -> None:
        """
        Delete the file from the filesystem.
        """
        file_path: Path = self.save_dir / self.file.filename
        if file_path.exists():
            file_path.unlink()

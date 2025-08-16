from abc import ABC, abstractmethod
from typing import Any

from fastapi import UploadFile

from bill_manager.api.services.upload_file_handler import BaseFileHandler


class BaseOCR(BaseFileHandler, ABC):
    """
    Base class for OCR services.
    This class should be inherited by all OCR service implementations.
    """

    def __init__(self, file: UploadFile):
        super().__init__(file=file)

    @abstractmethod
    def _load_file(self) -> Any:
        """Preprocess the image file for OCR."""
        pass

    @abstractmethod
    def extract_text(self) -> Any:
        """Extract text from the image file."""
        pass

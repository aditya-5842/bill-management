from pathlib import Path

import pytesseract
from PIL import Image
from fastapi import UploadFile

from bill_manager.api.services.ocr.base_ocr import BaseOCR


class PytesseractOCR(BaseOCR):
    """
    Implementation of OCR using Pytesseract.
    This class inherits from BaseOCR and implements the required methods.
    """

    def __init__(self, file: UploadFile):
        super().__init__(file=file)
        self.loaded_file = self._load_file()

    def _load_file(self):
        """Load the image file for OCR processing."""
        file_path: Path = self.save_file()
        image = Image.open(file_path)
        return image

    def extract_text(self) -> str:
        """Extract text from the loaded image file using Pytesseract."""
        text = pytesseract.image_to_string(self.loaded_file)
        return text

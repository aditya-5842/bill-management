from typing import Annotated

from fastapi import UploadFile, Response
from fastapi.routing import APIRouter
from fastapi import APIRouter
from loguru import logger

from bill_manager.api.services import PytesseractOCR


router: APIRouter = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "OK"}


@router.post("/ocr")
async def create_upload_file(file: UploadFile, response: Response):
    ocr_handler = PytesseractOCR(file=file)
    try:
        text = ocr_handler.extract_text()
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "ocr_content": text,
        }
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        response.status_code = 500
        return {"error": "Failed to upload file"}
    finally:
        ocr_handler.delete_file()
        logger.info(f"File {file.filename} processed and deleted after upload.")

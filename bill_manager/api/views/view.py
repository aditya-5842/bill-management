from typing import Annotated

from fastapi import UploadFile, Response
from fastapi.routing import APIRouter
from fastapi import APIRouter
from loguru import logger

from bill_manager.api.services.upload_file_handler import BaseFileHandler


router: APIRouter = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "OK"}


@router.post("/ocr")
async def create_upload_file(file: UploadFile, response: Response):
    file_handler = BaseFileHandler(file=file)
    try:
        file_handler.save_file()
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": "File uploaded successfully",
        }
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        response.status_code = 500
        return {"error": "Failed to upload file"}
    finally:
        file_handler.delete_file()
        logger.info(f"File {file.filename} processed and deleted after upload.")

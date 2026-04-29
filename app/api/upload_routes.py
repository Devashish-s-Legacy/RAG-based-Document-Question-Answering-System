from fastapi import APIRouter, UploadFile, File
import os
from app.rag.ingest import ingest_docs

router = APIRouter()

UPLOAD_DIR = "data/documents"

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Re-ingest after upload
    ingest_docs()

    return {"message": f"{file.filename} uploaded and indexed successfully"}
from fastapi import APIRouter, File, UploadFile
from typing import Optional

router = APIRouter()
available_file_formats = ['text/plain']
file_path = '/app/static_sandbox/files'


@router.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@router.post("/upload_file/")
async def create_upload_file(file: UploadFile = File(...)):
    print(file.content_type)
    if check_file_type(file.content_type):
        contents = await file.read()
        save_file(file.filename, contents)
        return {"filename": file.filename}
    return {"status": "error", "msg": "Content type not available"}


def check_file_type(content_type):
    if content_type in available_file_formats:
        return True
    return False


def save_file(filename, data):
    with open(f'{file_path}/{filename}', 'w') as f:
        f.write(data.decode())

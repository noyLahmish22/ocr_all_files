import os
from fastapi import FastAPI, File, UploadFile, Form
from internal.functions.functions import get_text_from_files
from app.config.consts import path_dic_data
app = FastAPI()


@app.get("/isalive")
async def root():
    return {"message": "is alive"}


@app.post("/image_path")
async def create_upload_file(file: UploadFile = File(...), lang: str = Form()):
    cwd = os.getcwd()
    ex = str(file.filename).split(".")[1]
    fullpath = os.path.join(cwd + path_dic_data +"/doc." + ex)
    return get_text_from_files(fullpath, cwd, file, lang)

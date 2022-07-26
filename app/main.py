import os
from fastapi import FastAPI, File, UploadFile, Form
from app.internal.functions.functions import get_text_from_files
from app.config.consts import path_dic_data
from PIL import Image

app = FastAPI()


@app.get("/isalive")
async def root():
    return {"message": "is alive"}


@app.post("/image_path")
async def create_upload_file(file: UploadFile = File(...), language: str = Form()):
    cwd = os.getcwd()
    ex = str(file.filename).split(".")[-1:][0]
    fullpath = os.path.join(cwd + path_dic_data + "doc." + ex)
    test_flag = False
    text= get_text_from_files(fullpath, cwd, file, language, test_flag, ex)
    print(text)
    return text


@app.post('/test')
async def test_image(path: str = Form()):
    language="heb"
    print(path,language)
    file = open(path, 'rb')
    cwd = os.getcwd()
    ex = str(file.name).split(".")[-1:][0]
    test_flag = True
    fullpath = os.path.join(cwd + path_dic_data + "doc." + ex)
    img = Image.open(path)  # images are color images
    # img = img.resize((224, 224), Image.ANTIALIAS)
    img.save(fullpath)
    return get_text_from_files(fullpath, cwd, file, language, test_flag, ex)

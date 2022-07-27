tessdata_dir_config = r'--tessdata-dir "C:\Users\NOY-L\ArmyProject\pytesseract\app\tests\tessdata"'
# for docker
# tessdata_dir_config = r'--tessdata-dir "/app/app/tests/tessdata"'

options = "--psm 8 -c tessedit_char_whitelist=0123456789"

#tessarect config for images
custom_config = r'--oem 3 --psm 6'

path_dic_data = "/app/tests/data/"

poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin'
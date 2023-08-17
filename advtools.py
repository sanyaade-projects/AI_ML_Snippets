import pytesseract
from PIL import Image
from gtts import gTTS
import os

path = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path

def perform_ocr(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def text_to_speech(filename):
    language = 'en'
    myobj = gTTS(text=perform_ocr(filename), lang=language, slow=False)
    new_file = os.path.splitext(filename)[0] + '.mp3'
    myobj.save(new_file)

text_to_speech('import numpy as np.png')
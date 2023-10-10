import pyttsx3
from PIL import ImageGrab, Image

def get_screenshot_from_clipboard():
    screenshot = ImageGrab.grabclipboard()
    if screenshot and isinstance(screenshot, Image.Image):
        # Get the screenshot from the clipboard
        # Continue with OCR (text extraction) using pytesseract
        import pytesseract
        
        path = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = path

        text = pytesseract.image_to_string(screenshot)
        return text
    else:
        print("No valid image found in the clipboard.")
        return None

def talk(txt):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)     # setting up new voice rate
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    #engine.setProperty('voice', voice[1].id)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(txt)
    engine.runAndWait()

#talk(get_screenshot_from_clipboard())
txt = get_screenshot_from_clipboard()
talk(txt.replace('\n',' '))

print('Success!')
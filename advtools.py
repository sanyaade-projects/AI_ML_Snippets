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

def text_to_speech(txt,newfilename):
    language = 'en'
    myobj = gTTS(text=txt, lang=language, slow=False)
    #new_file = os.path.splitext(filename)[0] + '.mp3'
    myobj.save(newfilename+'.mp3')

#perform_ocr(filename)
#text_to_speech('import numpy as np.png')
txt='''In recent years, astronomers have been pursuing large aperture telescopes to improve detection ability. However, compared to the huge costs associated with large telescopes, small and mid-size telescopes can provide a cost effective alternative, especially considering the scientific investigations
that can be done with small and mid-size telescopes (Bailyn et al. 2007).
In China, there are more than 15 small and mid-size optical telescopes, whose apertures are
between 50 cm and 200 cm, that are located in different observatories. These telescopes, which have
different optical/mechanical systems and have been equipped with various instruments, are operated
for various scientific studies. Because the operational modes for controlling these telescopes are
different, observers have to learn different skills when using different telescopes. Troubleshooting
problems in different telescope systems is also a challenge for technical personnel. A telescope
that can be controlled in the same mode under a general framework is helpful for remote and joint
observations as well.
Currently, there are two types of general frameworks used in this field. One is the Astronomy
General Object Model (ASCOM) (Denny et al. 1998 based on Windows. The other is RTS2 (the
second version of a remote telescope system) (Kub´anek 2010; Castro-Tirado 2011) which is based
on Linux. Each framework is supported by many devices (see http://www.ascom-standards.org and
http://rts2.org). However, there are some obstacles for existing telescopes in China regarding how to
implement ASCOM or RTS2:
(1) When the observers’ attention is focused on variations of celestial objects, whether transient or
long-term, they need the observatory control software (OCS) to observe their objects of interest
1078 L. Ge et al.
flexibly at any time during normal observations. As a result, the framework has to be flexible
enough to meet the observers’ expectations. Both frameworks mentioned above are too big and
complicated to accommodate new ideas from observers when the telescope is operating.
(2) Most telescopes that currently exist were built in the last century. They do not support the standards of the above frameworks. Also, some devices that are part of one existing telescope may be
controlled in the operating system of Windows, but others may be controlled by Linux. Hence,
neither of these frameworks can cope with the entire system, because each of them only supports
part of the system.
(3) In China, most of the devices on existing telescopes, including hardware and software, are developed and upgraded by technical personnel themselves at different observatories. Therefore,
it is difficult to adopt a complete standard like ASCOM or RTS2 in these highly customized
telescopes.
The users of OCS are observers and technical personnel. To meet their expectations, it is ideal
for one to design a general framework for all existing telescopes. However, it is a huge challenge
to make the general framework operational for all telescopes, considering the numerous differences
that exist among these telescopes. As a result, we take an alternative approach by focusing on making
the framework flexible.
Due to the efforts of our engineers in recent years, all of the existing telescopes are computercontrolled, making them ‘modern’ telescopes to some extent. Hence, another principle in this framework is inheritance, which means making the best use of the original resources incorporated in the
telescopes.
The framework presented in this paper focuses more on how flexibility and inheritance are useful for different observers and various personalized telescopes. The detailed design is described in
Section 2. The applications are shown in Section 3. In the last section, we draw our conclusions.'''

text_to_speech(txt,'intro')
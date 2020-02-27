# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:23:11 2020

@author: Jérémie
"""

import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'C:\Users\Jérémie\AppData\Local\Tesseract-OCR\tesseract.exe'

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# récupération de l'image vers du texte
print(pytesseract.image_to_string(Image.open(r'C:\Users\Jérémie\Documents\GitHub\ia-fun-tp-Jeybow\Ceci_test.PNG')))
# récupération de l'image vers des informations
print(pytesseract.image_to_data(Image.open(r'C:\Users\Jérémie\Documents\GitHub\ia-fun-tp-Jeybow\Ceci_test.PNG')))
# récupération de l'image vers l'orientation
print(pytesseract.image_to_osd(Image.open(r'C:\Users\Jérémie\Documents\GitHub\ia-fun-tp-Jeybow\Ceci_test.PNG')))

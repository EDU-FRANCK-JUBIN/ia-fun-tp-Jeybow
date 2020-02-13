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

print(pytesseract.image_to_string(Image.open('/home/benoit/git/python_tutos/tesseract/image_1.png)))
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:11:40 2020

@author: Jérémie
"""

import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'C:\Users\Jérémie\AppData\Local\Tesseract-OCR\tesseract.exe'

from pdf2image import convert_from_path,  convert_from_bytes
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract  import Output


images = convert_from_path('Facture.pdf')
print  ("Nombre de pages: " + str(len(images)))
for i in range (len(images)):
    print("Page N°" + str(i+1) + "\n")
    print(pytesseract.image_to_string(images[i]))
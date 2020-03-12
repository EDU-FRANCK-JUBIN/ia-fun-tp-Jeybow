# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:32:28 2020

@author: Jérémie
"""

import pytesseract as pyt
from Librairie_TesseractAvance_2 import *

pyt.pytesseract.tesseract_cmd = r'C:\Users\Jérémie\AppData\Local\Tesseract-OCR\tesseract.exe'

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
import cv2
from matplotlib import pyplot as plt

simage = r'image_4.png'
image_original = cv2.imread(simage)
print(pytesseract.image_to_string(image_original, lang='fra'))
plt.imshow(image_original, 'gray')

retouche3 = remove_noise(image_original)
print(pytesseract.image_to_string(retouche3, lang='fra'))
plt.imshow(retouche3)

retouche4 = thresholding(grayscale(remove_noise(image_original)))
print(pytesseract.image_to_string(retouche4, lang='fra'))
plt.imshow(retouche4,'gray')
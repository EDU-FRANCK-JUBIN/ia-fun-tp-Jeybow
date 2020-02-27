# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:53:08 2020

@author: Jérémie
"""

import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'C:\Users\Jérémie\AppData\Local\Tesseract-OCR\tesseract.exe'

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
import cv2

simage = r'C:\Users\Jérémie\Documents\GitHub\ia-fun-tp-Jeybow\Ceci_test.PNG'
img = cv2.imread(simage)
d = pytesseract.image_to_data(img, output_type=Output.DICT)

NbBoites = len(d['level'])
print ("Nombre de boites: "+ str(NbBoites))
for i in range(NbBoites):
    #Récupère les coordonnées de chaque boîte
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    # Affiche un rectangle
    cv2.rectangle(img, (x,-y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows ()
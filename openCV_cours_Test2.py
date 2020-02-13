# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:33:44 2020

@author: Jérémie
"""

import cv2
import sys
from matplotlib import pyplot as plt

imagePath = r'OpenCv/image0.jpg'
dirCascadeFiles = r'OpenCv/opencv/haarcascades_cuda/'


cascadefile = dirCascadeFiles + "haarcascade_frontalface_alt.xml"
classCascade = cv2.CascadeClassifier(cascadefile)
image = cv2.imread(imagePath)
plt.imshow(image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
faces = classCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print("il y a {0} visage(s).".format(len(faces)))

# Dessine des rectangles autour des visages trouvés
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
plt.imshow(image)

for (x, y, w, h) in faces:
    crop_img = image[y:y+h, x:x+w]
    plt.imshow(crop_img)

i=0
for (x, y, w, h) in faces:
    cv2.imwrite('fichier_resultat_' + str(i) + '.jpg', image[y:y+h, x:x+w])
    i = i+1

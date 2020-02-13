# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:51:02 2020

@author: Jérémie
"""

import cv2
import sys
from matplotlib import pyplot as plt

imagePath = r'OpenCv/image0.jpg'
dirCascadeFiles = r'../OpenCv/haarcascades_cuda/'
cascadefile = dirCascadeFiles + "haarcascade_frontalface_default.xml"
classCascade = cv2.CascadeClassifier(cascadefile)
image = cv2.imread(imagePath)
plt.imshow(image)

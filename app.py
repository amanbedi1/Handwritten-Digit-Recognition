import sys 
from predict import predictDigit
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

directory = "TestImages"

#Function to read the image
def openImage(filepath):
    image=cv2.imread(filepath)
    return image

#Function to plot the image
def plot(image):
    plt.imshow(image)
    plt.show()

#Iterating over all test images and predicting them
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        image=openImage(f)
        plot(image)
        predictDigit(image)

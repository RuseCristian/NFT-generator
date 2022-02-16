from posixpath import dirname
import cv2
import numpy as np
import random
from PIL import Image


def add_transparency(image_opencv):
    '''to make a transparent background, prepare the file in advance
    such that, the pixels you want to make transparent to be 255,255,255 RGB'''
    height, width, channels = image_opencv.shape
    for i in range(0,height):
        for j in range(0,width):
            if image_opencv[i,j,0] == 255 and image_opencv[i,j,1] == 255 and  image_opencv[i,j,2] == 255:
                image_opencv[i,j,3] = 0
    return image_opencv



image = cv2.imread("C:/Users/Administrator/Desktop/laundering/randomizer/image.png",cv2.IMREAD_UNCHANGED)
image = add_transparency(image)
width,height, channel = image.shape

for i in range(0,width):
    for j in range(0,height):
        ratio = image[i,j,2]/255
        if image[i,j,2] > 0 and image[i,j,0] == 0 and image[i,j,1] == 0 and image[i,j,3] == 255:
            image[i,j,0] = (255 - random.randint(0,255)*30/100)*ratio
            image[i,j,2] = 0
            image[i,j,3] = 255

new_image = Image.fromarray(image)
new_image.save("result.png")

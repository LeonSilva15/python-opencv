import cv2
import numpy as np

# Draw Line
# https://docs.opencv.org/4.2.0/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2 line()

# We can create images using arrays:
# 0 means black, and the dimension will be set as 300x300 pixels
black_img = np.zeros((300, 300))
cv2.imshow('Black image', black_img)

# In order to give it some colors, we need to set the image on 3 channels
# As a good practice, we specify the data type (unsigned int 8 bits)
color_img = np.zeros((300,300,3),np.uint8)
# Set the color on every pixel
color_img[:] = 255,0,0
# Set the color on every pixel
color_img[:] = 255,0,0
cv2.imshow('Color image', color_img)

# Color only a part of the image
color_img = np.zeros((300,300,3),np.uint8)
# Set the color only in a box from 10y,100x to 200y,120x 
color_img[10:200, 100:120] = 255,0,0
cv2.imshow('Partially colored image', color_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
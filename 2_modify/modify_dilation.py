import cv2
import numpy as np

# Image dilation
# https://docs.opencv.org/4.2.0/d9/d61/tutorial_py_morphological_ops.html No. 2

# Read an image using cv2.imread
img = cv2.imread("../../resources/lena.png")

# The canny image is used since this is normally performed on binary images
img_edges = cv2.Canny(img, 100, 100)
cv2.imshow('Edge Detection Image', img_edges)

# We need to send a matrix to the cv2.dilate function with ones, this matrix is called kernel
# np.ones creates a matrix with only ones as values, it receives the matrix dimensions and
# the data type, wich will be set as unsigned (positive), integer of 8 bits, meaning a number
# between 1 and 255
kernel = np.ones((5, 5), np.uint8)

# cv2.dilation increases the white region in the image or size of foreground object increases
''' cv2.dilate
Parameters
    img: image
        Image from cv2.imread
    kernel: matrix
        Matrix used for to decide the nature of the operation
    iteration: integer
        How many iterations are wanted for the matrix to move around,
        which affects the thickness
'''
img_dilation = cv2.dilate(img_edges, kernel, iterations=1)
cv2.imshow('Dilation Image', img_dilation)

img_dilation = cv2.dilate(img_edges, kernel, iterations=3)
cv2.imshow('More Dilation Image', img_dilation)

cv2.waitKey(0) 
cv2.destroyAllWindows()
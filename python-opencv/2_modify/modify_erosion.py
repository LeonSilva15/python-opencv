import cv2
import numpy as np

# Erosion
# https://docs.opencv.org/4.2.0/d9/d61/tutorial_py_morphological_ops.html No. 1

# Read an image using cv2.imread
img = cv2.imread('../../resources/lena.png')

# As in cv2.dilate a matrix, called kernel, is needed 
kernel = np.ones((5, 5), np.uint8)

# The dilated image is used since this is normally performed on binary images
# and img_edges is so thin on its edges that it disappears when eroded
img_edges = cv2.Canny(img, 100, 100)

img_dilation = cv2.dilate(img_edges, kernel, iterations=2)
cv2.imshow('Dilation Image', img_dilation)

''' cv2.erode
Parameters
    img: image
        Image from cv2.imread
    kernel: matrix
        All the pixels near boundary will be discarded depending upon the size of kernel
    iteration: integer
        How many iterations are wanted for the matrix to move around,
        which affects the thickness
'''
img_erosion = cv2.erode(img_dilation, kernel, iterations=2)
cv2.imshow('Erosion Image', img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
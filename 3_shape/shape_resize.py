import cv2

# Scaling
# https://docs.opencv.org/4.2.0/da/d6e/tutorial_py_geometric_transformations.html

# Read an image using cv2.imread
img = cv2.imread('../../resources/lena.png')

# The size of the image can be specified manually, or you can specify the scaling factor
# Preferable interpolation methods are cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow)
# and cv2.INTER_LINEAR for zooming
img_scaled = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Bigger Image', img_scaled)

img_scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Smaller Image', img_scaled)

# Rezise modifing the number of pixels
img_scaled = cv2.resize(img, (1000, 500))
cv2.imshow('Modify pixels Image 1', img_scaled)

img_scaled = cv2.resize(img, (300, 1000))
cv2.imshow('Modify pixels Image 2', img_scaled)

cv2.waitKey(0)
cv2.destroyAllWindows()
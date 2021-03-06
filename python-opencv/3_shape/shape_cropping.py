import cv2

# Cropping

# Read an image using imread
img = cv2.imread('../../resources/lena.png')

# Since every image is coposed for an array of numbers describing each pixel
# we only need to ignore those pixels that we don't want to appear
# specifying the ones we want to keep
# From the original image, take from point 0y,0x (left up) to the poing 300y,300x (right down)
img_cropped = img[0:300, 0:300]

cv2.imshow('Cropped image', img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Draw Line
# https://docs.opencv.org/4.2.0/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2

# Create black backgrond 300x300 pixels with 3 layers (RGB)
img_black = np.zeros((300, 300, 3), np.uint8)

# Draw lines:
# Draw a line on img_black from 200x,20y to 20x, 200y, white color (255,255,255), thickness 2 pixels
cv2.line(img_black, (200,20), (20, 200), (255, 255, 255), 2)

# Draw a line on img_black from 0x,0y to max x, max y, blue color (255,255,255), no thickness defined
# .shape() retrieves the image dimension in a 2 spaces array
cv2.line(img_black, (0, 0), (img_black.shape[0], img_black.shape[1]), (255, 0, 0))

# Show image
cv2.imshow('Base image', img_black)

cv2.waitKey(0)
cv2.destroyAllWindows()
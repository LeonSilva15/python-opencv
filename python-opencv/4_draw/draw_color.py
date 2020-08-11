import cv2
import numpy as np

# Draw Line
# https://docs.opencv.org/4.2.0/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2 line()

# We can create images using arrays:
# 0 means black, and the dimension will be set as 300x300 pixels
black_img = np.zeros((300, 300))
cv2.imshow('Black image', black_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Draw Shapes
# https://docs.opencv.org/4.2.0/d6/d6e/group__imgproc__draw.html

# Create black backgrond 300x300 pixels with 3 layers (RGB)
img_black = np.zeros((300, 300, 3), np.uint8)

# Draw rectangle:
# image, starting point, ending point, color, thickness (optional), lineType (optional), shift (optional)
cv2.rectangle(img_black, (20,30), (250, 150), (0, 0, 255), cv2.FILLED)

# Draw circle:
# image, center, radius, color, thickness (optional), lineType (optional), shift (optional)
cv2.circle(img_black, (120,130), 50, (255, 255, 0), 5)

# Show image
cv2.imshow('Base image', img_black)

cv2.waitKey(0)
cv2.destroyAllWindows()
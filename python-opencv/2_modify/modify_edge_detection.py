import cv2

# Canny Edge Detection
# https://docs.opencv.org/4.2.0/da/d22/tutorial_py_canny.html

# Read an image using cv2.imread
img = cv2.imread("../../resources/lena.png")

# Canny is a multi-stage algorithm that goes through  the next stages:
# 1. Noise Reductiona using a 5x5 Gaussian filter
# 2. Finding Intensity Gradient of the Image
# 3. Non-maximum Suppression
# 4. Hysteresis Thresholding
img_edges = cv2.Canny(img, 100, 100)
cv2.imshow('Edge Detection Image', img_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
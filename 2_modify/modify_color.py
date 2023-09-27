import cv2

# Color convertions:
# https://docs.opencv.org/4.2.0/de/d25/imgproc_color_conversions.html

# Read an image using cv2.imread
img = cv2.imread("../../resources/lena.png")

# cv2.cvtColor() method converts an image from one color space to another
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", img_gray)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", img_hsv)

img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cv2.imshow("HLS Image", img_hls)

cv2.waitKey(0) 
cv2.destroyAllWindows()
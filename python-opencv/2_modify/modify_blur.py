import cv2

# Image blurring:
# https://docs.opencv.org/4.2.0/d4/d13/tutorial_py_filtering.html

# Read an image using cv2.imread
img = cv2.imread("../../resources/lena.png")

# cv2.blur() method blurs an image using the normalized box filter
img_blur = cv2.blur(img, (7,7))
cv2.imshow("Blurred Image", img_blur)

# Gaussian Blurring
# cv2.GaussianBlur() method blurs an image taking a weighted average around the pixel
img_gaussian_blur = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Gaussian Blurred Image", img_gaussian_blur)

# Median blurring
# cv2.medianBlur() method blurs an image taking the median of all the pixels under the
# kernel area and the central element is replaced with this median value
img_median_blur = cv2.medianBlur(img, 5)
cv2.imshow('Median Blurred Blurring', img_median_blur)

# Bilateral blurring
# cv2.bilateralFilter() method takes a Gaussian filter in space, but one more Gaussian
# filter which is a function of pixel difference.
# It preserves the edges since pixels at edges will have large intensity variation
img_bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Bilateral Blurred Blurring', img_bilateral_blur)

cv2.waitKey(0) 
cv2.destroyAllWindows()
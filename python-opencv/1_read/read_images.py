import cv2

# Read an image using cv2.imread specifying its path
img = cv2.imread("../../resources/lena.png")

# Show that image using cv2.imshow, with a title a title, and the image
cv2.imshow("First Image", img)

# Wait for the image to be read
cv2.waitKey(0)
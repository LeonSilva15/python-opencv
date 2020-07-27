import cv2

img = cv2.imread("../../resources/lena.png")

img_edges = cv2.Canny(img, 100, 100)

cv2.imshow('Edge Detection Image', img_edges)

cv2.waitKey(0)
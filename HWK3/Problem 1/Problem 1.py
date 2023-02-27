import cv2
import numpy as np

input_image = cv2.imread("p1_image1.png")
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
rows = input_image.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows/20, param1=80, param2=20, minRadius=35, maxRadius=45)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv2.circle(input_image, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv2.circle(input_image, center, radius, (255, 0, 255), 3)

input_image = cv2.resize(input_image, (960, 540))
cv2.imshow('test', input_image)
cv2.waitKey(0)

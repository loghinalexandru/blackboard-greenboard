import cv2
import numpy as np

original = cv2.imread("test.jpg")
hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
green_mask = cv2.inRange(hsv, (36, 0, 0), (100, 255,255))
result = cv2.bitwise_and(original,original, mask=green_mask)
kernel = np.ones((3, 3), np.uint8)
result = cv2.morphologyEx(result, cv2.MORPH_ERODE, kernel)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg", gray)
result = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imwrite("result.jpg", result)
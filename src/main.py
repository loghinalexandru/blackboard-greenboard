import cv2
import numpy as np

original = cv2.imread("../misc/test_2.jpg")
hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
green_mask = cv2.inRange(hsv, (25, 52, 72), (102, 255,255))
result = cv2.bitwise_and(original,original, mask=green_mask)
result = cv2.morphologyEx(result, cv2.MORPH_DILATE, cv2.getStructuringElement(cv2.MORPH_RECT, (10,10)))
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
_, gray = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
gray = cv2.morphologyEx(gray, cv2.MORPH_ERODE, cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)))
cv2.imwrite("result.jpg", cv2.bitwise_not(gray))
import cv2
import sys
import os

def get_note(path):
    original = cv2.imread(path)
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv, (25, 52, 72), (102, 255,255))
    filtered = cv2.bitwise_and(original,original, mask=green_mask)
    filtered = cv2.morphologyEx(filtered, cv2.MORPH_DILATE, cv2.getStructuringElement(cv2.MORPH_RECT, (10,10)))
    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    gray = cv2.morphologyEx(gray, cv2.MORPH_ERODE, cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)))
    return cv2.bitwise_not(gray)

def process_image(path, _):
    buffer = get_note(path)
    cv2.imwrite(path, buffer)

if __name__ == '__main__':
    cv2.imwrite('result.jpg', get_note(sys.argv[1]))
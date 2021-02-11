import numpy as np
import cv2

pic = cv2.imread("images/bird.jpg", 0)
cols = pic.shape[0]
rows = pic.shape[1]
cv2.imshow('original', pic)
threshold_value = 150

# cv2.threshold(grayscaleimg, threshold_value, max_value, thresolding type)
(T_value, binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary_threshold)

(T_value, binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('binary_inv', binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
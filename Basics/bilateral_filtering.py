import numpy as np
import cv2

pic = cv2.imread("images/noisy.jpg")
cols = pic.shape[0]
rows = pic.shape[1]
cv2.imshow('original', pic)
dimpixel = 10
color = 100
space = 100
filtered = cv2.bilateralFilter(pic, dimpixel, color, space)
cv2.imshow('filtered', filtered)



cv2.waitKey(0)
cv2.destroyAllWindows()
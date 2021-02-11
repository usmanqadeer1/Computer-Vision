import numpy as np
import cv2

pic = cv2.imread("images/people.jpg")
cols = pic.shape[0]
rows = pic.shape[1]
cv2.imshow('original', pic)

center = (cols/2, rows/2)
angle = 90
# getRotationMatrix2D(centerm angle, scale)
T = cv2.getRotationMatrix2D(center, angle, 1)
rotated = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('anticlockwise', rotated)

T = cv2.getRotationMatrix2D(center, -90, 1)
rotated = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('clockwise', rotated)

T = cv2.getRotationMatrix2D(center, angle, 0.5)
rotated = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('scaled_havled', rotated)

T = cv2.getRotationMatrix2D(center, angle, 2)
rotated = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('scaled_doubled', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
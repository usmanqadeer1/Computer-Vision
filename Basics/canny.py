import numpy as np
import cv2

pic = cv2.imread("images/bird.jpg")
cols = pic.shape[0]
rows = pic.shape[1]
cv2.imshow('original', pic)

thresh1 = 50
thresh2 = 100

# values below thresh1 are going to be 0, and above thresh2 are to be 1
canny = cv2.Canny(pic, thresh1, thresh2)
cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
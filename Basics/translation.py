import numpy as np
import cv2

pic = cv2.imread("images/people.jpg")
cols = pic.shape[0]
rows = pic.shape[1]
cv2.imshow('original', pic)

# T = [[x],[y]]

# translation matrix moving 100 pixels right and 50 pixels down
T = np.float32([[1,0,100], [0, 1, 50]])
shifted = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('shifted_right_down', shifted)


# # translation matrix moving 100 pixels left and 50 pixels up
T = np.float32([[1,0,-100], [0, 1, -50]])
shifted = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('shifted_left_up', shifted)


# translation matrix rotating anticlockwise
T = np.float32([[0,1,0], [1, 0, 0]])
shifted = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('shifted3', shifted)


# translation matrix tilting
T = np.float32([[1,0,0], [1, 1, 0]])
shifted = cv2.warpAffine(pic, T, (cols, rows))
cv2.imshow('shifted4', shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
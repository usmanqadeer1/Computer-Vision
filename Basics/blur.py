import numpy as np
import cv2

pic = cv2.imread("images/noisy.jpg")
cols = pic.shape[0]
rows = pic.shape[1]
cv2.imshow('original', pic)


blur = cv2.blur(pic, (5,5))
cv2.imshow("simple", blur)

# gaussian blur (center pixel replaced by weighted average of neighbouring pixels)
#medianBlur(img, kernel, sigmaX, sigmaY)

blur = cv2.GaussianBlur(pic, (5,5), 0)
cv2.imshow("gaussian", blur)

#median blur (center pixel replaced by median of neighbouring pixels)
#medianBlur(img, kernel)
blur = cv2.medianBlur(pic, 5)
cv2.imshow("median3", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
print(cv2.__version__)
img = cv2.imread('images/image.png')
cv2.imshow('Original', img)

img = cv2.imread('images/image.png', 0)
cv2.imshow('gray', img)

img = cv2.imread('images/image.png', -1)
cv2.imshow('with_alpha', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
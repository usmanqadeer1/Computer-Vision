import cv2
print(cv2.__version__)
img = cv2.imread('images/image.png')
cv2.imwrite('images/image.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
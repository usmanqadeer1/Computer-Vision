import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
# adding rectangle
cv2.rectangle(pic, (0,10), (490, 150), color = (123, 200, 98), thickness = 3, shift = 0)
# adding line (img, start, end, color, thickness)
cv2.line(pic, (10, 150), (490, 10), (0, 0, 255), 4)
# adding circle(img, center, radius, color, thickness)
cv2.circle(pic, (400, 100), 30, (255, 0, 255), 4)
cv2.circle(pic, (80, 60), 30, (255, 0, 255), 4)

# adding text (img, text, font, size, color, thickness, type of line)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'openCV', (50, 250), font, 3, (200, 255, 255), 4, cv2.LINE_8)
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
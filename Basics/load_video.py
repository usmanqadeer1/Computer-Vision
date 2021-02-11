import numpy as np
import cv2

vid = cv2.VideoCapture('videos/vid1.mp4')
while vid.isOpened():
    ret, frame = vid.read()
    
    cv2.imshow('video', frame)

    #press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
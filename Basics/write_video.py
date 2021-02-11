import numpy as np
import cv2

vid = cv2.VideoCapture('videos/vid1.mp4')
fps = 30
framesize = (int(vid.get(3)),int(vid.get(4)))
print(framesize)
fourcc = cv2.VideoWriter_fourcc(*'XVID')


out = cv2.VideoWriter('videos/sample.avi', fourcc, fps, framesize)

while vid.isOpened():
    ret, frame = vid.read()   
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayscale video
    out.write(frame)
 
    cv2.imshow('video', frame)
    
    #press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
vid.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
eyes_cascade = cv2.CascadeClassifier('raw/haarcascade_eye.xml')

# pic = cv2.imread('.jpg')
scale_factor = 1.3
webcam = cv2.VideoCapture(0)
while True:
    ret, pic = webcam.read()
    eyes = eyes_cascade.detectMultiScale(pic) 
    for (x,y,w,h) in eyes:
        center = (x + w//2, y + h//2)
        cv2.ellipse(pic, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'eyes', (x,y), font, 0.5, (255,255,255), 2, cv2.LINE_AA)


    print('number of eyes detected:', len(eyes))
    cv2.imshow('eyes', pic)
    
    if cv2.waitKey(1) &0xff == ord('q'):
        break

cv2.destroyAllWindows()
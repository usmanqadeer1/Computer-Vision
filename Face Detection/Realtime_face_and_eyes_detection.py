import cv2
face_cascade = cv2.CascadeClassifier('raw/haarcascade_frontalface_default.xml')
# eyes_cascade = cv2.CascadeClassifier('raw/haarcascade_eye.xml')
eyes_cascade = cv2.CascadeClassifier('raw/haarcascade_eye_tree_eyeglasses.xml')

# pic = cv2.imread('.jpg')
scale_factor = 1.3
webcam = cv2.VideoCapture(0)
while True:
    
    ret, pic = webcam.read()
    # first detect face
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5) 
    for (x,y,w,h) in faces:
        cv2.rectangle(pic, (x, y), (x+w, y+h), (255,0,0), 2, cv2.LINE_AA)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'face', (x,y), font, 2, (255,255,255), 2, cv2.LINE_AA)
        
        faceROI = pic[y:y+h,x:x+w]
        # Now detect eyes in face
        eyes = eyes_cascade.detectMultiScale(faceROI) 
        for (x2,y2,w2,h2) in eyes:
            center = (x + x2 + w2//2, y + y2 + h2//2)
            cv2.ellipse(pic, center, (w2//2, h2//2), 0, 0, 360, (255, 0, 255), 4)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(pic, 'eyes', (x+x2,y+y2), font, 0.5, (255,255,255), 2, cv2.LINE_AA)


    # print('number of eyes detected:', len())
    cv2.imshow('eyes', pic)
    
    if cv2.waitKey(1) &0xff == ord('q'):
        break

cv2.destroyAllWindows()
import cv2
# 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier('raw/haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('raw/haarcascade_frontalcatface_extended.xml')


# pic = cv2.imread('.jpg')
scale_factor = 1.3
webcam = cv2.VideoCapture(0)
while True:
    ret, pic = webcam.read()
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5) 
    for (x,y,w,h) in faces:
        cv2.rectangle(pic, (x, y), (x+w, y+h), (255,0,0), 2, cv2.LINE_AA)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'face', (x,y), font, 2, (255,255,255), 2, cv2.LINE_AA)

    print('number of faces detected:', len(faces))
    cv2.imshow('face', pic)
    
    if cv2.waitKey(1) &0xff == ord('q'):
        break

cv2.destroyAllWindows()
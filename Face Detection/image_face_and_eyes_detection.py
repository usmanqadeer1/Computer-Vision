import cv2
face_cascade = cv2.CascadeClassifier('raw/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('raw/haarcascade_eye.xml')

# pic = cv2.imread('images/people.jpg')
# pic = cv2.imread('images/people1.jpeg')
pic = cv2.imread('images/osman.png')


scale_percent = 30
width = pic.shape[1]
height = pic.shape[0]
if width > 2000:
    width = int(width * (scale_percent / 100))
if height > 1500:
    height = int(height * scale_percent / 100)
scale_factor = 1.3
while True:
    # first detect face
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5) 
    for (x,y,w,h) in faces:
        cv2.rectangle(pic, (x, y), (x+w, y+h), (255,0,0), 2, cv2.LINE_AA)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'face', (x,y), font, 1, (255,255,255), 2, cv2.LINE_AA)
        
        faceROI = pic[y:y+h,x:x+w]
        # Now detect eyes in face
        eyes = eyes_cascade.detectMultiScale(faceROI, scale_factor, 1) 
        for (x2,y2,w2,h2) in eyes:
            center = (x + x2 + w2//2, y + y2 + h2//2)
            cv2.ellipse(pic, center, (w2//2, h2//2), 0, 0, 360, (255, 0, 255), 4)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(pic, 'eyes', (x+x2,y+y2), font, 0.5, (255,255,255), 2, cv2.LINE_AA)


    resized = cv2.resize(pic, (width, height), interpolation = cv2.INTER_AREA)
    cv2.imshow('faces', resized)
    
    if cv2.waitKey(1) &0xff == ord('q'):
        break

cv2.destroyAllWindows()
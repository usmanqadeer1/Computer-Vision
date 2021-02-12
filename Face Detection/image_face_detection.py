import cv2
# 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier('raw/haarcascade_frontalface_default.xml')

# pic = cv2.imread('images/friends.png')
pic = cv2.imread('images/people.jpg')
scale_percent = 30
width = pic.shape[1]
height = pic.shape[0]
if width > 2000:
    width = int(width * (scale_percent / 100))
if height > 1500:
    height = int(height * scale_percent / 100)
scale_factor = 1.3

while True:
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5) 
    for (x,y,w,h) in faces:
        cv2.rectangle(pic, (x, y), (x+w, y+h), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'face', (x,y), font, 0.5, (255,255,255), 2, cv2.LINE_AA)

    print('number of faces detected:', len(faces))
    resized = cv2.resize(pic, (width, height), interpolation = cv2.INTER_AREA)
    cv2.imshow('faces', resized)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
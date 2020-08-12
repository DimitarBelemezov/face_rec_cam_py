import cv2
import sys
import os

faces_temp = 0
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
i=1;
video_capture = cv2.VideoCapture(0)
path = "C:/Users/Dimitar Belemezov/Desktop/python/face_detector/faces"
while True:

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if len(faces)>0:
            if len(faces)!=faces_temp:
                cv2.imwrite(os.path.join(path, 'kang'+str(i)+'.jpg'), frame)
            faces_temp=len(faces)
        i+=1

    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

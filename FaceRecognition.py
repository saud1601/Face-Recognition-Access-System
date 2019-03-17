import cv2
import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/Desktop/trainer/trainer.yml')
cascadePath = "/home/pi/Desktop/Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
# id counter
id = 0
names = ['Rafed', 'Saud'] 
cam = cv2.VideoCapture(0)
cam.set(3, 640) #  video widht
cam.set(4, 480) #  video height
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if (confidence < 55):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
             
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(20, GPIO.OUT) 
            GPIO.output(20, 1)
            cam.release()
            cv2.destroyAllWindows()

            print("Face Recognized...Door Unlocked")
            
            time.sleep(5)
            GPIO.output(20, 0)
            print("Door Locked")
           
            sys.exit()  

            
            
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
    
    cv2.imshow('camera',img)
    
    k = cv2.waitKey(0)
    if k == 27:
        break

print("\n Exiting Program ")
cam.release()
cv2.destroyAllWindows()
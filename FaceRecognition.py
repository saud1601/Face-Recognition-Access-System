import cv2
import RPi.GPIO as GPIO
import time
import BlynkLib
import datetime
tm = datetime.datetime.now()

blynk = BlynkLib.Blynk('c2e97d056d744994b1b8073963dec4be')
while True:              
    ree = 0
    rek = 0
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
    #  min window size recognized as a face
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

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(20, GPIO.OUT) 
                GPIO.output(20, 1)
                cam.release()
                cv2.destroyAllWindows()
                blynk.notify( id + ' has opened the door at: %d' % tm.hour + ':%d' % tm.minute  )
                print("Face Recognized...Door Unlocked")                    
                time.sleep(4)
                GPIO.output(20, 0)
                print("Door Locked")
                ree = 1
                break

                                        
            else:
                id = "unknown"

                                        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            
        cv2.imshow('camera',img)
            
        if ree == 1:
            break
        k = cv2.waitKey(0) 
        if k == 27:
            rek = 1
            break
    if rek == 1: 
        break
           
           
print("\nExiting Program")
cam.release()
cv2.destroyAllWindows()

import cv2
import sys

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier('/home/pi/Desktop/Cascades/haarcascade_frontalface_default.xml')

# Enter your name here..
users = ['Rafed', 'Saud']
    
face_id = len(users)

print ('\nYour ID is :' +str(face_id))
            
print("\nInitializing face capture. Look the camera and wait ... (Press Ctrl+C to exit)")

count = 0

while(True):
    try:
        img = cam.read()
   
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit()
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("/home/pi/Desktop/FaceRecognitionAccessSystem/dataset/" + str(face_id)  + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    
    if count >= 1: 
         break

print("\nUser created...Exiting Program")
cam.release()
cv2.destroyAllWindows()

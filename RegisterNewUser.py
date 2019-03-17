import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 640) # W
cam.set(4, 480) # H
face_detector = cv2.CascadeClassifier('/home/pi/Desktop/Cascades/haarcascade_frontalface_default.xml')
face_id = input('\nEnter user id then press enter:  ')
print("\nInitializing face capture. Look the camera and wait ...")
count = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Save the captured image into the dataset folder
        cv2.imwrite("/home/pi/Desktop/FaceRecognitionAccessSystem/dataset/" + str(face_id)  + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(0)
    if k == 27:
        break
    elif count >= 1:
         break
print("\nExiting Program")
cam.release()
cv2.destroyAllWindows()
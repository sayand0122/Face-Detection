import cv2

cap=cv2.VideoCapture(0)
#The path mentioned in the next line can be changed and the file is available in the previous directory
detect = cv2.CascadeClassifier(r'C:\Users\Sayan\Downloads\FaceDetection-master\haarcascade_frontalface_default.xml')

while True:
    ret, image=cap.read();
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face=detect.detectMultiScale(image,1.3,5)
    for(x,y,w,h) in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Camera',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

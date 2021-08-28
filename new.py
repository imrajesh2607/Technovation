import cv2 
import random as ran
import time
import pyttsx3

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

car_cascade = cv2.CascadeClassifier('cars.xml')
flag = True
cnt=1
# loop 
while(flag):
    a = ran.sample(range(1,4),3)
    movement = 0
    while movement<3:
        print(f'Case {cnt}: ')
        f=f"car{a[movement]}.jpg"
        # reading image from each frame
        frame = cv2.imread(f)
        img_grayscale = cv2.imread(f"car{a[movement]}.jpg",0)
        cv2.imshow('graycsale image',img_grayscale)
        cv2.waitKey(1000)
        # gray scale conversion
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        # Detects cars of different sizes in the input image 
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)   
        count=0
        # To draw a rectangle in each cars 
        for (x,y,w,h) in cars: 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2) 
            count+=1
        # Display frames in a window  
        cv2.imshow('TRAFFIC'+str(movement), frame)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        # Printing Output
        speed = ran.randint(0,120)                # Speed of Car (Input from ELM 327)
        safe_speed = ran.randint(0,120)           # Safe speed of car (Using OpenCV by detecting number in sign board)
        print(f'Safe Speed Limit is {safe_speed}km/hr. Speed of Your car is {speed}km/hr')
        if speed>safe_speed:
            SpeakText('Safe Speed Limit is breached. Slow down your car.')
            print('Safe Speed Limit is breached. Slow down your car.')
            flag=False
        movement+=1
        cnt+=1
        cv2.destroyAllWindows()

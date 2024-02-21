import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) #Create a video capture instance, for the webcam
#Camera configuration
cap.set(cv.CAP_PROP_AUTO_WB, 0.00)
cap.set(cv.CAP_PROP_SATURATION, 3.00)
cap.set(cv.CAP_PROP_BRIGHTNESS, -1000.00)

if not cap.isOpened():
    print("Cannot open camera") #prints an error if couldnt open the camera
    exit()

while True:
    e1 = cv.getTickCount() #used for tracking performance
    ret, frame = cap.read() #Capture one frame of the webcam, its a jpg image
    
    cv.imshow('Camera View', frame) #display the image onto a window
    

    if cv.waitKey(1) == ord('q'): #press "q" to quit the program
        break
    e2 = cv.getTickCount() #used for tracking performance
    time_running = (e2 - e1) / cv.getTickFrequency()
    print(time_running)

cap.release()
cv.destroyAllWindows() #stops recording and deletes all windows

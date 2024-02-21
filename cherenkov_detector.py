import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) #Create a video capture instance, for the webcam
if not cap.isOpened():
    print("Cannot open camera") #prints an error if couldnt open the camera
    exit()

while True:
    ret, frame = cap.read() #Capture one frame of the webcam, its a jpg image
    
    cv.imshow('Camera View', frame) #display the image onto a window
    

    if cv.waitKey(1) == ord('q'): #press "q" to quit the program
        break


cap.release()
cv.destroyAllWindows() #stops recording and deletes all windows

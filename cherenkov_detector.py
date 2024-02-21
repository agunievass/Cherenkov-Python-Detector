import cv2 as cv
import numpy as np
import argparse
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cherenkov Detector')
    parser.add_argument('--cam-id', type=int, default=0, help='Camera ID')

    args = parser.parse_args()
    

    cap = cv.VideoCapture(args.cam_id) #Create a video capture instance, for the webcam
    #Camera configuration
    # cap.set(cv.CAP_PROP_AUTO_WB, 0.00)
    # cap.set(cv.CAP_PROP_SATURATION, 3.00)
    # cap.set(cv.CAP_PROP_BRIGHTNESS, -1000.00)
    # Disable auto exposure
    cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.25)
    # Set exposure time
    cap.set(cv.CAP_PROP_EXPOSURE, 0.01)
    # Set fps
    # cap.set(cv.CAP_PROP_FPS, 30)


    if not cap.isOpened():
        print("Cannot open camera") #prints an error if couldnt open the camera
        exit()

    ret, last_frame = cap.read()

    while True:
        e1 = cv.getTickCount() #used for tracking performance
        ret, frame = cap.read() #Capture one frame of the webcam, its a jpg image

        cv.imshow('Exposed Frames', last_frame) 

        # Calcular la diferencia entre el frame actual y el anterior
        diff = frame - last_frame

        # Convertir a escala de grises
        gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

        cv.imshow('Diff', gray)

        last_frame = frame.copy() * 10000 + last_frame.copy()

        key  = cv.waitKey(1)
        if key == ord('q'): #press "q" to quit the program
            break
        elif key == ord('s'): #press "q" to quit the program
            # convert to DD-MM-YYYY HH:MM:SS:MS
            current_time = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time()))
            # Save the frame
            print("Saving frame" + current_time + ".png")
            cv.imwrite('frame_' + current_time + '_.png', frame)
        e2 = cv.getTickCount() #used for tracking performance
        time_running = (e2 - e1) / cv.getTickFrequency()
        print(time_running)

    cap.release()
    cv.destroyAllWindows() #stops recording and deletes all windows

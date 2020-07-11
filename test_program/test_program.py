#!/usr/bin/python
from picamera import PiCamera
from time import sleep
import cv2 as cv
import numpy as np

def main():
    print("Welcome to MJ Raspi!")
    print("Let's create something great!")

    #camera_test()
    #test_imshow()
    test_cv2()
    #test_resize()

def camera_test():
    print("camera_test started...")
    camera = PiCamera()

    camera.start_preview()
    sleep(5)
    camera.capture("test.jpg")
    camera.stop_preview()

def test_imshow():
    print("test_imshow() started...")

    img = cv.imread("/home/pi/tine_follower/test_program/test.jpg")

    cv.imshow("Test Imshow", img)
    cv.waitKey(3000)

    cv.destroyAllWindows()

def test_cv2():
    print("test_cv2() started...")
    #initialize kernel
    kernel = np.ones((3,3), np.uint8)
    sleep(3)
    cap = cv.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if not ret:
            print("Failed to retrieve frame")
            break
        imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        imgBlur = cv.GaussianBlur(imgGray, (7,7), 0 )
        imgCanny = cv.Canny(img, 100, 100)
        #Erode Canny Image then Dilate to reduce noise
        imgEroded = cv.erode(imgCanny, kernel, iterations = 1)
        imgDilated = cv.dilate(imgEroded, kernel, iterations = 1)
        cv.imshow("Original Image", img)
        cv.imshow('Blurred Gray Image', imgBlur)
        cv.imshow("Canny Image", imgCanny)
        cv.imshow("Improved Canny Image", imgDilated)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    print("Video preview terminated")
    cap.release()
    cv.destroyAllWindows()

def test_resizing():
    print("test_resizing() started...")

if __name__ == "__main__":
    main()

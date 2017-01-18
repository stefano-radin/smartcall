'''
Created on 12 gen 2017

@author: radin
'''
import sys
import face_detect
sys.path.append("C:\\opencv\\build\\python\\2.7")
import cv2
import cv2.cv as cv

# Set resolution
cap = cv2.VideoCapture(0)
cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 800)
print("Frame resolution set to: (" + str(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)) + "; " + str(cap.get(cv.CV_CAP_PROP_FRAME_HEIGHT)) + ")")

cap.open(0)
for i in range(1,2):
    img=cap.read()
    face_detect.faceDetection(img[1])
cap.release() 

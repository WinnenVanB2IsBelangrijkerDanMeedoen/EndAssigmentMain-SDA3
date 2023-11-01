import cv2
import numpy as np
from ColorRecognition import *

def ObjectDetection(frame):
    frameinfo = frame.shape
    _ , frameWidth, _ = frameinfo

    colorList = [
        ["Yellow",  [18, 160, 0], [39, 255, 255]],
        ["Red",     [120, 100, 0], [225, 255, 255]],
        ["Green",   [43, 79, 0], [84, 255, 255]],
        ["Blue",    [100, 90, 0], [162, 255, 255]], 
    ]

    #yellow
    minHSVYellow = np.array([18, 160, 0])
    maxHSVYellow = np.array([39, 255, 255])
    #Red
    minHSVRed = np.array([0, 0, 0])
    maxHSVRed = np.array([225, 255, 255])
    #green
    minHSVGreen = np.array([43, 79, 0])
    maxHSVGreen = np.array([84, 255, 255])
    #blue
    minHSVBlue = np.array([100, 90, 0])
    maxHSVBlue = np.array([162, 255, 255])

    def MergeImage(image1, image2):
        alpha_background = image1[:,:,2] / 255.0
        alpha_foreground = image2[:,:,2] / 255.0

        for color in range(0, 3):
            image1[:,:,color] = alpha_foreground * image2[:,:,color] + \
            alpha_background * image1[:,:,color] * (1 - alpha_foreground)

        image1[:,:,2] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255
        return image1

    #detect the collors with HSV so that the light intesenty has less of an inpact on the collor value
    imageHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Red detection
    maskHSVRed = cv2.inRange(imageHSV, minHSVRed, maxHSVRed)
    resultHSVRed = cv2.bitwise_and(frame, frame, mask = maskHSVRed)
    #yellow detection
    maskHSVYellow = cv2.inRange(imageHSV, minHSVYellow, maxHSVYellow)
    resultHSVYellow = cv2.bitwise_and(frame, frame, mask = maskHSVYellow)
    #green detection
    maskHSVGreen = cv2.inRange(imageHSV, minHSVGreen, maxHSVGreen)
    resultHSVGreen = cv2.bitwise_and(frame, frame, mask = maskHSVGreen)
    #blue detection
    maskHSVBlue = cv2.inRange(imageHSV, minHSVBlue, maxHSVBlue)
    resultHSVBlue = cv2.bitwise_and(frame, frame, mask = maskHSVBlue)

    #merging images
    resultBlueGreen = MergeImage(resultHSVBlue, resultHSVGreen)
    resultBlueGreenRed = MergeImage(resultBlueGreen, resultHSVRed)
    resultBlueGreenRedYellow = MergeImage(resultBlueGreenRed, resultHSVYellow)
    
    edged = cv2.Canny(resultBlueGreenRedYellow, 30, 100) #create edges on image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilate = cv2.dilate(edged, kernel, iterations=1) # zorgt ervoor dat er verbindgen zijn tussen de randen
    contoursresult, _ = cv2.findContours(image = dilate, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    contourImage = frame.copy()
    #Calculate contour center
    borderMargin = 10
    centerObjectList=[]
    colorObjectList =[]
    for contour in contoursresult:
        area = cv2.contourArea(contour)
        if 5000 > area > 400: #5000 is max area for an object and 400 is minimal area for object 
            if len(contour) > 0:
                x, _ = contour[0][0]
                if borderMargin <= x < frameWidth - borderMargin: #removes the frame edge as an contour
                    moment = cv2.moments(contour)
                    #calculating centroid
                    if moment["m00"] != 0:
                        cX = int(moment["m10"]/moment["m00"]) #center X coordinate
                        cY = int(moment["m01"]/moment["m00"]) #center Y coordinate
                    else:
                        cX, cY = 0, 0          
                colorName = PixelHsvColor(frame, cY, cX, colorList)
            cv2.circle(contourImage, (cX, cY), 5, (0, 255, 255), -1)
            cv2.putText(contourImage, colorName, (cX -25, cY -35), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 0), 1)
            centerObjectList.append((cX,cY))
            colorObjectList.append(colorName)
            cv2.drawContours(image=contourImage, contours=[contour], contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    return centerObjectList, colorObjectList, contourImage

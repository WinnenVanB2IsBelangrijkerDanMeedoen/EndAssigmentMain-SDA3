import cv2
import numpy as np
from ColorRecognition import *

def ObjectDetection(frame):
    frameinfo = frame.shape
    _ , frameWidth, _ = frameinfo


    colorList = [
        ["Yellow",  [18, 160, 0], [39, 255, 255]],
        ["Red",     [170, 150, 0], [180, 255, 255]],
        ["Green",   [43, 79, 0], [84, 255, 255]],
        ["Blue",    [100, 90, 0], [162, 255, 255]], 
    ]

    #yellow
    minHSVYellow = np.array([18, 160, 0])
    maxHSVYellow = np.array([39, 255, 255])
    #Red
    minHSVRed = np.array([170, 150, 0])
    maxHSVRed = np.array([180, 255, 255])
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


    imageHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Red detection
    maskHSVRed = cv2.inRange(imageHSV, minHSVRed, maxHSVRed)
    resultHSVRed = cv2.bitwise_and(frame, frame, mask = maskHSVRed)
    #cv2.imshow('red', resultHSVRed)
    #yellow detection
    maskHSVYellow = cv2.inRange(imageHSV, minHSVYellow, maxHSVYellow)
    resultHSVYellow = cv2.bitwise_and(frame, frame, mask = maskHSVYellow)
    #cv2.imshow('geel', resultHSVYellow)
    #green detection
    maskHSVGreen = cv2.inRange(imageHSV, minHSVGreen, maxHSVGreen)
    resultHSVGreen = cv2.bitwise_and(frame, frame, mask = maskHSVGreen)
    #cv2.imshow('groen', resultHSVGreen)
    #blue detection
    maskHSVBlue = cv2.inRange(imageHSV, minHSVBlue, maxHSVBlue)
    resultHSVBlue = cv2.bitwise_and(frame, frame, mask = maskHSVBlue)
    #cv2.imshow('blauw', resultHSVBlue)
    #merging images
    resultBlueGreen = MergeImage(resultHSVBlue, resultHSVGreen)
    #cv2.imshow('result blue green', resultBlueGreen)
    resultBlueGreenRed = MergeImage(resultBlueGreen, resultHSVRed)
    resultBlueGreenRedYellow = MergeImage(resultBlueGreenRed, resultHSVYellow)
    resultBGR = cv2.cvtColor(resultBlueGreenRedYellow, cv2.COLOR_HSV2BGR)
    #cv2.imshow('BGR', resultBGR)
    resultGrey = cv2.cvtColor(resultBGR, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('GRey', resultGrey)
    red, resultWhiteBlack = cv2.threshold(resultGrey, 127, 255, 0)
    #cv2.imshow('resultBlackWhite', resultWhiteBlack)
    #greyscale
    edged = cv2.Canny(resultBlueGreenRedYellow, 30, 100)
    retGreyresult, _ = cv2.threshold(resultBlueGreenRedYellow, 127, 255, cv2.THRESH_BINARY)
    #cv2.imshow('edged', edged)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilate = cv2.dilate(edged, kernel, iterations=1) # zorgt ervoor dat er verbindgen zijn tussen de randen
    #find countours
    contoursresult, _ = cv2.findContours(image = dilate, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    image_copyresult = frame.copy()
    #Calculate contour center
    frameSize = (frame.shape[1], frame.shape[0])
    borderMargin = 10
    centerObjectList=[]
    colorObjectList =[]
    for contour in contoursresult:
        area = cv2.contourArea(contour)
        if 5000 > area > 400:
            if len(contour) > 0:
                x, y = contour[0][0]
                if borderMargin <= x < frameWidth - borderMargin:
                    moment = cv2.moments(contour)
                    #calculating centroid
                    if moment["m00"] != 0:
                        cX = int(moment["m10"]/moment["m00"]) #center X coordinate
                        cY = int(moment["m01"]/moment["m00"]) #center Y coordinate
                    else:
                        cX, cY = 0, 0          
                colorName = PixelHsvColor(frame, cY, cX, colorList)
            cv2.circle(image_copyresult, (cX, cY), 5, (0, 255, 255), -1)
            cv2.putText(image_copyresult, colorName, (cX -25, cY -35), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 0), 1)
            print(colorName)
            centerObjectList.append((cX,cY))
            colorObjectList.append(colorName)
            cv2.drawContours(image=image_copyresult, contours=contour, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    return centerObjectList, colorObjectList, image_copyresult

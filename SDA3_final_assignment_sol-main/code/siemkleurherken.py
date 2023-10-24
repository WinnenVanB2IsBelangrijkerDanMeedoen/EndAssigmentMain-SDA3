import cv2
import numpy as np
show = False
vidCapture = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if (vidCapture.isOpened() == False):
    print("error opening video file")
else:

    fps = int(vidCapture.get(5))
    print("Frame Rate : ", fps, "frames per second")

    frameCount = vidCapture.get(7)
    print("Frame count : ", frameCount)


framwWidth = int(vidCapture.get(3))
framHeight = int(vidCapture.get(4))
frameSize = (framwWidth, framHeight)
fps = 10


#yellow
minHSVYellow = np.array([18, 160, 0])
maxHSVYellow = np.array([39, 255, 255])

#Red
minHSVRed = np.array([0, 170, 0])
maxHSVRed = np.array([90, 255, 255])

#green
minHSVGreen = np.array([43, 79, 0])
maxHSVGreen = np.array([84, 255, 255])

#blue
minHSVBlue = np.array([100, 90, 0]) #69
maxHSVBlue = np.array([162, 255, 255])

rsize = 400

def onTrackbarActivity(x):
    global show
    show = True
    pass

cv2.namedWindow('SelectHSV',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('HMin','SelectHSV',0,180,onTrackbarActivity)
cv2.createTrackbar('HMax','SelectHSV',0,180,onTrackbarActivity)
cv2.createTrackbar('SMin','SelectHSV',0,255,onTrackbarActivity)
cv2.createTrackbar('SMax','SelectHSV',0,255,onTrackbarActivity)
cv2.createTrackbar('VMin','SelectHSV',0,255,onTrackbarActivity)
cv2.createTrackbar('VMax','SelectHSV',0,255,onTrackbarActivity)


def MergeImage(image1, image2):
    alpha_background = image1[:,:,2] / 255.0
    alpha_foreground = image2[:,:,2] / 255.0

    for color in range(0, 3):
        image1[:,:,color] = alpha_foreground * image2[:,:,color] + \
        alpha_background * image1[:,:,color] * (1 - alpha_foreground)

    image1[:,:,2] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255
    return image1


while(vidCapture.isOpened()):
    ret, frame = vidCapture.read()
    if ret == True:

        frame = cv2.GaussianBlur(frame, (3,3), 0)

        HMin = cv2.getTrackbarPos('HMin','SelectHSV')
        SMin = cv2.getTrackbarPos('SMin','SelectHSV')
        VMin = cv2.getTrackbarPos('VMin','SelectHSV')
        HMax = cv2.getTrackbarPos('HMax','SelectHSV')
        SMax = cv2.getTrackbarPos('SMax','SelectHSV')
        VMax = cv2.getTrackbarPos('VMax','SelectHSV')
        minHSVRed = np.array([HMin, SMin, VMin])
        maxHSVRed = np.array([HMax, SMax, VMax])


        frame = cv2.resize(frame,(rsize,rsize))


        #greyscale 
        imageGrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        retGrey, threshGrey = cv2.threshold(imageGrey, 150, 255, cv2.THRESH_BINARY)
        
        #find countours
        contours, hierarchy = cv2.findContours(image = threshGrey, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
        image_copy = frame.copy()
        cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        cv2.imshow('None approximation', image_copy)

        #Red detection
        imageHSVRed = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskHSVRed = cv2.inRange(imageHSVRed, minHSVRed, maxHSVRed)
        resultHSVRed = cv2.bitwise_and(frame, frame, mask = maskHSVRed)
        cv2.imshow('red', resultHSVRed)

        #yellow detection
        imageHSVYellow = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskHSVYellow = cv2.inRange(imageHSVYellow, minHSVYellow, maxHSVYellow)
        resultHSVYellow = cv2.bitwise_and(frame, frame, mask = maskHSVYellow)
        cv2.imshow('geel', resultHSVYellow)

        #green detection
        imageHSVGreen = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskHSVGreen = cv2.inRange(imageHSVGreen, minHSVGreen, maxHSVGreen)
        resultHSVGreen = cv2.bitwise_and(frame, frame, mask = maskHSVGreen)
        cv2.imshow('groen', resultHSVGreen)

        #blue detection
        imageHSVBlue = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskHSVBlue = cv2.inRange(imageHSVBlue, minHSVBlue, maxHSVBlue)
        resultHSVBlue = cv2.bitwise_and(frame, frame, mask = maskHSVBlue)
        cv2.imshow('blauw', resultHSVBlue)

    
        resultBlueGreen = MergeImage(resultHSVBlue, resultHSVGreen)
        cv2.imshow('result blue green', resultBlueGreen)
        resultBlueGreenRed = MergeImage(resultBlueGreen, resultHSVRed)
        resultBlueGreenRedYellow = MergeImage(resultBlueGreenRed, resultHSVYellow)


        resultBGR = cv2.cvtColor(resultBlueGreenRedYellow, cv2.COLOR_HSV2BGR)
        cv2.imshow('BGR', resultBGR)
        resultGrey = cv2.cvtColor(resultBGR, cv2.COLOR_BGR2GRAY)
        cv2.imshow('GRey', resultGrey)
        red, resultWhiteBlack = cv2.threshold(resultGrey, 127, 255, 0)
        cv2.imshow('resultBlackWhite', resultWhiteBlack)

        #greyscale
        edged = cv2.Canny(resultBlueGreenRedYellow, 30, 100)
        retGreyresult, threshGreyresult = cv2.threshold(resultBlueGreenRedYellow, 127, 255, cv2.THRESH_BINARY)
        
        cv2.imshow('greyresult', edged)
        cv2.imshow('tresh', threshGreyresult)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilate = cv2.dilate(edged, kernel, iterations=1) # zorgt ervoor dat er verbindgen zijn tussen de randen
        #find countours
        contoursresult, hierarchyresult = cv2.findContours(image = dilate, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        image_copyresult = frame.copy()
        cv2.drawContours(image=image_copyresult, contours=contoursresult, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        cv2.imshow('result', image_copyresult)
        cv2.imshow('reuslt2HSV', resultBlueGreenRedYellow)
        cv2.imshow('SelectHSV',resultBlueGreenRedYellow)
        k = cv2.waitKey(20)
        if k == 113:
            break
    else:
        break



vidCapture.release()
cv2.destroyAllWindows()
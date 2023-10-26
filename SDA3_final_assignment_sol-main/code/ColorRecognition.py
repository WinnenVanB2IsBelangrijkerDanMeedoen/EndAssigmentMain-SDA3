import cv2
import numpy as np

def PixelHsvColor(frame, cY, cX, colorlist):
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsvPixelValue = hsvFrame[cY,cX]
    i=0
    for colorName, minimum, maximum in colorlist:
            lowerBound = np.array(minimum)
            upperBound = np.array(maximum)
            if(lowerBound <= hsvPixelValue).all() and (hsvPixelValue <= upperBound).all():
                return colorName
    return "unknown"
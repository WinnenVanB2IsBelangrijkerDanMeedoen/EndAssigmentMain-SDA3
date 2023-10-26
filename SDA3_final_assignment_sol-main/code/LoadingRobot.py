import cv2
from ObjectDetection import*
from ResizeFrame import *

class LoadingRobot():
    def __init__(self):
        super().__init__()
    
    def TrimFrame():
        resizedFrame = ResizeFrame()
        return resizedFrame
        

    def PickUp():
        pass

    def PlaceDown():
        pass
    def PickupPlaceDetection(resizedFrame):
        vidCapture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
        centerList, frame = ObjectDetection(resizedFrame)
        cv2.imshow("VideoFeed", frame)
        pass
    def CoordinateCalculation():
        pass

frame = LoadingRobot.TrimFrame()
LoadingRobot.PickupPlaceDetection(frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
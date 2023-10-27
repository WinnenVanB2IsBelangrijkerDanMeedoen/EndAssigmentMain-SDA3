from RoboticArm import *
from ObjectDetection import*
from ResizeFrame import *
import cv2

class LoadingRobot(RoboticArm):
    def __init__(self, ctrlBot = None, homeCoordinates = (None, None, None)):
        super().__init__()
        
    
    def TrimFrame():
        resizedFrame = ResizeFrame()
        return resizedFrame
    def PickUp():
        pass

    def PlaceDown():
        5, 145, 12
        pass
    def ConveyorBelt():
        pass

    def PickupPlaceDetection(resizedFrame):
        vidCapture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
        centerlist, frame = ObjectDetection(vidCapture)
        cv2.imshow("Videofeed", frame)

    def CoordinateCalculation():
        pass
    
frame = LoadingRobot.TrimFrame()
LoadingRobot.PickupPlaceDetection(frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
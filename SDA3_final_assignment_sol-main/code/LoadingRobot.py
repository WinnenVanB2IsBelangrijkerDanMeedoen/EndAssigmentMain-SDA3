import cv2
from RoboticArm import *
from ObjectDetection import *

class LoadingRobot(RoboticArm):
    def __init__(self, homeCoordinates = None):
        pass

    def initialize(self, homeCoordinates):
        super().__init__(True, homeCoordinates)
        return self.ctrlBot
    
    def PickUp():
        pass

    def PlaceDown():
        pass
    def ConveyorBelt():
        pass

    def PickupPlaceDetection(self, resizedFrame):
        vidCapture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
        centerList, frame = ObjectDetection(self.resizedFrame)
        cv2.imshow("VideoFeed", frame)
        return centerList

    def CoordinateCalculation():
        pass

frame = LoadingRobot.TrimFrame()
LoadingRobot.PickupPlaceDetection(frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
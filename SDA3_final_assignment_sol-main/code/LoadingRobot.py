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
        centerList, colorList, frame = ObjectDetection(resizedFrame)
        cv2.imshow("Videofeed", frame)
        print(centerList)
        print(colorList)

    def CoordinateCalculation():
        pass
    
#frame = LoadingRobot.TrimFrame()
#LoadingRobot.PickupPlaceDetection(frame)

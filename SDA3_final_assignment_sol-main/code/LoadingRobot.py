from RoboticArm import *
from ObjectDetection import*
from ResizeFrame import *
from CoordinateCalculation import CoordinateCalculation
import cv2

class LoadingRobot(RoboticArm):
    def __init__(self, ctrlBot = None, homeCoordinates = (None, None, None)):
        print("innit")
        super().__init__(homeCoordinates)
        
    def Initialize(self):
        print("initialize")
        return self.ctrlBot
    
    def TrimFrame():
        resizedFrame = ResizeFrame()
        return resizedFrame
    
    def PickUp():
        pass

    def PlaceDown():
        pass
    def ConveyorBelt():
        pass

    def PickupPlaceDetection(resizedFrame):
        centerList, colorList, frame = ObjectDetection(resizedFrame)
        cv2.imshow("Videofeed", frame)
        print(centerList)
        print(colorList)

    def CoordinateCalculation(centerList):
        RobotCoordinateCenterList = CoordinateCalculation(centerList)
        return RobotCoordinateCenterList
    
#frame = LoadingRobot.TrimFrame()
#LoadingRobot.PickupPlaceDetection(frame)

from RoboticArm import *
from ObjectDetection import*
from ResizeFrame import *
from CoordinateCalculation import CoordinateCalculation
from userColorSelector import SelectColor
import cv2

class LoadingRobot(RoboticArm):
    def __init__(self, ctrlBot):
        self.ctrlBot = ctrlBot
        print("innit")
        
    def Initialize(self):
        print("initialize")
        return self.ctrlBot
    
    def TrimFrame(self):
        self.resizedFrame, self.resizeValues = ResizeFrame()
    
    def PickUp(self, userCoordinates, defaultPickUpLocation = (145,215,60)):
        self.ctrlBot.moveArmXYZ(defaultPickUpLocation[0],defaultPickUpLocation[1],defaultPickUpLocation[2], jump = True, wait = True)
        self.ctrlBot.moveArmXY(userCoordinates[0], userCoordinates[1], wait = True)
        self.ctrlBot.SetConveyor(enabled=True)
        
        self.ctrlBot.pickToggle()
        self.ctrlBot.SetConveyor(enabled=False)
        self.ctrlBot.moveArmXYZ(None, None, 60, wait = False)

    def PlaceDown(self):
        self.ctrlBot.moveHome()
        self.ctrlBot.pickToggle()

    def ConveyorBelt():
        pass

    def PickupPlaceDetection(self):
        self.centerList, self.colorList, frame = ObjectDetection(self.resizedFrame)

    def RetakePhoto(self):
        vidCapture = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        _, frame = vidCapture.read()
        self.resizedFrame = frame[self.resizeValues[0]:self.resizeValues[1], self.resizeValues[2]:self.resizeValues[3]]

    def UserChoice(self):       
        userChoice = SelectColor(self.colorList)
        objectNumber = self.colorList.index(userChoice)
        return (self.RobotCoordinateCenterList[objectNumber])

    def CoordinateCalculation(self):
        self.RobotCoordinateCenterList = CoordinateCalculation(self.centerList)

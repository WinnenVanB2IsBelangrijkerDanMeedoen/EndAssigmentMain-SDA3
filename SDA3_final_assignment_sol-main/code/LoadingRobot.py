from RoboticArm import *
import cv2

class LoadingRobot(RoboticArm):
    def __init__(self):
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
        super().PickUpPlaceDetection(resizedFrame)
        return self.centerList

    def CoordinateCalculation():
        pass
    
frame = LoadingRobot.TrimFrame()
LoadingRobot.PickupPlaceDetection(frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
from RoboticArm import *
import cv2

class LoadingRobot(RoboticArm):
    def __init__(self, ctrlBot = None, homeCoordinates = (None, None, None)):
        
        pass
    
    def PickUp():
        pass

    def PlaceDown():
        5, 145, 12
        pass
    def ConveyorBelt():
        pass

    def PickupPlaceDetection(self, resizedFrame):
        super().PickUpPlaceDetection(resizedFrame)
        return self.centerList

    def CoordinateCalculation():
        pass
    
# frame = LoadingRobot.TrimFrame()
# LoadingRobot.PickupPlaceDetection(frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
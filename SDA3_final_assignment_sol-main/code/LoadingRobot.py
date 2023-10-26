from RoboticArm import *

class LoadingRobot(RoboticArm):
    def __init__(self, homeCoordinates, homing=False):
        pass

    def initialize(self,homeCoordinates, homing):
        super().__init__(homing, homeCoordinates)
        return self.ctrlBot
    
    def PickUp(x,y):
        pass

    def PlaceDown():
        pass

    def ConveyorBelt():
        pass

    def CoordinateCalculation():
        pass
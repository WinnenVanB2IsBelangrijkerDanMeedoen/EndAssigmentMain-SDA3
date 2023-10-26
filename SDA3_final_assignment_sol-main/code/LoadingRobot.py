from RoboticArm import *

class LoadingRobot(RoboticArm):
    def __init__(self, homeCoordinates = None):
        pass

    def initialize(self, homeCoordinates):
        super().__init__(True, homeCoordinates)
        return self.ctrlBot
    
    def PickUp(x,y):
        pass

    def PlaceDown():
        pass

    def ConveyorBelt():
        pass

    def CoordinateCalculation():
        pass
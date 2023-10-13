from abc import ABC, abstractmethod

class RoboticArm():
    def __init__(self):
        return 1

    @abstractmethod
    def PickUp():
        raise NotImplementedError
    
    @abstractmethod
    def PlaceDown():
        raise NotImplementedError

    @abstractmethod
    def CoordinateCalculation():
        raise NotImplementedError

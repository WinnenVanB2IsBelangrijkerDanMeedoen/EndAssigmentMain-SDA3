import threading
from DoBotArm import DoBotArm as Dbt
from serial.tools import list_ports
from abc import ABC, abstractmethod
from ObjectDetection import *

def portSelection():
    # Choosing port
    availablePorts = list_ports.comports()
    print('Available COM-ports0:')
    for i, port in enumerate(availablePorts):
        print(f"  {i}: {port.description}")

    choice = 0 #int(input('Choose port by typing a number followed by [Enter]: '))
    return availablePorts[choice].device

def homingPrompt():
    while (True):
        response = input("Do you wanna home? (y/n)")
        if(response == "y") :
            return True
        elif (response == "n"):
            return False
        else:
            print("Unrecognised response")

class RoboticArm(ABC):
    def __init__(self, ctrlBot, homeCoordinates): #dropcoordinates
        pass

    @abstractmethod
    def PickUp():
        raise NotImplementedError
    
    @abstractmethod
    def PlaceDown():
        raise NotImplementedError
    
    @abstractmethod
    def ConveyorBelt():
        raise NotImplementedError
    

    def PickUpPlaceDetection(self, resizedFrame):
        vidCapture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
        self.centerList, frame = ObjectDetection(resizedFrame)
        cv2.imshow("VideoFeed", frame)
        

    @abstractmethod
    def CoordinateCalculation():
        raise NotImplementedError


 
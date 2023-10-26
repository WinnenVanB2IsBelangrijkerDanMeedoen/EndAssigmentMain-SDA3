import threading
from DoBotArm import DoBotArm as Dbt
from serial.tools import list_ports
from abc import ABC, abstractmethod

def port_selection():
    # Choosing port
    available_ports = list_ports.comports()
    print('Available COM-ports0:')
    for i, port in enumerate(available_ports):
        print(f"  {i}: {port.description}")

    choice = 0#int(input('Choose port by typing a number followed by [Enter]: '))
    return available_ports[choice].device

def homing_prompt():
    while (True):
        response = input("Do you wanna home? (y/n)")
        if(response == "y") :
            return True
        elif (response == "n"):
            return False
        else:
            print("Unrecognised response")

class RoboticArm(ABC):
    def __init__(self, homing, homeCoordinates):
        if homing:
            print("Connecting...")
            port = port_selection()
            self.ctrlBot = Dbt.DoBotArm(port, homeCoordinates[0], homeCoordinates[1], homeCoordinates[2], home = True) #Create DoBot Class Object with home position x,y,z


    @abstractmethod
    def PickUp():
        raise NotImplementedError
    
    @abstractmethod
    def PlaceDown():
        raise NotImplementedError
    
    @abstractmethod
    def ConveyorBelt():
        raise NotImplementedError

    @abstractmethod
    def CoordinateCalculation():
        raise NotImplementedError


 
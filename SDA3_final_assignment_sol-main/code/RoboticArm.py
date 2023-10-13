import threading
from DoBotArm import DoBotArm as Dbt
import time
from serial.tools import list_ports
from abc import ABC, abstractmethod

def port_selection():
    # Choosing port
    available_ports = list_ports.comports()
    print('Available COM-ports0:')
    for i, port in enumerate(available_ports):
        print(f"  {i}: {port.description}")

    choice = int(input('Choose port by typing a number followed by [Enter]: '))
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
    def __init__(self):
        print("Disconnecting")

    @abstractmethod
    def PickUp():
        raise NotImplementedError
    
    @abstractmethod
    def PlaceDown():
        raise NotImplementedError

    @abstractmethod
    def CoordinateCalculation():
        raise NotImplementedError

def main():
    port = port_selection()
    if homing_prompt():
        homeX, homeY, homeZ = 200, 0, 20
        print("Connecting")
        print("Homing")
        ctrlBot = Dbt.DoBotArm(port, homeX, homeY, homeZ, home = True) #Create DoBot Class Object with home position x,y,z
    
    if homing_prompt():
        Dbt.moveHome(homeX, homeY, homeZ)


if __name__ == "__main__":
    main()
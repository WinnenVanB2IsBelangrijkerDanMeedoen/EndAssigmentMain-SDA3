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
    homing_prompt()
    homeX, homeY, homeZ = 200, 0, 20
    print("Connecting")
    print("Homing")
    ctrlBot = Dbt.DoBotArm(port, homeX, homeY, homeZ) #Create DoBot Class Object with home position x,y,z
    # position = ctrlBot.getPosition()
    # print("Current Location Nozzle: ", position[0], position[1], position[2])
    # homing_prompt()
    # time.sleep(2)
    # ctrlBot.moveArmRelXY(0,100,wait=False)
    # print(ctrlBot.getPosition())
    # if homing_prompt():
    #     Dbt.moveHome()
    ctrlBot.moveArmRelXY(0, 20) #deze slaat hij voor een of andere manier over

    ctrlBot.moveArmXY(200,-150,20)
    print(ctrlBot.getPosition())
    while(True):
        True
    
    print("klaar")


if __name__ == "__main__":
    main()


 
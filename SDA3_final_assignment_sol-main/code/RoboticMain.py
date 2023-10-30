from LoadingRobot import *
import time
import os
import keyboard
import threading
from DoBotArm import DoBotArm as Dbt
from serial.tools import list_ports
from abc import ABC, abstractmethod
from ObjectDetection import *
import tkinter as tk
from userColorSelector import SelectColor


def main():
    os.chdir(path= 'SDA3_final_assignment_sol-main/code/DoBotArm') 
    # position = ctrlBot.getPosition()
    # print("Current Location Nozzle: ", position[0], position[1], position[2])
    # homing_prompt()
    # time.sleep(2)
    # ctrlBot.moveArmRelXY(0,100,wait=False)
    # print(ctrlBot.getPosition())
    # if homing_prompt():
    #     Dbt.moveHome()


    roboticState = 'initialize'
    colorList = [("Blue"), ("Red"), ("Yellow"), ("Green")]
    centerList = []
    enableConveyor = False
    previousConveyorTime = 0

    centerList.append(("Blue(B)", (30,60)))
    centerList.append(("Red(R)", (70,140)))
    centerList.append(("Yellow(G)", (200,400)))

    while True:

        match roboticState:
            case 'initialize':
                port = portSelection()
                homeCoordinatesLoadingRobot = (5, 210, 60)
                ctrlBot = Dbt.DoBotArm(port, homeCoordinatesLoadingRobot[0], homeCoordinatesLoadingRobot[1], homeCoordinatesLoadingRobot[2], home = True) #Create DoBot Class Object with home position x,y,z
                #ctrlBot = LoadingRobot.Initialize(homeCoordinates= homeCoordinatesLoadingRobot)
                ctrlBot.moveArmRelXY(0, 0, wait=True) #deze slaat hij voor een of andere manier over

                #Resize Frame and detect cosntours
                #resizedFrame = LoadingRobot.TrimFrame()
                #LoadingRobot.PickupPlaceDetection(resizedFrame)
                print("done initializing")
                roboticState = 'pickUpPosition'

            case 'userColorChoice':
                userChoice = SelectColor(colorList)
                print(userChoice)
                match userChoice:
                    case 'Blue':
                        pass

                    case 'Green':
                        pass

                    case 'Red':
                        pass

                    case 'Yellow':
                        pass

            case 'pickUp':
                ctrlBot.pickToggle()
                ctrlBot.SetConveyor(enabled=False)
                ctrlBot.moveArmXYZ(None, None, 60, wait = False)
                roboticState = 'dropPosition'

            case 'drop':
                ctrlBot.pickToggle()
                roboticState = 'pickUpPosition'

            case 'dropPosition':
                ctrlBot.moveHome()
                roboticState = 'drop'

            case 'pickUpPosition':
                ctrlBot.moveArmXYZ(145,215,60, jump = True, wait = True)
                ctrlBot.SetConveyor(enabled=True)
                roboticState = 'pickUp'
        #print(ctrlBot.getPosition())

        # if(enableConveyor):
        #     ctrlBot.SetConveyor(enabled=True)
        #     if(time.time() - previousConveyorTime > 2.7):
        #         ctrlBot.SetConveyor(enabled=False)
        #         enableConveyor = False
            

        print("current:", time.time(), '\t', "previous:", previousConveyorTime, '\t', "conveyor status:", enableConveyor)

        if keyboard.is_pressed("esc"):
            #ctrlBot.moveArmXYZ(z=60, wait=True)
            ctrlBot.SetConveyor(enabled=False)
            break

    
        

if __name__ == "__main__":
    main()
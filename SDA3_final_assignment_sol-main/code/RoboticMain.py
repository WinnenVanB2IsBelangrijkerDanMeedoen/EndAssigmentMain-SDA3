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
    # colorList = [("Blue"), ("Red"), ("Yellow"), ("Green")]
    # centerList = []
    userCoordinates = (145,215)

    # centerList.append(("Blue(B)", (30,60)))
    # centerList.append(("Red(R)", (70,140)))
    # centerList.append(("Yellow(G)", (200,400)))

    
    while True:

        match roboticState:
            case 'initialize':
                port = portSelection()
                homeCoordinatesLoadingRobot = (5, 210, 60)
                ctrlBot = Dbt.DoBotArm(port, homeCoordinatesLoadingRobot[0], homeCoordinatesLoadingRobot[1], homeCoordinatesLoadingRobot[2], home = True) #Create DoBot Class Object with home position x,y,z
                loadingBot = LoadingRobot(ctrlBot)
                # ctrlBot = LoadingRobot.Initialize(homeCoordinates= homeCoordinatesLoadingRobot)
                ctrlBot.moveArmRelXY(0, 0, wait=True) #deze slaat hij voor een of andere manier over

                #Resize Frame and detect cosntours
                #resizedFrame = LoadingRobot.TrimFrame()
                #LoadingRobot.PickupPlaceDetection(resizedFrame)
                loadingBot.TrimFrame()
                loadingBot.PickupPlaceDetection()
                loadingBot.CoordinateCalculation()

                print("done initializing")
                roboticState = 'userColorChoice'

            case 'userColorChoice':
                userCoordinates = loadingBot.UserChoice()
                roboticState = 'pickUp'

            case 'pickUp':
                loadingBot.PickUp(userCoordinates)
                roboticState = 'placeDown'

            case 'placeDown':
                loadingBot.PlaceDown()
                roboticState = 'retakePhoto'

            case 'retakePhoto':
                loadingBot.RetakePhoto()
                loadingBot.PickupPlaceDetection()
                loadingBot.CoordinateCalculation()
                roboticState = 'userColorChoice'

        #print(ctrlBot.getPosition())

        # if(enableConveyor):
        #     ctrlBot.SetConveyor(enabled=True)
        #     if(time.time() - previousConveyorTime > 2.7):
        #         ctrlBot.SetConveyor(enabled=False)
        #         enableConveyor = False
            

        #print("current:", time.time(), '\t', "previous:", previousConveyorTime, '\t', "conveyor status:", enableConveyor)

        if keyboard.is_pressed("esc"):
            #ctrlBot.moveArmXYZ(z=60, wait=True)
            ctrlBot.SetConveyor(enabled=False)
            break

    
        

if __name__ == "__main__":
    main()
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
    roboticState = 'initialize'
    userCoordinates = (145,215)
    
    while True:

        match roboticState:
            case 'initialize':
                port = portSelection()
                homeCoordinatesLoadingRobot = (5, 210, 60)
                ctrlBot = Dbt.DoBotArm(port, homeCoordinatesLoadingRobot[0], homeCoordinatesLoadingRobot[1], homeCoordinatesLoadingRobot[2], home = True) #Create DoBot Class Object with home position x,y,z
                loadingBot = LoadingRobot(ctrlBot)
                ctrlBot.moveArmRelXY(0, 0, wait=True) #deze slaat hij voor een of andere manier over

                loadingBot.TrimFrame()
                loadingBot.PickupPlaceDetection()
                loadingBot.CoordinateCalculation()
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

        if keyboard.is_pressed("esc"): 
            ctrlBot.SetConveyor(enabled=False)
            break
        

if __name__ == "__main__":
    main()
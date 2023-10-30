from DoBotArm import DoBotArm as Dbt
from serial.tools import list_ports
import os
import keyboard

def portSelection():
    # Choosing port
    availablePorts = list_ports.comports()
    print('Available COM-ports0:')
    for i, port in enumerate(availablePorts):
        print(f"  {i}: {port.description}")

    choice = 0#int(input('Choose port by typing a number followed by [Enter]: '))
    return availablePorts[choice].device

def main():
    os.chdir(path= 'SDA3_final_assignment_sol-main/code/DoBotArm') 
    port = portSelection()
    homeCoordinatesLoadingRobot = (5, 210, 60)
    ctrlBot = Dbt.DoBotArm(port, homeCoordinatesLoadingRobot[0], homeCoordinatesLoadingRobot[1], homeCoordinatesLoadingRobot[2], home = True) #Create DoBot Class Object with home position x,y,z
    ctrlBot.moveArmRelXY(0, 0, wait = True) #deze slaat hij voor een of andere manier over

    while True:
        if keyboard.is_pressed("w"):
            ctrlBot.moveArmRelXY(-5, 0)
        if keyboard.is_pressed("s"):
            ctrlBot.moveArmRelXY(5, 0)
        if keyboard.is_pressed("a"):
            ctrlBot.moveArmRelXY(0, -5)
        if keyboard.is_pressed("d"):
            ctrlBot.moveArmRelXY(0, 5)
        if keyboard.is_pressed("c"):
            ctrlBot.moveArmRelXYZ(0, 0, -5)
        if keyboard.is_pressed("x"):
            ctrlBot.moveArmRelXYZ(0, 0, 5)
        print(ctrlBot.getPosition())

if(__name__ == '__main__'):
    main()
import os
import sys
import keyboard
import time

while(True):
    print("in loop")
    print(time.time())
    if keyboard.is_pressed("esc"):
            print("test")
            sys.exit

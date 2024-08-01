import time
import pydirectinput
import threading
import keyboard

from KeyCodes import *

#Main Variables
SETUP_TIME = 5 #How Long Before The Program Starts Autoclicking After Running Main.py
PRESS_TIME = 50 #In Milliseconds
PRESS_AMOUNT = 2000 #The Amount Of Times You Want The Autoclicker To Press The Specified Button


#Thread That Closes The Program When The Specified Key Is Pressed (Default F8)
def CloseProgramThread(threadEvent:threading.Event):
    print("Press F8 To Close Autoclicker Early")
    keyboard.wait("f8")
    print("Closing The Program")
    threadEvent.set()

if __name__ == "__main__":
    threadEvent = threading.Event()
    CloseProgram = threading.Thread(target=CloseProgramThread, args=(threadEvent,))
    CloseProgram.start()
    
    time.sleep(SETUP_TIME) #Sleeps The Program For The Specified Time
    
    for i in range(PRESS_AMOUNT):
        if threadEvent.is_set():
            break
        
        #HoldAndReleaseKey(E)
        pydirectinput.mouseDown()
        time.sleep(PRESS_TIME / 1000)
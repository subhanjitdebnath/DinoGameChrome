import pyautogui as pya
import time

class Findtarg:
    def __init__(self):
        pass

    def LocateDyno(self):
        x,y,z,w=pya.locateOnScreen("DinoLocation.png",confidence=0.5)
        print(x,y,z,w)

if "__main__"==__name__:
    f=Findtarg()
    f.LocateDyno()
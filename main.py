from tkinter import *
import tkinter as tk
import threading
import pyautogui as pya
import time
start=False

def startAuto():
    print("Starting")
    global start
    start=True
    lb1.config(text="Starting..")
    t1=threading.Thread(target=Mainstart)
    t1.start()
    
    
def StopAuto():
    global start
    start = False
    lb1.config(text="Stopped")
    

def Mainstart():
    global start
    while(start and ('normal'== window.state())):
        px=pya.pixel(1050,354)
        px2=pya.pixel(1050,315)
        px1=pya.position()
        lb1.config(text=str(px1))
        if(px!=(255,255,255)):
            pya.press("up")
        elif(px2!=(255,255,255) and px==(255,255,255)):
            pya.press("down")
        
window =Tk()
window.geometry("200x100")
window.positionfrom("user")
window.title("Auto")
bt1=tk.Button(window, text="START",bg="Green",font="Bold",command=startAuto)
bt1.place(x=10,y=10)
bt2=tk.Button(window ,text="STOP",bg="Red",font="Bold",command=StopAuto)
bt2.place(x=105,y=10)
lb1=tk.Label(window)
lb1.place(x=5,y=50)
window.mainloop()


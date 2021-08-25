from tkinter import *
from tkinter.ttk import Progressbar
#from tkinter import ttk
import tkinter.font as tkFont
import time

window = Tk()

window.title("Quad272021")

#800 = width of window
#500 = height of window
window.geometry('500x800')

lbl = Label(window, text="Welcome to Quad272021 control panel!", font=("Arial Bold", 15))

lbl.place(x=50, y=10)

step = DoubleVar()
step.set(1)

frame = Frame()
frame.pack(fill=BOTH, padx=2, pady=2)
frame.place(x=200,y=100)



def add_progbar(time):
    progbar = Progressbar(
        frame, 
        orient=HORIZONTAL,
        length=200,
        mode='determinate', 
        variable=step, 
        maximum=time)
    progbar.pack(fill=X, expand=True)
    
def start_progbar(cd):
    add_progbar(cd)
    for x in range(1, cd+1):
        step.set(x)
        time.sleep(1)
        window.update()
        print("prog bar count: ", x)
        
def stop():
    frame.pack_forget()
    frame.destroy()
    
    
def changeLabel():
    secLbl.configure(text="Process Started")
    
def startFun():
    stateLbl.configure(text="Washing in progress")
    if(setCountDown(10)=="done"):
        stateLbl.configure(text="idle")
        print("Done")
    start_progbar(10)
    
def stopFun():
    stateLbl.configure(text="idle")
    
def conFun():
    stateLbl.configure(text="Washing in progress")
    
def pauseFun():
    stateLbl.configure(text="Progress pause")

def extraWashFun():
    stateLbl.configure(text="Washing in progress")
    
def extraDryFun():
    stateLbl.configure(text="Drying in progress")

def setCountDown(t):
    mins, secs = divmod(t, 60)
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    timeLbl.config(text=timeformat)
    if(t!=0):
        t -=1
        window.after(1000, lambda: setCountDown(t))
    elif(t==0):
        return "done"
    else:
        return False

# Creating a photoimage object to use image
photoStart = PhotoImage(file = "/home/pi/Desktop/GUI Images/start.png")
photoStop = PhotoImage(file = "/home/pi/Desktop/GUI Images/stop.png")
photoPause = PhotoImage(file = "/home/pi/Desktop/GUI Images/pause.png")
photoContinue = PhotoImage(file = "/home/pi/Desktop/GUI Images/continue.png")
photoWash = PhotoImage(file = "/home/pi/Desktop/GUI Images/wash.png")
photoDry = PhotoImage(file = "/home/pi/Desktop/GUI Images/dry.png")

#btnStart = Button(window, text="START", bg="black", fg="white", width=10, height=2)
#command = start_progbar
btnStart = Button(window, text="START", bg="green", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoStart, compound = RIGHT, command = startFun)

btnStart.place(x=120, y=150)

btnStop = Button(window, text="STOP", bg="red", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoStop, compound = RIGHT, command = stopFun)

btnStop.place(x=120, y=250)

btnContinue = Button(window, text="CONTINUE", bg="teal", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoContinue, compound = RIGHT, command = conFun)

btnContinue.place(x=120, y=350)

btnPause = Button(window, text="PAUSE", bg="brown", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoPause, compound = RIGHT, command = pauseFun)

btnPause.place(x=120, y=450)

btnWash = Button(window, text="EXTRA WASHING", bg="blue", fg="white", width=200, font=("Arial Bold", 15), height=50, image= photoWash, compound = RIGHT, command = extraWashFun)

btnWash.place(x=120, y=550)

btnDry = Button(window, text="EXTRA DRYING", bg="orange", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoDry, compound = RIGHT, command = extraDryFun)

btnDry.place(x=120, y=650)

statusLbl = Label(window, text="Status: ", fg="red", font=("Arial Bold", 15))

statusLbl.place(x=120, y=60)

stateLbl = Label(window, text="Idle", fg="red", font=("Arial Bold", 15))

stateLbl.place(x=200, y=60)

timeLbl = Label(window, text="00:00", font=("Arial Bold", 15))

timeLbl.place(x=120, y=100)

#secLbl = Label(window, text="00", font=("Arial Bold", 10))

#secLbl.place(x=320, y=300)






      
window.mainloop()

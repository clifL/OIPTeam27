from tkinter import *
from tkinter.ttk import Progressbar
#from tkinter import ttk
import tkinter.font as tkFont
import time

window = Tk()

window.title("Quad272021")

#800 = width of window
#500 = height of window
window.geometry('800x500')

lbl = Label(window, text="Welcome to Quad272021 control panel!", font=("Arial Bold", 20))

lbl.place(x=100, y=0)

# set max for duration
max = 20
step = DoubleVar()
step.set(1)

frame = Frame()
frame.pack(fill=BOTH, padx=2, pady=2)
frame.place(x=100,y=325)


progbar = Progressbar

def add_progbar():
    progbar = Progressbar(
        frame, 
        orient=HORIZONTAL,
        length=600,
        mode='determinate', 
        variable=step, 
        maximum=max)
    progbar.pack(fill=X, expand=True)
    
def start_progbar():
    add_progbar()
    for x in range(1, 21):
        step.set(x)
        time.sleep(1)
        window.update()
        secLbl.configure(text=x)
        
        
def stop():
    frame.pack_forget()
    frame.destroy()
    
    
def changeLabel():
    secLbl.configure(text="Process Started")

# Creating a photoimage object to use image
photoStart = PhotoImage(file = "/home/pi/Desktop/GUI Images/start.png")
photoStop = PhotoImage(file = "/home/pi/Desktop/GUI Images/stop.png")  
# Resizing image to fit on button
photoimage = photoStart.subsample(2, 2)

#btnStart = Button(window, text="START", bg="black", fg="white", width=10, height=2)
#command = start_progbar
btnStart = Button(window, text="START", bg="green", fg="white", width=100, height=30, image= photoStart, compound = RIGHT, command = start_progbar)

btnStart.place(x=100, y=100)

btnStop = Button(window, text="STOP", bg="red", fg="white", width=100, height=30, image= photoStop, compound = RIGHT, command = stop)

btnStop.place(x=100, y=200)

btnWash = Button(window, text="Extra Washing", bg="black", fg="white", width=10, height=2)

btnWash.place(x=500, y=100)

btnDry = Button(window, text="Extra Drying", bg="black", fg="white", width=10, height=2)

btnDry.place(x=500, y=200)

countdownLbl = Label(window, text="Washing in progress", font=("Arial Bold", 10))

countdownLbl.place(x=100, y=300)

minLbl = Label(window, text="00", font=("Arial Bold", 10))

minLbl.place(x=300, y=300)

secLbl = Label(window, text="00", font=("Arial Bold", 10))

secLbl.place(x=320, y=300)






      
window.mainloop()

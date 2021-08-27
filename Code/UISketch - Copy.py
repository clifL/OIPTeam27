from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.font as tkFont
import time
from Helper import *
import datetime
from ReedSwitch import *


# 0 - Idle, 1 - Wash, 2 - Dry, 3 - Pause, 4 - Extra Washing, 5 - Extra Drying
status = 0
previous_status = 0
leftover_wash_duration = 0
leftover_dry_duration = 0
washing_duration = 20
drying_elapsed = 0
drying_duration = 20
# drying_duration = get_drying_time()
wash_end_time = datetime.datetime.now()
dry_end_time = datetime.datetime.now()


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
        # time.sleep(1)
        window.update()
        print("prog bar count: ", x)
        

def stop():
    frame.pack_forget()
    frame.destroy()
    
    
def changeLabel():
    secLbl.configure(text="Process Started")
    

def controller(washing_duration, drying_duration):
    global status
    global previous_status
    global wash_end_time
    global dry_end_time
    global leftover_wash_duration
    global leftover_dry_duration
    global drying_elapsed
    # Check if magnetic reed switch returns true
    if magnetic_status():
        if washing_duration > 0:
            status = 1
            # turn_motor(False)
            stateLbl.configure(text="Washing in progress")
            # turn_on_water_pump()
            wash_end_time = datetime.datetime.now() + datetime.timedelta(seconds=washing_duration)
            dry_end_time = datetime.datetime.now() + datetime.timedelta(seconds=drying_duration) + datetime.timedelta(seconds=washing_duration) 
            while (status == 1) and (datetime.datetime.now() < wash_end_time):
                leftover_wash_duration = (wash_end_time-datetime.datetime.now()).total_seconds()
                stateLbl.configure(text="Washing in progress - " + str(leftover_wash_duration) + "seconds")
                if magnetic_status() == False:
                    previous_status = status
                    status = 3
                    # turn_off_water_pump()
                    leftover_wash_duration = (wash_end_time-datetime.datetime.now()).total_seconds()
                    leftover_dry_duration = drying_duration
                    stateLbl.configure(text="Washing paused. Please close the door and press 'Continue' button.")
                # time.sleep(1)
            if status == 1:
                # turn_off_water_pump()
                status = 2
                stateLbl.configure(text="Drying in progress")
                # turn_motor(True)
                # turn_on_heated_fan()
        if drying_duration > 0:
            current_time = datetime.datetime.now()
            while (status == 2) and (datetime.datetime.now() < dry_end_time):    
                leftover_dry_duration = (dry_end_time-datetime.datetime.now()).total_seconds()
                stateLbl.configure(text="Drying in progress - " + str(leftover_dry_duration) + "seconds")
                if magnetic_status() == False:
                    leftover_dry_duration = (dry_end_time-datetime.datetime.now()).total_seconds()
                    previous_status = status
                    status = 3
                    # turn_off_heated_fan()
                    stateLbl.configure(text="Drying paused. Please close the door and press 'Continue' button.")
                drying_elapsed = (datetime.datetime.now() - current_time).total_seconds() 
                # time.sleep(1)
            if status == 2:
                # turn_off_heated_fan()
                status = 0
                stateLbl.configure(text="Drying completed")
        if status == 3:
            leftover_wash_duration = (wash_end_time-datetime.datetime.now()).total_seconds()
            if leftover_wash_duration < 0:
                leftover_wash_duration = 0
            leftover_dry_duration = (dry_end_time-datetime.datetime.now()).total_seconds()
            if leftover_dry_duration < 0:
                leftover_dry_duration = 0
            # # Do ML here to check if is really dry
            # data = {'temp': [30], 'humidity': [70], 'fan_speed':[0], 'elapsed_time':drying_elapsed}
            # if prediction(data) == 1:
            #     print("The syringes is dry.")
            # else:
            #     print("The syringes is wet.")
    else:
        stateLbl.configure(text="Please close the door")


def start_operation():
    global status
    global washing_duration
    global drying_duration

    if status != 0:
        return
    # Do ML here to get washing and drying duration
    controller(washing_duration, drying_duration)
        

def stop_operation():
    global status
    global leftover_dry_duration
    global leftover_wash_duration
    stateLbl.configure(text="idle")
    status = 0
    # turn_off_water_pump()
    # turn_off_heated_fan()
    # turn_motor(False)
    leftover_wash_duration = 0
    leftover_dry_duration = 0


def continue_operation():
    global status
    global previous_status
    global leftover_dry_duration
    global leftover_wash_duration
    if status == 3:
        status = previous_status
        controller(leftover_wash_duration, leftover_dry_duration)

    
def pause_operation():
    global status
    global previous_status
    previous_status = status
    status = 3
    # turn_off_water_pump()
    # turn_off_heated_fan()
    stateLbl.configure(text="Progress pause")


def extra_wash_operation():
    global status
    global washing_duration
    status = 1
    controller(washing_duration, 0)
    status = 0
    

def extra_dry_operation():
    global status
    global drying_duration
    status = 2
    controller(0, drying_duration)
    status = 0


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
root_path = get_working_directory()
root_path = str(get_working_directory())
photoStart = PhotoImage(file = root_path + "/" + "GUI images/start.png")
photoStop = PhotoImage(file = root_path + "/" + "GUI images/stop.png")
photoPause = PhotoImage(file = root_path + "/" + "GUI images/pause.png")
photoContinue = PhotoImage(file = root_path + "/" + "GUI images/continue.png")
photoWash = PhotoImage(file = root_path + "/" + "GUI images/wash.png")
photoDry = PhotoImage(file = root_path + "/" + "GUI images/dry.png")

#btnStart = Button(window, text="START", bg="black", fg="white", width=10, height=2)
#command = start_progbar
btnStart = Button(window, text="START", bg="green", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoStart, compound = RIGHT, command = start_operation)

btnStart.place(x=120, y=150)

btnStop = Button(window, text="STOP", bg="red", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoStop, compound = RIGHT, command = stop_operation)

btnStop.place(x=120, y=250)

btnContinue = Button(window, text="CONTINUE", bg="teal", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoContinue, compound = RIGHT, command = continue_operation)

btnContinue.place(x=120, y=350)

btnPause = Button(window, text="PAUSE", bg="brown", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoPause, compound = RIGHT, command = pause_operation)

btnPause.place(x=120, y=450)

btnWash = Button(window, text="EXTRA WASHING", bg="blue", fg="white", width=200, font=("Arial Bold", 15), height=50, image= photoWash, compound = RIGHT, command = extra_wash_operation)

btnWash.place(x=120, y=550)

btnDry = Button(window, text="EXTRA DRYING", bg="orange", fg="white", width=200, height=50, font=("Arial Bold", 15), image= photoDry, compound = RIGHT, command = extra_dry_operation)

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

from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.font as tkFont
import time
from Helper import *
import datetime
# from ReedSwitch import *
from SVM import *


# 0 - Idle, 1 - Wash, 2 - Dry, 3 - Pause, 4 - Extra Washing, 5 - Extra Drying
init_status = False
pause_status = False
stop_status = False
status = 0
previous_status = 0
leftover_wash_duration = 0
leftover_dry_duration = 0
washing_duration = 180
drying_elapsed = 0
drying_duration = get_drying_time()
# drying_duration = get_drying_time()
time_now = datetime.datetime.now()
wash_end_time = time_now
dry_end_time = time_now
early_completion = False
early_predict_status = False
addition_dry_time = False


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
    


def controller():
    global init_status
    global pause_status
    global stop_status
    global status
    global previous_status
    global wash_end_time
    global dry_end_time
    global leftover_wash_duration
    global leftover_dry_duration
    global drying_elapsed
    global early_completion
    global drying_duration
    global early_predict_status
    global addition_dry_time


    # Check if magnetic reed switch returns true
    if stop_status == True:
        stateLbl.configure(text="Idle")
        stop_status = False
        pause_status = False
        return
    
    if pause_status != True:
        if True:
            if leftover_wash_duration > 0:
                status = 1
                # turn_motor(False)
                stateLbl.configure(text="Washing in progress")
                # turn_on_water_pump()
                if init_status == False:
                    init_status == True
                    # wash_end_time = datetime.datetime.now() + datetime.timedelta(seconds=washing_duration)
                    # dry_end_time = datetime.datetime.now() + datetime.timedelta(seconds=drying_duration) + datetime.timedelta(seconds=washing_duration) 

                # Initially is while
                if (status == 1) and (datetime.datetime.now() < wash_end_time):
                    leftover_wash_duration = (wash_end_time-datetime.datetime.now()).total_seconds()
                    stateLbl.configure(text="Washing in progress... Left: " + str(int(leftover_wash_duration)) + " seconds")
                    # if magnetic_status() == False:
                    #     previous_status = status
                    #     status = 3
                    #     # turn_off_water_pump()
                    #     leftover_wash_duration = (wash_end_time-datetime.datetime.now()).total_seconds()
                    #     leftover_dry_duration = drying_duration
                    #     stateLbl.configure(text="Washing paused. Please close the door and press 'Continue' button.")
                # if status == 1:
                #     # turn_off_water_pump()
                #     status = 2
                #     stateLbl.configure(text="Drying in progress")
                #     # turn_motor(True)
                #     # turn_on_heated_fan()
            elif leftover_dry_duration > 0:
                status = 2
                # current_time = datetime.datetime.now()
                # Initially is while
                if (status == 2) and (datetime.datetime.now() < dry_end_time):    
                    leftover_dry_duration = (dry_end_time-datetime.datetime.now()).total_seconds()
                    if addition_dry_time:
                        stateLbl.configure(text="Additional drying in progress...  Left: " + str(int(leftover_dry_duration)) + " seconds")
                    else:
                        stateLbl.configure(text="Drying in progress...  Left: " + str(int(leftover_dry_duration)) + " seconds")
                # # Do ML here to check if is really dry
                drying_elapsed = drying_duration - leftover_dry_duration
                if ((leftover_dry_duration < 79) and (early_predict_status == False)):
                    early_predict_status = True
                    data = {'temp': [70], 'humidity': [0], 'fan_speed':[1], 'elapsed_time':[drying_elapsed]}
                    if prediction(data) == 1:
                        print("The syringes is predicted to be dry.")
                        early_completion = True
                    else:
                        print("The syringes is predicted to be wet.")

            if status == 3:
                leftover_wash_duration = (wash_end_time-datetime.datetime.now()).total_seconds()
                if leftover_wash_duration < 0:
                    leftover_wash_duration = 0
                leftover_dry_duration = (dry_end_time-datetime.datetime.now()).total_seconds()
                if leftover_dry_duration < 0:
                    leftover_dry_duration = 0
            else:
                leftover_wash_duration = (wash_end_time-datetime.datetime.now()).total_seconds()
                leftover_dry_duration = (dry_end_time-datetime.datetime.now()).total_seconds()
                if leftover_wash_duration < 1:
                    leftover_wash_duration = 0
                if leftover_dry_duration < 1:
                    leftover_dry_duration = 0
                if leftover_dry_duration <= 0 and leftover_wash_duration <= 0:
                    drying_elapsed = drying_duration
                    data = {'temp': [30], 'humidity': [70], 'fan_speed':[0], 'elapsed_time':drying_elapsed}
                    if ((prediction(data) == 0) and (addition_dry_time == False)):
                        addition_dry_time = True
                        stateLbl.configure(text="The syringes are still wet, adding additional 2 min to drying")
                        dry_end_time = datetime.datetime.now() + datetime.timedelta(seconds=120)
                        leftover_dry_duration = 120
                        window.after(200, controller)
                    stateLbl.configure(text="Process completed")
                    status = 0
                    leftover_wash_duration = 0
                    leftover_dry_duration = 0
                else:
                    if early_completion:
                        saved_time = drying_duration - drying_elapsed
                        stateLbl.configure(text="The syringes are predicted to be dry via Machine Learning (SVM)." + '\n' + "Early Termination, saved " + str(saved_time) + " seconds.")
                        write_drying_time(int(saved_time))            
                    else:
                        window.after(200, controller)
        else:
            stateLbl.configure(text="Please close the door.")
    else:
        stateLbl.configure(text="Paused")


def start_operation():
    global status
    global washing_duration
    global drying_duration
    global leftover_dry_duration
    global leftover_wash_duration
    global pause_status
    global wash_end_time
    global dry_end_time
    global early_completion
    global early_predict_status
    global drying_duration
    global addition_dry_time
    

    if status != 0:
        return
    if status == 0 and pause_status == False:
        # Do ML here to get washing and drying duration
        leftover_dry_duration = drying_duration
        leftover_wash_duration = washing_duration
        early_completion = False
        early_predict_status = False
        drying_duration = get_drying_time()
        addition_dry_time = False
        wash_end_time = datetime.datetime.now() + datetime.timedelta(seconds=washing_duration)
        dry_end_time = datetime.datetime.now() + datetime.timedelta(seconds=drying_duration) + datetime.timedelta(seconds=washing_duration) 
        controller()
        

def stop_operation():
    global status
    global leftover_dry_duration
    global leftover_wash_duration
    global stop_status
    global pause_status
    global early_completion
    global early_predict_status
    global addition_dry_time
    stateLbl.configure(text="Idle")
    status = 0
    # turn_off_water_pump()
    # turn_off_heated_fan()
    # turn_motor(False)
    early_completion = False
    stop_status = True
    pause_status = True
    early_predict_status = False
    leftover_wash_duration = 0
    leftover_dry_duration = 0
    addition_dry_time = False


def continue_operation():
    global pause_status
    global status
    global previous_status
    global pause_status
    global leftover_dry_duration
    global leftover_wash_duration
    global wash_end_time
    global dry_end_time
    wash_end_time = datetime.datetime.now() + datetime.timedelta(seconds=leftover_wash_duration)
    dry_end_time = datetime.datetime.now() + datetime.timedelta(seconds=leftover_dry_duration) + datetime.timedelta(seconds=leftover_wash_duration)
    if status == 3:
        pause_status = False
        status = previous_status
        controller()

    
def pause_operation():
    global pause_status
    global status
    global previous_status
    previous_status = status
    status = 3
    pause_status = True
    # turn_off_water_pump()
    # turn_off_heated_fan()
    stateLbl.configure(text="Paused")


def extra_wash_operation():
    global status
    global washing_duration
    global pause_status
    global leftover_wash_duration
    global wash_end_time
    global early_completion
    if status == 0 and pause_status == False:
        status = 1
        early_completion = False
        leftover_wash_duration = washing_duration
        wash_end_time = datetime.datetime.now() + datetime.timedelta(seconds=leftover_wash_duration)
        controller()
    status = 0
    

def extra_dry_operation():
    global status
    global drying_duration
    global addition_dry_time
    global leftover_wash_duration
    global pause_status
    global leftover_dry_duration
    global dry_end_time
    global early_completion
    global early_predict_status
    global wash_end_time
    status = 2
    controller()
    if status == 0 and pause_status == False:
        status = 2
        early_completion = False
        early_predict_status = False
        leftover_dry_duration = 120
        leftover_wash_duration = 0
        wash_end_time = datetime.datetime.now()
        dry_end_time = datetime.datetime.now() + datetime.timedelta(seconds=leftover_dry_duration) + datetime.timedelta(seconds=leftover_wash_duration)
        addition_dry_time = True
        controller()
    status = 0


def setCountDown(t):
    mins, secs = divmod(t, 60)
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    # timeLbl.config(text=timeformat)
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

statusLbl = Label(window, text="Status: ", fg="red", font=("Arial Bold", 14))

statusLbl.place(x=10, y=60)

stateLbl = Label(window, text="Idle", fg="red", font=("Arial Bold", 14))

stateLbl.place(x=85, y=60)

# timeLbl = Label(window, text="00:00", font=("Arial Bold", 15))

# timeLbl.place(x=120, y=100)

#secLbl = Label(window, text="00", font=("Arial Bold", 10))

#secLbl.place(x=320, y=300)
      
window.mainloop()

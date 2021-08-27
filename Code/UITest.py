# import tkinter as tk
from tkinter import *

master = Tk()

def my_mainloop():
    print("Hello World!")
    master.after(1000, my_mainloop)    

master.after(1000, my_mainloop)

master.mainloop()
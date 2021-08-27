import RPi.GPIO as GPIO
import time

def turn_on_water_pump():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)
    GPIO.output(23,GPIO.HIGH)
    print("Water Pump is on")

def turn_off_water_pump():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)
    GPIO.output(23,GPIO.LOW)
    print("Water Pump is on")


def turn_on_heated_fan():
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # GPIO.setup(21,GPIO.OUT)
    print("Heated fan is on")
    # GPIO.output(21,GPIO.HIGH)


def turn_off_heated_fan():
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # GPIO.setup(21,GPIO.OUT)
    print("Heated fan is off")
    # GPIO.output(21,GPIO.LOW)
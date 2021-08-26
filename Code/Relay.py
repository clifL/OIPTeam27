import RPi.GPIO as GPIO
import time

def turn_on_water_pump():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)
    print("Water Pump is on")
    GPIO.output(23,GPIO.HIGH)

def turn_off_water_pump():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)
    GPIO.output(23,GPIO.LOW)


def turn_on_heated_fan():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    print("Heated fan is on")
    GPIO.output(21,GPIO.HIGH)


def turn_off_heated_fan():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    print("Heated fan is off")
    GPIO.output(23,GPIO.LOW)
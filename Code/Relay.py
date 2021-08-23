import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("Pin 18 on")
GPIO.output(18,GPIO.HIGH)
time.sleep(10)
print("Pin 18 off")
GPIO.output(18,GPIO.LOW)
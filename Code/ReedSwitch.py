def magnetic_status():
	import RPi.GPIO as GPIO  # import the GPIO library
	import time
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	status = False
	# False means open
	if GPIO.input(8):
		status = False
	# True means closed
	else:
		status = True
	GPIO.cleanup()
	return status
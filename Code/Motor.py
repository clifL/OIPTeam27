def turn_motor(signal):
	import RPi.GPIO as GPIO
	import time
	servo_pin = 13
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo_pin,GPIO.OUT)
	# setup PWM process
	pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)
	if signal:
		pwm.start(7) # start PWM by rotating to 90 degrees
	else:
		pwm.start(12.0)
	time.sleep(0.5)
	pwm.ChangeDutyCycle(0) # this prevents jitter
	pwm.stop() # stops the pwm on 13
	GPIO.cleanup()


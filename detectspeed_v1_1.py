import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.IN)
last_time = time.time()
this_time = time.time()
RPM = 0

def EventsPerTime(channel):
	global RPM, this_time, last_time
	if GPIO.input(channel) > 0.5:
		this_time = time.time()
		RPM = (1/(this_time - last_time))*60
		print("Current RPM = ",RPM)
		last_time = this_time

GPIO.add_event_detect(7, GPIO.RISING, callback=EventsPerTime, bouncetime=1)

GPIO.output(11, True)
time.sleep(1)
for x in range(0,100):
	print("Last RPM = ",RPM)
	time.sleep(0.5)

GPIO.cleanup()
print("Done")

import RPi.GPIO as GPIO   #import the GPIO library
import time #import the time library

buzzer_pin = 22                   #set the buzzer pin variable to number 18
GPIO.setmode(GPIO.BCM)  #Use the Broadcom method for naming the GPIO pins
GPIO.setup(buzzer_pin, GPIO.OUT)  #Set pin 22 as an output pin

def buzz(pitch, duration):   #create the function "buzz" and feed it the pitch and duration)
 period = 1 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
 delay = period / 0.5     #calcuate the time for half of the wave
 cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency

 for i in range(cycles):    #start a loop from 0 to the variable "cycles" calculated above
   GPIO.output(buzzer_pin, True)   #set pin 18 to high
   time.sleep(delay)    #wait with pin 18 high
   GPIO.output(buzzer_pin, False)    #set pin 18 to low
   time.sleep(delay)    #wait with pin 18 low


while True:
	tone = raw_input("enter tone:")

	if(tone == "a"):
		buzz(911.0, 0.5)
	elif(tone == "s"):
		buzz(966.0, 0.5)
	elif(tone == "d"):
		buzz(1028.0, 0.5)
	elif(tone == "f"):
		buzz(1090.0, 0.5)
	elif(tone == "g"):
		buzz(1160.0, 0.5)
	elif(tone == "h"):
		buzz(1230.0, 0.5)
	elif(tone == "j"):
		buzz(1310.0, 0.5)
	elif(tone == "k"):
		buzz(1375.0, 0.5)
	elif(tone == "l"):
		buzz(1460.0, 0.5)
	else:
		print(tone)

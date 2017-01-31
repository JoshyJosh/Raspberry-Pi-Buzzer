import RPi.GPIO as GPIO   #import the GPIO library
import time #import the time library


buzzer_pin = 22                   #set the buzzer pin variable to number 18
GPIO.setmode(GPIO.BCM)#Use the Broadcom method for naming the GPIO pins
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

pitch = float(500)    #convert user input to a floating decimal

duration = float(0.01)  #convert user input to a floating decimal
for i in range(0,50):
	pitch += i * 1
	print(pitch)
	buzz(pitch, duration)  #feed the pitch and duration to the function, "buzz"

for i in range(0,50):
	pitch -= i
	print(pitch)
	buzz(pitch, duration)

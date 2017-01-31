# implementing buzzer with curses
import RPi.GPIO as GPIO   #import the GPIO library
import time #import the time library
import curses

from curses import wrapper

#curses init setup
#https://docs.python.org/3/howto/curses.html#curses-howto
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

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


foo = """while True:
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
"""
def main(stdscr):
	#Clear screen
	stdscr.clear()


	while True:
		c = stdscr.getch()
		stdscr.refresh()


		if(c == 60):
			buzz(448.0,0.02)
		elif(c == 121):
			buzz(474.0,0.02)
		elif(c == 120):
			buzz(503.0,0.02)
		elif(c == 99):
			buzz(534.0,0.02)
		elif(c == 118):
			buzz(566.0,0.02)
		elif(c == 98):
			buzz(601.0,0.02)
		elif(c == 110):
			buzz(637.0,0.02)
		elif(c == 109):
			buzz(676.0,0.02)
		elif(c == 44):
			buzz(718.0,0.02)
		elif(c == 46):
			buzz(761.0,0.02)
		elif(c == 45):
			buzz(809.0,0.02)
		elif(c == 32):
			buzz(858.0,0.02)
		elif(c == 97):
			buzz(911.0,0.02)
		elif(c == 115):
			buzz(966.0,0.02)
		elif(c == 100):
			buzz(1028.0,0.02)
		elif(c == 102):
			buzz(1090.0,0.02)
		elif(c == 103):
			buzz(1160.0,0.02)
		elif(c == 104):
			buzz(1230.0,0.02)
		elif(c == 106):
			buzz(1310.0,0.02)
		elif(c == 107):
			buzz(1375.0,0.02)
		elif(c == 108):
			buzz(1460.0,0.02)
		elif(c == 141):
			buzz(1550.0,0.02)
		elif(c == 135):
			buzz(1650.0,0.02)
		elif(c == 190):
			buzz(1750.0,0.02)
		elif(c == 113):
			buzz(1884.0,0.02)
		elif(c == 119):
			buzz(2008.0,0.02)
		elif(c == 101):
			buzz(2142.0,0.02)
		elif(c == 114):
			buzz(2280.0,0.02)
		elif(c == 116):
			buzz(2424.0,0.02)
		elif(c == 122):
			buzz(2585.0,0.02)
		elif(c == 117):
			buzz(2750.0,0.02)
		elif(c == 105):
			buzz(2935.0,0.02)
		elif(c == 111):
			buzz(3128.0,0.02)
		elif(c == 112):
			buzz(3335.0,0.02)
		elif(c == 161):
			buzz(3560.0,0.02)
		elif(c == 145):
			buzz(3820.0,0.02)
		elif(c == 49):
			buzz(4082.0,0.02)
		else:
			stdscr.clear()
			stdscr.addstr(0, 0, str(c))


	stdscr.getkey()

wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

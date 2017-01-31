# Raspberry Pi Buzzer

This is a project to see how python can be used with a piezo buzzer and a Raspberry Pi. Originally I wanted a responsive (and slightly annoying) instrument with the pi. Sadly keydown events don't work correctly (stuttering sound).

## buzz-tuner.py
A program I used to check what values create certain tones

## buzz.py
A simple buzzer pitch loop with a linear addition and subtraction of pitch

## buzz-keydown.py
A program which asks for input and buzzes a keyboard calibrated sound (similar to buzz-tuner.py)

## buzz-keydown1.py
A program that listens for keyboard input and buzzes the set up keys. Sadly pressing and holding the key makes a stuttered sound (might need to shorten the the buzz duration). Used curses to try to get a keydown event to work.

original buzzer schematics and code: http://domoticx.com/raspberry-pi-buzzer-speaker-via-gpio/

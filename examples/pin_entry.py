## Imports, for time delays, controlling Explorer HAT and GPIO pin 18
## for the piezo buzzer.

import time
import explorerhat as eh
import RPi.GPIO as GPIO

## Sets up GPIO pin 18 as a PWM output with freq. of 400 Hz.

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 400)

## Lists for the correct PIN and an empty one to add digits to.

correct_pin = [1,2,3,4]
pin = []

## Function to add a digit pressed on EHP cap. touch to our pin list.

def add_to_pin(channel, event):
	if channel > 4:  ## Only use channels 1-4
		return
	if event == 'press':
		global pin
		pin.append(channel)
		eh.light[channel-1].on()  ## Blink the corresponding LED
		time.sleep(0.05)
		eh.light[channel-1].off()

## We use a try, except, finally to run our code and catch exceptions.

try:

	## The while True loop keeps the program running until control-c breaks out.

	while True:
		while len(pin) < 4:  ## Keeping adding until 4 digits added
			eh.touch.pressed(add_to_pin)
			time.sleep(0.05)
		if pin == correct_pin:  ## Runs with correct PIN
			print 'PIN correct!'
			for i in range(5):  ## Blinks LEDs and buzzes 5 times
				buzzer.ChangeFrequency(400)  ## High frequency
				buzzer.start(50)
				eh.output.one.on()  ## Turns green LED on
				time.sleep(0.1)
				buzzer.stop()
				eh.output.one.off()  ## Turns green LED off
				time.sleep(0.1)
		else:  ## Runs with incorrect PIN
			print 'PIN incorrect! Try again.'
			for i in range(5):  ## Similar to previous block
				buzzer.ChangeFrequency(50)  ## Low frequency
				buzzer.start(50)
				eh.output.two.on()  ## Turns red LED on
				time.sleep(0.1)
				buzzer.stop()
				eh.output.two.off()  ## Turns red LED off
				time.sleep(0.1)
		pin = []  ## Resets the list after 4 digits have been entered

## Catches control-c.

except KeyboardInterrupt:
	pass

## Catches any other exceptions.

except Exception:
	pass

## Clean up GPIO before exit.

finally:
	GPIO.cleanup()

import time
import explorerhat as eh
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 400)

correct_pin = [1,2,3,4]
pin = []

def add_to_pin(channel, event):
	if channel > 4:
		return
	if event == 'press':
		global pin
		pin.append(channel)
		eh.light[channel-1].on()
		time.sleep(0.05)
		eh.light[channel-1].off()

try:
	while True:
		while len(pin) < 4:
			eh.touch.pressed(add_to_pin)
			time.sleep(0.05)
		if pin == correct_pin:
			print 'PIN correct!'
			for i in range(5):
				buzzer.ChangeFrequency(400)
				buzzer.start(50)
				eh.output.one.on()
				time.sleep(0.1)
				buzzer.stop()
				eh.output.one.off()
				time.sleep(0.1)
		else:
			print 'PIN incorrect! Try again.'
			for i in range(5):
				buzzer.ChangeFrequency(50)
				buzzer.start(50)
				eh.output.two.on()
				time.sleep(0.1)
				buzzer.stop()
				eh.output.two.off()
				time.sleep(0.1)
		pin = []

except KeyboardInterrupt:
	pass

except Exception:
	pass

finally:
	GPIO.cleanup()

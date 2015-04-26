#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Read the tutorial here:
## https://github.com/sandyjmacdonald/pimoroni_learning_materials/blob/master/lights_out.md

import explorerhat
import random
import time

num_moves = 0

def toggle_light(channel, event):
	if channel > 4:
		return
	if event == 'press':
		global num_moves
		num_moves += 1
		explorerhat.light[channel-1].toggle()
		if channel == 1:
			explorerhat.light[channel].toggle()
		elif channel == 4:
			explorerhat.light[channel-2].toggle()
		else:
			explorerhat.light[channel-2].toggle()
			explorerhat.light[channel].toggle()
		print 'You have taken %i moves so far. Keep going!' % num_moves

print 'Press a button to toggle its LED and adjacent LEDs on/off'
light_nums = random.sample(range(0,4), random.randint(1,4))

for l in light_nums:
	explorerhat.light[l].toggle()

while len(light_nums) > 0:
	explorerhat.touch.pressed(toggle_light)
	light_nums = [i for i in range(0,4) if explorerhat.light[i].is_on()]
	time.sleep(0.05)

if len(light_nums) == 0:
	print 'Congratulations! You won in %i moves!' % num_moves
	explorerhat.light.stop()
	for i in range(0,4) + range(0,3)[::-1] + range(1,4):
		explorerhat.light[i].on()
		time.sleep(0.25)
		explorerhat.light[i].off()

explorerhat.pause()

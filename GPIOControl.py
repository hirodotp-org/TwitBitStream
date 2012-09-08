#!/usr/bin/env python

import RPi.GPIO as GPIO

class Controller:
	"""
	GPIO Controller Class
	"""

	# see http://elinux.org/RPi_Low-level_peripherals for more information
	validPins = (7, 11, 12, 13, 15, 16, 18, 22)

	def __init__(self, pins = validPins):
		# set the mode to count the pins on the board, not the broadcom bin numbering
		GPIO.setmode(GPIO.BOARD)
		for pin in self.validPins:
			GPIO.setup(pin, GPIO.OUT)
			# Turn pin to low
			GPIO.output(pin, GPIO.LOW)

	def high(self, pin):
		if not self.isValidPin(pin):
			return False

		# Turn pin to high and return True
		GPIO.output(pin, GPIO.HIGH)
		return True

	def low(self, pin):
		if not self.isValidPin(pin):
			return False

		# Turn pin to low
		GPIO.output(pin, GPIO.LOW)
		return True

	def isValidPin(self, pin):
		try:
			self.validPins.index(pin)
		except:
			return False

		# pin was valid
		return True


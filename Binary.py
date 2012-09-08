#!/usr/bin/env python

import binascii

class BinaryHandler:
	def __init__(self, bigEndian = False):
		self.binary = []
		self.bigEndian = bigEndian

	def push(self, s):
		binary = bin(int(binascii.hexlify(s), 16)).replace('b', '')
		i = 0
		x = 8
		while x <= len(binary):
			try:
				ch = binary[i:x]
				self.binary.append(ch)
				i = x
				x += 8
			except:
				break

	def pop(self):
		"""
		return a binary character with endianess taken into consideration.
		"""
		r = self.binary.pop(0)
		if self.bigEndian:
			return r
		return r[::-1]


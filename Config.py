#!/usr/bin/env python

import ConfigParser

class Parser:
	def __init__(self):
		self.config = ConfigParser.RawConfigParser()

	def load(self, file):
		self.config.read(file)

	def get(self, section, key):
		self.config.get(section, key)


#!/usr/bin/env python -u

import json
import time
import sys
import traceback
import ConfigParser

from twitter.Stream import TwitterStreamClient, CustomStreamListener
from Binary import BinaryHandler
from GPIOControl import Controller
from Config import Parser
from Daemon import Daemon

LOGFILE = "/tmp/twitbitstream.log"
PIDFILE = "/tmp/twitbitstream.pid"

def printLog(msg):
	f = open(LOGFILE, 'a')
	f.write(str(time.time()) + " " + str(msg))
	f.close()

class TwitBitListener(CustomStreamListener):
	def __init__(self, pins, pinTimeout = 0.1):
		super(TwitBitListener, self).__init__()
		self.b = BinaryHandler()
		self.gpio = Controller()
		self.pins = pins
		self.pinTimeout = pinTimeout
		self.listening = 0

	def on_data(self, data):
		# skip first two feed messages
		if self.listening > 1:
			if self.listening == 2:
				printLog("Twitter stream initialized, waiting for data.")
				self.listening += 1

			if "text" in data:
				tweet = json.loads(data).get("text")
				self.b.push(tweet)
				while True:
					try:
						ch = self.b.pop()
					except:
						break
	
					i = 0
					for c in ch:
						pin = int(self.pins[i])
						if c == "1":
							self.gpio.high(int(pin))
						elif c == "0":
							self.gpio.low(int(pin))
						i += 1

					time.sleep(self.pinTimeout)

				# reset pins to low state
				for pin in self.pins:
					self.gpio.low(int(pin))
		else:
			self.listening += 1

class TwitBitStream(Daemon):
	"""
	Twitter to GPIO controller.
	"""
	def setOAuthInfo(self, ck, cs, at, ats, pins):
		self.ck = ck
		self.cs = cs
		self.at = at
		self.ats = ats
		self.pins = pins

	def run(self):
		"""
		Override the daemon run() method with what to actually do.
		"""
		listener = TwitBitListener(self.pins)
		self.stream = TwitterStreamClient(self.ck, self.cs, self.at, self.ats)
		self.stream.setListener(listener)
		self.stream.login()
		self.stream.stream()

if __name__ == "__main__":
	try:
		if sys.argv[1] == "--kill":
			t = TwitBitStream('/tmp/twitbitstream.pid')
			t.stop()
			sys.exit(0)
			
		config = ConfigParser.RawConfigParser()
		config.read(sys.argv[1])
	
		consumerKey = config.get('oauth', 'consumerKey')
		consumerSecret = config.get('oauth', 'consumerSecret')
		accessToken = config.get('oauth', 'accessToken')
		accessTokenSecret = config.get('oauth', 'accessTokenSecret')
	
		pins = []
		pins.append(config.get('gpio', 'bit0'))
		pins.append(config.get('gpio', 'bit1'))
		pins.append(config.get('gpio', 'bit2'))
		pins.append(config.get('gpio', 'bit3'))
		pins.append(config.get('gpio', 'bit4'))
		pins.append(config.get('gpio', 'bit5'))
		pins.append(config.get('gpio', 'bit6'))
		pins.append(config.get('gpio', 'bit7'))

		t = TwitBitStream(PIDFILE)
		t.setOAuthInfo(consumerKey, consumerSecret, accessToken, accessTokenSecret, pins)
		t.start()
		sys.exit(0)
	except Exception, e:
		f = open(LOGFILE, 'a')
		f.write('-'*60 + '\n')
		traceback.print_exc(file=f)
		f.close()


#!/usr/bin/env python

import time
import tweepy

class CustomStreamListener(tweepy.StreamListener):
	pass

class TwitterStreamClient:
	def __init__(self, ck, cs, at, ats):
		self.consumerKey = ck
		self.consumerSecret = cs
		self.accessToken = at
		self.accessTokenSecret = ats
		self._stream = None
		self.auth = None
		self.listener = None

	def setListener(self, listener):
		self.listener = listener

        def login(self):
                self.auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
                self.auth.set_access_token(self.accessToken, self.accessTokenSecret)
		self._stream = tweepy.streaming.Stream(self.auth, self.listener)

	def stream(self):
		self._stream.userstream()


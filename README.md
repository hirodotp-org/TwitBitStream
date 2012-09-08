TwitBitStream
================

Twitter to Raspberry Pi GPIO pins

Taking advantage of the GPIOs on the RPi to relay twitter data in binary.


Requirements
============
* Raspberry Pi.
* Some LEDs to wire up to your GPIOs.
* python-rpi.gpio 0.3.1a-1 or later
* tweepy 2.x branch available at https://github.com/tweepy/tweepy.
* Twitter oauth streaming API access (see the "Twitter Application Access" section below).


Raspberry Pi GPIOs
==================
First you need to hook up something to trigger on the GPIOs.  You can get a list of RPi GPIOs
from http://elinux.org/RPi_Low-level_peripherals.  Next define the GPIOs you want to use for each
bit to be transmitted over, a HIGH signal indicates 1, a LOW indicates 0, you must define all
bits in the TwitBitStream.conf with a GPIO pin to use, however, you may re-use the same GPIO pin
for multiple bits.


Twitter Application Access
==========================
You will need to visit https://dev.twitter.com and sign in with your twitter username and password.
Once you're logged in, you will need to go to the "Create an app" link on the main page.
Provide a name, description, website (this can be just about anything that is a valid url), agree
to the terms of service, fill out the captcha and create your project.

Once you have your project created, you need to create your access tokens.
This is done by going to the project page for your newly created project (under My Projects),
scrolling down to the bottom of the page and clicking the button to create your access token.

Finally, copy down your Consumer Key, Consumer Secret, Access Token and Access Token Secret.
Define them in the TwitBitStream.conf file and you should be good to go with twitter.



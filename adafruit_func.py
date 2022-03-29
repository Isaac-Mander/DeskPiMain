


import time
import Adafruit_IO
import adafruit_var as adv
import RPi.GPIO as GPIO

#Adafruit IO setup
from Adafruit_IO import *
#Replace with your adafruit username and key
aio = Client(adv.username,adv.key)

def feed_setup(feed_name):
    """ A function for setting up an adafruit io feed"""
    try: # if we have a 'digital' feed
        feed_info = aio.feeds(feed_name)
        print("FEED",feed_name,"FOUND")
    except RequestError: # create a digital feed
        feed = Feed(name={feed_name})
        feed_info = aio.create_feed(feed)
        print("FEED",feed_name,"CREATED")
    return feed_info

def check_rgb_feed(feed_to_check):
    val = aio.receive(feed_to_check.key).value
    if val == "1" or val == "4" or val == "5":
        red_val = GPIO.LOW
    else:
        red_val = GPIO.HIGH
    if val == "2" or val == "4" or val == "6":
        green_val = GPIO.LOW
    else:
        green_val = GPIO.HIGH
    if val == "3" or val == "5" or val == "6":
        blue_val = GPIO.LOW
    else:
        blue_val = GPIO.HIGH
    
    if val == "0":
        red_val = GPIO.LOW
        green_val = GPIO.LOW
        blue_val = GPIO.LOW
    
    if val == "*" or val == "#":
        red_val = GPIO.HIGH
        green_val = GPIO.HIGH
        blue_val = GPIO.HIGH

    #Return RGB Values
    return red_val, green_val, blue_val

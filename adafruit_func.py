# .gitignore 


import time
import Adafruit_IO
import adafruit_var as adv

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
        feed = Feed(name=feed_name)
        feed_info = aio.create_feed(feed)
        print("FEED",feed_name,"CREATED")
    return feed_info



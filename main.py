""" 
This is the main program for my desk pi project. This program is for the pi that sits under my desk dirrectly controlling my desk features
Currently it controls:
1. RGB under desk lights
2. Gathers data from my desk box arduino (e.g. switch controls, volume knob)

Features to add
1. Voice recognition
2. Enviroment Monitors (e.g. temperature)
"""


if __name__ == '__main__':

    #Function declaration



    #Library Setup

    import time
    import serial
    import Adafruit_IO
    import RPi.GPIO as GPIO

    import adafruit_var as adv
    import adafruit_func as adaf


    #Adafruit IO setup
    from Adafruit_IO import *
    #Replace with your adafruit username and key
    aio = Client(adv.username,adv.key)

    #Setting up feeds
    #This will create feeds automatically if not present

    #Under Desk RGB
    under_desk_rgb_feed = adaf.feed_setup("db-rgb")

    print("Adafruit IO set up")

    #Set up serial communication
    #Arduino Control Panel Desk Box
    ard_box = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ard_box.reset_input_buffer()

    #Setting up GPIO pins
    GPIO.setmode(GPIO.BOARD)
    ##GPIO.setmode(GPIO.BCM)

    #GPIO CONST
    #Under desk rgb
    UD_RGB_R_RELAY = 0
    UD_RGB_G_RELAY = 0
    UD_RGB_B_RELAY = 0

    #Main Loop
    running = True
    while running:

        #Check Serial Devices
        #Ardunio Box
        if ard_box.in_waiting > 0:
            ard_info = ard_box.readline().decode('utf-8').rstrip()

            #Arduino Box controls RGB,Music/Sound

            #RGB is switch 1 of box
            if ard_info == "1H":
                #RGB ON
                print("RGB ON")
            elif ard_info == "1L":
                #RGB OFF
                print("RGB OFF")





        #Pause of 0.5 sec as no need for faster reaction times
        time.sleep(0.5)
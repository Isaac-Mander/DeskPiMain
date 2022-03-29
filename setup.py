""" This is a script designed to speed up the process of getting setup with Desk Pi"""

#Library Crap
import subprocess
import sys


def install(package):
    """ Function for installing libraries"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        print("Error installing",package)

#Install Adafruit
install("adafruit-io")

#Add important adafruit files
try:
    ada_var = open("adafruit_var.py", "x")
except FileExistsError:
    print("adafruit_var already exists")

print("Setup Done :)")
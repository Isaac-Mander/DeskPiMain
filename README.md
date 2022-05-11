# DeskPiMain
This is the repo for my DeskPiProject. Feel free to copy/improve my code I have uploaded here.


Short stroy: DeskPi is a group of seperate diy home automation projects licked together by a signle raspberry pi, e.g. pi A collects room temperature data from pi B to provide a centeral control panel. It involves anything from auto shutting curtins to under desk rgb lights to room temperature readouts. Its called DeskPi because that centeral server sits under my desk.


It contains all my code in one place, so there may be repeats in other more focused repositorys. Each project is labeled and organised into seperate folders with a README describing it. Hopefully my descriptions are good enough and allow you to understand and use any of my code/designs.


adafruit_func.py contains a bunch of functions I have made that makes using systems like adafruit_io easier than working with the raw functions. Feel free to add to it if you feel I have missed something or if there is something you may see as useful.


setup.py will install all libraries and dependancys required to use my code. 

**IN ORDER FOR MY CODE TO WORK YOU MUST EDIT THE LINE aio = Client(adv.username,adv.key) AND REPLACE WITH USERNAME/KEY WITH YOUR ADAFRUIT_IO INFO RESPECTIVLY. If you want to be fancy create a file named adafruit_var.py and place your variables in there and git ignore it so you don't have any key leaks. (key leaks require you to update your key every time you commit your code to github)** You will want to do this before commiting to this respotory for the aformentioned reason.

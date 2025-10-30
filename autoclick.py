# --- AUTOCLICKER PROGRAM --- #
# --- Nathan Fairweather  --- #
# --- RUN PROGRAM TO ACTIVATE --- #

# Import Libraries
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener
from time import sleep
from threading import Thread

# Variables #
# DELAY TABLE #
# .1 = 10 CPS #
# .05 = 20 CPS #
# .01 = 100 CPS #
delay = .01 # Adjust to your liking, at your own risk
# Controller
mouse = Controller()

# Class for the autoclicker
class AutoClicker(Thread):
    # Vars
    clicking = False

    def run(self):
        while True:
            if AutoClicker.clicking:
                mouse.click(Button.left)
            # Delay the clicking
            sleep(delay)

# Handler from the keyboard to turn the clicker on and off
def keypress(key):
    if key == KeyCode(char="t"): # This is the character used to turn the autoclicker on and off
        AutoClicker.clicking = not AutoClicker.clicking

# Start the autoclicker thread
AutoClicker().start()

with Listener(on_press=keypress) as listener:
    listener.join()
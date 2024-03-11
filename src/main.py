import hid
import constants as CONST
from constants import *

import time
import numpy as np
import matplotlib.pyplot as plt

#Device Imports
import piplates.DAQC2plate as DAQ
import RPi.GPIO as GPIO


#Stepper Motor Configuration
PUL1 = 17
DIR1 = 27
ENA1 = 22

PUL2 = 6
DIR2 = 13
ENA2 = 26

PUL3 = 4
DIR3 = 5
ENA3 = 12

PUL4 = 16
DIR4 = 20
ENA4 = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(PUL1, GPIO.OUT)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(ENA1, GPIO.OUT)

GPIO.setup(PUL2, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(ENA2, GPIO.OUT)

GPIO.setup(PUL3, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(ENA3, GPIO.OUT)

GPIO.setup(PUL4, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(ENA4, GPIO.OUT)


delay = 0.001


def moveBy(motor, duration, direction):
    
    if motor == 0:
        PUL = PUL1
        DIR = DIR1
        ENA = ENA1
    
    if motor == 1:
        PUL = PUL2
        DIR = DIR2
        ENA = ENA2
      
    if motor == 2:
        PUL = PUL3
        DIR = DIR3
        ENA = ENA3
        
    if motor == 3:
        PUL = PUL4
        DIR = DIR4
        ENA = ENA4
    
    GPIO.output(ENA, GPIO.HIGH)
    
    time.sleep(.1)
    
    if direction == 1:
        GPIO.output(DIR, GPIO.LOW)
        
    elif direction == -1:
        GPIO.output(DIR, GPIO.HIGH)
    
    else:
        print("ERROR: Direction Unknown")
        return
   
    for x in range(duration): 
        GPIO.output(PUL, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        time.sleep(delay)
    #GPIO.output(ENA, GPIO.LOW)
    
    time.sleep(.1)
    return



def main():
    current_motor = 1
    
    # Open the Vaydeer multimedia volume controller knob.
    with hid.Device(ID_VENDOR, ID_PRODUCT) as dev:
        # Iterate until the user interrupts.
        while True:
            # Block until data is available, and then get the data.
            data = dev.read(SIZE_PACKET)

            # Check whether data was received, and check whether the data comes from a consumer control function.
            if data and data[IDX_REPORT] == ID_CONSUMER_CTRL:
                # Match the consumer control function.
                if data[IDX_FUNCTION] == CONST.FN_VOLUME_DECREMENT:
                    moveBy(current_motor, duration=10, direction=-1)
                    
                elif data[IDX_FUNCTION] == CONST.FN_VOLUME_INCREMENT:
                    moveBy(current_motor, duration=10, direction=1)
                    
                elif data[IDX_FUNCTION] == CONST.FN_MUTE:
                    print("Mute")

                elif data[IDX_FUNCTION] == CONST.FN_PLAY_PAUSE:
                    print("Play/Pause")
                    
                elif data[IDX_FUNCTION] == CONST.FN_EJECT:
                    print("Eject")
                    
                elif data[IDX_FUNCTION] == CONST.FN_STOP:
                    print("Stop")
                    
                elif data[IDX_FUNCTION] == CONST.FN_SCAN_PREVIOUS_TRACK:
                    print("Scan Previous Track")
                    
                elif data[IDX_FUNCTION] == CONST.FN_SCAN_NEXT_TRACK:
                    current_motor = (current_motor + 1) % 4
                    print(f"Current Motor: {current_motor}")
                    


if __name__ == "__main__":
    main()

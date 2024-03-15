import RPi.GPIO as GPIO
from enum import Enum
import time


class Pin(Enum):
    """Define the pins for controlling stepper motors."""
    # Motor Zero
    PUL0 = 17  # PULSE
    DIR0 = 27  # DIRECTION
    ENA0 = 22  # ENABLE
    # Motor One
    PUL1 = 6
    DIR1 = 13
    ENA1 = 26
    # Motor Two
    PUL2 = 4
    DIR2 = 5
    ENA2 = 12
    # Motor Three
    PUL3 = 16
    DIR3 = 20
    ENA3 = 21


class Direction(Enum):
    """Define the directions in which the stepper motors can move."""
    FORWARDS = GPIO.HIGH
    BACKWARDS = GPIO.LOW


# The pulse delay is a measured in seconds.
PUL_DELAY = 0.001


class Motor():
    def __init__(self, pul_pin: int, dir_pin: int, ena_pin: int):
        """
        The object represents a stepper motor.
        
        :param pul_pin: Pulse Pin
        :param dir_pin: Direction Pin
        :param ena_pin: Enable Pin
        """

        self.pul_pin = pul_pin
        self.dir_pin = dir_pin
        self.ena_pin = ena_pin
        
    def step(self, direction: Direction, duration: int = 10) -> None:
        """Move the stepper motor forwards or backwards."""
        
        # Enable the motor.
        GPIO.output(self.ena_pin, GPIO.HIGH)
        time.sleep(PUL_DELAY)
        
        # Set the direction.
        GPIO.output(self.dir_pin, direction.value)
        time.sleep(PUL_DELAY)
        
        # Move the motor.
        for idx in range(duration):
            # Propage the rising edge.
            GPIO.output(self.pul_pin, GPIO.HIGH)
            time.sleep(PUL_DELAY)
            
            # Propage the falling edge.
            GPIO.output(self.pul_pin, GPIO.LOW)
            time.sleep(PUL_DELAY)


MOTORS = [
    Motor(Pin.PUL0.value, Pin.DIR0.value, Pin.ENA0.value),
    Motor(Pin.PUL1.value, Pin.DIR1.value, Pin.ENA1.value),
    Motor(Pin.PUL2.value, Pin.DIR2.value, Pin.ENA2.value),
    Motor(Pin.PUL3.value, Pin.DIR3.value, Pin.ENA3.value)
]
"""Let the list maintain an instance of each stepper motor."""

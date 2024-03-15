import hid
import RPi.GPIO as GPIO

from vaydeer import *
from motor import *


def setup_gpio():
    """Configure the GPIO pins for controlling stepper motors."""
    
    # Identify pins according to the Broadcom SOC channel.
    GPIO.setmode(GPIO.BCM)

    # Get a list of all pins, and configure them to output.
    GPIO.setup([pin.value for pin in Pin], GPIO.OUT)


def main():
    # Maintain the current motor index in the list.
    motor_idx = 0
    # Indicate whether motor control is enabled.
    is_enabled = True
    
    # Open the Vaydeer multimedia volume controller knob.
    with hid.Device(ID_VENDOR, ID_PRODUCT) as dev:
        # Iterate until the user interrupts.
        while True:
            # Block until data is available, and then get the data.
            data = dev.read(SIZE_PACKET)

            # Check whether data was received, and check whether the data comes from a consumer control function.
            if data and data[IDX_REPORT] == ID_CONSUMER_CTRL:
                # Match the consumer control function.
                if data[IDX_FUNCTION] == FN_VOLUME_DECREMENT:
                    if is_enabled:
                        MOTORS[motor_idx].step(Direction.FORWARDS)
                    
                elif data[IDX_FUNCTION] == FN_VOLUME_INCREMENT:
                    if is_enabled:
                        MOTORS[motor_idx].step(Direction.BACKWARDS)
                    
                elif data[IDX_FUNCTION] == FN_MUTE:
                    is_enabled = not is_enabled
                    print(f"Motor Control: {'Enabled' if is_enabled else 'Disabled'}")
                    
                elif data[IDX_FUNCTION] == FN_SCAN_PREVIOUS_TRACK:
                    motor_idx = (motor_idx - 1) % len(MOTORS)
                    print(f"Current Motor: {motor_idx + 1}")
                    
                elif data[IDX_FUNCTION] == FN_SCAN_NEXT_TRACK:
                    motor_idx = (motor_idx + 1) % len(MOTORS)
                    print(f"Current Motor: {motor_idx + 1}")
                    


if __name__ == "__main__":
    try:
        # Configure the GPIO pins for output.
        setup_gpio()
        
        # Enter the event loop.
        main()
        
    finally:
        # Mitigate the risk of damage by resetting all configured pins to input mode.
        # This only cleans up pins configured in this program.
        GPIO.cleanup()

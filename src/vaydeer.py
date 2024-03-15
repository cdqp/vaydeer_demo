ID_VENDOR, ID_PRODUCT = 0x0e6a, 0x0305
"""Vaydeer Multimedia Volume Controller Knob (0E6A:0305)"""

SIZE_PACKET = 3
"""The size of the HID packet in bytes."""

IDX_REPORT = 0
"""The index of the report ID, which is one byte."""
IDX_FUNCTION = 1
"""The index of the function ID, which is one byte."""

ID_CONSUMER_CTRL = 2
"""The report ID associated the consumer control functions."""

FN_SCAN_NEXT_TRACK = 0x01
"""HID Usage Tables, Consumer Page (0x0C), B5, One-Shot Control"""
FN_SCAN_PREVIOUS_TRACK = 0x02
"""HID Usage Tables, Consumer Page (0x0C), B6, One-Shot Control"""
FN_STOP = 0x04
"""HID Usage Tables, Consumer Page (0x0C), B7, One-Shot Control"""
FN_EJECT = 0x08
"""HID Usage Tables, Consumer Page (0x0C), B8, One-Shot Control"""
FN_PLAY_PAUSE = 0x10
"""HID Usage Tables, Consumer Page (0x0C), CD, One-Shot Control"""
FN_MUTE = 0x20
"""HID Usage Tables, Consumer Page (0x0C), E2, On/Off Control"""
FN_VOLUME_INCREMENT = 0x40
"""HID Usage Tables, Consumer Page (0x0C), E9, Re-Trigger Control"""
FN_VOLUME_DECREMENT = 0x80
"""HID Usage Tables, Consumer Page (0x0C), EA, Re-Trigger Control"""

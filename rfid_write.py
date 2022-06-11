'''
This module enables register data on RFID
However, this only runs on Raspberry pi.
Hence, checking pylint on import module is disabled.
'''
from RPi import GPIO  # pylint: disable-msg=E0401
from mfrc522 import SimpleMFRC522  # pylint: disable-msg=E0401

reader = SimpleMFRC522()

try:
    text = input('New data:')
    print("Now place your tag to write")
    reader.write(text)
    print("Written")
finally:
    GPIO.cleanup()

from time import sleep
import sys
import RPi.GPIO as GPIO

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print(id)
        print(text)
        sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
    raise

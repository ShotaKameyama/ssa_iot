'''
This module will detect the RFID, decode and send
RFID data to controller.
'''
from time import sleep
from RPi import GPIO
from mfrc522 import SimpleMFRC522
from paho.mqtt import publish
import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig
config = BaseConfig(parse_config('./config/config.yml'))

reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        rfid_id, rfid_body = reader.read()
        print(rfid_id)
        print(rfid_body)
        publish.single(
            config.client_camera.publish.controller,
            payload=rfid_body,
            hostname=config.mqtt.host,
            port=int(config.mqtt.port),
            protocol=mqtt.MQTTv311,
            qos=config.mqtt.qos,
            auth={
                'username': config.client_camera.user,
                'password': config.client_camera.password})
        print("published to: " + config.client_camera.publish.controller)
        print("payload: " + rfid_body)
        sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
    raise

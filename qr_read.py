'''
This module will detect the QR code, decode and send
QR code data to controller.
'''
import time
from paho.mqtt import publish
import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig
from module.camera import capture_qr_code
config = BaseConfig(parse_config('./config/config.yml'))

qr = capture_qr_code()

if qr:
    print("QR code detected...")
    time.sleep(5)
    print("Send a message to controller")
    publish.single(
        config.client_camera.publish.controller,
        payload=qr,
        hostname=config.mqtt.host,
        port=int(config.mqtt.port),
        qos=config.mqtt.qos,
        protocol=mqtt.MQTTv311,
        auth={
            'username': config.client_camera.user,
            'password': config.client_camera.password})

    print("published to: " + config.client_camera.publish.controller)
    print("payload: " + qr)

"""
iot_publish_doorlock.py with auth and tls
"""

import sys
from paho.mqtt import publish
import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig

config = BaseConfig(parse_config('./config/config.yml'))
CERT_PATH = 'certs/ca.crt'

if len(sys.argv) == 1:
    # Missing arguments
    print("Missing arguments. Usage: iot_publish_doorlock.py <Request>")

if sys.argv[1] in ("Open", "Close"):
    # Door Open / Close request
    print(sys.argv[1])
    tls = {'ca_certs': CERT_PATH}
    publish.single(
        config.controller.publish.lock,
        payload=sys.argv[1],
        qos=config.mqtt.qos,
        hostname=config.mqtt.host,
        # TLS port number
        port=8883,
        protocol=mqtt.MQTTv311,
        auth={
            'username': config.controller.user,
            'password': config.controller.password
        }, tls=tls)
    # Publish MQTT message
    print("published to: " + config.controller.publish.lock)
    print("payload: " + sys.argv[1])

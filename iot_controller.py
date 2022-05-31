import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig

config =  BaseConfig(parse_config('./config/config.yml'))
door_messages = ["b'Door Opened'","b'Door Closed'"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(
        config.controller.subscribe.lock)

def on_message(client, userdata, msg):
    req = str(msg.payload)
    print(msg.topic + " " + req)
    if req in door_messages:
        client.publish(
            config.controller.publish.camera,
            "Capture",
            config.mqtt.qos)

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.username_pw_set(
    config.controller.user,
    config.controller.password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    config.mqtt.host,
    int(config.mqtt.port),
    config.mqtt.keep_alive)
client.loop_forever()
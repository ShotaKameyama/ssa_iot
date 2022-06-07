'''
This file works as a controller that supports the following:
1. When door lock is opened/closed, controller orders camera to take a picture.
'''
from pyaml_env import parse_config, BaseConfig
from module.mqtt_connector import connect_mqtt, print_connect, print_message

config = BaseConfig(parse_config('./config/config.yml'))
door_messages = ["b'Door Opened'", "b'Door Closed'"]


def on_connect(client, userdata, flags, rc):
    '''
    when connected to the MQTT client,
    subscribe door lock message.
    '''
    print_connect(client, userdata, flags, rc)
    client.subscribe(
        config.controller.subscribe.lock)
    print("Subscribed to: " + config.controller.subscribe.lock)


def on_message(client, userdata, msg):
    '''
    when message delivered on MQTT,
    Show client, userdata and messages.
    And publish a message to camera to capture a picture,
    when the door message is either Door Opened/Closed.
    '''
    req = str(msg.payload)
    print_message(client, userdata, msg)
    if req in door_messages:
        client.publish(
            config.controller.publish.camera,
            "Capture",
            config.mqtt.qos)


if __name__ == "__main__":
    connect_mqtt(
        config.controller.user,
        config.controller.password,
        on_connect,
        on_message
    )

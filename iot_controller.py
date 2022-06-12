'''
This file works as a controller that supports the following:
1. When door lock is opened/closed, controller orders camera to take a picture.
'''
from pyaml_env import parse_config, BaseConfig
from module.mqtt_connector import connect_mqtt, print_connect, print_message

config = BaseConfig(parse_config('./config/config.yml'))
door_messages = ["Door Opened", "Door Closed"]
# Controller subscribe topics with QoS configuration
topic = [(config.controller.subscribe.lock, config.mqtt.qos),
         (config.controller.subscribe.camera, config.mqtt.qos)]


def on_connect(client, userdata, flags, rc):
    '''
    when connected to the MQTT client,
    subscribe door lock message.
    '''
    print_connect(client, userdata, flags, rc)
    client.subscribe(topic)
    print("Subscribed to: " + config.controller.subscribe.lock +
          " & " + config.controller.subscribe.camera)


def on_message(client, userdata, msg):
    '''
    when message delivered on MQTT,
    Show client, userdata and messages.
    And publish a message to camera to capture a picture,
    when the door message is either Door Opened/Closed.
    '''
    # Decode MQTT payload message
    req = str(msg.payload.decode("utf-8")).strip()
    print_message(client, userdata, msg)
    print(req)
    # When receive Door message, publish a message to camera to capture a picture
    if req in door_messages:
        client.publish(
            config.controller.publish.camera,
            "Capture",
            config.mqtt.qos)
    # When receive QR/RFID message valid, publish a message to Door
    if req in config.qr.code:
        print("...checking QR/RFID Code")
        print("...Code Verified")
        print("...Door Open")
        # Publish message to Open Door
        client.publish(
            config.controller.publish.lock,
            "Open",
            config.mqtt.qos
        )


if __name__ == "__main__":
    # Main program to connect MQTT broker
    connect_mqtt(
        config.controller.user,
        config.controller.password,
        on_connect,
        on_message
    )

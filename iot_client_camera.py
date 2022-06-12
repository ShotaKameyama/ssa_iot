'''
This module represents camera iot client, which
subscribe the messagae from controller and
take a picture when ordered.
'''
from pyaml_env import parse_config, BaseConfig
from module.camera import take_photo
from module.mqtt_connector import connect_mqtt, print_connect, print_message

config = BaseConfig(parse_config('./config/config.yml'))


def on_connect(client, userdata, flags, rc):
    '''
    when connected to the MQTT client,
    subscribe controller message.
    '''
    print_connect(client, userdata, flags, rc)
    # Camera subscribe controller topic
    client.subscribe(
        config.client_camera.subscribe.controller)
    print("Subscribed to: " + config.client_camera.subscribe.controller)


def on_message(client, userdata, msg):
    '''
    when message delivered on MQTT,
    Show client, userdata and messages.
    And if the message is "Capture", then
    capture a picture and return the message.
    '''
    print_message(client, userdata, msg)
    req = str(msg.payload.decode("utf-8"))
    # When receive camera message, take a photo and publish a message to controller
    if req == "Capture":
        take_photo()
        client.publish(
            config.client_camera.publish.controller,
            "Captured",
            config.mqtt.qos)


if __name__ == "__main__":
    # Main program to connect MQTT broker
    connect_mqtt(
        config.client_camera.user,
        config.client_camera.password,
        on_connect,
        on_message
    )

'''
This file works as a door lock iot client that supports the following:
1. subscribe controller message
2. Open/Close the door lock when ordered.
'''
from pyaml_env import parse_config, BaseConfig
from module.mqtt_connector import connect_mqtt, print_connect, print_message

config = BaseConfig(parse_config('./config/config.yml'))
door_requests = {"b'Open'": "Door Opened", "b'Close'": "Door Closed"}


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    '''
    when connected to the MQTT client,
    subscribe controller message.
    '''
    print_connect(client, userdata, flags, rc)
    client.subscribe(
        config.client_lock.subscribe.controller
    )
    print("Subscribed to: " + config.client_lock.subscribe.controller)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    '''
    when message delivered on MQTT,
    Show client, userdata and messages.
    When order received,
    publish a message to controller the result of door order

    '''
    req = str(msg.payload)
    print_message(client, userdata, msg)
    if req in door_requests:
        client.publish(
            config.client_lock.publish.controller,
            door_requests[req],
            config.mqtt.qos)


if __name__ == "__main__":
    connect_mqtt(
        config.client_lock.user,
        config.client_lock.password,
        on_connect,
        on_message
    )

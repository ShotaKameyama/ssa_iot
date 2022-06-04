'''
This file is a module to support mqtt connection.
'''
# Import paho as mqtt client
import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig

config = BaseConfig(parse_config('./config/config.yml'))


def connect_mqtt(user, password, on_connect, on_message):
    '''
    Main function to connect MQTT
    '''
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.username_pw_set(user, password)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(
        config.mqtt.host,
        int(config.mqtt.port),
        config.mqtt.keep_alive)
    client.loop_forever()


def print_connect(client, userdata, flags, reason_code):
    '''
    This is to show the common connect message for each iot devices.
    '''
    print("Connected with result code " + str(reason_code))
    print(f'Client: {client} | User Data: {userdata}'
          f'Flags: {flags} | Reason Code {reason_code}')


def print_message(client, userdata, msg):
    '''
    This is to show the common message for each iot devices.
    '''
    print(f'Client: {client} | User Data: {userdata}')
    print(f'Topic: {msg.topic} | '
          f'QOS: {msg.qos}  | '
          f'Message: {msg.payload}')

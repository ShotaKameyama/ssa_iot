'''
This file tries to fetch all the sys info on MQMT protocol
by accessing $SYS/# and #.
'''
import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig

# Import all the config from the config.yml file.
config = BaseConfig(parse_config('./config/config.yml'))


def on_connect(client, userdata, flags, return_code):
    '''
    when connected to the MQTT client,
    subscribe $SYS/# and #, which fetches
    almost all information on MQTT.
    '''
    print(f'Client: {client} | User Data: {userdata}'
          f'Flags: {flags} | return_code {return_code}')
    client.subscribe('#', qos=0)
    client.subscribe('$SYS/#')


def on_message(client, userdata, message):
    '''
    when message delivered on MQTT,
    Show client, userdata and messages.
    '''
    print(f'Client: {client} | User Data: {userdata}')
    print(f'Topic: {message.topic} | '
          f'QOS: {message.qos}  | '
          f'Message: {message.payload}')


def main():
    '''
    Main function to connect MQTT
    '''
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


if __name__ == "__main__":
    main()

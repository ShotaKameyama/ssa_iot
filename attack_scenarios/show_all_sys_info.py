'''
This file tries to fetch all the sys info on MQMT protocol
by accessing $SYS/# and #.
'''
from pyaml_env import parse_config, BaseConfig
from module.mqtt_connector import connect_mqtt, print_connect, print_message

# Import all the config from the config.yml file.
config = BaseConfig(parse_config('./config/config.yml'))


def on_connect(client, userdata, flags, rc):
    '''
    when connected to the MQTT client,
    subscribe $SYS/# and #, which fetches
    almost all information on MQTT.
    '''
    print_connect(client, userdata, flags, rc)
    client.subscribe('#', qos=0)
    client.subscribe('$SYS/#')
    print("Subscribed to: # and $SYS/#")


def on_message(client, userdata, message):
    '''
    when message delivered on MQTT,
    Show client, userdata and messages.
    '''
    print_message(client, userdata, message)


if __name__ == "__main__":
    connect_mqtt(
        None,  # config.controller.user,
        None,  # config.controller.password,
        on_connect,
        on_message
    )

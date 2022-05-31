import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig

config =  BaseConfig(parse_config('./config/config.yml'))
door_requests = {"b'Open'": "Door Opened", "b'Close'":"Door Closed"}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(
        config.client_lock.subscribe.controller
    )
    print ("Subscribed to: " + config.client_lock.subscribe.controller)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    req = str(msg.payload)
    print(msg.topic + " " + req)
    if req in door_requests:
        client.publish(
            config.client_lock.publish.controller,
            door_requests[req],
            config.mqtt.qos)

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.username_pw_set(
    config.client_lock.user,
    config.client_lock.password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    config.mqtt.host,
    int(config.mqtt.port),
    config.mqtt.keep_alive)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
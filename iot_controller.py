import paho.mqtt.client as mqtt
import yaml
with open('./config/config.yml', 'r') as file:
    c = yaml.safe_load(file.read())

door_messages = ["b'Door Opened'","b'Door Closed'"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(
        c['controller']['subscribe'][0])

def on_message(client, userdata, msg):
    req = str(msg.payload)
    print(msg.topic + " " + req)
    if req in door_messages:
        client.publish(
            c['controller']['publish'][0],
            "Capture",
            c['mqtt']['qos'])

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    c['mqtt']['host'],
    c['mqtt']['port'],
    c['mqtt']['keep_alive'])
client.loop_forever()
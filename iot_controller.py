import paho.mqtt.client as mqtt
door_messages = ["b'Door Opened'","b'Door Closed'"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Message2Controller")

def on_message(client, userdata, msg):
    req = str(msg.payload)
    print(msg.topic + " " + req)
    if req in door_messages:
        client.publish("DoorCamera", "Capture", 2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
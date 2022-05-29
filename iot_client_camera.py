# Import opencv for computer vision
import cv2
# Import paho as mqtt client
import paho.mqtt.client as mqtt
# Import metaplotlib to visualize an image
from matplotlib import pyplot as plt
import datetime

dt_now = datetime.datetime.now()
dt_now_format = dt_now.strftime('%Y-%m-%d-%H%M%S')

def take_photo():
    # Connect to capture device
    cap = cv2.VideoCapture(0)
    # Get a frame from the capture device
    ret, frame = cap.read()
    # Save into a picture
    cv2.imwrite(dt_now_format + '_capture.jpg',frame)
    # Release the connection
    cap.release()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("DoorCamera")

def on_message(client, userdata, msg):
    req = str(msg.payload)
    print(msg.topic + " " + req)
    if req == "b'Capture'":
        take_photo()
        print("took Photo")
        client.publish("Message2Controller", "Captured", 2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
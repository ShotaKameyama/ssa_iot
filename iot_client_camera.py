# Import opencv for computer vision
import cv2
# Import paho as mqtt client
import paho.mqtt.client as mqtt
# Import metaplotlib to visualize an image
from matplotlib import pyplot as plt
import datetime
from pyaml_env import parse_config, BaseConfig

config =  BaseConfig(parse_config('./config/config.yml'))


dt_now = datetime.datetime.now()
dt_now_format = dt_now.strftime('%Y-%m-%d-%H%M%S')

def take_photo():
    # Connect to capture device
    cap = cv2.VideoCapture(
        config.client_camera.vid_cap
    )
    # Get a frame from the capture device
    ret, frame = cap.read()
    # Save into a picture
    cv2.imwrite(dt_now_format + '_capture.jpg',frame)
    # Release the connection
    cap.release()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(
        config.client_camera.subscribe.controller)

def on_message(client, userdata, msg):
    req = str(msg.payload)
    print(msg.topic + " " + req)
    if req == "b'Capture'":
        take_photo()
        client.publish(
            config.client_camera.publish.controller,
            "Captured",
            config.mqtt.qos)

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.username_pw_set(
    config.client_camera.user,
    config.client_camera.password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    config.mqtt.host,
    int(config.mqtt.port),
    config.mqtt.keep_alive)
client.loop_forever()